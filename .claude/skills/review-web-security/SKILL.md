---
name: review-web-security
description: Review bảo mật website, backend, frontend, API, database và cấu hình triển khai. Dùng khi người dùng yêu cầu security review, audit code, tìm lỗ hổng, kiểm tra xác thực/phân quyền, upload, thanh toán, hoặc sửa lỗi bảo mật. Đưa ra bằng chứng trong code, điều kiện khai thác, mức độ ảnh hưởng, bản sửa và kiểm thử hồi quy; hỗ trợ mọi stack, gồm Laravel và React. KHÔNG tự ý chạy kiểm thử phá hoại/quét ngoài phạm vi cho phép, không tự thực thi migration hay đổi kiến trúc ngoài yêu cầu.
license: MIT
metadata:
  version: "1.0"
---

# Review Web Security

## Mục tiêu

Phát hiện lỗ hổng thực tế, ưu tiên theo rủi ro và đưa ra cách sửa có thể kiểm chứng. Dùng checklist như bản đồ kiểm tra, không coi mọi mục là một lỗi đã tồn tại. Không tuyên bố ứng dụng an toàn tuyệt đối hoặc checklist bao phủ mọi lỗ hổng.

## Nguyên tắc làm việc

- Đọc hướng dẫn dự án và xác định phạm vi người dùng yêu cầu trước khi làm việc.
- Review code và cấu hình được cung cấp; chỉ thử nghiệm trên môi trường thuộc phạm vi được cho phép. Dùng dữ liệu giả và tài khoản thử nghiệm; không chạy kiểm thử phá hoại hoặc gây tải lên production.
- Nếu chỉ được yêu cầu review, báo cáo và đề xuất patch. Nếu được yêu cầu sửa, thực hiện thay đổi nhỏ nhất xử lý nguyên nhân gốc và chạy kiểm thử phù hợp ([`rules/01-simplicity.md`](../../rules/01-simplicity.md)).
- Không in giá trị secret, token, mật khẩu hoặc dữ liệu cá nhân. Che giá trị nhạy cảm trong bằng chứng; nếu secret bị lộ, đề xuất thu hồi/xoay vòng, không chỉ xóa khỏi code.
- Phân biệt lỗ hổng đã xác nhận, nghi vấn cần xác minh và đề xuất tăng cường. Thiếu một header không tự động là lỗi nghiêm trọng.
- Không suy luận rằng UUID, URL khó đoán, frontend validation, CORS, ORM hoặc framework tự động bảo vệ toàn bộ ứng dụng.
- Không chạy công cụ quét hoặc cài dependency mới khi không cần thiết. Không sửa toàn bộ kiến trúc để xử lý một lỗi cục bộ.
- Xác minh khuyến nghị phụ thuộc phiên bản bằng tài liệu chính thức ([`rules/14-search-priority.md`](../../rules/14-search-priority.md)). Không bịa CVE, CWE, CVSS, phiên bản hoặc kết quả scanner.

## Quy trình

### 1. Lập bản đồ ứng dụng

Xác định stack và phiên bản từ manifest/lockfile; đọc route, middleware, controller, service, policy, serializer, component frontend, schema và cấu hình triển khai liên quan.

Ghi lại:
- Điểm vào: HTTP, GraphQL, WebSocket, webhook, upload, import, queue, scheduled job.
- Danh tính: guest, user, admin, service account; tenant, role và quyền.
- Dữ liệu quan trọng: tài khoản, hồ sơ cá nhân, tài liệu riêng tư, thanh toán, secret.
- Ranh giới tin cậy: browser → API → database/storage/queue → dịch vụ bên ngoài.
- Luồng nhạy cảm: login, reset password, đổi email, CRUD, bulk action, export, thanh toán.

### 2. Truy vết và xác minh

