# Behavioral Patterns — Nhóm hành vi (10 pattern)

Giúp phân chia trách nhiệm, tổ chức thuật toán và điều phối giao tiếp giữa các đối tượng.

| Pattern | Ngữ cảnh nên dùng | Ví dụ backend |
|---|---|---|
| **Chain of Responsibility** | Request cần đi qua chuỗi handler; mỗi handler có thể xử lý, chuyển tiếp hoặc dừng chuỗi. Thứ tự xử lý có ý nghĩa. | Chuỗi kiểm tra xác thực → quyền → hạn mức → xử lý request; bước không đạt sẽ dừng. |
| **Command** | Muốn đóng gói một thao tác thành đối tượng để truyền đi, xếp hàng, lên lịch hoặc hỗ trợ undo. | `GenerateReportCommand` chứa dữ liệu yêu cầu và được thực thi sau. Undo cần được thiết kế riêng cho thao tác. |
| **Iterator** | Muốn duyệt collection mà không để bên sử dụng biết cấu trúc lưu trữ hoặc thuật toán duyệt. | Iterator tự lấy từng trang dữ liệu từ API; phía export chỉ duyệt từng bản ghi. |
| **Mediator** | Nhiều thành phần gọi chéo nhau khiến phụ thuộc rối; cần một nơi điều phối tương tác. | `CheckoutMediator` điều phối giỏ hàng, kho và thanh toán; các thành phần trao đổi qua mediator. |
| **Memento** | Cần chụp và phục hồi trạng thái đối tượng mà không để bên ngoài can thiệp vào dữ liệu nội bộ. | Bộ dựng trang lưu snapshot bố cục để undo/redo thao tác chỉnh sửa. |
| **Observer** | Một sự kiện cần thông báo cho nhiều bên đăng ký, và muốn thêm hoặc bỏ bên nhận mà ít ảnh hưởng bên phát. | Sự kiện tạo đơn hàng được các listener nhận để gửi email, ghi log và cập nhật thống kê. |
| **State** | Cùng thao tác nhưng hành vi khác nhau theo trạng thái; logic trạng thái và chuyển trạng thái đang trở nên phức tạp. | `Order::cancel()` xử lý khác nhau khi đơn đang chờ, đã thanh toán hoặc đang giao. |
| **Strategy** | Có nhiều thuật toán cho cùng một nhiệm vụ và cần chọn hoặc thay thế chúng. | Tính giảm giá bằng `PercentageDiscount`, `FixedDiscount`, `MemberDiscount`. |
| **Template Method** | Nhiều quy trình có cùng khung bước, nhưng khác cách thực hiện một số bước; muốn cố định trình tự chung. | `BaseImporter` chạy đọc → kiểm tra → chuẩn hóa → lưu; importer CSV và XML ghi đè bước đọc. |
| **Visitor** | Cấu trúc gồm nhiều loại đối tượng khá ổn định, nhưng thường cần bổ sung thao tác mới trên chúng. | Cây field của form nhận `ValidationVisitor`, `DocumentationVisitor`, `ExportVisitor`; mỗi visitor xử lý từng loại field. Thêm loại field mới thường phải sửa các visitor. |
