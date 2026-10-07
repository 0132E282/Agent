---
description: Tạo/cập nhật pull request theo skill git-workflow (check conflict trước, resolve đúng quy tắc)
argument-hint: "[nhánh đích, tuỳ chọn — mặc định main]"
---

Dùng skill `git-workflow` mục "Trước khi tạo Pull Request / khi gặp conflict":

1. Kiểm tra nhánh hiện tại có **conflict** với nhánh đích không ($ARGUMENTS nếu có, mặc định `main`).
2. Nếu có conflict: đọc cả hai phía (`<<<<<<<`/`=======`/`>>>>>>>`) trước khi resolve — không xóa một bên mà không xem nội dung. Nghi ngờ mất fix quan trọng không liên quan task → dừng lại hỏi người dùng.
3. Resolve xong, chạy lại test/lint liên quan.
4. Tạo hoặc cập nhật PR với tiêu đề/mô tả rõ ràng.
