---
description: Dọn file tạm/scratch/debug/test thử nghiệm do Claude tự tạo trong session này (skill cleanup-temp-files)
---

Dùng skill `cleanup-temp-files`: rà lại các file tạm/scratch/debug/test thử nghiệm đã tự tạo trong session hiện tại, phân loại file rác (không phải deliverable, không phải test chính thức) với file cần giữ lại (code/test/doc được yêu cầu, test chính thức theo rules/08-quality-assurance.md). Xóa trực tiếp file rác đã xác định, không cần hỏi xác nhận. Không đụng vào file không rõ có phải do mình tạo ra không, hoặc file có sẵn trong workspace — việc đó thuộc agent `workspace-auditor-agent`.

Báo ngắn gọn: đã xóa file nào, giữ lại file nào và vì sao.
