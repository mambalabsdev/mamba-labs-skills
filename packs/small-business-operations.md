# Small Business Operations

**The weekly and monthly routines a small company actually has to run.**

## Who it is for

Owner operators and small teams with no finance function and no operations hire.

## The problem

The recurring work of running a business gets done badly and late because it is nobody's job: the weekly brief, the month end close, the runway question, and the invoices nobody wants to chase.

## What is in it

Five routines, built on whatever connectors are available rather than on one vendor. The brief reports movement and names what it could not see. The close refuses to narrate numbers that have not reconciled. The runway snapshot separates committed from expected income and models the late payment case that actually happens.

## Free skills in this pack

Install in this order. Each assumes the ones above it have run at least once.

| # | Skill | What it does |
| --- | --- | --- |
| 1 | [`brand-context-builder`](../skills/brand-context-builder) | Interview once and write the shared context files that every other skill reads |
| 2 | [`monday-morning-brief`](../skills/monday-morning-brief) | Produce the weekly operating brief: what moved, what is at risk, and the three things that need a decision |
| 3 | [`weekly-pipeline-review`](../skills/weekly-pipeline-review) | Run a weekly pipeline review that finds the deals that are quietly dying rather than admiring the big ones |
| 4 | [`invoice-chaser`](../skills/invoice-chaser) | Chase overdue invoices on a fixed escalation ladder that gets paid without damaging the relationship |
| 5 | [`cash-runway-snapshot`](../skills/cash-runway-snapshot) | Work out how many months of cash are left and what actually changes it |
| 6 | [`mamba-gtm-router`](../skills/mamba-gtm-router) | Route a plain language go to market request to the right skill, and name the ones that would help but are not installed |

Every free skill sits on a 30 day review cycle. Fixes and improvements ship as repo updates.

## Premium skills in this pack

These encode the system rather than the single task. They are not in this repo.

| Skill | What it does |
| --- | --- |
| `month-end-narrative` | Close the month and write the narrative that explains the numbers, with the reconciliation done before a word is written |

Most premium skills are on a weekly review cycle. Fixes and improvements ship as updates, and buyers receive release notes by email.

The full pack: https://mambabuilt.com/skills

## Shared context

Every skill in this pack reads `BRAND.md`, `ICP.md` and `VOICE.md` from your
project root where they exist. `brand-context-builder` writes all three from one
interview, and output quality compounds across the pack as those files improve.

