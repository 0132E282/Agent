# Chọn cách phân tích theo engine

Đây là checklist định hướng, không phải bảng tương thích mọi phiên bản. Xác minh cú pháp, quyền và việc lệnh có thực thi workload bằng tài liệu chính thức đúng phiên bản. Ưu tiên estimated plan trước actual execution khi đủ cho câu hỏi.

| Engine | Bằng chứng cần xem | Điểm cần điều tra |
|---|---|---|
| MySQL | EXPLAIN; actual analysis khi phiên bản hỗ trợ và được phép; slow query/performance metrics | access path, key, rows/filtered, loops, sort/temp, join fan-out, lock waits |
| PostgreSQL | EXPLAIN; ANALYZE/BUFFERS khi được phép thực thi | estimated vs actual rows, loops, buffers, spill, scan/join, statistics |
| SQLite | EXPLAIN QUERY PLAN; timing trong môi trường phù hợp | scan/search, temporary B-tree, composite index, giới hạn concurrency |
| SQL Server | estimated/actual plan và I/O/time metrics đúng công cụ | logical reads, estimates, seek/scan, spill, parameter sensitivity, waits |
| MongoDB | explain verbosity phù hợp; execution statistics nếu được phép | keys/docs examined so với nReturned, stage order, lookup/unwind, sort, shard fan-out |
| Redis | slowlog/latency và đặc tính command theo tài liệu | blocking work, key/value size, hot key, round-trip, giới hạn batch; SCAN không phải snapshot và có thể lặp key |
| DynamoDB | consumed capacity, latency/throttle, key/index schema, evaluated/returned items | Query vs Scan, partition key, hot partition, GSI và consistency; filter không tự giảm số item đã đọc |
| Cassandra | data model theo access pattern, partition size, tombstone, tracing/metrics trong phạm vi phù hợp | partition fan-out, hot partition, filtering, clustering order, consistency |
| Elasticsearch | mapping, shard count, query/profile metrics khi phù hợp | text vs keyword, filter/query semantics, aggregation, deep pagination, shard fan-out; profiling thêm overhead |

Với engine khác: đọc tài liệu chính thức cho query language, access path, index/data model, plan/profiler, consistency và limits. Không chuyển nguyên SQL optimization sang engine đó.

## Laravel và nhiều connection

Xác định connection và SQL/bindings thực tế, global scope, soft-delete, tenant filter, eager loading và N+1. Dùng Query Builder/Eloquent khi phù hợp convention; giữ parameter binding. Transaction trên một connection không tạo atomicity giữa MySQL, SQLite hoặc NoSQL connection khác. Kiểm tra engine đích thay vì chỉ test SQLite rồi khẳng định MySQL tương đương.
