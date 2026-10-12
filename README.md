# Mamba Labs Skills

[![skills.sh](https://skills.sh/b/mambalabsdev/mamba-labs-skills)](https://skills.sh/mambalabsdev/mamba-labs-skills)

Free skills that teach AI agents to run signal based go to market work. Built from production campaigns and wired to live data, not prompt text.

**56 free skills, 12 families, 10 packs.**

## Install

As a Claude Code plugin marketplace:

```
/plugin marketplace add mambalabsdev/mamba-labs-skills
```

With the skills CLI, for any agent that reads `SKILL.md`:

```
npx skills add mambalabsdev/mamba-labs-skills
```

As a Gemini CLI extension:

```
gemini extensions install https://github.com/mambalabsdev/mamba-labs-skills
```

Or drop any skill folder into `~/.claude/skills/`. Every skill is a single
`SKILL.md` and works in Claude Code, Codex CLI, Cursor and other MCP compatible
agents.

## What every skill does before it returns

- Skills that read live data call the Mamba Labs MCP server (`@mambalabsdev/mcp-gtm-suite`,
  pinned to an exact version) with your own Apify token, or a direct Apify script where
  the actor has no MCP tool.
- Each skill checks its own output with `scripts/check-output.py` and reports a half empty
  result as incomplete rather than returning it as finished.
- Skills that send, post, or write stop for your approval first.
- Every skill opens with a Requirements table: each account, key or service it needs,
  provider by provider, and what each one costs you. The line after each skill below
  is the same summary.

## Shared context

Each skill reads the files its Shared context section names, from `BRAND.md`, `ICP.md`
and `VOICE.md`, where they exist, so you stop repeating yourself. `brand-context-builder`
writes all three from one interview and every other skill gets sharper from it.

## Review cadence

Every free skill sits on a 30 day review cycle. Fixes and improvements ship as repo updates.

## Skills by family

### Signal research

- [`ai-adoption-signal-reader`](skills/ai-adoption-signal-reader): Detect whether a company has shipped AI features or adopted AI vendors, and read that as a budget and priority signal. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`event-presence-prospecting`](skills/event-presence-prospecting): Find which conferences a company sponsors, exhibits at, or speaks at, and use that as a budget and audience signal. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`hiring-signal-spotter`](skills/hiring-signal-spotter): Read a company's open roles as a buying signal and turn them into an outreach angle. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`job-board-keyword-scanner`](skills/job-board-keyword-scanner): Scan a company's job postings for the specific words that indicate a problem your product solves. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`outbound-stack-fingerprint`](skills/outbound-stack-fingerprint): Detect whether a company runs cold outbound, which tools it sends with, and how many sending domains it operates. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`public-award-prospecting`](skills/public-award-prospecting): Find companies that just won a government contract or public grant and reach them while the money is new. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`tech-stack-signal-reader`](skills/tech-stack-signal-reader): Detect which tools a company runs from its own website and turn the stack into a qualification and an angle. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`workplace-program-signal`](skills/workplace-program-signal): Detect which workplace programs and benefits a company runs, as a signal for anyone selling into people operations, benefits or internal communications. Needs an Apify token (usage billed to your Apify account); Python 3.

### Identity and enrichment

- [`company-identity-resolution`](skills/company-identity-resolution): Resolve a messy company name to the right domain and canonical record, and say how confident the match is. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`contact-classification`](skills/contact-classification): Classify contacts by department, seniority and role from their job title, and route them to the right persona. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`firmographic-enrichment`](skills/firmographic-enrichment): Fill headcount, industry, headquarters and revenue band on a company list, and report honestly which fields actually filled. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`icp-definition-builder`](skills/icp-definition-builder): Turn a description of a business into a structured ideal customer profile with firmographic criteria, signals, pain indicators and exclusion rules. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`legal-entity-resolution`](skills/legal-entity-resolution): Resolve a company domain to its registered legal entity, company number and tax identifier. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`linkedin-url-resolution`](skills/linkedin-url-resolution): Turn a list of company domains into company profile URLs, and fill the gaps a native enrichment leaves behind. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`people-finder-recipe`](skills/people-finder-recipe): Find the right people at a list of companies without pulling a hundred irrelevant contacts per account. Needs an Apify token (usage billed to your Apify account); Python 3; Serper API key. Optional: one of Prospeo API key or Icypeas API key; one of Reoon API key or BounceBan API key.

### Clay builds

