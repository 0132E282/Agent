---
description: Phân tích yêu cầu thô (text/ảnh/PDF/DOCX...) ở mức PM — mục đích, cần làm gì, tác động ở đâu — rồi đề xuất bước tiếp theo (plan hay giao thẳng coding-agent)
argument-hint: "<mô tả yêu cầu, hoặc đường dẫn file/ảnh/PDF>"
---

Phân tích yêu cầu sau bằng agent `requirement-analysis-agent`: $ARGUMENTS

1. Agent `requirement-analysis-agent` convert input sang Markdown (skill `markitdown`) nếu không phải text thường, phân tích mục đích/cần làm gì/tác động ở đâu, và phân loại "task mới" hay "fix/thay đổi nhỏ".
2. Agent tự `Write` kết quả ra `docs/requirement-analysis.md`, rồi xuất report (skill `report`) tóm tắt kết quả phân tích + lý do phân loại.
3. **Dừng lại, hỏi người dùng** hướng tiếp theo — không tự động chạy tiếp:
   - "Task mới" → hỏi có chạy tiếp `/lumina:plan` không (khi chạy, báo cho `/lumina:plan` biết đã có sẵn `docs/requirement-analysis.md` để `system-design-agent`/`planner-agent` đọc trực tiếp, không cần phân tích lại từ đầu).
   - "Fix/thay đổi nhỏ" → hỏi có giao thẳng `coding-agent` triển khai (bỏ qua system-design-agent/planner-agent) rồi `reviewer-agent` review không.

Không tự chuyển sang bước tiếp theo khi chưa có xác nhận của người dùng.
