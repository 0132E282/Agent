---
name: docs
description: Viết hoặc đồng bộ tài liệu dự án (README.md, CLAUDE.md, docs/) — (1) ĐỒNG BỘ khi đã có tài liệu, đối chiếu với trạng thái THỰC TẾ của codebase, phát hiện phần lỗi thời/sai và sửa lại; (2) VIẾT MỚI khi project/module chưa có gì để đối chiếu — quét stack/lệnh/convention thật rồi viết gọn, giống `/init` nhưng tối ưu hơn (không liệt kê dư). Dùng khi nghi ngờ docs không còn khớp code, ngay sau khi đổi cấu trúc lớn (xóa/đổi tên/thêm agent-skill-command), hoặc khi project/module chưa có CLAUDE.md/README cần viết lần đầu. KHÔNG dùng để viết đặc tả kiến trúc hệ thống (HLD/LLD, sơ đồ cấu trúc) — đó là agent system-design-agent.
license: MIT
metadata:
  version: "1.3"
---

# 🔄 Docs

Hai chế độ cho tài liệu dự án (README.md, CLAUDE.md, docs/) — không phải đặc tả kiến trúc hệ thống (xem [`system-design-agent`](../../agents/system-design-agent.md), skill này không đi vào HLD/LLD/sơ đồ). Mọi kết luận "đúng/sai" hoặc nội dung viết mới phải có bằng chứng (đọc file, Glob, Grep), theo [`rules/14`](../../rules/14-search-priority.md) — không bịa lệnh/convention chưa xác minh.

## Chế độ 1 — Đồng bộ (đã có tài liệu)

Phạm vi mặc định: `README.md`, `CLAUDE.md` (nếu có), `docs/**/*.md` (nếu có). Người dùng có thể giới hạn vào một file cụ thể.

1. Trích "claim" kiểm chứng được: đường dẫn, tên agent/skill/command/hook, số lượng/liệt kê, mô tả hành vi cụ thể.
2. Đối chiếu từng claim với thực tế: đường dẫn → `Glob`; tên agent/skill/command → danh sách thật trong `.claude/agents|skills|commands/` (đọc frontmatter, không suy diễn); mô tả hành vi → đọc đúng file nguồn để so khớp.
3. Phân loại: **sai rõ ràng** (file không còn tồn tại, tên đổi, số liệu sai) → sửa ngay theo thực tế vừa đọc; **không chắc** (mơ hồ, không kiểm chứng trực tiếp được) → không tự xóa, đưa vào "cần hỏi thêm" (giống cách [`workspace-auditor-agent`](../../agents/workspace-auditor-agent.md) xử lý phần không chắc).
4. Sửa trực tiếp phần đã xác nhận sai, giữ văn phong/cấu trúc tài liệu — không viết lại toàn bộ file, không tự thêm tính năng/mục mới ngoài việc sửa đúng-sai ([`rules/01`](../../rules/01-simplicity.md)).
5. Báo cáo theo `change-report-template.md` của skill [`report`](../report/SKILL.md): mỗi chỗ sửa ghi *trước → sau* + bằng chứng, cộng danh sách "cần hỏi thêm" nếu có.

## Chế độ 2 — Viết mới (chưa có gì để đối chiếu)

Dùng khi project/module/feature chưa có CLAUDE.md/README, cần viết lần đầu — tương tự lệnh `/init` có sẵn nhưng **gọn và tối ưu hơn**: chỉ ghi điều thực sự cần để làm việc hiệu quả trong repo, không liệt kê toàn bộ cấu trúc file hay lặp lại thông tin Glob/Grep tự tra được.

1. Xác định stack/ngôn ngữ chính từ file manifest thật (`package.json`, `composer.json`, `pyproject.toml`, `go.mod`...) — không đoán theo tên thư mục.
2. Đọc lệnh dev/build/test/lint **thật đang dùng** (scripts trong manifest, `Makefile`, CI config) — chỉ ghi lệnh đã xác minh tồn tại, không bịa lệnh "thường gặp" của stack đó.
3. Đọc vài file mẫu đại diện (không phải toàn bộ codebase) để rút convention thật đang áp dụng — quy ước đặt tên, cấu trúc module lặp lại, test pattern — không áp khung convention chung của stack khi code thật làm khác.
4. Viết theo cấu trúc gọn, mỗi mục một đoạn ngắn, bỏ mục không áp dụng kèm lý do thay vì để trống:
   - **Mục đích dự án** (1–2 câu).
   - **Cấu trúc thư mục chính** — chỉ cấp cao mang ý nghĩa điều hướng, không liệt kê từng file.
   - **Lệnh thường dùng** (dev/build/test/lint) — chỉ lệnh đã xác minh chạy được.
   - **Convention quan trọng cần biết trước khi sửa code** — quy ước/rule bắt buộc nếu có, pattern lặp lại thật đang dùng.
5. Không đi vào kiến trúc hệ thống (HLD/LLD, luồng nghiệp vụ, sơ đồ Mermaid) — phần đó thuộc agent [`system-design-agent`](../../agents/system-design-agent.md); trỏ người dùng sang đó nếu nhu cầu thực chất là thiết kế hệ thống, không phải định hướng codebase.

## Khi áp dụng

- **Đồng bộ**: ngay sau khi xóa/đổi tên/thêm agent-skill-command, đổi cấu trúc thư mục lớn, hoặc khi nghi ngờ docs lỗi thời.
- **Viết mới**: project/module/feature chưa có CLAUDE.md/README, cần viết lần đầu một cách gọn gàng.
- Không dùng cho đặc tả kiến trúc hệ thống (HLD/LLD/sơ đồ) ở cả hai chế độ — đó là agent `system-design-agent`.
