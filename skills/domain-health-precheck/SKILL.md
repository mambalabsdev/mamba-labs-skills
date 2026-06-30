---
name: domain-health-precheck
description: |
  Check if a sending domain is safe for cold outreach by scanning SPF, DKIM, DMARC records, and blacklist status. Takes a single domain, calls the Mamba Labs Domain Deliverability Checker MCP server, and returns a plain-English deliverability verdict with pass/fail per check and recommended DNS fixes. Use this skill whenever someone asks about email deliverability, domain health, SPF/DKIM/DMARC setup, whether a domain is blacklisted, whether their sending domain is ready for cold email, or if their email infrastructure is configured correctly. Also trigger when someone says "check my domain" or "am I going to land in spam."
license: MIT
metadata:
  category: deliverability
  tags: [dns, spf, dkim, dmarc, domain-health]
compatibility: [Claude Code, Codex CLI, Cursor, MCP-compatible agents]
version: 1.0.0
---

# Domain Health Pre-Check

Check whether a sending domain is ready for cold outreach. This skill calls the Mamba Labs Domain Deliverability Checker MCP server to scan SPF, DKIM, DMARC records and blacklist status, then returns an actionable verdict.

## Requirements

Install the MCP server and set your Apify token:

```
npx -y @mambalabsdev/mcp-domain-deliverability-checker
```

Environment variable: `APIFY_TOKEN`

## How to Run

1. Get the sending domain from the user (e.g., `outreach.acme.com`).
2. Call the `check_domain_deliverability` tool with that domain.
3. Format the response as a Domain Health Report (see template below).

## Output Template

```
## Domain Health Report: [domain]

**Overall Verdict:** [PASS / WARN / FAIL]

### Record Status
| Check | Status | Value |
|-------|--------|-------|
| SPF   | [Pass/Fail] | [record value or "Missing"] |
| DKIM  | [Pass/Fail] | [selector found or "Not detected"] |
| DMARC | [Pass/Fail] | [policy value or "Missing"] |

### Blacklist Status
[Clean / Listed on X blacklists: list them]

### Catch-All Detection
[Yes / No] - [If yes: "This domain accepts all addresses. Email verification tools cannot confirm whether a specific mailbox exists."]

### Recommended Fixes
[Numbered list of DNS changes needed. If all pass, say "No action needed. This domain is ready for outbound."]
```

## Verdict Logic

- **PASS:** SPF present, DKIM detected, DMARC policy is `quarantine` or `reject`, zero blacklists.
- **WARN:** One record missing or DMARC policy is `none`, or catch-all detected, zero blacklists.
- **FAIL:** Two or more records missing, OR listed on any blacklist.

## Fix Recommendations

When a check fails, provide the exact DNS record to add:

- **Missing SPF:** "Add a TXT record: `v=spf1 include:[sender-provider] ~all`"
- **Missing DMARC:** "Add a TXT record at `_dmarc.[domain]`: `v=DMARC1; p=quarantine; rua=mailto:dmarc@[domain]`"
- **DMARC policy is none:** "Change `p=none` to `p=quarantine` in your DMARC record. A `none` policy tells receivers you are not enforcing authentication."
- **Blacklisted:** "Submit a delisting request at [blacklist provider URL]. This typically takes 24 to 72 hours."

## What This Skill Does NOT Do

- Does not check bulk domain lists. For bulk auditing, see the Cold Email Deliverability Audit skill (paid).
- Does not test inbox placement or sender reputation scores.
- Does not configure DNS records for you.

---

Built by Mamba Labs. Part of a fleet of 12 Apify actors and 13 MCP servers for GTM signal intelligence. Browse the full toolkit at https://mambabuilt.com
