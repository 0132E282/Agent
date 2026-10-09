# Shared Agent Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A reusable **`.claude/` configuration** that turns Claude Code into a structured, multi-agent software development pipeline — from raw requirement to reviewed, committed code — enforcing a consistent set of engineering rules at every step.

---

## 🗂 Structure

| Folder | What it holds |
|---|---|
| [`AGENTS.md`](./AGENTS.md) | Codex instructions referencing the shared conventions and rules |
| [`.agents/rules/`](./.agents/rules) | Canonical shared Markdown rules for Claude and Codex |
| [`.agents/skills/`](./.agents/skills) | Canonical shared skills and workflow adapters, discovered by Codex |
| [`.codex/agents/`](./.codex/agents) | Codex custom agents in TOML, inheriting the session model |
| [`.codex/rules/`](./.codex/rules) | Link to `.agents/rules/`, loaded through AGENTS.md |
| [`.codex/skills/`](./.codex/skills) | Convenience link to `.agents/skills/`; Codex discovery remains in `.agents/skills/` |
| [`.claude/agents/`](./.claude/agents) | Subagents — each with its own tools, model, and single responsibility |
| [`.claude/commands/lumina/`](./.claude/commands/lumina) | Slash commands, namespaced `/lumina:...` — the entry points a user actually types |
| [`.claude/skills/`](./.claude/skills) | Link to the shared `.agents/skills/` directory |
| [`.claude/rules/`](./.claude/rules) | Link to the 19 shared rules in `.agents/rules/` |
| [`.claude/hooks/`](./.claude/hooks) | Automated hooks (audit log, commit-msg guard, secret scan, auto-format, auto-lint...) |

### Agents

| Agent | Role |
|---|---|
| `requirement-analysis-agent` | Turns a raw requirement (text/image/PDF/DOCX...) into a clear purpose/scope/impact analysis, classifies it as a new feature vs. a small fix, and recommends the next step |
| `system-design-agent` | Produces HLD/LLD, data model, API, and reliability/security/performance design for features that need architecture |
| `planner-agent` | Breaks a spec or design doc into traceable tasks (REQ → Task → AC → Test) — plan only, never touches product code |
| `coding-agent` | Implements code per SOLID/DRY/KISS/YAGNI, strictly within the assigned scope |
| `setup-agent` | Installs and configures requested tools, libraries, runtimes and applications; verifies compatibility and a working smoke test |
| `qa-tester-agent` | Designs and executes test cases (equivalence partitioning, boundary values, decision tables...) with full requirement traceability |
| `reviewer-agent` | Independent "fresh eyes" review for code, plans, or test cases — never fixes, only reports |
| `researcher-agent` | Reads widely, answers briefly — local docs first, then web, no fabrication |
| `workspace-auditor-agent` | Finds likely-unneeded files/folders — lists with evidence, never deletes |
| `leak-hunter` | Finds where protected data (correct answers, unreleased content, PII...) could reach the client early — lists with evidence, never fixes |

### Commands

| Command | Does |
|---|---|
| `/lumina:analyze` | Run `requirement-analysis-agent`, then stop and ask whether to continue to `/lumina:plan` or go straight to `coding-agent` |
| `/lumina:plan` | Full planning pipeline: research → system-design-agent → planner-agent → review → report |
| `/lumina:implement` | Hand a task (or `docs/implementation-plan.json`) to `coding-agent` |
| `/lumina:test` | Hand a feature/flow to `qa-tester-agent` |
| `/lumina:review` | Review the current diff (via the `open-code-review` skill) or a plan/test case (via `reviewer-agent`) |
| `/lumina:report` | Produce a change report for recent edits |
| `/lumina:commit` | Commit with Conventional Commits, validated by script |
| `/lumina:pr` | Create/update a PR — checks for conflicts first |
| `/lumina:cleanup` | Delete temp/scratch files Claude created this session |
| `/lumina:audit-workspace` | List (never delete) suspicious leftover files in the workspace |

### Skills

| Skill | Purpose |
|---|---|
| `git-workflow` | Gatekeeper for every commit/PR — Conventional Commits, conflict-safe merging |
| `report` | Formats change reports and review reports from already-done work |
| `docs` | Reconciles README/CLAUDE.md/docs against the actual codebase, or writes a lean first version when none exists (leaner `/init`) — not system architecture specs |
| `cleanup-temp-files` | Removes Claude's own temp files from the current session |
| `markitdown` | Converts PDF/DOCX/PPTX/XLSX/images/... to Markdown |
| `database` | SQL/NoSQL query review, schema/index design, performance analysis |
| `design-patterns` | Reference for the 22 GoF patterns, grouped by when to actually use them |
| `review-web-security` | Web security review (authn/authz, injection, frontend, API, infra...) with evidence, severity, fix, and regression tests |
| `testing-strategy` | Technical unit testing: picking the right test double, Arrange-Act-Assert structure, risk-based coverage |
| `dependency-audit` | Read-only dependency vulnerability audit (npm/composer/pip/cargo/go) — reports and suggests, never auto-upgrades |
| `refactoring-catalog` | Fowler-style refactoring techniques mapped to specific code smells |
| `ci-pipeline` | Authoring/reviewing CI workflows (GitHub Actions/GitLab CI) — fail-fast job order, caching, secret handling |
| `testcase` | Writing a few structured test cases quickly (ID/Priority/Steps/Expected result) without spawning the full `qa-tester-agent` agent |

