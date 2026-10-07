---
name: workflow-analyze
description: "Phân tích yêu cầu thô (text/ảnh/PDF/DOCX...) ở mức PM — mục đích, cần làm gì, tác động ở đâu — rồi đề xuất bước tiếp theo (plan hay giao thẳng coding-agent)"
---

# workflow-analyze

Đọc và thực hiện workflow trong `.claude/commands/lumina/analyze.md`. Thay `$ARGUMENTS` bằng yêu cầu/đường dẫn người dùng cung cấp; giải quyết link từ `.claude/commands/lumina/`. Đọc hướng dẫn vai trò liên quan trong `.claude/agents/`; khi workflow yêu cầu delegation và có công cụ, dùng agent cùng vai trò do runtime hỗ trợ (Codex dùng custom agent cùng tên). Nếu không có delegation, thực hiện tuần tự theo cùng phạm vi và nêu rõ cách thực hiện. Không coi slash command/hook Claude là chức năng Codex tự chạy. Giữ điểm bàn giao, kiểm chứng và phạm vi cho phép của workflow.
