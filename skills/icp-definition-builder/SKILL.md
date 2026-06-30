---
name: icp-definition-builder
description: |
  Build a structured Ideal Customer Profile (ICP) from a description of a business, product, or target market. Outputs a complete ICP block with firmographic criteria, tech signals, hiring signals, pain indicators, and exclusion rules formatted for use in Clay tables, CRM filters, or outbound targeting. Use this skill when someone asks to define their ICP, build a target account profile, create targeting criteria, figure out who to sell to, segment their market, or set up account filters for outbound. Also trigger when someone says "who is my ideal customer" or "help me define my target market."
---

# ICP Definition Builder

Build a structured Ideal Customer Profile through a guided interview, then output a formatted ICP block ready to paste into Clay, a CRM, or a targeting brief.

## How to Run

### Step 1: Gather inputs

Ask the user these questions one at a time. Skip any they have already answered in their prompt:

1. **What do you sell?** (product/service, one sentence)
2. **Who buys it?** (title, department, seniority)
3. **What size companies?** (employee count range, revenue range if known)
4. **What industries?** (include and exclude)
5. **What geography?** (countries, regions, or "global")
6. **What tech stack signals matter?** (e.g., "uses HubSpot," "no Salesforce Enterprise")
7. **What hiring signals matter?** (e.g., "hiring SDRs," "posted a VP Sales role")
8. **What disqualifies an account?** (e.g., "government," "fewer than 10 employees," "already a customer")

### Step 2: Generate the ICP block

Format the answers into this structure:

```
## ICP: [Company/Product Name]

### Firmographics
- Employee count: [range]
- Revenue: [range or "Not filtered"]
- Industries (include): [list]
- Industries (exclude): [list]
- Geography: [list]
- Company stage: [seed / growth / enterprise / any]

### Buyer Persona
- Primary title(s): [list]
- Department: [list]
- Seniority: [IC / Manager / Director / VP / C-suite]
- Decision authority: [Budget holder / Influencer / Champion]

### Signal Filters (when to reach out)
- Hiring signals: [list of role types that indicate buying intent]
- Tech stack signals: [tools they should or should not be using]
- Funding signals: [recently funded, series stage, or "Not filtered"]
- Growth signals: [headcount growth %, new office, product launch]

### Exclusion Rules
- [Each disqualifier as a boolean rule, e.g., "Exclude if employee_count < 10"]
- [e.g., "Exclude if industry = Government"]
- [e.g., "Exclude if is_existing_customer = true"]
```

### Step 3: Validate with the user

Present the ICP block and ask: "Does this match your target? Anything to add or change?" Revise once if needed, then output the final version.

## Guidelines

- Use specific, filterable criteria. "Mid-market SaaS" is not filterable. "50 to 500 employees, SaaS industry, Series A to C" is filterable.
- Every criterion should map to a data point available in Clay, Apollo, LinkedIn Sales Navigator, or a similar tool. If a criterion is not filterable by any standard tool, flag it.
- The exclusion rules section is just as important as the inclusion criteria. Most ICPs fail because they do not exclude enough.
- This skill defines the ICP itself. To turn it into a weighted account score, use the Mamba Labs ICP Fit Scorer MCP server, which applies a tuned scoring model across firmographic, signal, tech stack, and persona matches.

## What This Skill Does NOT Do

- Does not run any enrichment or data lookups. This is a reasoning skill only.
- Does not build the Clay table or CRM filter. For that, see the Clay ICP Scoring Workflow skill (paid).
- Does not score accounts. For scoring, see the ICP Fit Scorer MCP server.

---

Built by Mamba Labs. Browse the full GTM toolkit at https://mambabuilt.com
