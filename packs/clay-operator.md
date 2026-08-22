# The Clay Operator

**Build tables that produce rows you can send to, at a cost you decided in advance.**

## Who it is for

Anyone building enrichment tables who has watched a credit balance disappear into a column nobody gated.

## The problem

Clay builds fail in the workspace, not in the plan. The wrong action name returns zero rows silently, an extraction path taken from provider documentation returns null, and an ungated expensive column runs on every row in the table.

## What is in it

The pack starts with the gate that refuses to emit an instruction until the run order, the ramp and the cost ceiling are decided, and ends with the full company to contact workbook. Between them sit the parts operators actually get stuck on: failure triage by symptom, run conditions that handle blanks, waterfalls ordered by cost per found address, and merges that prove they did not lose enrichment.

## Free skills in this pack

Install in this order. Each assumes the ones above it have run at least once.

| # | Skill | What it does |
| --- | --- | --- |
| 1 | [`brand-context-builder`](../skills/brand-context-builder) | Interview once and write the shared context files that every other skill reads |
| 2 | [`icp-definition-builder`](../skills/icp-definition-builder) | Turn a description of a business into a structured ideal customer profile with firmographic criteria, signals, pain indicators and exclusion rules |
| 3 | [`clay-actor-column-wiring`](../skills/clay-actor-column-wiring) | Wire an external actor or API into a Clay column so the types survive the round trip |
| 4 | [`clay-failure-triage`](../skills/clay-failure-triage) | Diagnose a Clay column that returns null, zero rows, or the wrong shape, by symptom rather than by guesswork |
| 5 | [`clay-conditional-gates`](../skills/clay-conditional-gates) | Write the run conditions that stop expensive Clay columns from firing on rows that will never qualify |
| 6 | [`clay-cost-audit`](../skills/clay-cost-audit) | Price a Clay table before it runs and find the columns that are burning credits for no return |
| 7 | [`clay-credit-forecast`](../skills/clay-credit-forecast) | Forecast how far a Clay credit balance goes across a month of planned builds, and say which build to cut when it does not reach |
| 8 | [`clay-dedupe-and-merge`](../skills/clay-dedupe-and-merge) | Deduplicate and merge people or company rows across Clay tables without losing enrichment or double counting a person |
| 9 | [`company-identity-resolution`](../skills/company-identity-resolution) | Resolve a messy company name to the right domain and canonical record, and say how confident the match is |
| 10 | [`linkedin-url-resolution`](../skills/linkedin-url-resolution) | Turn a list of company domains into company profile URLs, and fill the gaps a native enrichment leaves behind |
| 11 | [`firmographic-enrichment`](../skills/firmographic-enrichment) | Fill headcount, industry, headquarters and revenue band on a company list, and report honestly which fields actually filled |
| 12 | [`contact-classification`](../skills/contact-classification) | Classify contacts by department, seniority and role from their job title, and route them to the right persona |
| 13 | [`people-finder-recipe`](../skills/people-finder-recipe) | Find the right people at a list of companies without pulling a hundred irrelevant contacts per account |
| 14 | [`legal-entity-resolution`](../skills/legal-entity-resolution) | Resolve a company domain to its registered legal entity, company number and tax identifier |
| 15 | [`mamba-gtm-router`](../skills/mamba-gtm-router) | Route a plain language go to market request to the right skill, and name the ones that would help but are not installed |

Every free skill sits on a 30 day review cycle. Fixes and improvements ship as repo updates.

## Premium skills in this pack

These encode the system rather than the single task. They are not in this repo.

| Skill | What it does |
| --- | --- |
| `clay-build-gate` | Gate every Clay table instruction through a pre flight check before the user touches the workspace |
| `clay-waterfall-designer` | Design a work email waterfall that finds the most addresses for the least money, with verification placed where it actually protects the send |
| `icp-fit-scoring` | Score an account list from zero to one hundred against your ICP and split it into tiers you can route on |
| `clay-people-search-workbook` | Build the full company to contact workbook in Clay: source companies, qualify them, find the right people, waterfall their emails, and export a send ready list |
| `company-discovery-list-builder` | Build a company list from a market definition rather than from an existing list, using hiring activity or filing language as the discovery mechanism |

Most premium skills are on a weekly review cycle. Fixes and improvements ship as updates, and buyers receive release notes by email.

The full pack: https://mambabuilt.com/skills

## Shared context

Every skill in this pack reads `BRAND.md`, `ICP.md` and `VOICE.md` from your
project root where they exist. `brand-context-builder` writes all three from one
interview, and output quality compounds across the pack as those files improve.

