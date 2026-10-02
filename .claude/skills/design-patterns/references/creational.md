# Creational Patterns — Nhóm khởi tạo đối tượng (5 pattern)

Giúp kiểm soát cách tạo đối tượng, nhất là khi việc khởi tạo có nhiều biến thể hoặc cấu hình.

| Pattern | Ngữ cảnh nên dùng | Ví dụ backend |
|---|---|---|
| **Factory Method** | Lớp cha có quy trình chung nhưng cần cho lớp con quyết định loại đối tượng được tạo. Hữu ích khi xây thư viện có điểm mở rộng. | `BaseExporter` gọi `createWriter()`; `CsvExporter` và `PdfExporter` trả về writer tương ứng. |
| **Abstract Factory** | Cần tạo một bộ đối tượng liên quan, bảo đảm chúng thuộc cùng một biến thể và tương thích với nhau. | `PaymentProviderFactory` tạo đồng bộ payment client, refund client và webhook verifier cho cùng nhà cung cấp. |
| **Builder** | Đối tượng phức tạp, có nhiều tham số tùy chọn hoặc cần được xây qua nhiều bước. | Xây cấu hình báo cáo bằng `withColumns()`, `withFilters()`, `withRelations()`, rồi `build()`. |
| **Prototype** | Cần tạo đối tượng bằng cách sao chép mẫu đã cấu hình; không muốn bên sử dụng phụ thuộc vào lớp cụ thể. | Clone cấu hình một module CRUD mẫu rồi đổi tên, trường dữ liệu và quyền. Cần xác định rõ phần nào sao chép sâu (deep copy), phần nào dùng chung. |
| **Singleton** | Thực sự cần một instance dùng chung trong phạm vi chương trình và một điểm truy cập thống nhất. | Một registry cấu hình dùng chung trong tiến trình. **Không** đồng nghĩa với "một instance duy nhất trên mọi server"; cần cân nhắc vì trạng thái toàn cục làm việc kiểm thử khó hơn. |
