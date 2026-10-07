# Mẫu Báo Cáo Thay Đổi

Dùng ngay sau khi Edit/Write hoàn tất một task code. Copy khối dưới đây và điền vào — **đây là bản mặc định, dừng lại ở "Tóm tắt"**. Không tự thêm mục code cũ/mới hay giải thích quyết định kỹ thuật, kể cả khi thay đổi có vẻ đáng kể.

```markdown
## 📝 Báo cáo thay đổi

Tổng số file đã tạo/sửa/xóa: [N] file ([tóm tắt ngắn, ví dụ: 2 tạo mới, 3 sửa, 1 xóa])

| Trạng thái | File | Mô tả |
|---|---|---|
| Tạo / Sửa / Xóa | `path/to/file.ext` | [mô tả ngắn gọn thay đổi gì] |

### Tóm tắt
- ➕ Thêm mới: [số dòng/function]
- ✏️ Sửa đổi: [số dòng/function]
- ➖ Xóa bỏ: [số dòng/function] (nếu có)
```

## Chỉ dùng khi người dùng yêu cầu rõ ("chi tiết hơn", "xem code cụ thể")

Thêm mục này **sau** khối trên, không thay cho nó:

```markdown
### Chi tiết thay đổi

#### 1. [Tên file]
**Dòng [X-Y]**: [mô tả thay đổi]

🔴 Code cũ:
```[lang]
// code cũ
```

🟢 Code mới:
```[lang]
// code mới
```

**Lý do**: [tại sao thay đổi — vấn đề nghiệp vụ/kỹ thuật nào được giải quyết]
```
