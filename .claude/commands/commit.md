---
description: Commit thay đổi hiện tại theo skill git-workflow (Conventional Commits, validate message)
argument-hint: "[ghi chú phạm vi/ý định commit, tuỳ chọn]"
---

Đây là lệnh commit rõ ràng từ người dùng — dùng skill `git-workflow` mục "Trước khi `git commit`":

1. Xem lại `git status`/`git diff` để xác nhận đúng phạm vi thay đổi liên quan đến task hiện tại — không gộp thêm thay đổi ngoài phạm vi, không tách vụn.
2. Soạn message theo Conventional Commits: tiêu đề `<type>: <mô tả>` ≤ 75 ký tự, body nêu rõ vấn đề được giải quyết.
3. Chạy `validate-commit-message.sh` để kiểm tra message trước khi commit thật.
4. Tạo commit.

Ghi chú thêm từ người dùng (nếu có): $ARGUMENTS
