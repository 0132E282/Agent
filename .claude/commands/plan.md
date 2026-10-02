---
description: Pipeline lập kế hoạch đầy đủ — research → system-design (nếu cần) → planner → review kế hoạch → report
argument-hint: "<đường dẫn đặc tả hoặc mô tả tính năng>"
---

Lập kế hoạch triển khai đầy đủ cho: $ARGUMENTS — chạy tuần tự từng bước, báo ngắn gọn sau mỗi bước trước khi sang bước kế, không dồn cả pipeline thành một lần xuất:

1. **Research** (agent `researcher`) — chỉ khi đặc tả thiếu thông tin cần tra (tài liệu/API bên ngoài, phần codebase chưa rõ). Bỏ qua bước này nếu đặc tả đã đủ rõ để thiết kế ngay.
2. **System Design** (agent `system-design`) — chỉ khi bài toán cần kiến trúc/HLD/LLD/mô hình dữ liệu mới. Tự `Write` tài liệu ra `docs/system-design.md` theo các mục: bài toán & phạm vi, kiến trúc tổng thể, dữ liệu & API, độ tin cậy/bảo mật/hiệu năng, rủi ro. Bỏ qua nếu chỉ là thay đổi nhỏ trong kiến trúc đã có.
3. **Planner** (agent `planner`, chế độ PLAN) — giao đường dẫn file (`docs/system-design.md` và/hoặc `docs/requirement-analysis.md` nếu có, hoặc đặc tả gốc nếu không có gì) để `planner` tự đọc bằng Read/Grep, **không dán nguyên văn tài liệu vào prompt** — agent tự đọc file sẽ luôn đủ ngữ cảnh và tránh prompt quá dài. Có hook an toàn chặn prompt bất thường dài, nhưng với cách gọi bằng đường dẫn file này thường không cần tới. `planner` tự `Write` kế hoạch ra `docs/implementation-plan.md`, chia task có truy vết REQ → Task → AC → Test.
4. **Review kế hoạch** (agent `reviewer`) — review lại chính bản kế hoạch vừa tạo (không phải code): yêu cầu nào chưa có task tương ứng, task nào mơ hồ/thiếu acceptance criteria, rủi ro nào chưa có phương án. Sửa trực tiếp các vấn đề tìm thấy.
5. **Report** (skill `report`) — xuất báo cáo ngắn tóm tắt: phạm vi, số task, rủi ro chính, bước tiếp theo — để người dùng duyệt nhanh.

Không tự sửa code sản phẩm ở bất kỳ bước nào. Sau khi có kế hoạch + report, chờ người dùng duyệt rồi mới giao `coding-agent` triển khai.
