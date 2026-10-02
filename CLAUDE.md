# CLAUDE.md

Đây là repo cấu hình Claude Code (`.claude/`) — một framework agent cho quy trình phát triển có cấu trúc. Không phải một ứng dụng/sản phẩm; nội dung repo chính là các file `.md`/`.sh`/`.json` định nghĩa agent/skill/rule/hook.

## Quy ước

- Nội dung bên trong `.claude/` (agents, commands, skills, rules, hook) viết **tiếng Việt**. `README.md` ở gốc viết **tiếng Anh** (quyết định có chủ đích, giữ nguyên khi sửa).
- Đây là dự án cá nhân đang được xây dần — khi sửa một agent/skill, luôn đọc file đó trước, không suy đoán theo tên.
- `.claude/rules/` là nguồn sự thật cho mọi quy tắc bắt buộc — xem [`rules/README.md`](./.claude/rules/README.md) để biết agent nào đọc rule nào.

## Luồng làm việc chính

`/analyze` (requirement-analysis) → `/plan` (research → system-design → planner → review → report) → `/implement` (coding-agent) → `/test` (qa-tester) → `/review` → `/commit` → `/pr`.

Mỗi bước dừng lại chờ xác nhận trước khi sang bước kế — không có lệnh nào tự chạy hết cả pipeline. Tài liệu bàn giao giữa các bước là **file** (`docs/requirement-analysis.md`, `docs/system-design.md`, `docs/implementation-plan.md`), agent sau tự đọc file, không dán nguyên văn vào prompt.

## Khi được giao việc

- Sửa agent/skill/rule/hook: đọc toàn bộ file liên quan trước, giữ đúng convention đang có trong file đó (không áp văn phong cá nhân), cập nhật mọi nơi tham chiếu nếu đổi tên.
- Thêm agent/skill/command mới: theo đúng format frontmatter đang dùng (xem một file cùng loại làm mẫu), không tạo abstraction/layer không cần thiết ([`rules/01`](./.claude/rules/01-simplicity.md)).
- **Sau khi hoàn thành một plan/task làm thay đổi file**: luôn kiểm tra README/CLAUDE.md/docs có đoạn nào nhắc tới phần vừa đổi mà giờ sai không, cập nhật ngay trong cùng lượt — đây là một phần của "hoàn thành", không phải việc làm sau ([`rules/15`](./.claude/rules/15-docs-sync.md)). Phạm vi lớn hoặc không chắc hết chỗ bị ảnh hưởng → dùng skill [`docs-sync`](./.claude/skills/docs-sync/SKILL.md).
- Nghi ngờ docs (README này, CLAUDE.md này, hoặc file trong `docs/`) không còn khớp code dù không vừa sửa gì: cũng dùng skill [`docs-sync`](./.claude/skills/docs-sync/SKILL.md).
- Commit/PR: chỉ khi người dùng yêu cầu rõ ràng — xem [`rules/10`](./.claude/rules/10-commit-discipline.md) và skill [`git-workflow`](./.claude/skills/git-workflow/SKILL.md).

## Lưu ý

- `.claude/logs/logs.jsonl` (audit log của hook) đã nằm trong `.gitignore` — không commit nhầm. `docs/requirement-analysis.md`/`docs/system-design.md`/`docs/implementation-plan.md` do pipeline sinh ra **không** bị ignore — đây là tài liệu thật, được coi là deliverable nên commit lại nếu người dùng xác nhận giữ.
- Badge MIT trong README hiện chưa có file `LICENSE` tương ứng trong repo — cần người dùng tự quyết có thêm file này không trước khi coi đây là license chính thức.