- [`clay-actor-column-wiring`](skills/clay-actor-column-wiring): Wire an external actor or API into a Clay column so the types survive the round trip. Needs a Clay workspace.
- [`clay-conditional-gates`](skills/clay-conditional-gates): Write the run conditions that stop expensive Clay columns from firing on rows that will never qualify. Needs a Clay workspace.
- [`clay-cost-audit`](skills/clay-cost-audit): Price a Clay table before it runs and find the columns that are burning credits for no return. Needs a Clay workspace.
- [`clay-credit-forecast`](skills/clay-credit-forecast): Forecast how far a Clay credit balance goes across a month of planned builds, and say which build to cut when it does not reach. Needs a Clay workspace.
- [`clay-dedupe-and-merge`](skills/clay-dedupe-and-merge): Deduplicate and merge people or company rows across Clay tables without losing enrichment or double counting a person. Needs a Clay workspace.
- [`clay-failure-triage`](skills/clay-failure-triage): Diagnose a Clay column that returns null, zero rows, or the wrong shape, by symptom rather than by guesswork. Needs a Clay workspace.

### Outbound email

- [`cold-email-structure-checker`](skills/cold-email-structure-checker): Audit a cold email draft against a seven point outbound framework and return a pass or fail scorecard with a rewritten version. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`merge-variable-linter`](skills/merge-variable-linter): Check that every merge variable in a sequence resolves against the fields actually present on the rows, before the campaign sends. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`outbound-copy-humanizer`](skills/outbound-copy-humanizer): Rewrite outbound copy so it reads like a person wrote it, removing the tells that mark a message as generated. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`sending-capacity-planner`](skills/sending-capacity-planner): Work out how many contacts a set of sending accounts can actually reach per week, and how long a list will take to work through. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`sequencer-campaign-config`](skills/sequencer-campaign-config): Configure a sending platform campaign correctly the first time: schedule, tracking, limits, timezone and the fields that silently reset. Needs an Apify token (usage billed to your Apify account); Node.js 18+; Instantly v2 or Smartlead API key.
- [`subject-line-lab`](skills/subject-line-lab): Generate and screen cold email subject lines against truncation, spam triggers and the preview text they create. Needs no account, key or paid service: it works from the files, exports and answers you give it.

### Agency operations

- [`brand-context-builder`](skills/brand-context-builder): Interview once and write the shared context files that every other skill reads. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`friction-log-to-rules`](skills/friction-log-to-rules): Turn the things that went wrong in a working session into standing rules that stop them recurring. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`mamba-gtm-router`](skills/mamba-gtm-router): Route a plain language go to market request to the right skill, and name the ones that would help but are not installed. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`partner-sourcing-plan`](skills/partner-sourcing-plan): Find the partners whose customers are your buyers, and structure the first conversation so it produces something. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`work-order-writer`](skills/work-order-writer): Write a work order an agent or a contractor can execute end to end without asking a question. Needs no account, key or paid service: it works from the files, exports and answers you give it.

### SEO and content

- [`agent-readability-audit`](skills/agent-readability-audit): Check whether a website can be read and used by AI agents, and fix what blocks them. Needs an Apify token (usage billed to your Apify account); Node.js 18+.
- [`comparison-page-builder`](skills/comparison-page-builder): Write a comparison or alternatives page that a reader trusts and a competitor cannot get taken down. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`content-brief-builder`](skills/content-brief-builder): Write a content brief a writer can execute without inventing the substance, including where the non generic part comes from. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`directory-submission-plan`](skills/directory-submission-plan): Pick the directories and marketplaces worth listing on, and prepare one set of assets that fits all of them. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`publishing-cadence-reader`](skills/publishing-cadence-reader): Measure how often a company actually publishes and read that as a content investment signal. Needs an Apify token (usage billed to your Apify account); Node.js 18+.

### Deliverability

- [`bounce-and-catchall-policy`](skills/bounce-and-catchall-policy): Decide what to do with catch all domains, role addresses and soft bounces before they cost you a domain. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`domain-health-precheck`](skills/domain-health-precheck): Check whether one sending domain is safe for cold outreach by reading its SPF, DKIM and DMARC records and its blacklist status. Needs an Apify token (usage billed to your Apify account); Node.js 18+. Optional: DNS access at your registrar, to apply the fixes.
- [`domain-warmup-planner`](skills/domain-warmup-planner): Plan the warmup ramp for new sending domains and inboxes so real campaign volume starts on the date it is needed. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`unsubscribe-compliance-check`](skills/unsubscribe-compliance-check): Check that outbound campaigns carry a working unsubscribe path and that opt outs land somewhere that actually stops the next send. Needs access to your sending platform (Instantly, Smartlead or similar); seed inboxes at Gmail, Microsoft and Yahoo that you control, or an inbox placement test service.

### Sales enablement