Với từng luồng áp dụng:
1. Theo dõi input từ nguồn vào đến nơi truy vấn, ghi dữ liệu, render, thực thi hoặc gửi ra ngoài.
2. Kiểm tra xác thực, quyền chức năng, quyền đối tượng, quyền field, tenant và trạng thái nghiệp vụ.
3. Đọc helper/middleware/policy thực sự được gọi trước khi kết luận thiếu bảo vệ.
4. Kiểm tra đường đi phụ: bulk, export, download, restore, preview, API cũ, queue và webhook.
5. Thu thập vị trí code, điều kiện tiền đề và đường đi khả thi. Xác minh bằng kiểm thử nhỏ trên môi trường an toàn nếu có.
6. Nếu không thể kiểm chứng, ghi rõ dữ kiện còn thiếu và cách xác minh; không nâng nghi vấn thành lỗi chắc chắn.

### 3. Phân loại và ưu tiên

Đánh giá mức độ từ khả năng tiếp cận, đặc quyền cần có, tương tác nạn nhân, dữ liệu bị ảnh hưởng, phạm vi tenant và tác động thực tế.

- Critical: tác động rất lớn với đường khai thác khả thi, như chiếm quyền hệ thống hoặc truy cập hàng loạt dữ liệu quan trọng.
- High: chiếm tài khoản, vượt quyền đáng kể, truy cập dữ liệu nhạy cảm hoặc thao túng tài chính trong điều kiện thực tế.
- Medium: ảnh hưởng giới hạn hoặc cần điều kiện bổ sung đáng kể.
- Low: ảnh hưởng nhỏ; ghi riêng các đề xuất tăng cường chưa chứng minh khả năng khai thác.

Không gán severity chỉ dựa trên tên lỗi. Chỉ đưa CVSS khi có đủ dữ kiện và giải thích vector.

### 4. Sửa và kiểm thử

- Sửa tại ranh giới tin cậy và điểm thực thi; xử lý mọi đường đi cùng nguyên nhân.
- Dùng cơ chế chuẩn của framework, thư viện duy trì tốt và cấu hình phù hợp phiên bản.
- Thêm kiểm thử hồi quy có ý nghĩa: thao tác hợp lệ vẫn thành công, thao tác vượt quyền/độc hại bị từ chối và không gây side effect ([`rules/08-quality-assurance.md`](../../rules/08-quality-assurance.md)).
- Kiểm tra user khác, tenant khác, guest, role thấp, field cấm và endpoint phụ khi liên quan.
- Với race condition và replay, kiểm tra tính nguyên tử, idempotency và request đồng thời khi môi trường cho phép.
- Báo rõ kiểm thử đã chạy, kết quả, phần chưa chạy và rủi ro còn lại.

## Checklist bảo mật

Đánh dấu mỗi mục theo trạng thái: `Đạt`, `Lỗi xác nhận`, `Cần xác minh`, `Không áp dụng`. Với `Đạt` hoặc `Lỗi xác nhận`, dẫn bằng chứng; với `Không áp dụng`, nêu lý do ngắn. Gom những mục cùng nguyên nhân thành một finding.

### A. Xác thực và tài khoản

- Mật khẩu plaintext, hash nhanh/không phù hợp, credential mặc định hoặc yếu.
- Brute force, credential stuffing; thiếu giới hạn lượt thử và phát hiện lạm dụng.
- User enumeration qua response, thời gian hoặc luồng reset/đăng ký.
- Reset token dễ đoán, không hết hạn, dùng lại được hoặc không gắn đúng tài khoản.
- Đổi mật khẩu/email và liên kết tài khoản thiếu xác minh phù hợp.
- OTP/MFA thiếu giới hạn, hết hạn, dùng một lần; bypass qua endpoint phụ/recovery.
- OAuth/OIDC kiểm tra sai redirect URI, state, nonce, PKCE, issuer hoặc audience.
- JWT không kiểm tra đúng chữ ký, thuật toán cho phép, issuer, audience, thời hạn.
- Session/token còn hiệu lực trái chính sách sau logout, khóa tài khoản, đổi quyền hoặc đổi mật khẩu.
- API key dùng chung, quyền rộng, lộ hoặc thiếu thu hồi/xoay vòng.

### B. Session, cookie và CSRF

