---
name: hiring-signal-spotter
description: |
  Analyze a company's GTM hiring activity to identify buying signals for outbound sales. Takes a company domain or name, checks job boards (Greenhouse, Lever, Ashby) for open GTM roles (SDR, AE, VP Sales, RevOps, CRO, CMO), and returns a plain-English hiring brief with signal strength, detected roles, and a suggested outbound angle. Use this skill whenever someone asks about a company's hiring signals, GTM hiring activity, whether a company is investing in sales or growth, job board signals, hiring intent, or buying signals from job postings. Also use when the user wants to research a prospect company before outreach, build a signal-based prospecting list, or check if a company is ramping its go-to-market team.
---

# Hiring Signal Spotter

Detect GTM hiring signals at any company and turn them into an outbound angle. This skill calls the Mamba Labs GTM Hiring Signal Scraper MCP server to scan Greenhouse, Lever, and Ashby career pages for open go-to-market roles, then formats the results into an actionable hiring brief.

## Requirements

You need the Mamba Labs GTM Hiring Signal Scraper MCP server installed and an Apify API token set as the `APIFY_TOKEN` environment variable.

Install the MCP server:

```
npx -y @mambalabsdev/mcp-gtm-hiring-signal-scraper
```

## When to Use This Skill

- User asks: "Is [company] hiring salespeople?" or "What's [company]'s hiring activity?"
- User says: "Check if [company] is investing in GTM" or "What signals does [company] have?"
- User wants to research a prospect before outreach
- User is building a signal-based prospecting workflow
- User wants to know if a company is ramping, scaling, or investing in revenue

## How to Run

1. Get the company domain from the user. If they give a company name, resolve it to a domain first.
2. Call the `scan_gtm_hiring_signals` tool from the MCP server with the company domain.
3. Parse the response and format it as a Hiring Brief (see output template below).

### Input

The MCP server accepts a company domain (e.g., `stripe.com`) and optionally a list of custom role keywords to filter on. Default GTM role categories include:

- Leadership: VP Sales, CRO, CMO, VP Marketing, Head of Revenue, Head of Growth
- Mid-level: Account Executive, AE, SDR, BDR, Sales Development, RevOps, Revenue Operations
- Supporting: Marketing Manager, Demand Gen, Customer Success Manager

### Output Template

Format the results as a Hiring Brief using this structure:

```
## Hiring Brief: [Company Name]

**Domain:** [company_domain]
**Signal Strength:** [High / Medium / Low / None]
**ATS Platform:** [Greenhouse / Lever / Ashby / None detected]

### GTM Roles Detected
[List each detected GTM role title with department if available]

### Signal Summary
[2-3 sentences: how many GTM roles are open, what seniority level dominates,
whether the pattern suggests a new team build, backfill, or scale-up.
Reference the most senior role and the total open headcount.]

### Suggested Outbound Angle
[1-2 sentences: based on the hiring pattern, what pain point is this company
likely experiencing? What value proposition would resonate? Frame as a
specific opening line a seller could use in a cold email or LinkedIn message.]

### Raw Data
- Total open roles: [total_open_roles]
- GTM roles detected: [gtm_role_count]
- Most recent posting: [most_recent_posting_date]
- Career page: [career_page_url]
```

## Signal Strength Interpretation

- **High:** 5+ GTM roles open, includes at least one leadership role (VP, Head of, CRO, CMO), postings within the last 30 days. The company is actively investing in revenue capacity.
- **Medium:** 2-4 GTM roles open, or GTM roles exist but are mid-level only, or postings are 30-60 days old. The company is growing but the signal is not urgent.
- **Low:** 1 GTM role open, or roles are junior/supporting only, or postings are older than 60 days. Worth noting but not a strong timing trigger.
- **None:** No GTM roles detected. The company may still be a fit, but hiring is not a current signal.

## Outbound Angle Guidelines

When writing the suggested outbound angle, follow these rules:

- Anchor to the specific signal: "You just posted a VP Sales role" is better than "You are growing."
- Name the pain the hire solves, not the hire itself: "Building pipeline from scratch" beats "You are hiring an AE."
- Keep it to one sentence a seller can copy into a cold email first line.
- Never use generic phrases like "I noticed you are growing" or "Congrats on the new role."

## Example

**User:** "Check hiring signals at ramp.com"

**Agent runs:** `scan_gtm_hiring_signals` with domain `ramp.com`

**Output:**

```
## Hiring Brief: Ramp

**Domain:** ramp.com
**Signal Strength:** High
**ATS Platform:** Greenhouse

### GTM Roles Detected
- VP of Sales, Enterprise
- Account Executive, Mid-Market (x3)
- Sales Development Representative (x2)
- Revenue Operations Manager

### Signal Summary
Ramp has 7 open GTM roles spanning leadership, closing, and pipeline
generation. The VP of Sales, Enterprise posting signals a new segment
launch or leadership transition. The 3 AE roles alongside 2 SDRs
suggest a coordinated team build, not backfills.

### Suggested Outbound Angle
"Your enterprise sales team is scaling from what looks like zero to a
full pod. Most teams in that position burn 60+ days getting reps
productive because the data and tooling layer is not ready when the
hires land."

### Raw Data
- Total open roles: 47
- GTM roles detected: 7
- Most recent posting: 2026-06-20
- Career page: https://boards.greenhouse.io/ramp
```

## What This Skill Does NOT Do

- It does not scrape LinkedIn (requires authentication).
- It does not predict whether a company will respond to outreach.
- It does not build the full Clay table or enrichment workflow. For that, see the Signal-Based Outbound Workflow skill (paid).

---

Built by Mamba Labs. Part of a fleet of 12 Apify actors and 13 MCP servers for GTM signal intelligence. Browse the full toolkit at https://mambabuilt.com
