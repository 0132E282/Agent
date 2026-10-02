#!/usr/bin/env bash
# PostToolUse hook: tự động format lại file bằng Prettier ngay sau khi
# subagent/Claude Code vừa Edit hoặc Write xong.
#
# Nhận JSON input từ stdin theo schema của Claude Code hook (PostToolUse):
#   { "tool_name": "Edit", "tool_input": { "file_path": "..." }, ... }
#
# Luôn exit 0 — đây là hook phụ trợ (best-effort), không được phép chặn
# (block) hành động của agent nếu format lỗi hoặc thiếu Prettier.
#
# Cố ý KHÔNG dùng `set -e`: bất kỳ lệnh nào trong script lỗi bất ngờ
# (jq thiếu, prettier crash, v.v.) cũng không được làm gián đoạn agent —
# script phải luôn chạy tới dòng `exit 0` cuối cùng. `trap ERR` là lưới an
# toàn cuối, phòng khi có lỗi lọt qua các điểm xử lý ở trên.

set -o pipefail
trap 'exit 0' ERR

input="$(cat)"

file_path="$(echo "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null || true)"

[ -z "$file_path" ] && exit 0
[ -f "$file_path" ] || exit 0

case "$file_path" in
  *.js|*.jsx|*.mjs|*.cjs|*.ts|*.tsx|*.json|*.jsonc|*.css|*.scss|*.less|*.html|*.vue|*.md|*.mdx|*.yaml|*.yml|*.graphql)
    ;;
  *)
    # Loại file Prettier không hỗ trợ -> bỏ qua, không phải lỗi.
    exit 0
    ;;
esac

run_prettier() {
  "$@" --write "$file_path" >/dev/null 2>&1
}

if command -v prettier >/dev/null 2>&1; then
  run_prettier prettier || true
elif npx --no-install prettier --version >/dev/null 2>&1; then
  run_prettier npx --no-install prettier || true
fi
# Không có Prettier trong project/PATH -> bỏ qua êm, không báo lỗi để
# tránh chặn các project không dùng JS/TS.

exit 0
