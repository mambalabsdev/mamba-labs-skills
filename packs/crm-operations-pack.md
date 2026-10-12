# CRM Operations

**Make the pipeline report mean something, then keep it that way.**

## Who it is for

Operators who inherited an instance, and teams whose reports do not reconcile.

## The problem

CRM work is usually a one off cleanup that decays back within a quarter, because the intake that produced the defects was never touched and the stage definitions were never observable.

## What is in it

The audit starts from the reports the business needs rather than from the object model, and ends with a plan that has a stop line. The merge plan treats the dry run as the job, since merges cannot be undone. The lifecycle and attribution skills fix the definitions that make reports disagree, and the hygiene sweep keeps the whole thing from decaying.

## Free skills in this pack

Install in this order. Each assumes the ones above it have run at least once.

| # | Skill | What it does |
| --- | --- | --- |
| 1 | [`brand-context-builder`](../skills/brand-context-builder) | Interview once and write the shared context files that every other skill reads |
| 2 | [`crm-hygiene-sweep`](../skills/crm-hygiene-sweep) | Run a recurring cleanup on new and changed CRM records so the database stops degrading between audits |
| 3 | [`weekly-pipeline-review`](../skills/weekly-pipeline-review) | Run a weekly pipeline review that finds the deals that are quietly dying rather than admiring the big ones |
| 4 | [`mamba-gtm-router`](../skills/mamba-gtm-router) | Route a plain language go to market request to the right skill, and name the ones that would help but are not installed |

Every free skill sits on a 30 day review cycle. Fixes and improvements ship as repo updates.

## Premium skills in this pack

These encode the system rather than the single task. They are not in this repo.

| Skill | Price | What it does |
| --- | --- | --- |
| `crm-audit` | 5.99 USD | Audit a CRM for the data and process problems that are costing pipeline, and produce a prioritized remediation plan |
| `crm-dedupe-plan` | 5.99 USD | Plan and execute a duplicate merge in a CRM without losing history, associations or enrichment |
| `lead-lifecycle-designer` | 5.99 USD | Define lifecycle stages and the entry and exit rules that make pipeline reporting mean something |
| `deal-attribution-audit` | 5.99 USD | Work out which deals a channel or an agency actually sourced, and produce a number both sides accept |
| `win-loss-analysis` | 9.99 USD | Work out why deals are actually won and lost, using evidence that did not come from the person who lost them |
| `crm-enrichment-refresh` | 7.99 USD | Keep CRM company data current with a scheduled enrichment that only re enriches what actually changed |
| `expansion-signal-monitor` | 7.99 USD | Watch existing customers for the public signals that mean expansion or risk, and act before renewal |

Most premium skills are on a weekly review cycle. Fixes and improvements ship as updates, and buyers receive release notes by email.

The full pack, every premium skill above plus the free ones: 24 USD at https://mambabuilt.com/store

## Shared context

Each skill in this pack reads the files its Shared context section names, from
`BRAND.md`, `ICP.md` and `VOICE.md`, where they exist. `brand-context-builder` writes
all three from one interview, and output quality compounds as those files improve.

