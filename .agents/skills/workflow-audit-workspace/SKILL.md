---
name: workflow-audit-workspace
description: "Quét workspace tìm file/thư mục không cần thiết bằng agent workspace-auditor (chỉ liệt kê, không tự xóa)"
---

# workflow-audit-workspace

Đọc và thực hiện workflow trong `.claude/commands/audit-workspace.md`. Thay `$ARGUMENTS` bằng yêu cầu/đường dẫn người dùng cung cấp; giải quyết link từ `.claude/commands/`. Đọc hướng dẫn vai trò liên quan trong `.claude/agents/`; khi workflow yêu cầu delegation và có công cụ, dùng agent cùng vai trò do runtime hỗ trợ (Codex dùng custom agent cùng tên). Nếu không có delegation, thực hiện tuần tự theo cùng phạm vi và nêu rõ cách thực hiện. Không coi slash command/hook Claude là chức năng Codex tự chạy. Giữ điểm bàn giao, kiểm chứng và phạm vi cho phép của workflow.
