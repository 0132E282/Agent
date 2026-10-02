# 🪝 Hooks

Hook phụ trợ cho các subagent trong [`agents/`](../agents) — tự động hóa các bước nên làm nhưng dễ bị bỏ quên.

## format-on-edit — tự động format bằng Prettier

Sau mỗi lần Claude Code (hoặc subagent) **Edit/Write** một file, hook này tự động chạy `prettier --write` trên đúng file vừa sửa — tương ứng quy tắc [`rules/08-quality-assurance.md`](../rules/08-quality-assurance.md) (format thống nhất, không tranh cãi khoảng trắng trong review).

- **Script**: [`scripts/format-on-edit.sh`](./scripts/format-on-edit.sh)
- **Loại hook**: `PostToolUse`, matcher `Edit|Write`
- **Phạm vi file**: các định dạng Prettier hỗ trợ (`.js .jsx .ts .tsx .json .css .scss .less .html .vue .md .yaml .yml ...`). File không thuộc danh sách này bị bỏ qua, không lỗi.
- **An toàn**: luôn `exit 0` — nếu project không có Prettier (không có trong `PATH` và `npx` không resolve được), hook bỏ qua êm thay vì chặn agent.
- **Phụ thuộc**: cần có `jq` trong `PATH` để parse JSON input của hook (`brew install jq` / `apt install jq`).

### Cài đặt vào project khác

1. Copy thư mục này vào `.claude/hook/` của project đích:
   ```bash
   cp -r .claude/hook /path/to/project/.claude/hook
   ```
2. Merge nội dung [`settings.snippet.json`](./settings.snippet.json) vào `.claude/settings.json` của project đích (key `hooks`). Nếu project đã có `hooks` khác, gộp mảng thay vì ghi đè.
3. Đảm bảo project có Prettier (local `devDependencies` hoặc global) — nếu không có, hook sẽ không làm gì (không báo lỗi).

### Dùng formatter khác (Black, gofmt, dotnet format, PHP-CS-Fixer...)

`format-on-edit.sh` hiện chỉ xử lý các file Prettier hỗ trợ. Với project đa ngôn ngữ, thêm nhánh `case` tương ứng trong script, theo mẫu `automator.py` của `tester-agent` (tự phát hiện loại project rồi gọi đúng formatter).

## audit-log — ghi audit trail cho mọi tool call

Trước mỗi lần Claude Code (hoặc subagent) gọi **bất kỳ tool nào** (Edit, Write, Bash, Grep...), hook này ghi một dòng JSON vào log — phục vụ truy vết "ai/khi nào/làm gì", liên hệ [`rules/07-data-safety.md`](../rules/07-data-safety.md).

- **Script**: [`scripts/audit-log.sh`](./scripts/audit-log.sh)
- **Loại hook**: `PreToolUse`, matcher `.*` (mọi tool)
- **File log**: `.claude/logs/logs.jsonl` (JSON Lines, append-only) — cả thư mục `.claude/logs/` đã nằm trong `.gitignore`, không commit nhầm.
- **Nội dung mỗi dòng**: `ts` (UTC ISO8601), `session_id`, `tool`, `cwd`, `input` (tóm tắt — chỉ `file_path`/`command` (≤200 ký tự)/`pattern` tùy loại tool, **không** ghi nguyên nội dung file Write/Edit để tránh log phình to và rò rỉ dữ liệu nhạy cảm).
- **An toàn**: luôn `exit 0`; input JSON hỏng, thiếu `jq`, hoặc `tool_name` rỗng đều bị bỏ qua êm, không ghi dòng rác.
- **Phụ thuộc**: cần `jq`.

### Xem log

```bash
tail -f .claude/logs/logs.jsonl | jq .
```

## commit-msg-guard — chặn commit message sai format

Trước mỗi lần chạy `git commit` (qua tool Bash), hook này trích message sắp dùng và validate bằng chính script `validate-commit-message.sh` của skill `git-workflow`, chặn (deny) nếu sai Conventional Commits — enforce [`rules/10-commit-discipline.md`](../rules/10-commit-discipline.md) tự động, không phụ thuộc Claude tự giác.

