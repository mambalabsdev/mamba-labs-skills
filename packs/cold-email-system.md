# The Cold Email System

**Everything between a list and a reply, in the order it has to happen.**

## Who it is for

Founders and teams running their own outbound who keep rebuilding the same campaign and getting a different result.

## The problem

Cold email fails in five places and only one of them is the copy. The list is not suppressed, the variables do not resolve, capacity was estimated from first touches, the exit gate does not cover every channel, and nobody set a stop rule. Each failure is invisible until the send.

## What is in it

This pack is the sequence of gates a campaign passes through before it is allowed to send, plus the copy work that happens inside those gates. The free skills fix one email and one setting. The paid skills encode the system: the whole sequence with its exit gate, the suppression layer that holds across channels, the reactivation motion, and the launch precheck that blocks a wave rather than blessing it.

## Free skills in this pack

Install in this order. Each assumes the ones above it have run at least once.

| # | Skill | What it does |
| --- | --- | --- |
| 1 | [`brand-context-builder`](../skills/brand-context-builder) | Interview once and write the shared context files that every other skill reads |
| 2 | [`cold-email-structure-checker`](../skills/cold-email-structure-checker) | Audit a cold email draft against a seven point outbound framework and return a pass or fail scorecard with a rewritten version |
| 3 | [`subject-line-lab`](../skills/subject-line-lab) | Generate and screen cold email subject lines against truncation, spam triggers and the preview text they create |
| 4 | [`outbound-copy-humanizer`](../skills/outbound-copy-humanizer) | Rewrite outbound copy so it reads like a person wrote it, removing the tells that mark a message as generated |
| 5 | [`merge-variable-linter`](../skills/merge-variable-linter) | Check that every merge variable in a sequence resolves against the fields actually present on the rows, before the campaign sends |
| 6 | [`sequencer-campaign-config`](../skills/sequencer-campaign-config) | Configure a sending platform campaign correctly the first time: schedule, tracking, limits, timezone and the fields that silently reset |
| 7 | [`sending-capacity-planner`](../skills/sending-capacity-planner) | Work out how many contacts a set of sending accounts can actually reach per week, and how long a list will take to work through |
| 8 | [`objection-handling-library`](../skills/objection-handling-library) | Build an objection library from the replies you actually received, with a tested response per objection |
| 9 | [`domain-health-precheck`](../skills/domain-health-precheck) | Check whether one sending domain is safe for cold outreach by reading its SPF, DKIM and DMARC records and its blacklist status |
| 10 | [`bounce-and-catchall-policy`](../skills/bounce-and-catchall-policy) | Decide what to do with catch all domains, role addresses and soft bounces before they cost you a domain |
| 11 | [`unsubscribe-compliance-check`](../skills/unsubscribe-compliance-check) | Check that outbound campaigns carry a working unsubscribe path and that opt outs land somewhere that actually stops the next send |
| 12 | [`mamba-gtm-router`](../skills/mamba-gtm-router) | Route a plain language go to market request to the right skill, and name the ones that would help but are not installed |

Every free skill sits on a 30 day review cycle. Fixes and improvements ship as repo updates.

## Premium skills in this pack

These encode the system rather than the single task. They are not in this repo.

| Skill | Price | What it does |
| --- | --- | --- |
| `cold-email-sequence-system` | 9.99 USD | Build a complete multi step cold email sequence with per step angles, timing, exit rules and merge variables that actually resolve |
| `suppression-architect` | 9.99 USD | Design the suppression layer so a contact who should never be emailed cannot be emailed from any campaign or channel |
| `multichannel-enrollment-rules` | 5.99 USD | Set the rules that let email and social outreach run on the same prospect without double touching or double counting them |
| `reply-classifier-router` | 5.99 USD | Classify inbound replies to outbound campaigns and route each one to the right next action, with a draft reply where a draft is appropriate |
| `reactivation-campaign-builder` | 7.99 USD | Rework a list of previously contacted prospects into a compliant reactivation campaign, with cooldown windows, field coverage checks and copy that acknowledges the prior contact |
| `wave-launch-precheck` | 9.99 USD | Run the pre launch check on a campaign wave and either clear it or block it with a named reason |
| `clay-waterfall-designer` | 7.99 USD | Design a work email waterfall that finds the most addresses for the least money, with verification placed where it actually protects the send |
| `linkedin-connection-campaign` | 9.99 USD | Run a connection and message campaign that stays inside platform limits, does not double touch a prospect, and hands off cleanly to email |

Most premium skills are on a weekly review cycle. Fixes and improvements ship as updates, and buyers receive release notes by email.

The full pack, every premium skill above plus the free ones: 29 USD at https://mambabuilt.com/store

## Shared context

Every skill in this pack reads `BRAND.md`, `ICP.md` and `VOICE.md` from your
project root where they exist. `brand-context-builder` writes all three from one
interview, and output quality compounds across the pack as those files improve.

