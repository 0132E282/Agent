---
trigger: model_decision
description: "Áp dụng khi nhiệm vụ liên quan: 🗄️ An toàn database — Read-Only by Default + Manual Migration Only"
---

# 🗄️ An toàn database — Read-Only by Default + Manual Migration Only

**Nhóm quy tắc kết hợp**: mở rộng của Phân quyền + Transaction ([`rules/07`](./07-data-safety.md)) áp dụng riêng cho thao tác trực tiếp lên database.

## Cách áp dụng

- **Mặc định mọi truy cập database là read-only.** Được tự do `SELECT`/query/aggregation/explain/profiler trong phạm vi đã cho phép truy cập — nhưng **không tự ý** `INSERT`/`UPDATE`/`DELETE`, không tự ý chạy DDL (`CREATE`/`ALTER`/`DROP` table, column, index), không tự ý chạy migration hay seed dữ liệu.
- Áp dụng cho cả SQL và NoSQL (không update/delete document, không đổi index/collection schema, không flush cache của production).
- **Được soạn/viết** migration, câu lệnh đổi schema, hoặc script ghi dữ liệu khi người dùng cần — mặc định chỉ đưa ra để người dùng **tự chạy thủ công**, giống nguyên tắc Explicit Authorization của [`rules/10`](./10-commit-discipline.md) áp dụng cho git: viết xong không đồng nghĩa được phép chạy.
- **Ngoại lệ**: nếu người dùng yêu cầu rõ ràng *cả hai* — thiết kế migration **và** chạy nó trong project — thì được phép tự chạy đúng migration đó. Không suy rộng từ một yêu cầu đọc/phân tích/thiết kế sang việc tự "tiện tay" chạy luôn khi chưa được yêu cầu chạy.
- Môi trường test/sandbox do người dùng chỉ định rõ là ngoại lệ hợp lệ; không tự suy đoán một kết nối là "chỉ để test" nếu không được xác nhận.

## Khi áp dụng

- Mọi lúc có kết nối tới database thật (không phải sandbox đã được xác nhận) — trước khi chạy bất kỳ câu lệnh ghi hoặc migration.
- Khi dùng skill [`database`](../skills/database/SKILL.md): rule này là lớp bắt buộc chung, phần "Phạm vi và bảo vệ dữ liệu" của skill là chi tiết bổ sung theo từng engine.
