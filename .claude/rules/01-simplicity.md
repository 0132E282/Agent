# 🎯 Đơn giản — KISS + YAGNI

**Nhóm quy tắc kết hợp**: KISS + YAGNI (You Ain't Gonna Need It)

## Cách áp dụng

- Chọn **giải pháp đơn giản nhất** đáp ứng đúng yêu cầu hiện tại — không thêm config/interface/layer trừu tượng cho nhu cầu *giả định* tương lai.
- Ba dòng lặp lại còn tốt hơn một abstraction sinh non "phòng khi cần mở rộng".
- Giải pháp cần vẽ sơ đồ mới giải thích được → đang quá phức tạp, đơn giản hóa lại.

```javascript
// ❌ Factory + strategy pattern cho 2 loại discount cố định
class DiscountStrategyFactory { ... }
// ✅ KISS: xử lý trực tiếp
function calculateDiscount(order) {
  return order.total * (order.type === "VIP" ? 0.2 : 0.1);
}
```

## Khi áp dụng

- Trước khi thêm abstraction: *"Đang giải quyết vấn đề đã tồn tại, hay vấn đề tưởng tượng?"*
- Khi tự review trước khi báo cáo: loại bỏ phần không phục vụ trực tiếp yêu cầu đã giao.
