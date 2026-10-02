# Phân tích chi phí và query nặng

## Ba loại kết luận

- Quan sát: có plan/metrics thực tế, nêu nguồn, tham số và môi trường.
- Giả thuyết: rủi ro dựa trên query/data model; nêu điều kiện làm rủi ro xảy ra.
- Chưa xác định: thiếu cardinality, index, plan hoặc workload.

Không tính điểm độ phức tạp bằng số JOIN/subquery hay độ dài query. Không suy ra milliseconds từ Big-O hoặc optimizer cost. Cost của engine thường là đơn vị mô hình, không so sánh tùy tiện giữa engine hay cấu hình.

## Độ phức tạp có điều kiện

Nếu người dùng yêu cầu Big-O, định nghĩa n/m/k và giả định physical operator. Ví dụ scan thường O(n); sort so sánh thường O(k log k); nested-loop không có lookup phù hợp có thể O(n*m); index lookup thường có thành phần O(log n + k), nhưng phụ thuộc loại index, I/O và data layout. Hash join, spill, parallelism và distributed fan-out thay đổi mô hình. Đây là ước lượng thuật toán, không phải dự đoán latency.

Với NoSQL, phân tích document/key examined, partition/shard fan-out, payload, network round-trip, read/write capacity, hot partition và consistency. Không gán một Big-O chung cho mọi NoSQL.

## Dấu hiệu cần điều tra

- SQL: predicate không sargable, implicit cast, join tăng số dòng, correlated subquery lặp, sort/hash spill, offset sâu, count lớn, fetch dư cột, N+1, lock wait.
- Document/search: scan nhiều document, filter muộn, lookup/unwind nhân bản, sort không có đường truy cập phù hợp, aggregation lớn, deep pagination, nhiều shard và payload lớn.
- Key/value/wide-column: keyspace scan không giới hạn, hot key/partition, fan-out, nhiều round-trip, oversized value/collection, tombstone hoặc filtering tốn kém khi engine liên quan.

Scan có thể hợp lý với bảng nhỏ hoặc query đọc phần lớn dữ liệu. Index có thể tốn hơn scan. Covering/composite/partial/expression index tùy engine và phiên bản; kiểm chứng thay vì áp dụng công thức cố định.

## Xếp hạng

Nếu có telemetry, nhóm query theo fingerprint để giữ cấu trúc và ẩn literals. Dùng count, latency p50/p95/p99, tổng thời gian, CPU/I/O, rows/docs examined, bytes, waits, spill hoặc capacity. Count × mean latency chỉ là xấp xỉ tổng thời gian thực thi, không phải CPU và không thay thế dữ liệu tổng sẵn có. Query hiếm rất chậm và query nhanh gọi cực nhiều có tác động khác nhau.

Nếu chỉ có một query hoặc không có workload, không tuyên bố đã tìm query nặng nhất hệ thống. Nêu phạm vi và mức tin cậy.

## Tối ưu và kiểm chứng

1. Đo baseline với tham số phổ biến và lệch phân bố; ghi row count, cache state, concurrency, cấu hình.
2. Kiểm tra kết quả tương đương theo kiểu dữ liệu và semantics: set/multiset, duplicate, ordering, null/missing, pagination, timezone, consistency. Không coi thứ tự dòng ổn định khi query không quy định ordering.
3. Thay từng yếu tố có thể cô lập; đo nhiều lần ở môi trường phù hợp.
4. So sánh latency phân phối và tài nguyên, cả write overhead/storage khi thêm index.
5. Với cache/precompute, nêu invalidation, TTL/freshness, failure và consistency; với cursor pagination nêu thay đổi hợp đồng nếu có.
6. Báo giới hạn dữ liệu mẫu; không ngoại suy chắc chắn lên production.