- Session fixation; không regenerate session sau xác thực hoặc nâng quyền.
- Thiếu idle/absolute timeout phù hợp; logout không vô hiệu hóa session server.
- Cookie thiếu Secure/HttpOnly/SameSite phù hợp; domain/path quá rộng.
- Token/session xuất hiện trong URL, log, referrer hoặc analytics.
- CSRF trên thao tác dùng credential tự động gửi như cookie; GET có side effect.
- WebSocket dùng cookie nhưng thiếu kiểm tra origin phù hợp.
- Cơ chế chống CSRF có nhưng endpoint liên quan được miễn sai hoặc có đường bypass.

### C. Phân quyền và cách ly dữ liệu

- IDOR/BOLA: truy cập đối tượng của người khác qua ID hoặc quan hệ.
- BFLA: role thấp gọi chức năng quản trị; chỉ kiểm tra quyền ở UI.
- Thiếu quyền đọc/sửa field; mass assignment role, owner, tenant, giá hoặc trạng thái.
- Tin user_id/tenant_id/role từ client thay vì danh tính và ngữ cảnh được xác minh.
- Thiếu tenant scope ở query, cache, storage, search, export hoặc job.
- Bulk action chỉ kiểm tra một phần bản ghi; export/download/restore/preview bỏ qua quyền.
- Model/module/relation/action động không có allowlist và policy tương ứng.
- Quyền cũ còn trong cache; default allow khi policy thiếu hoặc kiểm tra lỗi.
- Tài liệu riêng tư có URL công khai; signed URL không ràng buộc phạm vi/thời hạn phù hợp.

### D. Injection và xử lý input backend

- SQL/NoSQL injection; ghép raw query hoặc cho phép operator/query tùy ý.
- OS command/code/expression injection; eval, shell hoặc script động từ input.
- Server-side template injection; input trở thành template thực thi.
- LDAP/XPath/XML injection; XXE qua parser cho phép external entity.
- Unsafe deserialization hoặc prototype pollution khi input tác động object/config nhạy cảm.
- CRLF/HTTP header/email header injection; log injection.
- CSV/formula injection khi export dữ liệu không đáng tin.
- Dynamic sort/filter/table/column/relation không giới hạn; nhầm giá trị với identifier.
- Validation thiếu kiểu, chiều dài, miền giá trị, cấu trúc lồng nhau hoặc canonicalization cần thiết.

### E. Frontend và trình duyệt

- Stored/reflected/DOM XSS; encode không đúng ngữ cảnh HTML, attribute, URL hoặc JavaScript.
- innerHTML, dangerouslySetInnerHTML, v-html, document.write nhận dữ liệu chưa xử lý an toàn.
- Rich text/Markdown/SVG dùng sanitizer không phù hợp hoặc có cấu hình bypass.
- HTML injection, URL scheme nguy hiểm, DOM clobbering; eval/new Function từ input.
- postMessage không kiểm tra chính xác origin, source và schema dữ liệu.
- Clickjacking trên thao tác nhạy cảm; open redirect hỗ trợ lừa đảo.
- Secret/private key nhúng trong bundle hoặc biến môi trường frontend.
- Token/storage có mô hình bảo vệ không phù hợp; XSS có thể đọc dữ liệu hoặc gọi API thay user.
- Dữ liệu nhạy cảm vào analytics, URL, source map công khai hoặc error report.
- Browser/service worker cache giữ dữ liệu giữa user hoặc sau logout.
- Script bên thứ ba thiếu kiểm soát nguồn/toàn vẹn phù hợp; CSP quá rộng.
- Tin dữ liệu API là an toàn để render; tin hidden field hoặc frontend validation.

### F. HTTP, API và tích hợp

- CORS phản chiếu origin hoặc cho origin không đáng tin đọc response có credential.
- SSRF qua fetch URL, import ảnh, PDF renderer; bỏ qua redirect, DNS hoặc truy cập nội bộ.
- WebSocket/channel/message thiếu xác thực, quyền hoặc giới hạn tài nguyên.
- HTTP parameter pollution, parser differential, request smuggling giữa proxy và backend.
- Host-header poisoning; tin X-Forwarded-* từ nguồn không được cấu hình tin cậy.
- Webhook thiếu xác minh chữ ký, timestamp, chống replay hoặc đối chiếu sự kiện.
- API bên thứ ba thiếu schema validation, timeout, giới hạn kích thước hoặc xử lý lỗi an toàn.
- Endpoint cũ/debug/internal bị lộ; inventory API không đầy đủ.
- GraphQL resolver thiếu quyền; query depth/complexity/batching không giới hạn phù hợp.
- Serializer trả field thừa hoặc dữ liệu nhạy cảm ngoài nhu cầu.

