---
trigger: model_decision
description: "Kiểm soát thay đổi rule/template và báo cáo bắt buộc khi setup-agent cấu hình repository"
---

# Quy tắc setup rule/template và báo cáo

Áp dụng khi tạo, chỉnh sửa, đổi tên hoặc xóa rule/template trong repository, đặc biệt khi `setup-agent` thực hiện setup công cụ, cấu hình agent hoặc đồng bộ tài nguyên dùng chung.

## Trước khi sửa

- Đọc hướng dẫn hiện có và kiểm tra các file liên quan trước khi sửa.
- Xác định nguồn chuẩn, adapter hoặc symlink liên quan trước khi tạo file mới.
- Giữ nội dung nhất quán; không tạo quy tắc trùng lặp hoặc mâu thuẫn.

## Khi thay đổi

- Nếu đổi tên, đường dẫn hoặc cấu trúc, cập nhật mọi tham chiếu, tài liệu và ví dụ sử dụng liên quan.
- Giữ placeholder, cú pháp Markdown/YAML/JSON và format của template hợp lệ.
- Không ghi secret, credential hoặc giá trị môi trường thật vào rule/template.
- Chỉ mở rộng phạm vi khi có file tham chiếu thực sự bị ảnh hưởng.

## Kiểm tra sau khi sửa

- Kiểm tra cú pháp file đã đổi.
- Kiểm tra link tương đối, path, symlink và placeholder của template.
- Chạy checker/validator sẵn có của repository trong đúng phạm vi.
- Không khẳng định đã kiểm tra nếu chưa thực sự chạy; nếu chưa thể kiểm tra, ghi rõ lý do.

## Báo cáo bắt buộc của setup-agent

Sau khi hoàn tất, báo cáo phải nêu:

- File đã thay đổi.
- Nội dung thay đổi chính.
- Lý do thay đổi.
- Ảnh hưởng đến cách agent làm việc hoặc kết quả tạo từ template.
- Kiểm tra đã thực hiện và kết quả thực tế.
- Vấn đề còn tồn tại, bước thủ công cần người dùng làm hoặc giới hạn chưa kiểm chứng.

### Mẫu báo cáo

```markdown
## 🛠️ Báo cáo setup rule/template

- File: `[đường dẫn]`
  Mô tả: [đã thêm/sửa/xóa nội dung gì; lý do và ảnh hưởng chính]
  Điều kiện kích hoạt: [khi nào rule/template được áp dụng hoặc agent nào sử dụng]

### Kiểm tra

- [lệnh/nội dung đã kiểm tra] — [kết quả thực tế]

### Còn tồn tại

- [vấn đề, bước thủ công hoặc giới hạn chưa kiểm chứng; nếu không có ghi `Không có`]
```
