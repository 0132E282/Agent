---
trigger: model_decision
description: "Áp dụng khi nhiệm vụ liên quan: ♻️ Tái sử dụng — DRY"
---

# ♻️ Tái sử dụng — DRY

**Nhóm quy tắc kết hợp**: DRY (Don't Repeat Yourself)

## Cách áp dụng

- Gom logic trùng lặp lại một nơi **khi chúng cùng ý nghĩa nghiệp vụ** và cùng lý do thay đổi.
- **Không gom chỉ vì nhìn giống nhau** — hai đoạn code giống hệt nhưng phục vụ nghiệp vụ khác nhau (validate địa chỉ giao hàng vs thanh toán) có thể cần tiến hóa độc lập. Gom nhầm tạo coupling sai, gãy cả hai nơi khi chỉ một nơi cần đổi.
- **Rule of Three**: trùng lặp 2 lần chấp nhận được, trùng lần thứ 3 mới refactor — tránh trừu tượng hóa sớm khi chưa rõ pattern thật.

```javascript
// ❌ Gom sai vì "nhìn giống nhau"
function validateAddress(address) { /* dùng chung shipping+billing nhưng billing cần check thêm thuế */ }

// ✅ Tách theo ý nghĩa nghiệp vụ, dùng chung phần thật sự giống nhau
function validatePostalFormat(address) { ... }
function validateShippingAddress(a) { validatePostalFormat(a); }
function validateBillingAddress(a) { validatePostalFormat(a); validateTaxId(a.taxId); }
```

## Khi áp dụng

- Copy-paste lần 2–3: dừng lại hỏi *"cùng ý nghĩa nghiệp vụ, hay chỉ tình cờ giống cú pháp?"*
- Trước khi tạo shared helper/util: xác nhận mọi nơi gọi nó thực sự nên đổi cùng nhau trong tương lai.
