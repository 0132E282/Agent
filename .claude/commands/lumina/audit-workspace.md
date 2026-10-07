---
description: Quét workspace tìm file/thư mục không cần thiết bằng agent workspace-auditor (chỉ liệt kê, không tự xóa)
argument-hint: "[thư mục cần quét, tuỳ chọn — mặc định toàn workspace]"
---

Giao cho agent `workspace-auditor` quét: $ARGUMENTS (nếu trống, quét toàn bộ workspace).

Agent chỉ liệt kê file/thư mục nghi ngờ không cần (build artifact, cache, file tạm/backup, log cũ, trùng lặp, mồ côi) kèm bằng chứng và mức tin cậy — tuyệt đối không tự xóa. Sau khi có danh sách, chờ người xác nhận trước khi tiến hành xóa bất cứ gì.