### G. File và nội dung upload

- Chỉ tin extension/MIME client; file executable hoặc HTML/SVG chủ động được phục vụ cùng origin.
- File upload có thể được thực thi; thiếu cách ly storage phù hợp.
- Path traversal, arbitrary file read/write/overwrite qua đường dẫn hoặc tên file.
- Zip Slip, archive symlink hoặc decompression bomb.
- Upload/giải nén/chuyển đổi thiếu giới hạn dung lượng, số file, thời gian và tài nguyên.
- Parser ảnh/PDF/Office/video có lỗ hổng; công cụ chuyển đổi nhận input nguy hiểm.
- File tạm, file riêng tư, thumbnail hoặc kết quả chuyển đổi thiếu kiểm soát quyền.

### H. Nghiệp vụ và thanh toán

- Tin giá, thuế, tổng tiền, giảm giá, số dư hoặc payment status do frontend gửi.
- Không đối chiếu giao dịch với order, amount, currency, merchant và trạng thái từ nguồn tin cậy.
- Số âm, overflow, rounding/currency sai hoặc số lượng vượt miền hợp lệ.
- Bypass bước quy trình; sửa đối tượng đã khóa; thiếu kiểm tra chuyển trạng thái.
- Race condition, double spending, TOCTOU; thiếu transaction/locking/constraint phù hợp ([`rules/07-data-safety.md`](../../rules/07-data-safety.md)).
- Thiếu idempotency hoặc chống replay cho thanh toán, webhook, refund và retry.
- Refund vượt giá trị, nhiều lần; coupon/referral/multi-account abuse.
- Exception/timeout làm hệ thống fail-open hoặc ghi dữ liệu một phần.

### I. Database, dữ liệu và mật mã

- Database/cache/search public; tài khoản ứng dụng quá quyền.
- Backup/dump/snapshot lộ; dữ liệu production đưa sang test không che phù hợp.
- Mật khẩu, OTP, session, token, PII trong log hoặc telemetry.
- Thuật toán tự thiết kế, primitive lỗi thời hoặc sử dụng thư viện sai.
- Random token yếu; nonce/IV dùng lại sai yêu cầu; ciphertext thiếu bảo vệ toàn vẹn.
- Khóa lộ, quyền rộng, lưu không phù hợp hoặc thiếu lifecycle management.
- Thiếu bảo vệ dữ liệu nhạy cảm khi truyền/lưu theo threat model.
- Retention/xóa dữ liệu không nhất quán giữa database, file, cache và bản sao theo chính sách.

### J. Cache, tài nguyên và availability

- Cache key thiếu user/tenant/quyền; private response bị cache dùng chung.
- Cache poisoning/deception; cache giữ quyền hoặc dữ liệu đã thu hồi.
- Login/OTP/search/export/SMS/email/AI thiếu rate limit, quota và chống abuse phù hợp.
- Pagination, GraphQL, filter, regex hoặc request body tạo tải không giới hạn.
- ReDoS, query nặng, upload lớn, queue flooding hoặc decompression gây cạn tài nguyên.
- Thiếu timeout, concurrency limit, backpressure; retry storm.
- Rate limit chỉ dựa IP dễ bypass hoặc khóa nhầm; không kiểm tra giới hạn theo danh tính/nghiệp vụ.

### K. Hạ tầng và cấu hình

- Debug/profiler bật production; .env, .git, backup, directory listing bị phục vụ công khai.
- HTTP/TLS cấu hình không phù hợp; backend tắt certificate verification.
- Bucket/storage/port quản trị/database/dashboard public trái nhu cầu.
- Container/process chạy quyền cao; service account và filesystem quyền quá rộng.
- Dev/staging dùng secret hoặc tài nguyên production trái phạm vi.
- Dangling DNS/subdomain takeover; origin bị truy cập trực tiếp bỏ qua kiểm soát cần thiết.
- Secret commit vào code/history; thiếu thu hồi secret đã lộ.
- Runtime/framework/OS không được cập nhật bản vá phù hợp.

