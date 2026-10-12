---
name: people-finder-recipe
description: |
  Find the right people at a list of companies without pulling a hundred irrelevant contacts per account. Use when someone needs contacts at target accounts, wants to cap contacts per company, or is building a people list from a company list.
license: MIT
compatibility: "Claude Code, Claude Desktop, Codex CLI, Cursor, Gemini CLI, and other agents that read SKILL.md. Live data steps need Node.js 18 or newer and an Apify API token."
tags: [clay_operator, identity_enrichment]
metadata:
  title: "People Finder Recipe"
  category: "identity-enrichment"
  tags: "clay_operator, identity_enrichment"
  keywords: "identity, find contacts at these companies, who works at this company, build a people list from company list, cap contacts per account, find the buyer"
  version: "2.1.0"
---

# People Finder Recipe

## What this does

An uncapped people search returns whoever the source has most of, which is rarely the buyer. This skill sets the per company cap and the title filter before the search runs, uses the company's own team page as a second source where the database is thin, and reports contacts per company so a skewed distribution is visible.

## When to use it

- find contacts at these companies
- who works at this company
- build a people list from company list
- cap contacts per account
- find the buyer

## Inputs

- **companies**: the company list with domains
- **titles**: target titles and titles to exclude
- **cap**: maximum contacts per company

## Shared context this skill reads

Before doing anything else, read whichever of these exist at the project root and
use them instead of asking the user to repeat themselves:

- `ICP.md`

If none exist, do the work from what the user gives you, then offer to write the
missing file so the next skill in the pack starts warmer.

## Tool connection

Two complementary sources: a database backed people search, and a direct extraction from the company's own team page, which often carries the people a database is missing at smaller companies.

| Actor | MCP tool | Used for | Store page |
| --- | --- | --- | --- |
| People Finder and Email Verifier | none, use `scripts/apify-run.py` | people search by company with title and seniority filters | https://apify.com/mambalabs/people-finder |
| Team Page People Extractor | none, use `scripts/apify-run.py` | people extracted directly from a company team or leadership page | https://apify.com/mambalabs/team-page-people-extractor |

These actors have no MCP tool. Call them directly:

```
APIFY_TOKEN=<your token> python3 scripts/apify-run.py people-finder [input.json]
APIFY_TOKEN=<your token> python3 scripts/apify-run.py team-page-people-extractor [input.json]
```

With no input file the script runs the example in `scripts/inputs/`. It exits non zero
on a failed or empty run, so an empty result is never read as an answer.

**Cost line.** Before any live call, state how many calls you plan and which actors
they bill. After the run, report the calls made, the calls that failed, and the Apify
usage where the tool reports it. Each actor bills the user's own Apify account at its
Store price.

**No token, no live data.** If no Apify token is available, say so and stop the live
steps. Never fill a live section from memory and present it as live.

## Method

1. Set the cap first. Contacts per company is a budget decision and an uncapped search will spend it on the largest company in the list.
2. Write the exclusion list before the inclusion list. Interns, assistants, advisors and alumni are the bulk of the noise and they are cheap to exclude.
3. Run the database search, then fall back to the team page extraction for companies that returned fewer than the cap. Smaller companies are systematically under represented in databases and well represented on their own site.
4. Report contacts per company as a distribution, not an average. An average of three hides a list where one company contributed forty.
5. Deduplicate people across companies before enrichment, because the same person appears at two companies during a job change.
6. Verify the position before enriching an email, so the waterfall is not spent on people who left.
7. Check the output with `scripts/check-output.py` before you return it.

## Approval stop

This skill does not send email or write to a CRM. If the user asks it to, stop first:
show what would be sent or written and wait for an explicit yes.

## Output

The people list with company, title, source and confidence; the per company distribution; the companies that returned nothing; and the dedupe count.

## Check the output before you return it

Save the output to a file and run `python3 scripts/check-output.py <file>`. The
contract it checks is `scripts/output-contract.json`.

- Exit 0, `COMPLETE`: return the output.
- Exit 2, `INCOMPLETE`: do not present the output as finished. Fill what you can, run
  the check again, and if parts stay missing, return the output under the heading
  `Incomplete` with every reason the check printed.

## Quality bar

- The per company cap is set before the search
- Exclusions are written before inclusions
- Team page fallback is used for under filled companies
- Contacts per company is reported as a distribution
- People are deduplicated before any paid enrichment

## Related skills

- `contact-classification`
- `clay-waterfall-designer`
- `clay-people-search-workbook`

Ships in the **clay-operator** pack.
