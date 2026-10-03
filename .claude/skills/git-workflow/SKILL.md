---
name: git-workflow
description: Thực thi quy tắc git bắt buộc — commit (rules/10-commit-discipline.md) và tạo pull request/resolve conflict (rules/11-pull-request-conflict.md). Tuyệt đối không tự ý git commit khi chưa có lệnh rõ ràng, không commit vụn vặt, message theo Conventional Commits (tiêu đề "<type>: mô tả" ≤ 75 ký tự); khi tạo PR phải check conflict và biết nhánh nào được ưu tiên giữ. Dùng ngay trước khi chạy git commit, tạo/update PR, hoặc resolve conflict. Đi kèm script validate-commit-message.sh để kiểm tra message tự động.
license: MIT
metadata:
  version: "1.2"
---

# 🔧 Git Workflow

Skill gatekeeper bắt buộc cho **commit** và **pull request** — hành động git có thể thay đổi lịch sử/chia sẻ trạng thái với người khác. Áp dụng dù đang ở phiên chính hay subagent, độc lập với [`coding-agent`](../../agents/coding-agent.md).

## 1. Trước khi `git commit` ([rules/10](../../rules/10-commit-discipline.md))

1. **Có lệnh rõ ràng từ người dùng chưa?** Chưa có → dừng, không commit, bất kể code đã xong hay chưa.
2. **Gộp đúng phạm vi** — một commit cho toàn bộ thay đổi liên quan của task hiện tại, không tách vụn, không gộp thêm thay đổi ngoài phạm vi. Chỉ 2 kiểu phạm vi hợp lệ: "push hết" (toàn bộ thay đổi hiện có, khi người dùng nói rõ) hoặc "push theo tính năng" (chỉ phần liên quan task, mặc định khi không chỉ định) — **cả hai đều tuyệt đối không được kèm file tmp/scratch/debug/test thử nghiệm hoặc file rác**. Chạy `git status` rà lại trước `git add`; thấy file rác do mình tạo trong session thì dọn bằng skill [`cleanup-temp-files`](../cleanup-temp-files/SKILL.md) trước, không add vào commit.
3. **Conventional Commits**: tiêu đề `<type>: <mô tả ngắn gọn>` (`feat`/`fix`/`refactor`/`docs`/`test`/`chore`/`style`/`perf`/`build`/`ci`), tối đa **75 ký tự**; body liệt kê thay đổi chính, nêu rõ vấn đề được giải quyết.
4. **Chạy script kiểm tra** trước khi commit thật:
   ```bash
   echo "feat: thêm hook tự động format code bằng Prettier sau khi edit" \
     | bash .claude/skills/git-workflow/scripts/validate-commit-message.sh -
   ```
   `exit 0` + `✅` nếu hợp lệ; `exit 1` + lỗi cụ thể nếu sai format hoặc vượt 75 ký tự. Script chỉ kiểm tra format máy kiểm được (tiêu đề không rỗng, đúng `<type>: <mô tả>`, độ dài) — phần "why" trong body do người soạn tự đảm bảo theo rule.

Có thể cài làm git hook để áp dụng cho mọi lần commit kể cả thủ công:
```bash
cp .claude/skills/git-workflow/scripts/validate-commit-message.sh .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

## 2. Trước khi tạo Pull Request / khi gặp conflict ([rules/11](../../rules/11-pull-request-conflict.md))

1. Trước khi tạo PR, luôn kiểm tra nhánh có **conflict** với nhánh đích (base, thường `main`) không.
2. Có conflict: **đọc cả hai phía** (`<<<<<<<` / `=======` / `>>>>>>>`) trước khi quyết định — không xóa trắng một bên mà không xem nội dung.
3. **Conflict chỉ do format/vị trí dòng**: giữ code của **nhánh nguồn** (nhánh đang tạo PR).
4. **Conflict do logic thật sự thay đổi ở cả hai bên**: giữ logic của **nhánh nguồn** (vì đó là thay đổi cần merge vào), nhưng vẫn đọc lướt phần bị ghi đè ở nhánh đích — nghi ngờ đó là fix quan trọng không liên quan task của PR thì dừng lại hỏi người dùng thay vì tự quyết.
5. Resolve xong, chạy lại test/lint liên quan trước khi coi là hoàn tất.

```
<<<<<<< HEAD (nhánh đích / main)
const DISCOUNT_RATE = 0.1;
=======
const DISCOUNT_RATE = 0.15; // cập nhật theo yêu cầu kinh doanh mới
>>>>>>> feature/update-discount (nhánh nguồn / PR)
```
→ Giữ `0.15` (nhánh nguồn) vì đó là thay đổi logic mới nhất cần đưa vào PR.

## Checklist

**Commit**: có lệnh rõ ràng từ người dùng · đã gộp đúng phạm vi (push hết hoặc push theo tính năng — không trộn lẫn) · không có file tmp/test/rác lẫn vào · tiêu đề đúng format `<type>: <mô tả>` ≤ 75 ký tự · body nêu rõ vấn đề được giải quyết · đã chạy `validate-commit-message.sh` và nhận `✅`.

**Pull Request**: đã kiểm tra conflict với nhánh đích · nếu có conflict đã đọc cả hai phía trước khi resolve · xử lý đúng ưu tiên (nhánh nguồn) và rà soát để không mất fix quan trọng ở nhánh đích · đã chạy lại test/lint sau khi resolve.
