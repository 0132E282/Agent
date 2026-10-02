---
name: report
description: CHỈ tạo báo cáo (report), KHÔNG tự thực hiện review/phân tích code. (1) Báo cáo thay đổi/commit: file nào bị sửa, sửa gì, tại sao — dùng ngay sau khi hoàn thành một task code (Edit/Write) hoặc trước khi soạn commit. (2) Báo cáo kết quả review: trình bày lại issue, mức độ nghiêm trọng, đề xuất xử lý, độ phức tạp Big O theo format chuẩn — dùng sau khi việc review/audit đã được thực hiện (bởi coding-agent hoặc skill review khác), không dùng skill này để tự đi tìm lỗi.
license: MIT
metadata:
  version: "1.0"
---

# 📊 Report

Skill này **chỉ format và xuất báo cáo** — không tự đi tìm lỗi, không tự đánh giá chất lượng code. Việc review/phân tích là của subagent [`coding-agent`](../../agents/coding-agent.md) hoặc một skill review khác; skill này nhận kết quả đó (hoặc diff/thay đổi đã làm) và trình bày lại theo format chuẩn, dễ đọc, dễ copy vào PR/commit.

| Loại báo cáo | Input là gì | Dùng khi | Template |
|---|---|---|---|
| **Báo cáo thay đổi/commit** | Danh sách file + diff vừa Edit/Write | Vừa sửa code xong, hoặc trước khi soạn commit message | [`assets/change-report-template.md`](./assets/change-report-template.md) |
| **Báo cáo kết quả review** | Issue/finding đã có sẵn (từ review trước đó) | Sau khi review/audit đã xong, cần trình bày lại kết quả | [`assets/review-report-template.md`](./assets/review-report-template.md) |

Cả hai bắt buộc theo [08-quality-assurance.md](../../rules/08-quality-assurance.md) — báo cáo là bước cuối, không được bỏ qua.

## 1. Báo cáo thay đổi (Change Report)

Copy khung trong `assets/change-report-template.md` và điền: danh sách file đã đổi, chi tiết từng thay đổi (code cũ/mới kèm lý do), tóm tắt số dòng/hàm thêm/sửa/xóa.

Nguyên tắc: chỉ liệt kê những gì **thật sự thay đổi**, không diễn giải lại toàn bộ file; phần "Lý do" trả lời đúng câu hỏi *"vấn đề gì đang được giải quyết"* (liên hệ [06-fail-fast-validation.md](../../rules/06-fail-fast-validation.md), [10-commit-discipline.md](../../rules/10-commit-discipline.md) — body commit có thể lấy thẳng từ phần Tóm tắt này).

## 2. Báo cáo kết quả review (Review Report)

> Dùng để **trình bày lại** kết quả review đã có (do `coding-agent`, một skill review khác, hoặc con người cung cấp) — không phải để skill này tự review code.

Copy khung trong `assets/review-report-template.md`, gồm:

- **4 mức nghiêm trọng** (bắt buộc dùng đúng khi phân loại lại finding): CRITICAL 🚨 (lỗi logic nặng/bảo mật/crash), WARNING ⚠️ (code smell/hiệu năng/thiếu edge case), SUGGESTION 💡 (gợi ý refactor nhỏ), GOOD ✅ (giải pháp tốt, nên nhân rộng).
- **Bảng tóm tắt**: `# | File:Dòng | Vấn đề | Mức độ | Big O | Đề xuất xử lý` — cột Big O chỉ điền khi có vòng lặp/đệ quy/thuật toán đáng chú ý (độ phức tạp hiện tại → sau khi áp dụng đề xuất). Đề xuất xử lý luôn cụ thể, áp dụng được ngay.
- **So sánh chi tiết** (cho mỗi CRITICAL/WARNING): code hiện tại vs code đề xuất, kèm giải thích lý do + lợi ích.
- **Thống kê cuối**: `[X]` issue cần sửa (CRITICAL + WARNING) | `[Y]` điểm sáng (GOOD) | `[Z]` gợi ý (SUGGESTION).

## Khi áp dụng

- Báo cáo thay đổi/commit: ngay sau khi hoàn thành một task Edit/Write, trước khi báo "xong" với người dùng hoặc trước khi soạn commit message (xem [git-workflow](../git-workflow/SKILL.md)).
- Báo cáo kết quả review: ngay sau khi một review/audit đã hoàn tất (ở nơi khác) và cần trình bày lại kết quả cho người dùng — không dùng để tự thực hiện review.
