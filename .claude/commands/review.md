---
description: Review code hiện tại bằng skill open-code-review:review (OCR)
argument-hint: "[file/diff/PR cần review, tuỳ chọn — mặc định diff hiện tại]"
---

Dùng skill `open-code-review:review` (OpenCodeReview) để review phạm vi sau: $ARGUMENTS (nếu trống, review toàn bộ diff/thay đổi chưa commit hiện tại).

Nếu đối tượng cần review là **kế hoạch (plan)** hoặc **test case** — không phải code — dùng agent [`reviewer`](../agents/reviewer.md) thay vì skill này (OCR chỉ review code; `reviewer` mới có tiêu chí riêng cho plan/test case).

Nếu yêu cầu là **security review** chuyên sâu (lỗ hổng, xác thực/phân quyền, upload, thanh toán...) — dùng skill [`review-web-security`](../skills/review-web-security/SKILL.md) thay vì OCR (OCR review chất lượng code tổng quát, không có checklist bảo mật chuyên biệt).
