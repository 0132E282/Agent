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
| 19 | Viết plan | JSON Schema + Task dạng bảng (chỉ áp dụng cho kế hoạch triển khai của `planner-agent`) | [19-plan-format.md](./19-plan-format.md) |
| 20 | Câu hỏi mở | Bảng quyết định — áp dụng mọi agent khi hỏi lại ≥2 câu hỏi mở bằng văn bản | [20-open-questions-table.md](./20-open-questions-table.md) |
| 21 | Báo cáo bắt buộc | Qua skill `report`, mặc định ngắn gọn — áp dụng cả phiên chính và mọi subagent | [21-mandatory-report.md](./21-mandatory-report.md) |

## Cách dùng

Thư mục này đã nằm sẵn trong `.claude/rules/` của repo — Claude Code tự đọc được khi subagent/skill tham chiếu tới. Muốn dùng ở project khác, copy nguyên `.claude/rules/` sang `.claude/rules/` của project đích, rồi tham chiếu trong subagent/skill để bắt buộc tuân thủ:

- [`agents/coding-agent.md`](../agents/coding-agent.md) — subagent đọc trực tiếp cả 18 file (01-18) làm system prompt; rule #19/#20/#21 không nằm trong danh sách đọc blanket này nhưng #21 vẫn áp dụng (xem checklist riêng của agent).
- [`skills/git-workflow`](../skills/git-workflow/SKILL.md) — skill gatekeeper riêng cho mọi hành động git (rule #10 commit + rule #11 pull request/conflict), kèm script `validate-commit-message.sh` kiểm tra commit message tự động.
- [`agents/planner-agent.md`](../agents/planner-agent.md) — áp dụng riêng rule #19 khi xuất kế hoạch triển khai (`docs/implementation-plan.json`); rule #20 khi hỏi lại nhiều câu hỏi mở trong chat; rule #21 khi báo cáo kế hoạch.
- [`agents/requirement-analysis-agent.md`](../agents/requirement-analysis-agent.md), [`agents/system-design-agent.md`](../agents/system-design-agent.md) — áp dụng rule #20 khi liệt kê nhiều câu hỏi mở/thiếu thông tin cần người dùng xác nhận.
- `CLAUDE.md`/`AGENTS.md` (gốc repo) — tham chiếu rule #21 để áp dụng cho cả phiên chính, không chỉ subagent.
