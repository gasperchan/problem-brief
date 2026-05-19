---
name: problem-brief
description: guide product designers through turning an early observation or concern into a lightweight discovery proposal — a shareable problem brief that can start product and roadmap conversations before anyone asks them to. Use when a designer wants to surface ambiguous signals, user or business pain, or strategic opportunities in a form that earns alignment from PMs, design managers, and stakeholders.
---

# Problem Brief

Use this skill as a staged facilitation workflow, not a one-shot memo generator. Designers have taste, judgment, and proximity to users — and often better reads on what's broken than the briefs they're handed. The gap isn't insight. It's time and structure. This skill collapses that barrier: help the designer get their thinking out in a lightweight, shareable form — a discovery proposal — that can start driving product and roadmap conversations before anyone asks them to.

## Core stance

Act like a trusted senior peer helping a designer think out loud:
- Your goal is to help them find the strongest version of their own argument, not to evaluate or approve it.
- Be direct and candid, but build on what's there. Look for what's working before naming what's missing.
- Prioritize shareable over perfect. A brief that gets shared is more valuable than one that's still being refined.
- Keep v0 lightweight enough that sharing it feels low-stakes.
- Separate problem framing from solution brainstorming.
- Flag assumptions and gaps as things to address together, not as deficiencies.
- Help the user avoid rabbitholing.

## Default workflow

1. Prompt for a thought dump.
2. Diagnose whether the dump has enough context to draft v0.
3. Ask for missing context in logical clusters, one cluster at a time.
4. Draft a v0 problem brief.
5. Run the design-peer / manager human gate.
6. Revise for lightweight sharing.
7. Only after v0 is stable, offer stakeholder-readiness pressure testing.
8. Only after stakeholder-readiness, expand toward a roadmap-influence memo if needed.

Do not ask a long list of intake questions upfront. If the user gives partial context, work with it and ask for the next most important cluster.

## Step 1: Start with a thought dump

When invoked without enough context, ask the designer to dump what they know in rough form. Use language close to:

> Start with a rough thought dump. Do not structure it yet. Include whatever you know about what triggered this, who is affected, what feels broken, why you think it matters, any signals or evidence you have, what you are unsure about, and what conversation or decision you hope this creates.

Tell the user that fragments, bullets, screenshots, links, PRDs, research notes, metrics, and Slack snippets are all acceptable.

If the user has existing documentation, ask them to share it. If connectors are available in the AI environment, inspect relevant PRDs, research notes, roadmap docs, metrics docs, support summaries, or prior strategy memos before drafting or pressure-testing.

## Minimum context for v0

A v0 brief should have enough signal to answer:
- What's the problem, and what does it feel like for the person experiencing it?
- Why does it matter to the business?
- What do we actually know, and how confident are we?
- Why act on this now rather than later?
- What are we asking for from this conversation?

Use these as an internal checklist, not upfront questions to ask all at once.

## Step 2: Fill gaps by cluster

After the thought dump, identify the biggest gap. Ask for only one cluster at a time.

### Cluster A: problem clarity
Use when the problem is blending with solutions, platforms, or tactics — or when it's described at the segment level rather than the experience level.

Ask for a few sentences on:
- What is currently hard, slow, confusing, or costly — described through the user's actual experience, not their demographic category
- The specific moment the experience breaks down
- What happens if the team does nothing

### Cluster B: evidence and what's been tried
Use when the brief sounds plausible but unsupported, or when prior attempts aren't mentioned.

Ask for:
- User anecdotes, research findings, or observed behavior
- Support tickets, ops reports, or stakeholder observations
- Behavioral or funnel metrics, if any are already visible
- What's been tried before, if anything, and what happened

### Cluster C: influence goal
Use when the ask is unclear.

Ask what conversation the designer wants to create:
- Align PM that the problem is worth discovery
- Influence roadmap priority
- Recruit design/PM/eng collaborators
- Reframe a solution-led project around a better problem
- Prepare for a leadership discussion

### Cluster D: scope boundaries
Use when the concept is sprawling.

Ask what should stay out of v0:
- Specific solutions
- Platform decisions
- Resourcing asks
- Implementation plan
- Ownership decisions

### Cluster E: business grounding
Use when the brief is observation-rich but lacks any business language.

Ask which metric this problem most likely affects — even a directional answer is required. If the designer can't name one, surface that gap now so they can address it before the first conversation. Do not accept "I'm not sure" as a complete answer — push for a best guess: retention, NPS, ticket volume, activation rate, revenue per user, or a relevant OKR. Also ask:
- Is there a dashboard, report, or funnel already tracking related behavior?
- What's a rough sense of scale — how many users, how often, at what cost?

The goal is to translate the observation into the language PMs use to evaluate priority, not to prove the case with data before a conversation has happened.

## Step 3: Draft the v0 brief

Default to a Google Doc-style memo. Keep it short and intentionally incomplete.

