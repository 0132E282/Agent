---
name: markitdown
description: Chuyển đổi tài liệu (PDF, DOCX, PPTX, XLSX/XLS, HTML, CSV, JSON, XML, ảnh, audio, ZIP, URL YouTube, EPUB) sang Markdown bằng công cụ markitdown của Microsoft. Dùng skill này mỗi khi người dùng đưa một file .pdf/.docx/.pptx/.xlsx, một thư mục tài liệu, hoặc một URL và muốn đọc, trích xuất, tóm tắt, dịch, hoặc tái sử dụng nội dung trong code, docs, hay website — ngay cả khi người dùng không nhắc tới từ "markdown" hay "markitdown".
---

# markitdown — chuyển đổi tài liệu sang Markdown

Chuyển các file office và định dạng khác thành Markdown sạch, dễ đọc, dễ tóm tắt và tái sử dụng. Nguồn: https://github.com/microsoft/markitdown

## Bắt đầu nhanh

```bash
markitdown --version || uv tool install "markitdown[all]"   # [all] = PDF, DOCX, PPTX, XLSX, audio, YouTube
markitdown file.docx -o /tmp/file.md                         # một file
python scripts/convert.py ./docs -o /tmp/md                  # cả thư mục, mỗi file ra một .md
```

Yêu cầu Python 3.10+. Nếu không cài `[all]`, một số định dạng sẽ lỗi `MissingDependencyException` kèm tên extra cần cài thêm (ví dụ `markitdown[pdf]`).

## Quy trình

1. **Chuyển đổi vào thư mục tạm/scratchpad, không phải vào repo.** Output là artifact trung gian — không commit các file `.md` vừa sinh ra hay tài liệu nguồn.
2. **Đọc lại kết quả trước khi dùng.** Kiểm tra heading, bảng, và văn bản non-ASCII (ví dụ dấu tiếng Việt). PDF scan và ảnh không có text layer nên sẽ cho ra rất ít hoặc không có nội dung — nói rõ điều này thay vì đoán nội dung.
3. **Dọn dẹp rồi mới đặt vào đúng vị trí.** Bỏ số trang/header/footer và gộp lại các dòng bị wrap cứng. Đặt nội dung vào nơi project cần (locale files, components, docs), theo convention có sẵn gần đó thay vì dán thẳng Markdown thô vào nơi không render được.

## Xem thêm

- Các điểm cần lưu ý và cách dọn dẹp theo từng định dạng (PDF, DOCX, XLSX, PPTX, HTML, ảnh, audio): đọc [FORMATS.md](FORMATS.md)
- Toàn bộ flag CLI, Python API, extras tùy chọn, tùy chọn Azure/LLM: đọc [REFERENCE.md](REFERENCE.md)
- Chuyển đổi theo lô (batch) một file hoặc một thư mục: chạy `scripts/convert.py --help`

## An toàn

- Không bật `--use-plugins` hoặc chuyển đổi file/URL không tin cậy; nó chạy với quyền của người dùng.
- Không copy dữ liệu cá nhân (bệnh nhân, khách hàng, nhân viên) từ tài liệu nguồn vào repo trừ khi người dùng rõ ràng muốn công khai.
- Không thiết lập các tính năng Azure/LLM trừ khi người dùng yêu cầu — chúng cần key và gửi dữ liệu đến dịch vụ bên ngoài.