- [`customer-research-interview`](skills/customer-research-interview): Run customer interviews that produce usable language instead of agreement, and turn the transcripts into a sharper ICP. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`objection-handling-library`](skills/objection-handling-library): Build an objection library from the replies you actually received, with a tested response per objection. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`positioning-statement`](skills/positioning-statement): Write a positioning statement that names the real alternative and survives contact with a sales call. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`sales-one-pager`](skills/sales-one-pager): Write the one page document a prospect forwards internally to the person who has to approve. Needs no account, key or paid service: it works from the files, exports and answers you give it.

### Small business operations

- [`cash-runway-snapshot`](skills/cash-runway-snapshot): Work out how many months of cash are left and what actually changes it. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`invoice-chaser`](skills/invoice-chaser): Chase overdue invoices on a fixed escalation ladder that gets paid without damaging the relationship. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`monday-morning-brief`](skills/monday-morning-brief): Produce the weekly operating brief: what moved, what is at risk, and the three things that need a decision. Needs connectors in your agent for the sources the brief reads (calendar, mail, CRM, finance, tracker).
- [`weekly-pipeline-review`](skills/weekly-pipeline-review): Run a weekly pipeline review that finds the deals that are quietly dying rather than admiring the big ones. Needs read access to your CRM, or an export of the records.

### Knowledge operations

- [`handoff-writer`](skills/handoff-writer): Write the handoff that lets the next person or the next session continue without re deriving anything. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`knowledge-write-discipline`](skills/knowledge-write-discipline): Write to a knowledge base so the document is findable later and provably stored. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`results-doc-verifier`](skills/results-doc-verifier): Check a results write up for claims that were asserted rather than verified, before anyone acts on it. Needs no account, key or paid service: it works from the files, exports and answers you give it.

### LinkedIn

- [`linkedin-comment-strategy`](skills/linkedin-comment-strategy): Decide which posts to comment on and write comments that do something other than agree. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`linkedin-post-writer`](skills/linkedin-post-writer): Write a LinkedIn post that sounds like the person and earns a reason to exist. Needs no account, key or paid service: it works from the files, exports and answers you give it.
- [`linkedin-profile-optimizer`](skills/linkedin-profile-optimizer): Rewrite a profile so it converts the visits that outbound and commenting send to it. Needs no account, key or paid service: it works from the files, exports and answers you give it.

### CRM operations

- [`crm-hygiene-sweep`](skills/crm-hygiene-sweep): Run a recurring cleanup on new and changed CRM records so the database stops degrading between audits. Needs read access to your CRM, or an export of the records.

## Packs

A pack is a job, not a category: the free skills that get you started plus the
premium skills that finish it.

| Pack | Free here | Premium | Pack price | The job |
| --- | --- | --- | --- | --- |
| [The Cold Email System](packs/cold-email-system.md) | 12 | 8 | 29 USD | Everything between a list and a reply, in the order it has to happen. |
| [The Clay Operator](packs/clay-operator.md) | 15 | 5 | 19 USD | Build tables that produce rows you can send to, at a cost you decided in advance. |
| [Signal Based Selling](packs/signal-based-selling.md) | 14 | 13 | 49 USD | Reach accounts at the moment something changed, with a message about the change. |
| [The Deliverability Pack](packs/deliverability.md) | 8 | 3 | 14.99 USD | Get the mail delivered, and know why when it is not. |
| [LinkedIn Authority](packs/linkedin-authority.md) | 6 | 2 | 12.99 USD | Post, comment and connect in a way that makes the outbound land. |
| [The SEO And Content Engine](packs/seo-content-engine.md) | 8 | 3 | 9.99 USD | Pages and posts that exist because there is something on them worth reading. |
| [CRM Operations](packs/crm-operations-pack.md) | 4 | 7 | 24 USD | Make the pipeline report mean something, then keep it that way. |
| [Small Business Operations](packs/small-business-operations.md) | 6 | 1 | 19 USD | The weekly and monthly routines a small company actually has to run. |
| [Agency Delivery](packs/agency-delivery.md) | 15 | 16 | 59 USD | Run client work so the first argument is about a written line rather than a memory. |
| [Knowledge Operations](packs/knowledge-ops-pack.md) | 7 | 1 | 19 USD | Write things down so the next person, or the next session, does not start over. |

## Premium catalog

35 premium skills, sold at https://mambabuilt.com/store: 11 at 9.99 USD, 13 at 7.99 USD, 11 at 5.99 USD. The full catalog bundle, all 35 premium skills, is 99 USD.

## More

Premium skills and packs: https://mambabuilt.com/skills

The live data behind the signal skills runs on the Mamba Labs actor fleet:
https://apify.com/mambalabs

## License

MIT. See LICENSE.

