---
name: ci-pipeline
description: Soạn/review pipeline CI (GitHub Actions, GitLab CI...) đảm bảo lint + test + build chạy trước khi merge — thứ tự job fail-fast, cache dependency, trigger push/pull_request hợp lý, secret injection an toàn qua biến CI (không hardcode). Dùng khi thêm workflow CI mới, sửa workflow hiện có, hoặc review PR có đổi .github/workflows. KHÔNG tự ý trigger deploy/production job hoặc chạy workflow thật — chỉ soạn/review file cấu hình, việc chạy thật do CI platform hoặc người dùng xác nhận.
license: MIT
metadata:
  version: "1.0"
---

# ⚙️ CI Pipeline

Skill soạn/review **file cấu hình CI** (không chạy workflow thật, không deploy) — đảm bảo mọi thay đổi code đều qua lint + test + build trước khi merge, nối tiếp [`rules/08-quality-assurance.md`](../../rules/08-quality-assurance.md) ở tầng tự động hóa.

## Quy trình

1. **Xác định platform** đang dùng trong repo — đọc file có sẵn, không suy đoán: `.github/workflows/*.yml` (GitHub Actions), `.gitlab-ci.yml` (GitLab CI), `azure-pipelines.yml` (Azure). Repo chưa có CI và không có platform nào được chỉ định → hỏi lại trước khi chọn.
2. **Xác định stack thật** của project từ file manifest (`package.json`, `composer.json`, `requirements.txt`/`pyproject.toml`, `go.mod`) để chọn đúng action/step cài đặt (`actions/setup-node`, `actions/setup-php`, `actions/setup-python`, `actions/setup-go`) và cache dependency (`actions/cache`, hoặc cache tích hợp sẵn của `setup-*`).
3. **Thứ tự job chuẩn, fail fast** ([`rules/06`](../../rules/06-fail-fast-validation.md)): `install → lint → test → build`. Lint/test fail thì dừng ngay, không chạy tiếp build — không để job build chạy xong rồi mới biết lint fail.
4. **Trigger hợp lý**:
   - `pull_request` → chạy full suite (lint + test + build) trên code sắp merge.
   - `push` vào branch chính → có thể thêm job riêng (ví dụ build artifact/deploy), **tách job riêng** khỏi lint/test, không gộp chung để tránh một lần fail làm rối trách nhiệm từng job ([`rules/03`](../../rules/03-separation-of-concerns.md)).
5. **Secret luôn qua biến CI** (`secrets.*` của GitHub Actions, CI/CD Variables của GitLab) — không hardcode giá trị thật vào file YAML, không `echo`/log giá trị secret ra output ([`rules/07-data-safety.md`](../../rules/07-data-safety.md)).
6. **Review workflow hiện có** (khi được giao review, không phải tự ý sửa): thiếu bước lint/test, thiếu cache (dependency cài lại mỗi lần → chậm), matrix version không khớp runtime thật project dùng, step chạy trên self-hosted runner không rõ nguồn gốc.

```yaml
# ✅ Fail fast: lint/test trước, build sau; cache dependency; trigger đúng
name: CI
on:
  pull_request:
  push:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"
      - run: npm ci
      - run: npm run lint
      - run: npm test

  build:
    needs: lint-and-test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"
      - run: npm ci
      - run: npm run build
```

## Không tự ý

- Thêm job **deploy production**, chạy **migration thật**, hoặc đổi secret/environment variable của repo thật trên GitHub/GitLab — đây là thay đổi hạ tầng chia sẻ ảnh hưởng người khác, luôn xác nhận với người dùng trước (xem phần "Executing actions with care" ở system prompt).
- Trigger chạy workflow thật (`gh workflow run`, push lên remote) khi chỉ được yêu cầu soạn/review file cấu hình.

## Khi áp dụng

- Thêm/sửa file workflow CI, hoặc review PR đổi `.github/workflows`/`.gitlab-ci.yml`.
- Dự án chưa có CI và người dùng yêu cầu thiết lập pipeline lint/test/build cơ bản.
- **Không dùng** để tự chạy deploy hoặc thay đổi secret thật trên platform CI — những việc đó cần xác nhận riêng, ngoài phạm vi soạn file cấu hình.