- **Script**: [`scripts/commit-msg-guard.sh`](./scripts/commit-msg-guard.sh)
- **Loại hook**: `PreToolUse`, matcher `Bash`
- **Cách trích message**: ưu tiên heredoc (`git commit -m "$(cat <<'EOF' ... EOF)"` — cách Claude Code luôn dùng), fallback sang `-m "..."` đơn giản.
- **An toàn**: best-effort — không trích được message (commit mở editor, dùng `-F`, thiếu `jq`/validator) thì không chặn, để git tự xử lý.
- **Phụ thuộc**: cần `jq` và `skills/git-workflow/scripts/validate-commit-message.sh`.

## secret-scan — chặn hỏi xác nhận khi nghi ngờ lộ secret

Trước mỗi lần `git add`/`git commit`, hook này quét path sắp add hoặc diff đã staged để tìm pattern giống secret (private key, AWS key, `api_key=...`, file `.env`) — liên hệ [`rules/07-data-safety.md`](../rules/07-data-safety.md).

- **Script**: [`scripts/secret-scan.sh`](./scripts/secret-scan.sh)
- **Loại hook**: `PreToolUse`, matcher `Bash`
- **Hành vi khi phát hiện**: `permissionDecision: "ask"` (không `"deny"`) — heuristic regex có thể false positive, nên hỏi lại người dùng thay vì chặn cứng.
- **Phụ thuộc**: cần `jq`.

## protected-branch-guard — cảnh báo trước khi push rủi ro cao

Trước mỗi lần `git push`, hook này cảnh báo (ask) nếu push thẳng vào `main`/`master`, dùng `--force`/`--force-with-lease`, hoặc `--no-verify`/`--no-gpg-sign` — lớp phòng vệ thứ hai cho Git Safety Protocol.

- **Script**: [`scripts/protected-branch-guard.sh`](./scripts/protected-branch-guard.sh)
- **Loại hook**: `PreToolUse`, matcher `Bash`
- **Hành vi khi phát hiện**: `permissionDecision: "ask"` — có tình huống hợp lệ cần push thẳng main/force push mà người dùng đã đồng ý, nên hỏi lại chứ không chặn cứng.
- **Phụ thuộc**: cần `jq`, `git`.

## lint-on-edit — static analysis sau khi Edit/Write

Sau mỗi lần Edit/Write, hook này chạy linter/type-checker tương ứng loại file (`tsc` cho `.ts/.tsx`, `eslint` cho `.js/.jsx`, `ruff`/`flake8` cho `.py`, `phpstan` cho `.php`) và trả lỗi lại cho Claude qua `additionalContext` — liên hệ [`rules/08-quality-assurance.md`](../rules/08-quality-assurance.md). Thuần cố vấn, không block vì tool đã chạy xong.

- **Script**: [`scripts/lint-on-edit.sh`](./scripts/lint-on-edit.sh)
- **Loại hook**: `PostToolUse`, matcher `Edit|Write`
- **An toàn**: không có linter tương ứng, hoặc file không thuộc loại hỗ trợ → bỏ qua êm.
- **Phụ thuộc**: cần `jq`; linter tương ứng ngôn ngữ (tuỳ chọn, thiếu thì bỏ qua).

## test-reminder — tự chạy test tương ứng sau khi sửa file nguồn

Sau mỗi lần Edit/Write một file nguồn, hook này tìm file test tương ứng theo convention đặt tên phổ biến (`foo.test.ts`, `foo.spec.ts`, `test_foo.py`, `foo_test.py`...) và tự chạy, báo kết quả qua `additionalContext` — liên hệ [`rules/08-quality-assurance.md`](../rules/08-quality-assurance.md) (regression test ngay sau khi sửa).

- **Script**: [`scripts/test-reminder.sh`](./scripts/test-reminder.sh)
- **Loại hook**: `PostToolUse`, matcher `Edit|Write`
- **Phạm vi**: chỉ JS/TS (`jest`/`vitest`) và Python (`pytest`) — hai stack phổ biến nhất, không cố cover mọi ngôn ngữ (xem [`rules/01-simplicity.md`](../rules/01-simplicity.md)).
- **An toàn**: không tìm thấy test tương ứng, hoặc thiếu test runner → bỏ qua êm.

## remind-cleanup — nhắc dọn file tạm cuối session

