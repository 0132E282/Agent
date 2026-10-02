# 💬 Comment có kỷ luật — Minimal Comments + Better Comments

**Nhóm quy tắc kết hợp**: Minimal Comments + Better Comments Convention

## Khi nào được comment

- **Mặc định không comment.** Tên hàm/biến phải tự giải thích (xem [02-readability.md](./02-readability.md)).
- **Không comment logic đơn giản**: gán biến, gọi hàm tên rõ, `if`/vòng lặp hiển nhiên, CRUD, getter/setter.
- Chỉ comment khi giải thích **"tại sao"** mà code không tự nói được: ràng buộc nghiệp vụ, workaround, hành vi bất ngờ của thư viện/bên thứ ba.

## Nhãn comment (Better Comments)

| Nhãn | Ý nghĩa | Ví dụ |
|---|---|---|
| `*` | Thông tin quan trọng cần chú ý | `// * Tiền lưu int VND — không nhân 100.` |
| `!` | Cảnh báo: nguy hiểm, deprecated | `// ! Đổi thứ tự sẽ ghi đè locale khác.` |
| `?` | Câu hỏi / điểm cần xác nhận | `// ? Có nên expose method này ra API public?` |
| `TODO:` | Việc còn thiếu — kèm ngữ cảnh cụ thể | `// TODO: dispatch NewOrderNotification sau khi tạo đơn.` |
| `@param`/`@return` | Chỉ khi thêm thông tin kiểu mà signature không có | `@return array<string, int>` |

```php
/**
 * * Idempotent: VNPay gọi IPN nhiều lần cho cùng giao dịch.
 */
public function verifyIPN(array $data): array
{
    // ! Phải xác minh chữ ký trước khi đọc số tiền.
}
```

## Cấm

- Code bị comment-out (`// $old = ...`) — xoá, git đã lưu lịch sử.
- `TODO` không ngữ cảnh, comment lỗi thời, banner/đường kẻ trang trí.
- PHPDoc/JSDoc lặp lại đúng signature đã có trong code.

## Độ dài

- Mỗi dòng comment ≤ 180 ký tự; tối đa 1–3 dòng. Cần dài hơn ⇒ đưa vào docs thay vì nhồi vào comment.
- Sửa code có comment cũ, **cập nhật hoặc xoá** cho đúng với code mới — không để comment nói dối (xem [09-boy-scout-rule.md](./09-boy-scout-rule.md)).

## Khi áp dụng

- Định viết comment: tự hỏi *"xoá comment này đi, code còn tự giải thích được không?"* — nếu còn, không viết.
- Thấy comment giải thích "cái gì" thay vì "tại sao": xoá hoặc đổi tên biến/hàm cho rõ hơn thay vì giữ comment.
- Sửa đoạn code có comment liên quan: cập nhật cùng lúc, không để nó lỗi thời.
