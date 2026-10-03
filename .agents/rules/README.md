---
trigger: manual
description: "Danh mục quy tắc dùng chung."
---

# 📏 Coding Rules

Bộ quy tắc coding **bắt buộc** cho các subagent trong [`agents/`](../agents). Mỗi file kết hợp nhiều nguyên tắc kinh điển thành một nhóm quy tắc áp dụng được ngay.

| # | Nhóm | Quy tắc kết hợp | File |
|---|------|------------------|------|
| 1 | Đơn giản | KISS + YAGNI | [01-simplicity.md](./01-simplicity.md) |
| 2 | Dễ đọc | Clean Code + Coding Convention | [02-readability.md](./02-readability.md) |
| 3 | Tách trách nhiệm | SRP + Separation of Concerns | [03-separation-of-concerns.md](./03-separation-of-concerns.md) |
| 4 | Tái sử dụng | DRY | [04-dry.md](./04-dry.md) |
| 5 | Dễ mở rộng | SOLID + Composition over Inheritance | [05-extensibility.md](./05-extensibility.md) |
| 6 | Kiểm soát lỗi | Fail Fast + Validation | [06-fail-fast-validation.md](./06-fail-fast-validation.md) |
| 7 | An toàn dữ liệu | Phân quyền + Transaction | [07-data-safety.md](./07-data-safety.md) |
| 8 | Chất lượng | Test + Static Analysis + Code Review | [08-quality-assurance.md](./08-quality-assurance.md) |
| 9 | Cải thiện dần | Boy Scout Rule | [09-boy-scout-rule.md](./09-boy-scout-rule.md) |
| 10 | Commit có kỷ luật | Explicit Commit Authorization + Conventional Commits | [10-commit-discipline.md](./10-commit-discipline.md) |
| 11 | Tạo Pull Request | PR Safety Gate (chi tiết quy trình ở skill `git-workflow`) | [11-pull-request-conflict.md](./11-pull-request-conflict.md) |
| 12 | Comment có kỷ luật | Minimal Comments + Better Comments Convention | [12-comments.md](./12-comments.md) |
| 13 | An toàn database | Read-Only by Default + Manual Migration Only | [13-database-read-only.md](./13-database-read-only.md) |
| 14 | Ưu tiên tìm kiếm | Local-First Search + No Fabrication | [14-search-priority.md](./14-search-priority.md) |
| 15 | Đồng bộ tài liệu | Documentation as Code + Definition of Done | [15-docs-sync.md](./15-docs-sync.md) |
| 16 | An toàn type | Strict Typing + Type Reuse + Domain Organization | [16-type-safety.md](./16-type-safety.md) |
| 17 | Backend | API Correctness + Content Lifecycle + Secure Data Handling | [17-backend.md](./17-backend.md) |
| 18 | Frontend | Design Fidelity + Semantic HTML + Accessible Content Rendering | [18-frontend.md](./18-frontend.md) |

## Cách dùng

Thư mục này đã nằm sẵn trong `.claude/rules/` của repo — Claude Code tự đọc được khi subagent/skill tham chiếu tới. Muốn dùng ở project khác, copy nguyên `.claude/rules/` sang `.claude/rules/` của project đích, rồi tham chiếu trong subagent/skill để bắt buộc tuân thủ:

- [`agents/coding-agent.md`](../agents/coding-agent.md) — subagent đọc trực tiếp cả 18 file làm system prompt.
- [`skills/git-workflow`](../skills/git-workflow/SKILL.md) — skill gatekeeper riêng cho mọi hành động git (rule #10 commit + rule #11 pull request/conflict), kèm script `validate-commit-message.sh` kiểm tra commit message tự động.