### L. Supply chain, CI/CD và giám sát

- Dependency trực tiếp/gián tiếp có lỗ hổng khả dụng trong ngữ cảnh ứng dụng.
- Typosquatting, dependency confusion, package/build script không đáng tin.
- CI chạy code PR không tin cậy với secret; token runner/deploy quá quyền.
- Artifact/image/build provenance không được kiểm soát phù hợp.
- Thiếu audit log cho đổi quyền, truy cập tài liệu, export, thao tác tài chính.
- Log có thể bị sửa/xóa dễ dàng; thiếu cảnh báo cho hành vi rủi ro.
- Error response lộ SQL, stack trace, cấu hình hoặc secret.
- Backup chưa kiểm tra restore; thiếu khả năng thu hồi token/key và xử lý sự cố.

## Lưu ý Laravel + React

- Truy vết route → middleware/guard → FormRequest → policy/gate → service/query → resource; không coi route model binding là kiểm tra quyền.
- Với CRUD động, allowlist module/model/action/field/relation và áp dụng quyền trên từng đối tượng. Kiểm tra export/bulk/download riêng.
- Kiểm tra $request->all(), fill/create/update, $fillable/$guarded; validated input vẫn cần quyền sửa field nghiệp vụ.
- Kiểm tra whereRaw/orderByRaw/DB::raw; bind giá trị và allowlist identifier.
- Phân biệt Sanctum cookie session với bearer token; áp dụng CSRF và cookie phù hợp cơ chế thực tế.
- Kiểm tra APP_DEBUG, storage disk visibility, signed route, trusted proxies và rate limiter theo phiên bản.
- Kiểm tra biến VITE_* vì được đưa vào client; kiểm tra dangerouslySetInnerHTML và rich-text sanitizer.
- Không đổi stack hoặc phiên bản chỉ vì một ví dụ; đọc code dự án trước khi đề xuất.

## Định dạng báo cáo

Mở đầu bằng số lỗi xác nhận, mức độ cao nhất và giới hạn phạm vi. Sắp xếp findings theo rủi ro, không theo thứ tự đọc file.

Với mỗi finding, cung cấp:
1. ID, tiêu đề, severity và confidence.
2. Trạng thái: xác nhận hay cần xác minh.
3. Vị trí file/dòng hoặc route; đoạn code tối thiểu, che dữ liệu nhạy cảm.
4. Nguyên nhân gốc và luồng dữ liệu/quyền bị vi phạm.
5. Điều kiện tiền đề và kịch bản tái hiện tối thiểu trong môi trường thử nghiệm.
6. Tác động thực tế và phạm vi dữ liệu/tài khoản/tenant.
7. Cách sửa cụ thể hoặc patch nếu được yêu cầu.
8. Kiểm thử hồi quy: trường hợp hợp lệ, bị từ chối và side effect cần tránh.
9. CWE/OWASP mapping nếu xác minh được, không dùng mapping thay bằng chứng.

Kết thúc bằng kiểm thử đã thực hiện, các phần chưa truy cập/chưa kiểm thử, nghi vấn cần thêm dữ kiện và thứ tự xử lý. Nếu không có lỗi xác nhận, ghi "Chưa phát hiện lỗi trong phạm vi đã kiểm tra", không ghi "Không có lỗ hổng".

Nếu project có skill [`report`](../report/SKILL.md), dùng đúng format "Báo cáo kết quả review" của skill đó để trình bày kết quả thay vì tự bịa format khác.

## Tài liệu tham chiếu

Dùng nguồn chính thức để xác minh quy tắc, phiên bản và cách sửa khi cần:
- OWASP ASVS: https://owasp.org/projects/asvs
- OWASP Top 10: https://owasp.org/projects/top-ten
- OWASP API Security: https://owasp.org/projects/api-security-project
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- CWE: https://cwe.mitre.org/
- Tài liệu chính thức của framework, runtime và nhà cung cấp liên quan.