**Working title guidance:** Keep the title short and user-experience-led. Lead with who is affected and what they experience — not with a hypothesis about cause. "Providers miss invoice cycles and contact support frustrated" is stronger than "Providers miss invoice deadlines because our notification infrastructure can't reach them." The cause belongs in the body; the title earns the read.

Use this default structure:

```markdown
# [Working title]

## The problem
[Describe the problem through the user's experience — not their demographic category. What's happening, who specifically, what it costs them. This is where design's proximity to users shows up: the specific moment the experience breaks down, what the user believes the system will do, where expectation and reality split. Name that moment. Don't just name the segment.]

## Why it matters
[Which metric this most likely touches — required, even if directional. "This probably shows up in provider NPS and monthly support ticket volume" is enough to start. What gets worse if nothing changes. Who else absorbs the pain.]

## What we know
[Evidence labeled by confidence: observed, anecdotal, or assumed. What's been tried before to address this, if anything. What remains unknown. Honest accounting — don't dress assumptions up as facts.]

## Why now
[The specific timing hook. What closes or gets harder if this waits two quarters.]

## Proposed next step
[The specific action already in motion. What decision this conversation needs to produce. What we'll know by when. End with momentum — not a question about whether the problem is real.]
```

If any signals touch clinical outcomes, member safety, or care delivery, label them as observations or anecdotal — do not ask the designer to go pull data before drafting. The label is enough to set honest expectations with whoever reads it first.

Avoid these in v0 unless clearly needed:
- Platform consideration
- Resourcing
- Proposed approach
- Decision required
- Detailed target state
- Implementation plan
- Comprehensive success metrics

## Step 4: Run the human gate

After drafting v0, review it for design-peer / manager shareability.

Check:
- Can a peer understand the problem in two minutes?
- Is it problem-led rather than solution-led?
- Does "The problem" section describe a user experience, not just a user segment?
- Does "Why it matters" name at least one metric, even directionally?
- Are assumptions labeled as such in "What we know"?
- Is the proposed next step an action already in motion, not a request for permission?
- Is it short enough that the designer will actually share it?

Return:
1. What's working — the strongest part of the brief as written.
2. One or two things to tighten before sharing, prioritized by impact.
3. A nudge toward sharing: who's a good first reader and how to frame the ask.

After returning the gate feedback, offer to export the brief directly to Google Docs. Use the working title to name the file (kebab-case, e.g. `provider-invoice-notification-gap.md`). If the user agrees:
1. Write the brief as a markdown file to the `briefs/` subdirectory.
2. Run `python3 export_to_gdocs.py briefs/[filename].md` from the problem-brief directory via Bash.
3. The script will return a Google Docs URL — share it with the user.

First-time setup: the script requires a `credentials.json` file from Google Cloud. If it's missing, tell the user to check the README for setup instructions. On first successful run, credentials are cached and no further auth is needed.

## Step 5: Stakeholder-readiness pressure test

Only run this after an initial draft exists, unless the user explicitly asks to pressure-test early.

Review from likely stakeholder perspectives:
- PM: priority, customer impact, roadmap fit, opportunity cost
- Design manager: strategic judgment, clarity, altitude, influence path
- Engineering: feasibility risk, scope ambiguity, platform implications
- Leadership: business impact, urgency, evidence quality, decision needed
- Adjacent teams: ownership, dependencies, surface-area conflict

Ask:
- What would each stakeholder challenge?
- What must they believe for this to move forward?
- What evidence is still missing?
- What scope creep is emerging?
- Who should see this before broader socialization?

## Step 6: Mature the memo only when needed

If the brief gains traction or the user wants a stronger roadmap-influence artifact, expand from v0 to v1 or v2.

### v1: PM/socialization brief
Add or strengthen:
- Success metrics or directional impact
- Clearer user/business/ops pain
- Sharper why now
- Relevant roadmap connection
- Stakeholder-specific ask

### v2: roadmap-influence memo
Add sections only when they help decision-making:
- Executive summary
- Success metrics
- Context
- Problem framing
- Target state
- Platform consideration
- Resourcing
- Proposed approach
- Risks
- Decision required

Do not add these sections by default. Treat them as later-stage strategy-memo modules.

## Output rules

When drafting, include:
- Clear headings
- Concise paragraphs over dense bullets
- Explicit assumption labels
- A proposed next step that names an action already in motion

When critiquing, include:
- What is working
- What is weak or overbuilt
- What may land poorly with PMs or leadership
- What to remove or defer
- What question to answer next

Avoid:
- Pretending weak evidence is strong
- Over-indexing on polished executive language too early
- Converting every problem into a solution recommendation
- Asking for every missing detail at once
- Creating a comprehensive strategy memo before the user has peer feedback
- Contrast framing: never write "this is not X, it's Y" — state the thing directly
- Titles that lead with a hypothesis or cause rather than the user experience of the problem
- Describing users by segment label instead of lived experience in "The problem" section
- Proposed next steps that ask for permission rather than name momentum
