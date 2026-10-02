# 📖 Dễ đọc — Clean Code + Coding Convention

**Nhóm quy tắc kết hợp**: Clean Code + Coding Convention

## Cách áp dụng

- **Tên rõ nghĩa**, không viết tắt trừ thuật ngữ chuẩn ngành (`id`, `url`): `user` thay vì `usr`, `temporaryToken` thay vì `tmp`.
- **Hàm làm một việc**: tên cần chữ "và" (`validateAndSave`) để mô tả → tách nhỏ hơn.
- **Format thống nhất** với codebase hiện có — không áp đặt style cá nhân.
- **Early return** để tránh lồng `if/else` sâu.
- Comment giải thích **"tại sao"**, không giải thích **"cái gì"** (code đã tự nói).

```javascript
// ❌ function p(u) { if (u) { if (u.a) return u.n; } }
// ✅
function getUserDisplayName(user) {
  if (!user || !user.isActive) return null;
  return user.name;
}
```

## Khi áp dụng

- Mọi lần đặt tên biến/hàm/class/hằng số, hoặc viết/sửa comment.
- Trước khi commit: đọc lại code như người lần đầu thấy nó.
