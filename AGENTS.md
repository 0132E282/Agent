# Hướng dẫn chung cho Claude Code, Codex và Antigravity

Repo cấu hình agent phát triển phần mềm, không phải ứng dụng. Nội dung hướng dẫn viết tiếng Việt; README gốc viết tiếng Anh. Skill thiết kế import giữ ngôn ngữ nguồn.

## Nguồn chung và quy tắc

- Nội dung agent/rule/skill tự viết dùng tiếng Việt; README gốc dùng tiếng Anh, skill import giữ ngôn ngữ nguồn. Đọc file liên quan trước khi sửa, giữ convention hiện có. `.agents/rules/` là nguồn chung; `.claude/rules/` và `.codex/rules/` liên kết tới đó. Khi code, đọc toàn bộ file rule trong `.agents/rules/`, áp dụng phần liên quan đến nhiệm vụ; không tự mở rộng phạm vi.
- TypeScript không dùng `any`, ưu tiên type có sẵn/dẫn xuất và gom theo domain trong `types/`.
- UI/Figma có sẵn là mẫu chuẩn: không tự redesign, đổi theme hoặc tạo design system nếu chưa được yêu cầu. Đọc mẫu thật; không truy cập được thì nêu rõ, không đoán.
- Thao tác database thật mặc định read-only; viết migration không đồng nghĩa được phép chạy. Commit/push/deploy chỉ trong phạm vi được người dùng yêu cầu rõ.
- Sau sửa, chạy check phù hợp có sẵn, tự review diff và đồng bộ tài liệu liên quan. Không bịa kết quả test, benchmark hoặc kết quả tool.

Các file Markdown trong `.codex/rules/` được đọc theo hướng dẫn này, không phải rule thực thi lệnh dạng `.rules`. Liên kết tương đối bên trong được giải quyết từ thư mục nguồn `.agents/rules/`.

## Skill, vai trò và workflow

- `.codex/skills/` là đường dẫn liên kết để quản lý cùng bộ skill; Codex khám phá skill qua `.agents/skills/`. `.agents/skills/` là nguồn skill chung; `.claude/skills/` và `.codex/skills/` cùng liên kết tới đó. Giải quyết liên kết và script theo thư mục nguồn `.agents/skills/<name>/`; `.agents/agents`, `.agents/hook` và `.agents/commands` liên kết tới tài nguyên Claude để giữ các tham chiếu tương đối.
- `.codex/agents/*.toml` định nghĩa custom agent tương ứng `.claude/agents/*.md`, kế thừa model của phiên. Chỉ delegation khi nhiệm vụ/workflow được giao yêu cầu; đọc tài liệu vai trò trước khi thực hiện.
- Workflow gọi bằng `$workflow-analyze`, `$workflow-plan`, `$workflow-implement`, `$workflow-test`, `$workflow-review`, `$workflow-report`, `$workflow-commit`, `$workflow-pr`, `$workflow-cleanup`, `$workflow-audit-workspace`. Chúng chuyển hành vi từ `.claude/commands/lumina/` (Claude gọi bằng slash command namespace `/lumina:...`), không phải slash command Claude trên Codex.
- Bàn giao bằng file trong `docs/` theo vai trò, giữ điểm duyệt của workflow. Không tự chạy toàn pipeline từ phân tích tới commit.
- Hoàn thành task (dù tự làm trực tiếp hay qua subagent) → bắt buộc xuất báo cáo bằng skill `report`, mặc định ngắn gọn, chỉ chi tiết khi được yêu cầu ([`rules/mandatory-report`](./.agents/rules/mandatory-report.md)).

## Execution discipline

Ưu tiên hoàn thành task với effort tương xứng độ lớn/độ mơ hồ/rủi ro — không mặc định chạy đủ chuỗi `requirement-analysis-agent`/`planner-agent`/`reviewer-agent`/`qa-tester-agent` cho mọi thay đổi; chỉ dùng khi độ phức tạp, rủi ro hoặc yêu cầu thật sự cần.

- Đọc rule/tài liệu liên quan, khảo sát đúng phần bị ảnh hưởng; đủ bằng chứng cho một thay đổi nhỏ, đúng phạm vi thì triển khai luôn — không tiếp tục dò thêm phương án hay edge case giả định.
- Dùng pattern/component có sẵn; không tách file, thêm abstraction, hay refactor phần không liên quan chỉ để "cho gọn" hoặc nhất quán hình thức.
- Task rõ ràng, nhỏ → giao thẳng `coding-agent`; chỉ dùng plan/subagent/review độc lập khi độ phức tạp, rủi ro, hoặc khối lượng việc tách biệt thật sự cần.
- Giữ nguyên quyết định người dùng đã chốt và kết quả đã kiểm chứng trừ khi có bằng chứng mới mâu thuẫn; việc nhỏ, đảo ngược được thì tự quyết, không hỏi lại.
- Giới hạn phạm vi tìm kiếm/tool output đúng câu hỏi còn lại — không đọc lại file không đổi, dump nguyên văn log dài, hay poll trạng thái lặp lại không cần thiết.
- Review đúng phần hành vi/contract bị đổi rồi dừng — không mở rộng sang audit/dọn test/lỗi nền không liên quan; lỗi do task gây ra thì sửa, lỗi không liên quan thì báo riêng cho người dùng.

