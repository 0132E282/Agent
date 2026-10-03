# Mẫu Báo Cáo Test (digest)

Dùng để tóm tắt kết quả **đã thiết kế/thực thi** bởi agent [`qa-tester`](../../../agents/qa-tester.md) thành bản ngắn dễ copy vào PR/commit — không thay thế ma trận bao phủ, mẫu test case chi tiết hay bug report đầy đủ mà `qa-tester` đã tạo riêng.

```markdown
## ✅ Báo cáo test

**Phạm vi**: [feature/luồng được test] — **Tổng**: [N] test case cho [M] yêu cầu

| REQ | Test case ID | Priority | Trạng thái | Bằng chứng |
|---|---|---|---|---|
| REQ-001 | TC-MODULE-001 | P1 | Pass / Fail / Blocked / Skipped / Not Run | [log/response/screenshot đã che dữ liệu nhạy cảm] |

**Thống kê**: `[R]` Ready, `[D]` Draft | Đã thực thi `[E]`: `[P]` Pass, `[F]` Fail, `[B]` Blocked, `[S]` Skipped, `[U]` Not Run

### Bug phát hiện (nếu có)
- `BUG-xxx`: [điều kiện gây lỗi + hành vi sai, severity] — chi tiết đầy đủ ở bug report riêng của `qa-tester`.

### Rủi ro còn lại
- [Luồng/edge case chưa test và lý do — không ghi "đã test" khi chưa chạy]
```

Chưa thực thi → ghi rõ "Chưa thực thi kiểm thử", không suy ra Pass từ việc đã thiết kế xong.