---

## 🔄 End-to-end workflow

```
/lumina:analyze  →  (new feature?) → /lumina:plan  →  /lumina:implement  →  /lumina:test  →  /lumina:review  →  /lumina:commit  →  /lumina:pr
                 │                                               ↑
                 └── (small fix) ────────────────────────────────┘
```

Each stage **stops and asks for confirmation** before moving to the next — nothing auto-cascades from analysis straight to a commit. Documents are handed off **by file path** (`docs/requirement-analysis.md` → `docs/system-design.md` → `docs/implementation-plan.json`), not by pasting full text into the next agent's prompt, so context stays small and traceable.

---

## 📐 Core rules (`.claude/rules/`)

Every agent is bound by some or all of the rule files in `.claude/rules/` (one file per group, e.g. `simplicity.md`, `data-safety.md`):

KISS+YAGNI · Clean Code · SRP/Separation of Concerns · DRY · SOLID · Fail-Fast Validation · Data Safety (authz/transactions) · Quality Assurance (test/lint/review) · Complexity/Performance · Setup Rule/Template Changes · Boy Scout Rule · Commit Discipline · PR Conflict Safety · Comment Discipline · Database Read-Only by Default · Local-First Search + No Fabrication · Documentation as Code Sync · Type Safety · Backend Contract/Content/Security · Frontend Design Fidelity/Accessibility · Plan Output Format (JSON, `planner-agent` only) · Open Questions Table · Mandatory Report · Response Style.

`coding-agent` reads the 18 core rule files as its system prompt; other agents link to the specific rule files relevant to their task.

---

## 🚀 Using this in another project

This repository uses npm tooling for Git pre-commit formatting. Run `npm ci` to install Husky, lint-staged and Prettier and activate the hook. Each commit formats supported staged files; unknown formats are skipped. No typecheck or test step is configured because this configuration repository has no corresponding scripts. Copying `.claude/` alone does not install this repository's Git hooks.

For Codex, copy `AGENTS.md`, `.agents/`, `.codex/`, `.claude/` and `CLAUDE.md` together so relative references and skill symlinks remain valid. Start a new session to discover them. Invoke `$workflow-implement` or another `workflow-*` skill, or ask for a custom agent by name. Claude hook settings are not activated by this adapter; formatting and validation remain explicit workflow steps.

1. Copy `.claude/` and `.agents/` together into the target project; keep their relative paths so shared skill/rule links resolve.
2. Merge [`.claude/hooks/settings.snippet.json`](./.claude/hooks/settings.snippet.json) into the target's `.claude/settings.json` (see [`hook/README.md`](./.claude/hooks/README.md)).
3. Make sure `jq` is installed (required by most hooks) — missing tools degrade gracefully, hooks just skip.
4. Start with `/lumina:analyze "<your requirement>"` or jump straight to `/lumina:plan` if the requirement is already clear.

## ✅ GitHub Actions

Workflow [`agent-config.yml`](./.github/workflows/agent-config.yml) runs on `push` and `pull_request` events targeting `main`.

It checks:

- Shared rules and skills structure and links.
- Codex agent adapters and their role sources.
- Whitespace errors in the commit changes.

Run the equivalent checks locally:

```bash
python3 scripts/check-agent-config.py
git diff --check HEAD^ HEAD
```

When enabling branch protection on GitHub, require the `Validate agent configuration` status check before merging. This repository has no package manifest or runtime test suite, so CI does not install dependencies or deploy.

---

## 🤝 Contributing

Open a PR if you have a rule, agent, or skill worth adding — keep each one single-purpose and link it from the relevant table above.

**License**: [MIT](./LICENSE)

## Antigravity

Open the repository root in Antigravity and start a new conversation. It loads `AGENTS.md` and uses the shared `.agents/skills/` and `.agents/rules/`. Invoke `/workflow-implement` for the `coding-agent` role — it applies `coding-frontend`/`coding-backend` internally per stack, don't invoke those skills directly. Rules have activation metadata; no separate copy is needed. Codex TOML agents and Claude hooks are not Antigravity configurations.

Setup follows the official [skills](https://www.antigravity.google/docs/skills) and [rules](https://www.antigravity.google/docs/rules) documentation.

## Configuration maintenance

Edit shared rules and skills only in `.agents/`. Claude and Codex paths are relative symlinks to this source. Keep the three directories and root instruction files together when copying the framework. Tool-specific agents and hooks remain separate. Run `python3 scripts/check-agent-config.py` after structural changes; this checks file configuration, not runtime tool discovery.
