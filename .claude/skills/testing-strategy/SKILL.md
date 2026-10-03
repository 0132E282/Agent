---
name: testing-strategy
description: Chuẩn hóa viết unit test kỹ thuật khi implement/sửa code — chọn test double đúng loại (mock/stub/fake/spy), tổ chức test theo Arrange-Act-Assert, cách ly dependency ngoài (I/O, network, time, random), và review độ phủ theo rủi ro (không chạy theo % coverage cứng). Dùng khi coding-agent viết code mới/sửa logic cần test kỹ thuật kèm theo, hoặc khi review test hiện có thiếu cách ly dependency/test giả luôn pass. KHÔNG dùng để thiết kế test case nghiệp vụ theo đặc tả (equivalence/boundary/pairwise) — đó là agent qa-tester; skill này là lớp kỹ thuật viết test code khi implement, không phải thiết kế ca kiểm thử từ yêu cầu.
license: MIT
metadata:
  version: "1.0"
---

# 🧪 Testing Strategy

Skill kỹ thuật cho việc **viết test code** đi kèm khi implement/sửa logic — khác với agent [`qa-tester`](../../agents/qa-tester.md) (thiết kế test case **nghiệp vụ** từ đặc tả: equivalence partitioning, boundary value, decision table, truy vết REQ→AC). Hai việc này độc lập: `qa-tester` có thể không cần biết mock là gì; skill này không quan tâm case nghiệp vụ nào cần test, chỉ quan tâm *cách viết* bài test đúng kỹ thuật cho đơn vị code cụ thể.

## Nguyên tắc bắt buộc

- **Test hành vi quan sát được (behavior), không test chi tiết triển khai (implementation detail)** — đổi cách viết nội bộ hàm mà không đổi input/output thì test không được fail.
- **Luôn có test trước khi refactor/fix bug** ([`rules/08`](../../rules/08-quality-assurance.md)): sửa bug → viết test tái hiện bug trước, thấy fail, rồi fix cho tới khi pass (regression test).
- **Độ phủ theo rủi ro**, không theo % cứng: ưu tiên business logic, edge case, luồng ảnh hưởng tiền/dữ liệu nhạy cảm. Một hàm getter/setter/CRUD đơn giản không cần test riêng nếu đã được cover gián tiếp qua luồng lớn hơn.
- **Rule of Three** áp dụng cho test giống `rules/04-dry.md`: không vội tạo helper/fixture chung cho 2 test, đợi lần lặp thứ 3 mới gom.

## Chọn test double đúng loại

| Loại | Dùng khi | Ví dụ |
|---|---|---|
| **Stub** | Chỉ cần trả dữ liệu giả cố định để test chạy được, không quan tâm nó được gọi thế nào | `userRepo.findById = () => fakeUser` |
| **Mock** | Cần **xác nhận tương tác** đã xảy ra đúng (gọi đúng hàm, đúng tham số, đúng số lần) | Xác nhận `emailService.send()` được gọi đúng 1 lần với đúng địa chỉ |
| **Fake** | Cần một bản triển khai nhẹ, hoạt động thật nhưng không phù hợp production (in-memory DB thay SQL thật) | Repository in-memory thay cho kết nối Postgres khi test |
| **Spy** | Cần chạy hành vi thật **và** ghi lại lời gọi để kiểm tra sau | Wrap hàm thật, vẫn chạy logic, nhưng đếm số lần gọi |

Cách ly (double hóa) dependency **không xác định/không kiểm soát được** trong unit test: gọi I/O thật (DB, file, HTTP ra ngoài), thời gian hệ thống (`Date.now()`, `time.Now()`), số ngẫu nhiên, biến môi trường thay đổi giữa lần chạy. Logic nội bộ thuần (business logic không phụ thuộc I/O) nên test trực tiếp, không mock — mock quá tay làm test chỉ còn xác nhận lại mock, không bắt được bug thật ([`rules/01`](../../rules/01-simplicity.md): không thêm abstraction/mock cho thứ không cần cách ly).

## Cấu trúc một test

**Arrange–Act–Assert** (hoặc Given–When–Then nếu codebase đã dùng BDD):

```javascript
// ❌ Test tối nghĩa, trộn nhiều assert không liên quan
test("order", () => {
  const o = createOrder();
  expect(o.total).toBe(100);
  expect(o.status).toBe("pending");
  expect(mockSend).toHaveBeenCalled();
});

// ✅ Arrange - Act - Assert rõ ràng, tên test mô tả đúng hành vi
test("should_apply_vip_discount_when_customer_is_vip", () => {
  const order = buildOrder({ customerType: "VIP", subtotal: 100 });

  const result = calculateTotal(order);

  expect(result.total).toBe(80);
});
```

- Tên test mô tả **hành vi + điều kiện** (`should_X_when_Y`), không mô tả cách triển khai.
- Mỗi test tập trung **một khái niệm hành vi** — nhiều `assert` cùng kiểm tra một kết quả logic thì được, nhưng nhiều hành vi không liên quan trong một test thì tách ra.

## Dấu hiệu test có vấn đề khi review

- Test luôn pass dù code sai (thiếu assert thật, hoặc assert điều kiện luôn đúng như `expect(true).toBe(true)`).
- Test flaky do phụ thuộc `Date.now()`/`Math.random()`/thứ tự chạy mà không seed/cách ly.
- Test phụ thuộc trạng thái của test khác chạy trước (không độc lập, fail khi đổi thứ tự).
- Mock quá nhiều tới mức test chỉ còn xác nhận lại chính mock, không còn test logic thật.

## Khi áp dụng

- Ngay sau `coding-agent` viết/sửa logic mới cần test kỹ thuật — xác định dependency nào cần double hóa, viết test theo AAA.
- Ngay sau khi fix một bug — viết test tái hiện bug trước khi sửa (xem [`rules/08`](../../rules/08-quality-assurance.md)).
- Khi review test hiện có nghi ngờ giả/flaky — rà theo mục "Dấu hiệu test có vấn đề" ở trên.
- **Không dùng** khi cần thiết kế ca kiểm thử từ đặc tả nghiệp vụ (dùng agent `qa-tester`), hoặc khi cần chọn pattern kiến trúc (dùng skill [`design-patterns`](../design-patterns/SKILL.md)).
