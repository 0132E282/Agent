---
description: Triển khai code bằng agent coding-agent theo đúng phạm vi được giao (task cụ thể, hoặc theo docs/implementation-plan.json nếu có)
argument-hint: "<task/tính năng cần code, hoặc 'theo plan' để dùng docs/implementation-plan.json>"
---

Giao cho agent `coding-agent` triển khai: $ARGUMENTS

- Nếu có file `docs/implementation-plan.json` (do agent `planner-agent` tạo, JSON theo [`rules/19-plan-format.md`](../../rules/19-plan-format.md)) và người dùng không chỉ định task cụ thể khác, đọc file đó để biết task nào đang `TODO`/`IN_PROGRESS` và dependency giữa các task — triển khai đúng một hoặc vài task liên quan theo đúng thứ tự dependency, không tự làm tất cả task cùng lúc nếu không được yêu cầu.
- Tuân thủ toàn bộ 18 rule bắt buộc trong [`rules/`](../../rules) — không tự ý mở rộng phạm vi, không refactor ngoài task, không tự thêm tính năng.
- Sau khi code xong: chạy test/lint liên quan, kiểm tra README/CLAUDE.md/docs có đoạn nào nhắc tới phần vừa đổi mà giờ sai không — có thì cập nhật luôn (dùng skill `docs` nếu phạm vi lớn/không chắc hết chỗ — [`rules/15`](../../rules/15-docs-sync.md)), rồi xuất báo cáo thay đổi (skill `report`), và dừng lại chờ người dùng xác nhận trước khi `reviewer-agent` review hoặc commit.
