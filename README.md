# 🚀 Claude Code Agent Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A reusable **`.claude/` configuration** that turns Claude Code into a structured, multi-agent software development pipeline — from raw requirement to reviewed, committed code — enforcing a consistent set of engineering rules at every step.

---

## 🗂 Structure

| Folder | What it holds |
|---|---|
| [`.claude/agents/`](./.claude/agents) | Subagents — each with its own tools, model, and single responsibility |
| [`.claude/commands/`](./.claude/commands) | Slash commands — the entry points a user actually types |
| [`.claude/skills/`](./.claude/skills) | Reusable skills — git workflow, reporting, docs sync, format conversion, DB/pattern references |
| [`.claude/rules/`](./.claude/rules) | 14 mandatory rule files every agent must follow |
| [`.claude/hook/`](./.claude/hook) | Automated hooks (audit log, commit-msg guard, secret scan, auto-format, auto-lint...) |

### Agents

| Agent | Role |
|---|---|
| `requirement-analysis` | Turns a raw requirement (text/image/PDF/DOCX...) into a clear purpose/scope/impact analysis, classifies it as a new feature vs. a small fix, and recommends the next step |
| `system-design` | Produces HLD/LLD, data model, API, and reliability/security/performance design for features that need architecture |
| `planner` | Breaks a spec or design doc into traceable tasks (REQ → Task → AC → Test) — plan only, never touches product code |
| `coding-agent` | Implements code per SOLID/DRY/KISS/YAGNI, strictly within the assigned scope |
| `qa-tester` | Designs and executes test cases (equivalence partitioning, boundary values, decision tables...) with full requirement traceability |
| `reviewer` | Independent "fresh eyes" review for code, plans, or test cases — never fixes, only reports |
| `researcher` | Reads widely, answers briefly — local docs first, then web, no fabrication |
| `workspace-auditor` | Finds likely-unneeded files/folders — lists with evidence, never deletes |

### Commands

| Command | Does |
|---|---|
| `/analyze` | Run `requirement-analysis`, then stop and ask whether to continue to `/plan` or go straight to `coding-agent` |
| `/plan` | Full planning pipeline: research → system-design → planner → review → report |
| `/implement` | Hand a task (or `docs/implementation-plan.md`) to `coding-agent` |
| `/test` | Hand a feature/flow to `qa-tester` |
| `/review` | Review the current diff (via the `open-code-review` skill) or a plan/test case (via `reviewer`) |
| `/report` | Produce a change report for recent edits |
| `/commit` | Commit with Conventional Commits, validated by script |
| `/pr` | Create/update a PR — checks for conflicts first |
| `/cleanup` | Delete temp/scratch files Claude created this session |
| `/audit-workspace` | List (never delete) suspicious leftover files in the workspace |

### Skills

| Skill | Purpose |
|---|---|
| `git-workflow` | Gatekeeper for every commit/PR — Conventional Commits, conflict-safe merging |
| `report` | Formats change reports and review reports from already-done work |
| `docs-sync` | Reconciles README/CLAUDE.md/docs against the actual codebase — fixes stale references |
| `cleanup-temp-files` | Removes Claude's own temp files from the current session |
| `markitdown` | Converts PDF/DOCX/PPTX/XLSX/images/... to Markdown |
| `database` | SQL/NoSQL query review, schema/index design, performance analysis |
| `design-patterns` | Reference for the 22 GoF patterns, grouped by when to actually use them |
| `review-web-security` | Web security review (authn/authz, injection, frontend, API, infra...) with evidence, severity, fix, and regression tests |

---

## 🔄 End-to-end workflow

```
/analyze  →  (new feature?) → /plan  →  /implement  →  /test  →  /review  →  /commit  →  /pr
                 │                                        ↑
                 └── (small fix) ─────────────────────────┘
```

Each stage **stops and asks for confirmation** before moving to the next — nothing auto-cascades from analysis straight to a commit. Documents are handed off **by file path** (`docs/requirement-analysis.md` → `docs/system-design.md` → `docs/implementation-plan.md`), not by pasting full text into the next agent's prompt, so context stays small and traceable.

---

## 📐 Core rules (`.claude/rules/`)

Every agent is bound by some or all of 15 rule groups — see [`rules/README.md`](./.claude/rules/README.md) for the full table:

KISS+YAGNI · Clean Code · SRP/Separation of Concerns · DRY · SOLID · Fail-Fast Validation · Data Safety (authz/transactions) · Quality Assurance (test/lint/review) · Boy Scout Rule · Commit Discipline · PR Conflict Safety · Comment Discipline · Database Read-Only by Default · Local-First Search + No Fabrication · Documentation as Code Sync.

`coding-agent` reads all 15 as its system prompt; other agents link to the specific rules relevant to their task.

---

## 🚀 Using this in another project

1. Copy the whole `.claude/` folder into the target project.
2. Merge [`.claude/hook/settings.snippet.json`](./.claude/hook/settings.snippet.json) into the target's `.claude/settings.json` (see [`hook/README.md`](./.claude/hook/README.md)).
3. Make sure `jq` is installed (required by most hooks) — missing tools degrade gracefully, hooks just skip.
4. Start with `/analyze "<your requirement>"` or jump straight to `/plan` if the requirement is already clear.

---

## 🤝 Contributing

Open a PR if you have a rule, agent, or skill worth adding — keep each one single-purpose and link it from the relevant table above.

**License**: [MIT](./LICENSE)
