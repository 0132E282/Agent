# 🏕️ Cải thiện dần — Boy Scout Rule

**Nhóm quy tắc kết hợp**: Boy Scout Rule

## Cách áp dụng

- "Để lại khu cắm trại sạch hơn lúc bạn đến" — khi sửa một file, tiện tay dọn vấn đề nhỏ **trực tiếp liên quan** phần đang sửa (tên biến tối nghĩa, comment lỗi thời, dead code trong cùng hàm).
- **Giữ phạm vi thay đổi vừa đủ**: đây không phải giấy phép refactor toàn bộ file/module không liên quan đến task.
- Ranh giới: dọn dẹp trong **cùng function/block** đang sửa → làm. Ở **file/module khác** hoặc đòi hỏi thay đổi lớn → để lại, báo cho người giao task thay vì tự ý mở rộng.

```javascript
// Task: fix bug tính sai discount trong hàm calculateTotal

// ✅ Hợp lý: sửa bug + đổi tên biến tối nghĩa ngay trong hàm đang sửa
function calculateTotal(order) {
  const discountRate = order.isVip ? 0.2 : 0.1; // trước đây là "dr", đã đổi tên khi sửa bug tại đây
  return order.subtotal * (1 - discountRate);
}

// ❌ Vượt phạm vi: tiện tay refactor luôn toàn bộ OrderService không liên quan đến bug
```

## Khi áp dụng

- Mỗi lần mở một file để sửa: dọn những gì nhỏ, an toàn, nằm ngay trong phạm vi đang chạm vào.
- Không dùng quy tắc này để biện minh cho việc refactor lan rộng ngoài yêu cầu.
