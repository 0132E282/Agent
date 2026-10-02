---
description: Review code hiện tại bằng skill open-code-review:review (OCR)
argument-hint: "[file/diff/PR cần review, tuỳ chọn — mặc định diff hiện tại]"
---

Dùng skill `open-code-review:review` (OpenCodeReview) để review phạm vi sau: $ARGUMENTS (nếu trống, review toàn bộ diff/thay đổi chưa commit hiện tại).

Nếu đối tượng cần review là **kế hoạch (plan)** hoặc **test case** — không phải code — dùng agent [`reviewer`](../agents/reviewer.md) thay vì skill này (OCR chỉ review code; `reviewer` mới có tiêu chí riêng cho plan/test case).
