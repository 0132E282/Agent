---
name: report
description: CHỈ tạo báo cáo (report), KHÔNG tự thực hiện review/phân tích code. (1) Báo cáo thay đổi/commit: file nào bị sửa, sửa gì, tại sao — dùng ngay sau khi hoàn thành một task code (Edit/Write) hoặc trước khi soạn commit. (2) Báo cáo kế hoạch: tóm tắt plan vừa `planner-agent` viết xong (số REQ/task/câu hỏi mở/rủi ro) trước khi chờ duyệt. (3) Báo cáo kết quả review: trình bày lại issue, mức độ nghiêm trọng, đề xuất xử lý, độ phức tạp Big O theo format chuẩn — dùng sau khi việc review/audit đã được thực hiện (bởi coding-agent hoặc skill review khác), không dùng skill này để tự đi tìm lỗi.
license: MIT
metadata:
  version: "1.2"
---

# 📊 Report

Skill này **chỉ format và xuất báo cáo** — không tự đi tìm lỗi, không tự đánh giá chất lượng code. Việc review/phân tích là của subagent [`coding-agent`](../../agents/coding-agent.md) hoặc một skill review khác; skill này nhận kết quả đó (hoặc diff/thay đổi đã làm) và trình bày lại theo format chuẩn, dễ đọc, dễ copy vào PR/commit.

| Loại báo cáo | Input là gì | Dùng khi | Template |
|---|---|---|---|
| **Báo cáo thay đổi/commit** | Danh sách file + diff vừa Edit/Write | Vừa sửa code xong, hoặc trước khi soạn commit message | [`assets/change-report-template.md`](./assets/change-report-template.md) |
| **Báo cáo kế hoạch (Plan Summary)** | `docs/implementation-plan.json` vừa `Write` xong | Agent `planner-agent` vừa xong một plan, trước khi dừng chờ duyệt | [`assets/plan-summary-report-template.md`](./assets/plan-summary-report-template.md) |
| **Báo cáo kết quả review** | Finding đã có sẵn — code, plan (`planner-agent`/`system-design-agent`) hoặc test case (`qa-tester-agent`) | Sau khi agent `reviewer-agent` (hoặc coding-agent tự review) đã xong, cần trình bày lại | [`assets/review-report-template.md`](./assets/review-report-template.md) |
| **Báo cáo security review** | Finding đã có sẵn từ skill `review-web-security` | Sau khi security review xong — format riêng vì có field confidence/exploit condition/CWE mà bảng review thường không cần | [`assets/security-review-report-template.md`](./assets/security-review-report-template.md) |
| **Báo cáo dependency audit** | Kết quả audit đã có sẵn từ skill `dependency-audit` | Sau khi audit dependency xong, cần trình bày danh sách lỗ hổng + lệnh đề xuất | [`assets/dependency-audit-report-template.md`](./assets/dependency-audit-report-template.md) |
| **Báo cáo test (digest)** | Kết quả đã thiết kế/thực thi từ agent `qa-tester-agent` | Cần bản tóm tắt ngắn để copy vào PR/commit, không cần nguyên văn chi tiết của `qa-tester-agent` | [`assets/qa-test-report-template.md`](./assets/qa-test-report-template.md) |

Tất cả bắt buộc theo [08-quality-assurance.md](../../rules/08-quality-assurance.md) — báo cáo là bước cuối, không được bỏ qua.

## 1. Báo cáo thay đổi (Change Report)

Copy khung `assets/change-report-template.md`, điền: bảng tóm tắt `Trạng thái (Tạo/Sửa/Xóa) | File | Ghi chú` cho toàn bộ file đổi, kèm chi tiết code cũ/mới + lý do cho những thay đổi đáng kể (logic/behavior). File chỉ đổi nhỏ (xóa file tạm, đổi 1 dòng không ảnh hưởng hành vi) chỉ cần nằm trong bảng, không cần mục chi tiết riêng. Chỉ liệt kê những gì **thật sự thay đổi**, không diễn giải lại toàn bộ file; phần "Lý do" trả lời *"vấn đề gì đang được giải quyết"* ([10-commit-discipline.md](../../rules/10-commit-discipline.md) — body commit có thể lấy thẳng từ phần Tóm tắt này).

