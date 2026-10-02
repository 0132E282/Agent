# Mẫu đầu ra

Chỉ dùng mục cần thiết theo độ lớn yêu cầu.

## 1. Yêu cầu và dữ liệu

Nêu engine/phiên bản, semantics, input/output, schema/index được xác nhận, giả định và thông tin thiếu.

## 2. Query đề xuất

Đưa query native đúng dialect, bindings hoặc payload driver. Với Redis dùng command và key/argument; với MongoDB dùng filter/pipeline; không bắt mọi engine trả SQL. Ghi rõ có thể chạy hay chỉ là mẫu cần chỉnh schema. Cung cấp ORM nếu được yêu cầu.

## 3. Đánh giá

| Query/fingerprint | Finding | Bằng chứng | Tác động dự kiến/đã đo | Tin cậy |
|---|---|---|---|---|
| ... | ... | SQL/plan/metrics | ... | Quan sát/Giả thuyết/Chưa xác định |

Giải thích operator, cardinality, scan/sort/join/fan-out và độ phức tạp có điều kiện. Khi thiếu plan, không đưa latency hoặc optimizer cost tưởng tượng.

## 4. Đề xuất tối ưu

| Ưu tiên | Thay đổi | Vì sao | Tradeoff | Cách kiểm chứng |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

Tách query rewrite, index/data model và thay đổi kiến trúc. Cung cấp DDL/index command như đề xuất, không tự áp dụng. Nêu index hiện có trùng/lặp nếu có căn cứ.

## 5. Kết quả và giới hạn

Ghi các kiểm tra thật sự đã chạy, kết quả correctness và trước/sau, số liệu chưa có, rủi ro và bước tiếp theo. Nếu chỉ phân tích tĩnh, nói rõ chưa thực thi.

## Prompt mẫu

> Từ yêu cầu [nghiệp vụ], schema [đường dẫn] và engine [tên/phiên bản], viết query có tham số. Phân tích correctness, độ phức tạp và nguy cơ query nặng; đề xuất index hoặc rewrite kèm tradeoff. Chưa chạy query hay thay đổi database.

> Review các query và execution plan đính kèm. Xếp hạng theo metrics có sẵn, xác định bottleneck và đề xuất tối ưu. Không suy đoán số liệu bị thiếu.
