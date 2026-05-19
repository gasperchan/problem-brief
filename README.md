# Problem Brief Coach

A Claude Code skill for product designers who have observations, concerns, or hunches worth surfacing — but not the time to structure them into something shareable.

---

## Why this exists

Designers have taste, judgment, and proximity to users — and often better reads on what's broken than the briefs they're handed. The gap isn't insight. It's time and structure.

Ideas stay fuzzy, stay in your head, or get lost before they reach anyone who can act on them. By the time they're structured enough to share, the roadmap conversation has already happened.

This skill collapses that gap. You dump what you know in rough form — fragments, anecdotes, Slack threads, half-formed hunches — and it helps you shape it into a **discovery proposal**: a lightweight, shareable doc that can start a product or roadmap conversation before anyone asks you to.

Strategic partnership starts before any tool is open. It starts with getting an idea clear enough that other people can care about it.

---

## What it produces

A v0 problem brief — a Google Doc-style memo a PM, design manager, or collaborator can read in two minutes and react to. It's intentionally incomplete. The goal is to earn a conversation, not close one.

The brief separates problem framing from solution brainstorming by design. It's upstream of a PRD, upstream of a product request form, upstream of a roadmap commit. It's the document that argues a problem is worth investigating at all.

---

## How this differs from a PRD or product request form

| | Problem brief | Product request form | PRD |
|---|---|---|---|
| **When** | Before discovery | When you have a clear ask | After a decision is made |
| **Owned by** | Designer, PM, or both | Anyone | PM |
| **Requires** | A signal worth exploring | A solution direction | Full scope and metrics |
| **Goal** | Start a conversation | Route a request | Document what's being built |

A product request form assumes you're done thinking and submitting to a queue. A PRD assumes the problem is already agreed on. A problem brief is for when you've noticed something but haven't been asked to act on it yet.

---

## What the AI doesn't know

The skill helps you think — it doesn't know your organization. Who the right first reader is, what your PM is currently prioritizing, which problems have already been deprioritized and why — that judgment stays with you. The brief gets your thinking out; you decide where it goes.

---

## Installation

### Requirements
- [Claude Code](https://claude.ai/code) (CLI or desktop app)
- Python 3.8+ (for Google Docs export)

### Install the skill

Clone this repo:

```bash
git clone https://github.com/gasperchan/problem-brief-coach.git
cd problem-brief-coach
```

Open the `problem-brief-coach` directory as your Claude Code project. The skill loads automatically from `SKILL.md`.

To make it available globally (across all projects), copy the skill file to your Claude user skills directory:

```bash
mkdir -p ~/.claude/skills/problem-brief-coach
cp SKILL.md ~/.claude/skills/problem-brief-coach/SKILL.md
```

### Run it

In Claude Code, type:

```
/problem-brief-coach
```

Start with a rough thought dump. Fragments, bullets, Slack screenshots, PRD links — all fine.

---

## Export to Google Docs

Once a brief is drafted, the skill offers to export it directly to Google Docs and return a shareable link.

### Option A: Google Cloud setup (recommended)

One-time setup, then it's one command.

1. Go to [Google Cloud Console](https://console.cloud.google.com) and create a project.
2. Enable the **Google Docs API** and **Google Drive API** for that project.
3. Under **APIs & Services → Credentials**, create an OAuth 2.0 Client ID (type: Desktop app). Download the JSON.
4. Rename the downloaded file `credentials.json` and place it in this directory (next to `SKILL.md`).
5. Install the Python dependencies:

```bash
pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

6. The first export will open a browser for Google authorization. After that, credentials are cached at `~/.problem-brief-coach-token.json` — no further auth needed.

### Option B: Pandoc (fallback)

If Google Cloud setup isn't working, export to `.docx` and drag it into Google Drive instead.

```bash
brew install pandoc
```

Then ask the skill to export via pandoc. It will save a `.docx` file locally that Google Drive opens natively.

---

## A note on healthtech context

If your problem involves clinical outcomes, member safety, or care delivery, the skill labels those signals as observations or anecdotal in the brief. It won't ask you to pull data before drafting. The label sets honest expectations for whoever reads it first.

---

## Contributing

This skill was built for product designers at a mental healthtech company and is designed to be shared. If you use it, adapt it, or find gaps — open an issue or PR.
