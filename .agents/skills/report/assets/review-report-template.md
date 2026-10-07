# Mẫu Báo Cáo Review

Dùng để **trình bày lại** kết quả review/audit đã có sẵn (không phải để tự review) — cho cả 3 loại artifact mà agent [`reviewer-agent`](../../../agents/reviewer-agent.md) review: code/diff, kế hoạch triển khai (plan), test case. Copy các khối dưới đây và điền vào.

| Input | Output | Tổng |
|---|---|---|
| [N token / Không có số đo từ runtime] | [N token / Không có số đo từ runtime] | [N token / Không có số đo từ runtime] |

## Mức độ nghiêm trọng

- **CRITICAL** 🚨 `[!]` — lỗi logic nặng, lỗ hổng bảo mật, crash, silent catch, vi phạm SOLID nghiêm trọng.
- **WARNING** ⚠️ `[?]` — code smell, vấn đề hiệu năng (N+1, thuật toán độ phức tạp cao), thiếu edge case, magic number.
- **SUGGESTION** 💡 `[*]` — gợi ý refactor, đặt tên rõ hơn, tối ưu nhỏ.
- **GOOD** ✅ `[#]` — giải pháp tốt, đáng giữ nguyên, nên nhân rộng.

## Bảng tóm tắt

```markdown
| # | Vị trí | Vấn đề | Mức độ | Big O | Đề xuất xử lý |
|---|---|---|---|---|---|
| 1 | `path/to/file.ext:line` | [mô tả vấn đề] | [🚨/⚠️/💡/✅] | [O(n) hiện tại → O(?) sau sửa, nếu liên quan] | [hướng xử lý cụ thể] |
```

**Vị trí**: `file:dòng` khi review code; `REQ-xxx`/`TASK-xxx` khi review plan; `TC-xxx` khi review test case. Cột **Big O** chỉ điền khi review code và vấn đề liên quan hiệu năng — review plan/test case để trống.

## So sánh chi tiết (cho mỗi CRITICAL/WARNING)

```markdown
#### 📂 File: `path/to/file.ext`

🔴 Code hiện tại (dòng X-Y):
```[lang]
// code có vấn đề
```

🟢 Code đề xuất:
```[lang]
// code đã sửa
```

**Giải thích**: [lý do thay đổi + lợi ích, bao gồm Big O nếu liên quan hiệu năng]
```

## Thống kê cuối (bắt buộc)

```markdown
`[X]` issue cần sửa (CRITICAL + WARNING) | `[Y]` điểm sáng (GOOD) | `[Z]` gợi ý (SUGGESTION)
```