## 2. Báo cáo kế hoạch (Plan Summary)

Copy khung `assets/plan-summary-report-template.md`, điền ngay sau khi `planner-agent` `Write` xong `docs/implementation-plan.json`: số REQ/task/câu hỏi mở/rủi ro, bảng câu hỏi mở cần chốt (nếu ≥2 câu — theo [rules/20](../../rules/20-open-questions-table.md)), rủi ro chính, bước tiếp theo. Không chép lại nguyên văn plan — chỉ tóm tắt để người dùng duyệt nhanh.

## 3. Báo cáo kết quả review (Review Report)

Trình bày lại kết quả review **đã có** (do agent `reviewer-agent`, `coding-agent` tự review, hoặc con người cung cấp) — không tự review. Dùng chung cho cả 3 loại artifact `reviewer-agent` review (code/plan/test case). Copy khung `assets/review-report-template.md`, gồm:

- **4 mức nghiêm trọng** (bắt buộc dùng đúng khi phân loại lại finding): CRITICAL 🚨 (lỗi logic nặng/bảo mật/crash), WARNING ⚠️ (code smell/hiệu năng/thiếu edge case), SUGGESTION 💡 (gợi ý refactor nhỏ), GOOD ✅ (giải pháp tốt, nên nhân rộng).
- **Bảng tóm tắt**: `# | Vị trí | Vấn đề | Mức độ | Big O | Đề xuất xử lý` — Vị trí là `file:dòng` (code), `REQ-xxx`/`TASK-xxx` (plan), hoặc `TC-xxx` (test case); Big O chỉ điền khi review code và vấn đề liên quan hiệu năng. Đề xuất xử lý luôn cụ thể, áp dụng được ngay.
- **So sánh chi tiết** (cho mỗi CRITICAL/WARNING): hiện tại vs đề xuất, kèm giải thích lý do + lợi ích.
- **Thống kê cuối**: `[X]` issue cần sửa (CRITICAL + WARNING) | `[Y]` điểm sáng (GOOD) | `[Z]` gợi ý (SUGGESTION).

## 4. Báo cáo chuyên biệt (security, dependency, test)

Ba loại còn lại trong bảng trên có **field riêng không fit khung review chung** — copy đúng template tương ứng, không gộp vào `review-report-template.md`:

- **Security**: 9 field bắt buộc theo đúng mục "Định dạng báo cáo" của skill [`review-web-security`](../review-web-security/SKILL.md) (severity+confidence, điều kiện khai thác, CWE/OWASP...).
- **Dependency audit**: package/severity theo tool/version hiện tại→fix/loại thay đổi/lệnh đề xuất — không tự chạy lệnh, chỉ đề xuất.
- **Test (digest)**: bản tóm tắt từ kết quả `qa-tester-agent`, không thay thế ma trận bao phủ hay bug report chi tiết mà agent đó đã tạo riêng.

## Khi áp dụng

- Báo cáo thay đổi/commit: ngay sau khi hoàn thành một task Edit/Write, trước khi báo "xong" hoặc trước khi soạn commit message (xem [git-workflow](../git-workflow/SKILL.md)).
- Báo cáo kế hoạch: ngay sau khi `planner-agent` `Write` xong `docs/implementation-plan.json`, trước khi dừng chờ người dùng duyệt.
- Báo cáo review/security/dependency/test: ngay sau khi việc tương ứng đã hoàn tất (ở nơi khác) và cần trình bày lại kết quả — không dùng skill này để tự thực hiện review/audit/test.
