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

The brief is a designer's interpretive claim — not a problem report or ticket summary. What designers bring that's distinct: the specific moment the experience breaks down, the gap between what users believe the system will do and what it actually does, the pattern behind individual complaints that isn't visible from the backlog or the funnel alone. Write from that proximity.

## Default workflow

1. Prompt for a thought dump.
2. Draft v0 from whatever context exists — partial is fine.
3. Surface gaps as open questions in "Where I'm taking this" — not as blockers to drafting.
4. Run the design-peer / manager human gate.
5. Revise for lightweight sharing.
6. Only after v0 is stable, offer stakeholder-readiness pressure testing.
7. Only after stakeholder-readiness, expand toward a roadmap-influence memo if needed.

Do not ask a long list of intake questions upfront. If the user gives partial context, draft with what's there and name the gaps as open questions.

## Step 1: Start with a thought dump

When invoked without enough context, ask the designer to dump what they know in rough form. Use language close to:

> Start with a rough thought dump. Do not structure it yet. Include whatever you know about what triggered this, who is affected, what feels broken, why you think it matters, any signals or evidence you have, what you are unsure about, and what conversation or decision you hope this creates.

Tell the user that fragments, bullets, screenshots, links, PRDs, research notes, metrics, and Slack snippets are all acceptable.

If the user has existing documentation, ask them to share it. If connectors are available in the AI environment, inspect relevant PRDs, research notes, roadmap docs, metrics docs, support summaries, or prior strategy memos before drafting or pressure-testing.

## Minimum context for v0

A v0 brief needs enough signal to write something in each section — even if some of it is labeled "assumed." Use these as a completeness check after drafting, not as upfront questions:
- What's the problem, and what does it feel like for the person experiencing it?
- Why does it matter to the business?
- What do we actually know, and how confident are we?
- What are we asking for from this conversation?

If a section can't be written at all, ask for the minimum needed before drafting — one cluster, not a list.

## Step 2: Fill gaps by cluster

Use cluster questions to fill significant gaps — after drafting, or when a section can't be written at all. Ask for only one cluster at a time. Surface remaining gaps as open questions in "Where I'm taking this," not as blockers.

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
- Counterevidence or reasons this might not be a priority

### Cluster C: influence goal
Use when the ask is unclear. Ask what conversation the designer wants to create: align PM that the problem is worth discovery, influence roadmap priority, recruit collaborators, reframe a solution-led project, or prepare for a leadership discussion.

### Cluster D: scope boundaries
Use when the concept is sprawling. Ask what should stay out of v0: solutions, platform decisions, resourcing, implementation plan, ownership decisions.

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

## What's breaking — and for who
[Describe the problem through the user's experience — the specific moment the experience breaks down, where expectation and reality split. Not a segment label: the actual lived experience. Name who is affected and what it costs them.]

## Why it costs us — stakes and timing
[Which metric this most likely touches — required, even if directional. "This probably shows up in provider NPS and monthly support ticket volume" is enough to start. What gets worse if nothing changes. Who else absorbs the pain. The specific timing hook: what closes or gets harder if this waits.]

## What we're seeing — observations and assumptions
[Evidence labeled by confidence: observed, anecdotal, or assumed. What's been tried before to address this, if anything. What remains unknown. Honest accounting — don't dress assumptions up as facts.]

## Where I'm taking this — next steps and open questions
[Name the action already in motion — not a meeting request, not a question about whether the problem is real. State who, what decision, and by when. "I'm bringing this to [name] by [date] to get alignment that this is worth a 2-week discovery sprint before Q3 planning" is the right register. "Let's align on next steps" is not. Then name the open questions: which assumptions need validation, what research would strengthen this brief for the next conversation.]
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
- Does "What's breaking" describe a specific moment of breakdown — not just a user segment or category of friction?
- Does "Why it costs us" name at least one metric, even directionally?
- Are assumptions honestly labeled in "What we're seeing"?
- Is there enough signal to justify a conversation, not a roadmap commitment?
- Does "Where I'm taking this" name a specific person, a specific decision, and a timeframe — or does it describe an activity? Flag if it reads like a meeting request rather than a design-initiated action.
- Is it short enough that the designer will actually share it?

Return:
1. What's working — the strongest part of the brief as written.
2. One or two things to tighten before sharing, prioritized by impact.
3. A nudge on socialization sequencing: who's a good first reader, why that order matters (PM before DM vs. the other way around isn't neutral), and how to frame the ask so sharing feels low-stakes.

After returning the gate feedback, offer to export the brief directly to Google Docs. Use the working title to name the file (kebab-case, e.g. `provider-invoice-notification-gap.md`). If the user agrees:
1. Write the brief as a markdown file to the `briefs/` subdirectory of the current working directory, creating it if needed.
2. Run `export_to_gdocs briefs/[filename].md` via Bash.
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
Add only when it helps decision-making: executive summary, success metrics, target state, platform consideration, resourcing, proposed approach, risks, decision required. Add sections individually, not all at once.

## Output rules

When drafting, include:
- Clear headings
- Concise paragraphs over dense bullets
- Explicit assumption labels
- A "Where I'm taking this" that names an action already in motion and surfaces open questions for validation

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
- Describing users by segment label instead of lived experience in "What's breaking"
- Next steps that ask for permission rather than name momentum
