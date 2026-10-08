---
trigger: model_decision
description: "Áp dụng khi nhiệm vụ liên quan: 🔀 Pull Request — Conflict Safety Gate"
---

# 🔀 Pull Request — Conflict Safety Gate

**Nhóm quy tắc kết hợp**: PR Safety Gate (điều kiện bắt buộc, không phải quy trình)

## Quy tắc

- Trước khi tạo/cập nhật PR: **bắt buộc** kiểm tra nhánh có conflict với nhánh đích không.
- Nếu có conflict: **bắt buộc đọc cả hai phía** (`<<<<<<<` / `=======` / `>>>>>>>`) trước khi resolve — không bao giờ xóa một bên mà không xem nội dung.
- Nếu nghi ngờ việc resolve có thể làm mất một logic quan trọng không liên quan đến task của PR: **dừng lại và hỏi người dùng**, không tự quyết âm thầm.
- **Chỉ gộp đúng phần cần thiết để resolve conflict textual** — tuyệt đối không tự ý kéo thêm logic/tính năng từ nhánh đích (base, ví dụ `main`) vào nhánh nguồn nếu người dùng chưa yêu cầu rõ việc đó, kể cả khi thấy logic đó "có vẻ cần" hoặc "nên có cho đủ". Nhiệm vụ chỉ giới hạn ở nhánh/task được giao — thấy thiếu gì từ nhánh khác thì **báo cho người dùng biết và hỏi**, không tự gộp vào.

## Khi áp dụng

- Mỗi lần chuẩn bị tạo hoặc cập nhật PR mà git báo conflict.

> Đây là **điều kiện bắt buộc phải tuân thủ**, không phải hướng dẫn từng bước. Quy trình resolve chi tiết — ưu tiên giữ nhánh nào, checklist — nằm ở skill [`git-workflow`](../skills/git-workflow/SKILL.md).
