---
name: dependency-audit
description: Rà soát dependency (npm/yarn/pnpm, composer, pip/poetry, cargo, go mod...) tìm bản lỗi thời hoặc có lỗ hổng (CVE) đã biết bằng audit tool có sẵn của chính ecosystem (npm audit, composer audit, pip-audit, cargo audit, govulncheck), đề xuất upgrade tối thiểu giữ tương thích. Dùng trước khi thêm dependency mới, khi review PR có đổi package.json/composer.json/requirements.txt/go.mod, hoặc khi người dùng hỏi dependency có an toàn không. KHÔNG tự ý chạy upgrade/install — chỉ báo cáo và đề xuất lệnh, người dùng tự quyết chạy.
license: MIT
metadata:
  version: "1.0"
---

# 📦 Dependency Audit

Skill **read-only** cho dependency — áp dụng nguyên tắc tương tự [`rules/13-database-read-only.md`](../../rules/13-database-read-only.md) nhưng cho package manager: được tự do audit/kiểm tra, **không tự ý** `install`/`update`/`upgrade` khi chưa được yêu cầu rõ.

## Quy trình

1. **Xác định ecosystem và lockfile** đang dùng trong project — không suy đoán, đọc file thật: `package-lock.json`/`yarn.lock`/`pnpm-lock.yaml` (Node), `composer.lock` (PHP), `poetry.lock`/`requirements.txt` (Python), `Cargo.lock` (Rust), `go.sum` (Go). Một project có thể có nhiều ecosystem (monorepo) — audit riêng từng phần.
2. **Chạy audit tool read-only** tương ứng, không kèm flag tự sửa (`--fix`, `--force`):
   - Node: `npm audit` / `yarn audit` / `pnpm audit`
   - PHP: `composer audit`
   - Python: `pip-audit` (nếu có cài) hoặc `poetry run pip-audit`
   - Rust: `cargo audit`
   - Go: `govulncheck ./...`
   - Thiếu tool tương ứng trong `PATH` → nêu rõ không audit được, không bịa kết quả (xem [`rules/14`](../../rules/14-search-priority.md)).
3. **Phân loại đúng theo output thật của tool** (severity critical/high/medium/low) — không tự đặt mức độ khác với tool báo.
4. **Với mỗi lỗ hổng tìm được**, ghi rõ: package bị ảnh hưởng, version hiện tại, version fix tối thiểu, loại thay đổi (patch/minor/major theo SemVer) — version fix nhảy major thì cảnh báo khả năng breaking change, cần test lại kỹ hơn là chỉ bump version.
5. **Đề xuất, không tự chạy**: đưa ra lệnh cụ thể (`npm install pkg@x.y.z`, `composer require pkg:^x.y`...) để người dùng tự chạy — giống nguyên tắc Explicit Authorization của [`rules/10`](../../rules/10-commit-discipline.md) áp dụng cho git, áp dụng tương tự cho package manager. Lockfile đổi sau khi audit/upgrade cũng là thay đổi cần qua đúng quy trình commit ở [`rules/10`](../../rules/10-commit-discipline.md), không tự commit kèm.
6. **Ngoại lệ**: người dùng yêu cầu rõ ràng *cả hai* — audit **và** tự chạy upgrade trong project — thì được phép chạy đúng lệnh đã đề xuất. Không suy rộng từ một yêu cầu "kiểm tra dependency" sang việc tự tiện tay cài/update khi chưa được yêu cầu chạy.

## Khi không có audit tool hoặc không có mạng

Không bịa danh sách CVE từ kiến thức chung khi không chạy được audit tool thật — nói rõ "chưa audit được, thiếu `<tool>`" thay vì đoán ([`rules/14`](../../rules/14-search-priority.md)). Có thể gợi ý cài tool (`npm install -g pnpm` không cần vì đi kèm; `pip install pip-audit`, `cargo install cargo-audit`) nhưng để người dùng tự quyết cài.

## Khi áp dụng

- Trước khi thêm dependency mới vào project — audit trước khi đề xuất thêm.
- Khi review PR/diff có đổi file manifest hoặc lockfile của package manager.
- Khi người dùng hỏi trực tiếp "dependency có lỗ hổng không", "có nên upgrade X không".
- **Không dùng** để tự ý chạy `npm update`/`composer update` hàng loạt khi chỉ được yêu cầu kiểm tra — đó là vượt phạm vi đã giao.
