---
name: debugs
description: Chẩn đoán và sửa lỗi dựa trên đặc tả dự án. Dùng khi cần debug hành vi sai, exception, test thất bại hoặc lỗi hiệu năng; dùng được với Claude Code, Codex và các coding agent khác.
license: MIT
metadata:
  version: "1.1"
---

# Debugs

Dựa trên đặc tả để xác định hành vi đúng, tìm nguyên nhân gốc và kiểm chứng bản sửa. Dùng công cụ đọc, tìm kiếm và chạy lệnh có sẵn của agent.

## Quy trình

1. **Đọc căn cứ**: đọc hướng dẫn áp dụng (`AGENTS.md`, `CLAUDE.md` hoặc tương đương), rồi đặc tả liên quan trong README, `docs/`, issue hoặc yêu cầu người dùng. Phân biệt quy ước làm việc với đặc tả chức năng; nếu thiếu hoặc mâu thuẫn ảnh hưởng cách sửa, hỏi phần cần xác nhận.
2. **Tái hiện**: xác định hành vi mong đợi/thực tế, input và môi trường; chạy trường hợp nhỏ nhất gây lỗi. Ghi kết quả thật, không khẳng định nguyên nhân khi chưa có bằng chứng.
3. **Tìm nguyên nhân**: lần theo luồng dữ liệu và dependency, kiểm tra thay đổi gần đây nếu là regression. Kiểm chứng từng giả thuyết, mỗi lần đổi một yếu tố; không sửa bằng phỏng đoán.
4. **Sửa đúng phạm vi**: tạo regression test và xác nhận fail vì lỗi đang xét trước khi sửa. Nếu không thể tự động hóa, ghi cách kiểm tra trước/sau. Sửa nguyên nhân, không tắt test hoặc đổi expected trái đặc tả. Nếu chỉ được yêu cầu chẩn đoán, báo nguyên nhân và đề xuất sửa.
5. **Kiểm chứng**: chạy lại trường hợp lỗi, regression test, test liên quan và lint/type check phù hợp. Với hiệu năng, đo trước/sau trong cùng điều kiện. Dọn log tạm do mình thêm, giữ thay đổi của người dùng và cập nhật tài liệu bị ảnh hưởng.

## Báo cáo

Nêu ngắn gọn: **đặc tả làm căn cứ** (`file:line` hoặc nguồn yêu cầu), **nguyên nhân và bằng chứng**, **bản sửa**, **kết quả kiểm chứng và giới hạn còn lại**. Phân biệt dữ kiện với giả thuyết; không báo pass cho kiểm tra chưa chạy.
