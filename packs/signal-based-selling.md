# Signal Based Selling

**Reach accounts at the moment something changed, with a message about the change.**

## Who it is for

Teams whose targeting is a firmographic filter and whose reply rate reflects it.

## The problem

Signal based outbound usually means one signal, checked once, referenced generically. Real signals are public, dated and specific, and the message that works quotes the specific rather than noting that the signal exists.

## What is in it

Every skill in this pack reads live data rather than describing where to find it. Hiring, stack, funding, awards, events, reporting calendars and programs each become a qualification and an angle, and the aggregator collapses them into one score that ranks while keeping the reason that routes. It ends at the account brief, which is the same research compressed to the three facts that change a conversation.

## Free skills in this pack

Install in this order. Each assumes the ones above it have run at least once.

| # | Skill | What it does |
| --- | --- | --- |
| 1 | [`brand-context-builder`](../skills/brand-context-builder) | Interview once and write the shared context files that every other skill reads |
| 2 | [`icp-definition-builder`](../skills/icp-definition-builder) | Turn a description of a business into a structured ideal customer profile with firmographic criteria, signals, pain indicators and exclusion rules |
| 3 | [`hiring-signal-spotter`](../skills/hiring-signal-spotter) | Read a company's open roles as a buying signal and turn them into an outreach angle |
| 4 | [`job-board-keyword-scanner`](../skills/job-board-keyword-scanner) | Scan a company's job postings for the specific words that indicate a problem your product solves |
| 5 | [`tech-stack-signal-reader`](../skills/tech-stack-signal-reader) | Detect which tools a company runs from its own website and turn the stack into a qualification and an angle |
| 6 | [`ai-adoption-signal-reader`](../skills/ai-adoption-signal-reader) | Detect whether a company has shipped AI features or adopted AI vendors, and read that as a budget and priority signal |
| 7 | [`outbound-stack-fingerprint`](../skills/outbound-stack-fingerprint) | Detect whether a company runs cold outbound, which tools it sends with, and how many sending domains it operates |
| 8 | [`workplace-program-signal`](../skills/workplace-program-signal) | Detect which workplace programs and benefits a company runs, as a signal for anyone selling into people operations, benefits or internal communications |
| 9 | [`event-presence-prospecting`](../skills/event-presence-prospecting) | Find which conferences a company sponsors, exhibits at, or speaks at, and use that as a budget and audience signal |
| 10 | [`public-award-prospecting`](../skills/public-award-prospecting) | Find companies that just won a government contract or public grant and reach them while the money is new |
| 11 | [`publishing-cadence-reader`](../skills/publishing-cadence-reader) | Measure how often a company actually publishes and read that as a content investment signal |
| 12 | [`contact-classification`](../skills/contact-classification) | Classify contacts by department, seniority and role from their job title, and route them to the right persona |
| 13 | [`customer-research-interview`](../skills/customer-research-interview) | Run customer interviews that produce usable language instead of agreement, and turn the transcripts into a sharper ICP |
| 14 | [`mamba-gtm-router`](../skills/mamba-gtm-router) | Route a plain language go to market request to the right skill, and name the ones that would help but are not installed |

Every free skill sits on a 30 day review cycle. Fixes and improvements ship as repo updates.

## Premium skills in this pack

These encode the system rather than the single task. They are not in this repo.

| Skill | What it does |
| --- | --- |
| `funding-event-trigger` | Find companies that raised recently and build the timing aware outbound that follows a round |
| `earnings-window-timing` | Time outreach to public companies around their reporting calendar, avoiding the quiet period and landing when the relevant team is free |
| `company-change-monitor` | Watch an account list for meaningful changes and alert on the ones worth acting on |
| `gtm-signal-aggregator` | Combine hiring, tech stack and funding signals into one score per account and a branch decision on which message to send |
| `icp-fit-scoring` | Score an account list from zero to one hundred against your ICP and split it into tiers you can route on |
| `company-discovery-list-builder` | Build a company list from a market definition rather than from an existing list, using hiring activity or filing language as the discovery mechanism |
| `linkedin-engager-mining` | Turn the people engaging with relevant posts into a qualified prospect list |
| `clay-people-search-workbook` | Build the full company to contact workbook in Clay: source companies, qualify them, find the right people, waterfall their emails, and export a send ready list |
| `competitor-battlecard` | Build an internal battlecard against one competitor that a rep can use without getting caught out |
| `abm-account-plan` | Build a working plan for one named account: who to reach, in what order, on what trigger, and what has to be true to keep spending time on it |
| `expansion-signal-monitor` | Watch existing customers for the public signals that mean expansion or risk, and act before renewal |
| `crm-enrichment-refresh` | Keep CRM company data current with a scheduled enrichment that only re enriches what actually changed |
| `first-party-data-post` | Turn data you already have into a study nobody else can publish, and get every downstream asset out of one analysis |
| `account-intelligence-brief` | Produce a complete pre call brief on one company: identity, firmographics, social presence, hiring, stack, funding and fit score, with a recommended angle and talk track |

Most premium skills are on a weekly review cycle. Fixes and improvements ship as updates, and buyers receive release notes by email.

The full pack: https://mambabuilt.com/skills

## Shared context

Every skill in this pack reads `BRAND.md`, `ICP.md` and `VOICE.md` from your
project root where they exist. `brand-context-builder` writes all three from one
interview, and output quality compounds across the pack as those files improve.

