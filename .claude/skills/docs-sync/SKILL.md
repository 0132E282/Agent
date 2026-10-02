---
name: docs-sync
description: Rà soát tài liệu dự án (README.md, CLAUDE.md, docs/) đối chiếu với trạng thái THỰC TẾ của codebase — phát hiện phần đã lỗi thời/sai (nhắc tới file/module/skill/agent đã xóa hoặc đổi tên, mô tả không còn khớp hành vi hiện tại), xóa phần sai và cập nhật lại đúng. Dùng khi nghi ngờ docs không còn khớp code, ngay sau khi đổi cấu trúc lớn (xóa/đổi tên/thêm agent-skill-command), hoặc định kỳ kiểm tra tính nhất quán giữa docs và code. KHÔNG dùng để viết docs mới từ đầu khi chưa có gì để đối chiếu.
license: MIT
metadata:
  version: "1.0"
---

# 🔄 Docs Sync

Skill đối chiếu tài liệu với **thực tế codebase hiện tại** — không đối chiếu với trí nhớ hay giả định. Mọi kết luận "đúng/sai" phải có bằng chứng (đọc file, Glob, Grep), theo [`rules/14-search-priority.md`](../../rules/14-search-priority.md) — không tự bịa thông tin mới khi sửa.

## Phạm vi

Mặc định rà: `README.md` (gốc), `CLAUDE.md` (nếu có), toàn bộ `docs/**/*.md` (nếu có thư mục này). Người dùng có thể chỉ định phạm vi hẹp hơn (một file cụ thể).

## Quy trình

1. **Trích "claim" kiểm chứng được** từ tài liệu đang rà: đường dẫn file/thư mục được nhắc tới, tên agent/skill/command/hook được nhắc tới, số lượng/liệt kê (ví dụ "4 skill chính", "13 rule"), mô tả hành vi/tính năng cụ thể.
2. **Đối chiếu từng claim với thực tế**:
   - Đường dẫn → `Glob`/kiểm tra tồn tại thật.
   - Tên agent/skill/command → so với danh sách thật trong `.claude/agents/`, `.claude/skills/`, `.claude/commands/` (đọc frontmatter `name`/`description`, không suy diễn).
   - Mô tả hành vi → đọc đúng file nguồn (`SKILL.md`, agent `.md`) để so khớp, không dựa vào tên suy đoán.
3. **Phân loại mỗi claim**:
   - **Sai rõ ràng** (file/module không còn tồn tại, tên đã đổi, số liệu sai) → sửa/xóa ngay, viết lại đúng theo thực tế vừa đọc được.
   - **Không chắc** (mô tả mơ hồ, không có cách kiểm chứng trực tiếp, hoặc có thể đúng theo ý định dù không khớp 100% literal) → **không tự xóa**, liệt kê vào phần "cần hỏi thêm" của báo cáo cuối, giống cách [`workspace-auditor`](../../agents/workspace-auditor.md) xử lý phần không chắc.
4. **Sửa trực tiếp** các phần đã xác nhận sai — giữ nguyên văn phong/cấu trúc tài liệu, không viết lại toàn bộ file chỉ vì sửa một phần, không tự thêm tính năng/mục mới ngoài việc sửa đúng-sai (xem [`rules/01-simplicity.md`](../../rules/01-simplicity.md)).
5. **Báo cáo** theo khung `change-report-template.md` của skill [`report`](../report/SKILL.md): mỗi chỗ đã sửa ghi rõ *trước → sau* + lý do (bằng chứng đã kiểm chứng), cộng danh sách "cần hỏi thêm" nếu có.

## Nguyên tắc bắt buộc

- Không tự xóa toàn bộ file tài liệu — chỉ sửa/xóa đúng phần nội dung đã xác nhận sai.
- Không tự thêm thông tin/tính năng mới vào docs khi chỉ được yêu cầu đồng bộ lại — việc đó là viết docs mới, ngoài phạm vi skill này.
- Không chắc chắn → không xóa, đưa vào "cần hỏi thêm" (theo [`rules/06-fail-fast-validation.md`](../../rules/06-fail-fast-validation.md): dừng lại khi thiếu bằng chứng, không đoán).
- Mỗi lần sửa phải trích được bằng chứng cụ thể (đường dẫn đã kiểm tra, nội dung file đã đọc) — không ghi "có vẻ sai" mà không có căn cứ.

## Khi áp dụng

- Ngay sau khi xóa/đổi tên/thêm agent, skill, command, hoặc thay đổi cấu trúc thư mục lớn — kiểm tra docs có còn khớp không.
- Khi người dùng nghi ngờ hoặc hỏi thẳng "docs có còn đúng không", "README có lỗi thời không".
- **Không** dùng để viết `README.md`/`CLAUDE.md` mới từ đầu khi dự án chưa có tài liệu nào để đối chiếu — đó là việc viết docs mới, không phải đồng bộ.
