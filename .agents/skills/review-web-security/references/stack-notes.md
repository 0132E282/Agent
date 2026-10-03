# Lưu ý Laravel + React

- Truy vết route → middleware/guard → FormRequest → policy/gate → service/query → resource; không coi route model binding là kiểm tra quyền.
- Với CRUD động, allowlist module/model/action/field/relation và áp dụng quyền trên từng đối tượng. Kiểm tra export/bulk/download riêng.
- Kiểm tra `$request->all()`, fill/create/update, `$fillable`/`$guarded`; validated input vẫn cần quyền sửa field nghiệp vụ.
- Kiểm tra `whereRaw`/`orderByRaw`/`DB::raw`; bind giá trị và allowlist identifier.
- Phân biệt Sanctum cookie session với bearer token; áp dụng CSRF và cookie phù hợp cơ chế thực tế.
- Kiểm tra `APP_DEBUG`, storage disk visibility, signed route, trusted proxies và rate limiter theo phiên bản.
- Kiểm tra biến `VITE_*` vì được đưa vào client; kiểm tra `dangerouslySetInnerHTML` và rich-text sanitizer.
- Không đổi stack hoặc phiên bản chỉ vì một ví dụ; đọc code dự án trước khi đề xuất.