## Hook và format

`.claude/settings.json` và các script hook nhận payload Claude không tự được kích hoạt bởi cấu hình này trên Codex. Các quy tắc tương ứng vẫn phải được thực hiện qua hướng dẫn/workflow; không báo hook đã chạy khi chưa có runtime tích hợp.

Sau sửa file, dùng formatter/linter/test runner đã có trong project với đúng file/phạm vi. Nếu có Prettier local, chạy qua binary local hoặc package script; không tự tải package bằng `npx` khi chưa được giao cài. Repo chưa có formatter thì nêu rõ; không giả lập format. Trước commit kiểm tra diff và dùng script `.claude/skills/git-workflow/scripts/validate-commit-message.sh` theo workflow git.

## Antigravity

- Antigravity khám phá skill và rule trực tiếp trong `.agents/skills/` và `.agents/rules/`; không cần bản sao riêng. Rule có frontmatter `trigger: model_decision`, nhưng khi code vẫn phải đọc các rule theo hướng dẫn chung ở trên. README danh mục có trigger manual.
- Gọi `/coding-frontend`, `/coding-backend`, `/workflow-plan` hoặc `/workflow-implement` khi cần. Dùng công cụ và khả năng delegation thực tế của Antigravity; file TOML trong `.codex/agents/` không phải cấu hình agent Antigravity. Nếu không có custom agent tương ứng, thực hiện vai trò tuần tự từ `.claude/agents/`, giữ ranh giới trách nhiệm.
- Không tự chạy hook Claude trên Antigravity. Format, lint và test theo công cụ project; không giả lập kết quả.

## Chọn skill theo nhiệm vụ

- Setup tool/thư viện/runtime/ứng dụng: giao vai trò `setup-agent`, đọc `.claude/agents/setup-agent.md`; Codex dùng adapter `.codex/agents/setup-agent.toml`. Cài và kiểm chứng đúng phạm vi yêu cầu, không tự upgrade toàn hệ thống.
- Triển khai: luôn giao vai trò `coding-agent` (subagent Claude; adapter `.codex/agents/coding-agent.toml` trên Codex; vai trò tương đương trên Antigravity) — không tự `Edit`/`Write` code trực tiếp ở phiên chính. `coding-agent` áp dụng skill `coding-frontend`/`coding-backend` theo đúng stack, đọc rule tương ứng và tái sử dụng stack/component/contract hiện có.
- UI mới/redesign được yêu cầu: vai trò `ux-ui-designer-agent`; admin ưu tiên usability và mẫu project, website có thể dùng `design-taste-frontend`. Không áp phong cách marketing lên admin hoặc ghi đè Figma.
- SEO kỹ thuật: `seo-website`; nội dung: `seo-content-website`; debug: `debugs`. Chỉ đọc skill phù hợp, không tải toàn bộ thư viện.
- Thiếu công cụ/plugin thì dùng phương án thực tế cùng phạm vi và báo giới hạn, không giả lập kết quả.

## Điều phối giữa agent

- Agent sau đọc **bàn giao** của agent trước qua file trong `docs/` (`requirement-analysis.md`, `system-design.md`, `implementation-plan.json`) — không bắt người dùng diễn giải lại nội dung đã có trong file đó.
- Mỗi agent chỉ làm đúng vai trò được giao, không tự lấn sang vai trò agent khác trong cùng chuỗi: `reviewer-agent` không tự sửa code, `planner-agent` không tự triển khai, `qa-tester-agent` không tự sửa code ứng dụng để test đạt.
- Bàn giao cũ còn hợp lệ (yêu cầu chưa đổi) → tái dùng, không chạy lại agent đã làm xong cho cùng input.
- Giao task cho agent sau kèm đúng file/diff/phạm vi cụ thể cần xử lý — không bắt agent sau tự dò lại toàn repo hoặc toàn bộ hội thoại trước đó để suy ra phạm vi.

## Bảo trì cấu hình

Chỉnh rule/skill tại `.agents/`; giữ adapter theo runtime, không nhân bản nội dung. Kiểm tra README/docs bị ảnh hưởng sau thay đổi. Chạy `python3 scripts/check-agent-config.py` để kiểm tra symlink, skill và agent TOML. Copy nguyên cấu trúc chung khi chuyển project, không copy riêng một adapter.
