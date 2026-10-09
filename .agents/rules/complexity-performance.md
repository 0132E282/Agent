---
trigger: model_decision
description: "Kiểm soát độ phức tạp thuật toán, vòng lặp, tài nguyên và đánh giá hiệu năng khi code hoặc review"
---

# Quy tắc kiểm soát độ phức tạp và hiệu năng

## 1. Độ phức tạp thuật toán

- Phân tích độ phức tạp thời gian và bộ nhớ của đoạn xử lý chính.
- Xác định rõ `n`, `m` đại diện cho dữ liệu nào.
- Ưu tiên `O(n)` hoặc `O(n log n)` khi xử lý danh sách.
- Với `O(n²)` trở lên: giải thích lý do, giới hạn đầu vào và đề xuất tối ưu.
- Không kết luận hiệu năng chỉ dựa vào Big O; cần xét database, network, I/O và bộ nhớ.

## 2. Vòng lặp

- Khi có vòng lặp lồng nhau, xác định số lần thực thi tối đa.
- Không mặc định hai vòng lặp lồng nhau luôn là `O(n²)`; duyệt `n` phần tử, mỗi phần tử duyệt `m` mục là `O(n × m)`.
- Tránh truy vấn database hoặc gọi API cho từng phần tử; ưu tiên eager loading, batch query hoặc batch request.
- Nếu tìm kiếm lặp lại trong danh sách, cân nhắc `Map`, `Set` hoặc bảng tra cứu.
- Không tải toàn bộ dữ liệu lớn vào RAM; cân nhắc phân trang, chunk, cursor hoặc streaming.
- Mọi vòng lặp retry phải có giới hạn số lần và điều kiện dừng.

## 3. Độ dài và trách nhiệm của hàm

- Mỗi hàm nên xử lý một trách nhiệm rõ ràng.
- Mục tiêu tham khảo: khoảng 20–40 dòng logic mỗi hàm.
- Hàm trên 50 dòng cần được xem xét khả năng tách nhỏ.
- Không tách hàm máy móc chỉ để đạt giới hạn số dòng.
- Ưu tiên tối đa 3–4 tham số; nếu nhiều hơn, cân nhắc một object/DTO.
- Ưu tiên độ sâu lồng điều kiện/vòng lặp không quá 3 cấp; cân nhắc guard clause và early return.

## 4. Độ phức tạp luồng điều khiển

- Mục tiêu cyclomatic complexity: không quá 10 mỗi hàm.
- Nếu vượt 10, xem xét đơn giản hóa các nhánh hoặc tách trách nhiệm.
- Phân biệt cyclomatic complexity với Big O: một chỉ số đo số đường đi trong code, một chỉ số đo mức tăng chi phí xử lý.
- Các ngưỡng là tín hiệu cần review, không phải lý do tự động từ chối code.

## 5. Giới hạn dữ liệu và tài nguyên

- Xác định giới hạn cho page size, batch size, file upload và số phần tử đầu vào.
- Chọn giới hạn dựa trên yêu cầu thực tế và kết quả đo.
- Với xử lý lớn, cân nhắc queue/job thay vì chạy trong HTTP request.
- Đánh giá timeout, số lần retry và bộ nhớ tối đa.
- Không tự đặt ngưỡng tùy ý khi chưa có yêu cầu hoặc bằng chứng.

## 6. Báo cáo khi review

Với mỗi vấn đề, trình bày:

- Vị trí: file và hàm.
- Hiện trạng: Big O, số query hoặc mức lồng nhau.
- Điều kiện gây chậm: kích thước dữ liệu, số lần thực thi.
- Ảnh hưởng: thời gian, bộ nhớ hoặc tải database.
- Đề xuất: cách tối ưu và đánh đổi.
- Cách kiểm chứng: benchmark, query log hoặc profiler.

Không khẳng định mức cải thiện hiệu năng nếu chưa đo.