Khi Claude Code kết thúc một turn, hook này tìm file đã `Write` trong session hiện tại (qua `.claude/logs/logs.jsonl`), giới hạn trong phạm vi dự án (so khớp `cwd`), còn tồn trên đĩa và khớp pattern tên file tạm (`tmp`/`scratch`/`debug`/`draft`/`sandbox`/`test-output`/`.bak`/`.orig`) — nếu có, nhắc qua `additionalContext` để Claude thấy và tự quyết có chạy `/cleanup` không. Liên hệ skill [`cleanup-temp-files`](../skills/cleanup-temp-files/SKILL.md).

- **Script**: [`scripts/remind-cleanup.sh`](./scripts/remind-cleanup.sh) — gọi `skills/cleanup-temp-files/scripts/find-session-scratch-files.sh`
- **Loại hook**: `Stop`
- **Chỉ nhắc, không tự xóa**: dùng `hookSpecificOutput.additionalContext`, không dùng `decision`/`reason` (sẽ chặn Claude dừng lại).
- **An toàn**: luôn `exit 0`; không có ứng viên, thiếu `jq`, hoặc thiếu script tìm file thì im lặng, không báo gì.
- **Phụ thuộc**: cần `jq`; dựa vào log của hook `audit-log` nên phải bật hook đó cùng lúc.

## notify-done — phát âm thanh khi làm xong task

Khi Claude Code kết thúc một turn (trả lời xong, không còn việc gì đang chạy), hook này phát một âm thanh thông báo ngắn để biết task đã xong mà không cần nhìn màn hình liên tục.

- **Script**: [`scripts/notify-done.sh`](./scripts/notify-done.sh)
- **Loại hook**: `Stop` (không cần `matcher` — hook này không gắn với tool cụ thể)
- **Âm thanh theo hệ điều hành**: `afplay` (macOS, dùng `Glass.aiff`) → `paplay`/`aplay` (Linux) → `powershell.exe [console]::beep` (Windows/WSL). Không có công cụ nào khả dụng thì bỏ qua êm.
- **An toàn**: luôn `exit 0`, chạy ngầm (`&`) nên không làm chậm việc Claude Code dừng lại.

## condense-planner-input — lưới an toàn chặn prompt quá dài khi gọi planner

Trước mỗi lần gọi Agent tool với `subagent_type: planner`, hook này kiểm tra độ dài `prompt` — nếu vượt ngưỡng rất lớn (ví dụ dán nhầm nguyên văn cả tài liệu `system-design` dài), tự cắt gọn (giữ phần đầu + phần cuối, cắt phần giữa) trước khi `planner` nhận. **Đây chỉ là lưới an toàn cuối, không phải cơ chế rút gọn context chính** — bash không hiểu ngữ nghĩa nên không biết phần nào thật sự cần giữ; việc chọn lọc đúng phần liên quan là trách nhiệm của bước gọi `planner` (xem [`commands/plan.md`](../commands/plan.md)).

- **Script**: [`scripts/condense-planner-input.sh`](./scripts/condense-planner-input.sh)
- **Loại hook**: `PreToolUse`, matcher `Agent`
- **Cơ chế**: dùng `hookSpecificOutput.updatedInput` để thay `tool_input.prompt` trước khi tool chạy — giữ nguyên các field khác (`subagent_type`, `description`...).
- **Ngưỡng**: cắt khi `prompt` > 20000 ký tự, giữ 13000 ký tự đầu + 6000 ký tự cuối, chèn dòng đánh dấu phần đã cắt.
- **An toàn**: `prompt` dưới ngưỡng, không phải tool `Agent`, không phải `subagent_type: planner`, hoặc thiếu `jq` → không sửa gì.
- **Phụ thuộc**: cần `jq`.

## Đã bật sẵn trong chính repo này

`hook/` nằm trong `.claude/hook/` của repo này, và `.claude/settings.json` đã trỏ cả 9 hook (`audit-log`, `commit-msg-guard`, `secret-scan`, `protected-branch-guard`, `format-on-edit`, `lint-on-edit`, `test-reminder`, `remind-cleanup`, `notify-done`) tới đúng path `.claude/hook/scripts/...` — không cần cài thêm gì để dùng ngay trong repo này. [`settings.snippet.json`](./settings.snippet.json) có nội dung tương đương, dùng khi copy sang project khác theo hướng dẫn ở trên.
