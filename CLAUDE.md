# Claude Code

Đọc và tuân thủ [AGENTS.md](./AGENTS.md) trước khi làm việc. `.agents/rules/` và `.agents/skills/` là nguồn chung duy nhất; `.claude/rules/` và `.claude/skills/` liên kết tới đó, không tạo bản sao riêng.

## Cấu hình riêng

- `.claude/agents/*.md`: vai trò, tools và model cho Claude Code.
- `.claude/commands/lumina/*.md`: slash command, namespace `/lumina:...`; skill `workflow-*` dùng cùng nguồn quy trình trên các công cụ khác.
- `.claude/settings.json` và `.claude/hook/`: hook Claude, không tự chạy trên Codex hoặc Antigravity.
- `.claude/logs/` bị ignore; không commit log/file tạm. Tài liệu bàn giao `docs/` là deliverable.

## Pipeline

`/lumina:analyze` → `/lumina:plan` → `/lumina:implement` → `/lumina:test` → `/lumina:review` → `/lumina:commit` → `/lumina:pr`.

Chạy bước được giao, giữ điểm bàn giao/duyệt; không tự chạy toàn pipeline. Khi chuyển project, copy cùng `.agents/`, `.claude/`, `AGENTS.md` và `CLAUDE.md`, giữ symlink tương đối.
