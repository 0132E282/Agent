# ✅ Chất lượng — Test + Static Analysis + Code Review

**Nhóm quy tắc kết hợp**: Test + Static Analysis + Code Review

## Cách áp dụng

- **Test luồng quan trọng**: ưu tiên business logic, edge case, luồng ảnh hưởng tiền/dữ liệu nhạy cảm — không cần cover 100%, nhưng không bỏ qua luồng rủi ro cao.
- **Static analysis** (linter/type checker) để bắt lỗi kiểu dữ liệu và code smell **trước khi** chạy thử — bắt buộc trước khi báo hoàn thành.
- **Code review**: thay đổi đáng kể nên được review lại (tự review nếu không có người khác) — kiểm tra đúng phạm vi, đúng chuẩn, không phá vỡ hành vi hiện có.
- Sửa bug → **viết test tái hiện bug trước khi fix** — đảm bảo bug không quay lại (regression test).

### Checklist trước khi hoàn thành

- [ ] Luồng chính và edge case quan trọng đã có test?
- [ ] Không có lỗi linter/type checker?
- [ ] Test hiện có vẫn pass (không phá vỡ tính năng cũ)?
- [ ] Đã tự review lại diff trước khi báo cáo xong?

## Khi áp dụng

- Trước khi báo "hoàn thành task" — bước bắt buộc cuối cùng, không bỏ qua kể cả khi gấp.
- Ngay sau khi fix một bug — thêm test khóa lại hành vi đúng.
