#!/usr/bin/env python3
"""
Export a markdown problem brief to Google Docs.
Usage: python3 export_to_gdocs.py brief.md

First run: opens browser for Google OAuth. Credentials cached at ~/.problem-brief-coach-token.json.
Requires credentials.json in the same directory as this script (see README for setup).
"""

import sys
import re
import os
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/documents", "https://www.googleapis.com/auth/drive.file"]
TOKEN_PATH = Path.home() / ".problem-brief-coach-token.json"
CREDS_PATH = Path.home() / "skills" / "problem-brief" / "credentials.json"


def get_credentials():
    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDS_PATH.exists():
                print("ERROR: credentials.json not found.")
                print("See README for Google Cloud setup instructions.")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_PATH), SCOPES)
            print("Opening browser for Google authorization...", flush=True)
            creds = flow.run_local_server(port=8080, open_browser=True)
        TOKEN_PATH.write_text(creds.to_json())
    return creds


def parse_markdown(md_text):
    """Convert markdown to a list of (text, style, is_bullet) tuples for the Docs API."""
    segments = []
    title_seen = False
    for line in md_text.splitlines():
        if line.startswith("# ") and not title_seen:
            segments.append((line[2:], "TITLE", False))
            title_seen = True
        elif line.startswith("# "):
            segments.append((line[2:], "HEADING_1", False))
        elif line.startswith("## "):
            segments.append((line[3:], "HEADING_1", False))
        elif line.startswith("### "):
            segments.append((line[4:], "HEADING_2", False))
        elif line.strip() == "":
            pass  # skip blank lines; heading styles have built-in spacing
        elif line.startswith("- "):
            segments.append((line[2:], "NORMAL_TEXT", True))
        else:
            segments.append((line, "NORMAL_TEXT", False))
    return segments


def split_bold_segments(text):
    """Split a line into [(text, is_bold), ...] segments based on **markers**."""
    parts = []
    pattern = re.compile(r"\*\*(.+?)\*\*")
    last = 0
    for m in pattern.finditer(text):
        if m.start() > last:
            parts.append((text[last:m.start()], False))
        parts.append((m.group(1), True))
        last = m.end()
    if last < len(text):
        parts.append((text[last:], False))
    return parts if parts else [(text, False)]


def create_doc(title, segments, creds):
    docs = build("docs", "v1", credentials=creds)

    doc = docs.documents().create(body={"title": title}).execute()
    doc_id = doc["documentId"]

    # --- Pass 1: build insertText requests and record indices for every segment ---
    # stored_ranges: list of dicts describing each paragraph and each bold chunk
    # so that pass 2 can apply formatting without index confusion.
    insert_requests = []
    stored_ranges = []   # [{para_start, para_end, style, is_bullet, bold_chunks: [(start, end)]}]
    insert_index = 1

    for text, style, is_bullet in segments:
        para_start = insert_index
        bold_chunks = []

        bold_parts = split_bold_segments(text)
        for i, (part_text, is_bold) in enumerate(bold_parts):
            chunk = part_text + ("\n" if i == len(bold_parts) - 1 else "")
            chunk_start = insert_index
            chunk_end = insert_index + len(chunk)
            insert_requests.append({
                "insertText": {
                    "location": {"index": insert_index},
                    "text": chunk
                }
            })
            if is_bold:
                bold_chunks.append((chunk_start, chunk_end))
            insert_index = chunk_end

        para_end = insert_index
        stored_ranges.append({
            "para_start": para_start,
            "para_end": para_end,
            "style": style,
            "is_bullet": is_bullet,
            "bold_chunks": bold_chunks,
        })

    # Execute all text insertions in one call.
    docs.documents().batchUpdate(
        documentId=doc_id, body={"requests": insert_requests}
    ).execute()

    # --- Pass 2: apply paragraph styles, bullets, and bold using stored indices ---
    style_requests = []
    for r in stored_ranges:
        style_requests.append({
            "updateParagraphStyle": {
                "range": {"startIndex": r["para_start"], "endIndex": r["para_end"]},
                "paragraphStyle": {"namedStyleType": r["style"]},
                "fields": "namedStyleType"
            }
        })
        if r["is_bullet"]:
            style_requests.append({
                "createParagraphBullets": {
                    "range": {"startIndex": r["para_start"], "endIndex": r["para_end"]},
                    "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"
                }
            })
        for bold_start, bold_end in r["bold_chunks"]:
            style_requests.append({
                "updateTextStyle": {
                    "range": {"startIndex": bold_start, "endIndex": bold_end},
                    "textStyle": {"bold": True},
                    "fields": "bold"
                }
            })

    docs.documents().batchUpdate(
        documentId=doc_id, body={"requests": style_requests}
    ).execute()

    return doc_id


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 export_to_gdocs.py <brief.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"File not found: {md_path}")
        sys.exit(1)

    md_text = md_path.read_text()
    lines = md_text.splitlines()
    title = lines[0].lstrip("# ").strip() if lines else md_path.stem

    creds = get_credentials()
    segments = parse_markdown(md_text)
    doc_id = create_doc(title, segments, creds)

    print(f"https://docs.google.com/document/d/{doc_id}/edit")


if __name__ == "__main__":
    main()
