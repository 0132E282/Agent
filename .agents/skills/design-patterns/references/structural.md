# Structural Patterns — Nhóm cấu trúc (7 pattern)

Giúp kết hợp các đối tượng và lớp mà vẫn dễ thay đổi, mở rộng.

| Pattern | Ngữ cảnh nên dùng | Ví dụ backend |
|---|---|---|
| **Adapter** | Muốn sử dụng thư viện hoặc hệ thống có interface không tương thích với interface ứng dụng đang dùng. | Bọc SDK thanh toán bên ngoài thành `PaymentGatewayInterface` với các hàm `pay()` và `refund()`. |
| **Bridge** | Có hai chiều biến đổi độc lập; kế thừa theo mọi tổ hợp khiến số lớp tăng nhanh. | Tách loại báo cáo `SalesReport`, `InventoryReport` khỏi bộ render `PdfRenderer`, `HtmlRenderer`; có thể kết hợp tùy ý. |
| **Composite** | Dữ liệu có cấu trúc cây và muốn xử lý phần tử đơn lẻ lẫn nhóm phần tử qua cùng interface. | `Field` và `FieldGroup` đều có `validate()`; group gọi đệ quy xuống các field và group con. |
| **Decorator** | Cần bổ sung hành vi bằng các lớp bọc có thể kết hợp, giữ nguyên interface của đối tượng. | Bọc dịch vụ gửi thông báo bằng `LoggingNotifier`, rồi `RetryNotifier`. |
| **Facade** | Một subsystem có nhiều thành phần và bước gọi; muốn cung cấp một interface đơn giản cho bên sử dụng. | `InvoiceFacade::issue()` che giấu việc tạo hóa đơn, dựng PDF, lưu file và gửi email. |
| **Flyweight** | Có rất nhiều đối tượng giống nhau, dữ liệu lặp gây áp lực RAM; có thể tách phần bất biến để dùng chung. | Hàng chục nghìn field trong bộ dựng tài liệu cùng tham chiếu một định nghĩa kiểu chữ thay vì mỗi field giữ một bản sao. |
| **Proxy** | Cần đối tượng đại diện để kiểm soát truy cập, trì hoãn khởi tạo hoặc giao tiếp với dịch vụ từ xa. | `ProtectedDocumentProxy` kiểm tra quyền trước khi chuyển lời gọi sang dịch vụ đọc tài liệu. |
