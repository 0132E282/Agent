---
name: git-workflow
description: Thực thi quy tắc git bắt buộc — commit (rules/commit-discipline.md), format lại bằng Prettier trước khi push, và tạo pull request/resolve conflict (rules/pull-request-conflict.md). Tuyệt đối không tự ý git commit khi chưa có lệnh rõ ràng, không commit vụn vặt, message theo Conventional Commits (tiêu đề "<type>: mô tả" ≤ 75 ký tự); trước khi push format lại diff so với remote; khi tạo PR phải check conflict và biết nhánh nào được ưu tiên giữ. Dùng ngay trước khi chạy git commit, git push, tạo/update PR, hoặc resolve conflict. Đi kèm script validate-commit-message.sh để kiểm tra message tự động.
license: MIT
metadata:
  version: "1.4"
---

# 🔧 Git Workflow

Skill gatekeeper bắt buộc cho **commit** và **pull request** — hành động git có thể thay đổi lịch sử/chia sẻ trạng thái với người khác. Áp dụng dù đang ở phiên chính hay subagent, độc lập với [`coding-agent`](../../agents/coding-agent.md).

## 1. Trước khi `git commit` ([rules/commit-discipline](../../rules/commit-discipline.md))

1. **Có lệnh rõ ràng từ người dùng chưa?** Chưa có → dừng, không commit, bất kể code đã xong hay chưa.
2. **Gộp đúng phạm vi** — một commit cho toàn bộ thay đổi liên quan của task hiện tại, không tách vụn, không gộp thêm thay đổi ngoài phạm vi. Chỉ 2 kiểu phạm vi hợp lệ: "push hết" (toàn bộ thay đổi hiện có, khi người dùng nói rõ) hoặc "push theo tính năng" (chỉ phần liên quan task, mặc định khi không chỉ định) — **cả hai đều tuyệt đối không được kèm file tmp/scratch/debug/test thử nghiệm hoặc file rác**. Chạy `git status` rà lại trước `git add`; thấy file rác do mình tạo trong session thì dọn bằng skill [`cleanup-temp-files`](../cleanup-temp-files/SKILL.md) trước, không add vào commit.
3. **Conventional Commits**: tiêu đề `<type>: <mô tả ngắn gọn>` (`feat`/`fix`/`refactor`/`docs`/`test`/`chore`/`style`/`perf`/`build`/`ci`), tối đa **75 ký tự**; body liệt kê thay đổi chính, nêu rõ vấn đề được giải quyết.
4. **Chạy script kiểm tra** trước khi commit thật:
   ```bash
   echo "feat: thêm hook tự động format code bằng Prettier sau khi edit" \
     | bash .claude/skills/git-workflow/scripts/validate-commit-message.sh -
   ```
   `exit 0` + `✅` nếu hợp lệ; `exit 1` + lỗi cụ thể nếu sai format hoặc vượt 75 ký tự. Script chỉ kiểm tra format máy kiểm được — phần "why" trong body do người soạn tự đảm bảo theo rule.

## 2. Trước khi `git push`

1. **Format lại một lần** các file đã đổi so với remote tracking branch (`git diff --name-only @{upstream}...HEAD`) bằng Prettier, nếu project có cài — tránh đẩy lên code lệch format so với lúc Edit/Write (hook `format-on-edit.sh` format theo từng file sửa, bước này là lượt quét cuối trên toàn bộ diff trước khi push).
2. Prettier format sinh ra thay đổi → đó là thay đổi **chưa commit**; gộp vào đúng commit đang chuẩn bị push (xem mục 1) trước khi push, không để lại format fix trôi sang lần sau.
3. Project chưa cài Prettier (không có trong `PATH` và `npx` không resolve được) → bỏ qua bước này, không tự cài khi chưa được yêu cầu.

Hook [`format-before-push.sh`](../../hook/scripts/format-before-push.sh) tự chạy bước 1 mỗi lần phát hiện lệnh `git push` và cảnh báo (không chặn) nếu format sinh ra thay đổi chưa commit — xem [`hook/README.md`](../../hook/README.md#format-before-push--format-lại-trước-khi-push).

## 3. Trước khi tạo Pull Request / khi gặp conflict ([rules/pull-request-conflict](../../rules/pull-request-conflict.md))

1. Trước khi tạo PR, luôn kiểm tra nhánh có **conflict** với nhánh đích (base, thường `main`) không.
2. Có conflict: **đọc cả hai phía** (`<<<<<<<`/`=======`/`>>>>>>>`) trước khi quyết định — không xóa trắng một bên mà không xem nội dung.
3. **Conflict chỉ do format/vị trí dòng**: giữ code của **nhánh nguồn** (nhánh đang tạo PR).
4. **Conflict do logic thật sự thay đổi ở cả hai bên**: giữ logic của **nhánh nguồn** (thay đổi cần merge vào), nhưng đọc lướt phần bị ghi đè ở nhánh đích — nghi ngờ đó là fix quan trọng không liên quan task của PR thì dừng lại hỏi người dùng thay vì tự quyết.
5. **Không tự ý kéo thêm logic từ nhánh đích vào nhánh nguồn** ngoài phần bắt buộc phải gộp để resolve conflict — kể cả khi thấy nhánh đích có tính năng/fix "có vẻ nên có". Người dùng chỉ giao task trên nhánh nguồn; thấy thiếu gì từ nhánh khác thì báo và hỏi, không tự quyết gộp vào.
6. Resolve xong, chạy lại test/lint liên quan trước khi coi là hoàn tất.

## Checklist

**Commit**: có lệnh rõ ràng từ người dùng · đã gộp đúng phạm vi (push hết hoặc push theo tính năng — không trộn lẫn) · không có file tmp/test/rác lẫn vào · tiêu đề đúng format `<type>: <mô tả>` ≤ 75 ký tự · body nêu rõ vấn đề được giải quyết · đã chạy `validate-commit-message.sh` và nhận `✅`.

**Push**: đã format lại diff so với remote bằng Prettier (nếu project có cài) · không còn thay đổi format nào trôi ra ngoài commit đang push.

**Pull Request**: đã kiểm tra conflict với nhánh đích · nếu có conflict đã đọc cả hai phía trước khi resolve · xử lý đúng ưu tiên (nhánh nguồn) và rà soát để không mất fix quan trọng ở nhánh đích · không tự kéo thêm logic từ nhánh đích ngoài phần bắt buộc để resolve conflict · đã chạy lại test/lint sau khi resolve.
