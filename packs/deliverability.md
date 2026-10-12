# The Deliverability Pack

**Get the mail delivered, and know why when it is not.**

## Who it is for

Anyone sending cold email from domains they cannot afford to burn.

## The problem

Deliverability is treated as a content problem and it is usually an infrastructure problem. The diagnosis order is what costs weeks: teams rewrite copy while a blocked record or an unwarmed inbox is the actual cause.

## What is in it

One free skill checks a single domain and gives you the literal records to publish. The rest of the pack scales that to a whole estate: an audit that groups failures by cause, a warmup plan that works backward from the campaign date, a compliance check that tests the opt out end to end, and a triage that separates infrastructure from content from list before anyone touches the copy.

## Free skills in this pack

Install in this order. Each assumes the ones above it have run at least once.

| # | Skill | What it does |
| --- | --- | --- |
| 1 | [`brand-context-builder`](../skills/brand-context-builder) | Interview once and write the shared context files that every other skill reads |
| 2 | [`domain-health-precheck`](../skills/domain-health-precheck) | Check whether one sending domain is safe for cold outreach by reading its SPF, DKIM and DMARC records and its blacklist status |
| 3 | [`domain-warmup-planner`](../skills/domain-warmup-planner) | Plan the warmup ramp for new sending domains and inboxes so real campaign volume starts on the date it is needed |
| 4 | [`sending-capacity-planner`](../skills/sending-capacity-planner) | Work out how many contacts a set of sending accounts can actually reach per week, and how long a list will take to work through |
| 5 | [`bounce-and-catchall-policy`](../skills/bounce-and-catchall-policy) | Decide what to do with catch all domains, role addresses and soft bounces before they cost you a domain |
| 6 | [`unsubscribe-compliance-check`](../skills/unsubscribe-compliance-check) | Check that outbound campaigns carry a working unsubscribe path and that opt outs land somewhere that actually stops the next send |
| 7 | [`outbound-stack-fingerprint`](../skills/outbound-stack-fingerprint) | Detect whether a company runs cold outbound, which tools it sends with, and how many sending domains it operates |
| 8 | [`mamba-gtm-router`](../skills/mamba-gtm-router) | Route a plain language go to market request to the right skill, and name the ones that would help but are not installed |

Every free skill sits on a 30 day review cycle. Fixes and improvements ship as repo updates.

## Premium skills in this pack

These encode the system rather than the single task. They are not in this repo.

| Skill | Price | What it does |
| --- | --- | --- |
| `suppression-architect` | 9.99 USD | Design the suppression layer so a contact who should never be emailed cannot be emailed from any campaign or channel |
| `email-deliverability-audit` | 9.99 USD | Audit an entire sending infrastructure across every domain and inbox, rank the failures by risk, and produce the fix list in the order that recovers deliverability fastest |
| `inbox-placement-triage` | 9.99 USD | Diagnose why a campaign that used to get replies is now landing in spam, and separate an infrastructure cause from a content cause from a list cause |

Most premium skills are on a weekly review cycle. Fixes and improvements ship as updates, and buyers receive release notes by email.

The full pack, every premium skill above plus the free ones: 14.99 USD at https://mambabuilt.com/store

## Shared context

Each skill in this pack reads the files its Shared context section names, from
`BRAND.md`, `ICP.md` and `VOICE.md`, where they exist. `brand-context-builder` writes
all three from one interview, and output quality compounds as those files improve.

