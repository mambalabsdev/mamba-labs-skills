# Contributing

This repo follows the same SKILL.md standard as [anthropics/skills](https://github.com/anthropics/skills).

## Propose a new skill

1. Fork the repo and create a folder under `skills/<your-skill-name>/`.
2. Add a `SKILL.md` with YAML frontmatter at the top:
   - `name`: the skill folder name (kebab-case).
   - `description`: what the skill does and when an agent should trigger it. Include the natural-language phrases a user might say.
3. Optional supporting folders inside the skill directory:
   - `references/` for background docs the skill reads at runtime.
   - `scripts/` for runnable helper scripts.
   - `templates/` for output templates or boilerplate.
4. Keep the skill self-contained. If it depends on an MCP server, reference that server by name in the SKILL.md.
5. Open a pull request describing the job the skill does and a sample invocation.

## Report an issue with an existing skill

Open a GitHub issue and include:
- The skill name.
- What you asked the agent to do and what happened.
- The expected behavior.
- Your agent and platform (Claude Code, Codex CLI, Cursor, or other).

## Style

- American English spelling.
- Do not use em dashes or en dashes in skill content, comments, or docs.

## What may appear in a skill in this repo

Skills here are published free. What they may and may not contain is a standing rule,
last amended 2026-08-22.

Allowed: the job to be done, the method, the output format, the reasoning, public Apify
actor slugs, Apify Store URLs, and runnable actor input examples.

Not allowed: scoring weights and weight tables, provider waterfall order logic, Clay
formulas and column expressions, client names, internal hostnames, internal project
references, and anything resembling a credential.

The check that enforces this lives in the build repo and self tests before it sweeps, so
a clean result is only reported when the check could have failed.
