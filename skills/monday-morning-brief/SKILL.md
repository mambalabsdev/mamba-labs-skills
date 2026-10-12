---
name: monday-morning-brief
description: |
  Produce the weekly operating brief: what moved, what is at risk, and the three things that need a decision. Use when someone wants a Monday update, a weekly business summary, or a recurring brief across their tools.
license: MIT
compatibility: "Claude Code, Claude Desktop, Codex CLI, Cursor, Gemini CLI, and other agents that read SKILL.md. Live data steps need Node.js 18 or newer and an Apify API token."
tags: [small_business_operations, small_business_ops]
metadata:
  title: "Monday Morning Brief"
  category: "small-business-ops"
  tags: "small_business_operations, small_business_ops"
  keywords: "small business, monday morning brief, weekly business summary, what happened last week, weekly update across my tools, recurring operating brief"
  version: "2.1.0"
---

# Monday Morning Brief

## What this does

A weekly brief is only read if it is short and if it is honest about what it could not see. This skill pulls from whatever is connected, reports movement rather than levels, names the decisions that are waiting, and states plainly which sources were unavailable rather than quietly leaving them out.

## When to use it

- Monday morning brief
- weekly business summary
- what happened last week
- weekly update across my tools
- recurring operating brief

## Inputs

- **sources**: which systems are connected: calendar, mail, CRM, finance, project tracker
- **period**: the week being covered
- **focus**: what the reader is accountable for

## Shared context this skill reads

Before doing anything else, read whichever of these exist at the project root and
use them instead of asking the user to repeat themselves:

- `BRAND.md`

If none exist, do the work from what the user gives you, then offer to write the
missing file so the next skill in the pack starts warmer.

## Tool connection

This skill needs no live data tool. It works from the files, exports and answers
you give it, so it runs the same in any agent with no setup.

## Method

1. Read every connected source for the period and record which ones answered and which did not, before writing anything.
2. Report movement, not levels. Revenue is a level; revenue up on two new customers and down on one churn is movement, and only movement tells you what to do.
3. Separate what happened from what is at risk. The risk section is the reason the brief exists.
4. Name the decisions waiting on the reader, with what each one is blocked on and how long it has been waiting.
5. Cap the brief at one screen. A brief that scrolls is a report and it will not be read on a Monday.
6. State the coverage gaps explicitly at the end. A source that did not answer is not the same as a source with nothing to report, and conflating them is how a brief becomes misleading.
7. Carry forward last week's decisions and say whether each one was made.
8. Approval stop. Before sending the brief to anyone outside the operator, show the user exactly what will happen and wait for an explicit yes. Nothing live changes without it.
9. Check the output with `scripts/check-output.py` before you return it.

## Approval stop

Stop and ask before sending the brief to anyone outside the operator. Show exactly what will be sent or written, to whom or to
which records, and how many. Proceed only on an explicit yes from the user in this
conversation. A yes for one batch does not cover the next one.

## Output

One screen: movement, risks, decisions waiting, last week's decisions and their status, and a coverage line naming any source that did not answer.

## Check the output before you return it

Save the output to a file and run `python3 scripts/check-output.py <file>`. The
contract it checks is `scripts/output-contract.json`.

- Exit 0, `COMPLETE`: return the output.
- Exit 2, `INCOMPLETE`: do not present the output as finished. Fill what you can, run
  the check again, and if parts stay missing, return the output under the heading
  `Incomplete` with every reason the check printed.

## Quality bar

- Sources that did not answer are named, never silently omitted
- Movement is reported rather than levels
- Decisions carry what they are blocked on and how long they have waited
- The brief fits one screen
- Last week's decisions are carried forward with a status

## Related skills

- `weekly-pipeline-review`
- `month-end-narrative`
- `cash-runway-snapshot`

Ships in the **small-business-operations** pack.
