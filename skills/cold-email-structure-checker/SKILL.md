---
name: cold-email-structure-checker
description: |
  Audit a cold email draft against a 7-point outbound framework and return a pass/fail scorecard with a revised version. Checks for: signal anchor, relevance hook, value statement, social proof, single CTA, length (under 100 words), and spam word scan. Use this skill whenever someone asks to review a cold email, check their outreach copy, audit an email draft, improve a prospecting email, fix a cold email, or wants feedback on outbound messaging. Also trigger when someone pastes an email and asks "is this good?" or "will this get replies?"
---

# Cold Email Structure Checker

Audit a cold email against the 7-point framework that top-performing outbound teams use, then output a scorecard and a revised version.

## The 7-Point Framework

Every cold email that earns replies follows this structure. Each element is scored Pass or Fail.

### 1. Signal Anchor (first sentence)
Does the opening reference a specific, verifiable event at the prospect's company? Good: "You just posted a VP RevOps role on Greenhouse." Bad: "I noticed your company is growing."

**Pass criteria:** names a specific event (hire, funding round, product launch, job posting, tech adoption, leadership change) with enough detail that the reader knows you researched them.

### 2. Relevance Hook (second sentence)
Does the email connect that signal to a problem the recipient personally cares about? Good: "Most teams in that position burn 60 days getting new reps productive." Bad: "We help companies like yours."

**Pass criteria:** bridges from the signal to a pain point relevant to the recipient's role, not just the company.

### 3. Value Statement (third sentence)
Does it state the outcome the sender delivers, in one sentence, without jargon? Good: "We cut that ramp time to 21 days for 3 Series B teams last quarter." Bad: "Our platform provides a comprehensive solution for sales enablement."

**Pass criteria:** includes a quantified outcome or a named reference customer. No feature descriptions.

### 4. Social Proof (optional but scored)
Is there a reference to a similar company, a metric, or a recognizable name? Good: "including [Company X] who had the same challenge last year." Bad: "Trusted by hundreds of companies."

**Pass criteria:** at least one named company or specific metric. Generic claims fail.

### 5. Single CTA (closing)
Is there exactly one ask, and is it low-friction? Good: "Open to a 15-minute call next Tuesday?" Bad: "Let me know if you want to hop on a call, or I can send you a case study, or feel free to check out our website."

**Pass criteria:** one question, one action. The ask should take the recipient less than 30 seconds to answer.

### 6. Length Check
Is the email under 100 words (body only, excluding signature)?

**Pass criteria:** 100 words or fewer. Each word over 100 is a point against. Ideal range: 50 to 85 words.

### 7. Spam Word Scan
Does the email contain words that trigger spam filters or sound like marketing copy?

**Flagged words:** guarantee, free, act now, limited time, exclusive offer, click here, buy now, no obligation, risk-free, congratulations, winner, amazing, incredible, revolutionary, game-changing, synergy, best-in-class, world-class, next-generation, end-to-end, turnkey

**Pass criteria:** zero flagged words.

## How to Run

1. User provides their cold email draft.
2. Run each of the 7 checks. Score Pass or Fail.
3. Output the scorecard.
4. Below the scorecard, provide a revised version that fixes every Fail.

## Output Template

```
## Cold Email Audit

**Overall Score:** [X/7]

| # | Check | Result | Note |
|---|-------|--------|------|
| 1 | Signal Anchor | [Pass/Fail] | [one-line reason] |
| 2 | Relevance Hook | [Pass/Fail] | [one-line reason] |
| 3 | Value Statement | [Pass/Fail] | [one-line reason] |
| 4 | Social Proof | [Pass/Fail] | [one-line reason] |
| 5 | Single CTA | [Pass/Fail] | [one-line reason] |
| 6 | Length | [Pass/Fail] | [word count] |
| 7 | Spam Words | [Pass/Fail] | [flagged words or "Clean"] |

### Revised Version

Subject: [revised subject line]

[revised email body, fixing every failed check]

### What Changed
[Bullet list of each change made and why]
```

## Guidelines

- Be direct in the audit. "This email has no signal anchor" is better than "You might consider adding a signal."
- The revised version must preserve the sender's voice. Do not rewrite into a generic template.
- If the email scores 7/7, say so and do not force changes. Suggest one optional improvement if applicable.
- Never use the word "personalization" in the revised copy. Show it, do not name it.

## What This Skill Does NOT Do

- Does not look up real signals for the prospect. For signal research, see the Hiring Signal Spotter or the Signal-Based Outbound Workflow skill.
- Does not send the email or check deliverability.
- Does not generate emails from scratch. It audits and revises existing drafts.

---

Built by Mamba Labs. Browse the full GTM toolkit at https://mambabuilt.com
