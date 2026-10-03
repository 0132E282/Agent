---
name: refactoring-catalog
description: Tra cứu danh mục kỹ thuật refactor (theo Fowler/Refactoring.Guru) ứng với từng code smell cụ thể — Extract Method/Function, Extract Variable, Decompose Conditional, Replace Conditional with Polymorphism, Replace Magic Number with Symbolic Constant, Introduce Parameter Object, Extract Class, Replace Temp with Query — kèm khi nào nên và không nên áp dụng. Dùng khi thấy code smell cụ thể (hàm quá dài, điều kiện lồng sâu, trùng lặp, quá nhiều tham số) cần refactor nhưng chưa chắc kỹ thuật nào phù hợp. KHÔNG dùng để refactor tràn lan ngoài phạm vi đang sửa (xem rules/09-boy-scout-rule) hoặc khi vấn đề cần một design pattern mới cho cấu trúc mở rộng (dùng design-patterns).
license: MIT
metadata:
  version: "1.0"
---

# 🔨 Refactoring Catalog

Khác với [`design-patterns`](../design-patterns/SKILL.md) (áp pattern GoF để **tạo cấu trúc mới** cho nhu cầu mở rộng/thay thế), skill này là kỹ thuật **cải tiến code đang có** mà **không đổi hành vi quan sát được** (external behavior) — đầu vào/đầu ra giữ nguyên, chỉ thay đổi cách tổ chức code bên trong.

## Nguyên tắc bắt buộc

- **Không đổi hành vi** — nếu một thay đổi làm output khác đi, đó là sửa bug hoặc thêm tính năng, không phải refactor.
- **Phải có test bao phủ trước khi refactor** ([`rules/08`](../../rules/08-quality-assurance.md)) — không có test, refactor không thể xác nhận hành vi còn giữ nguyên. Thiếu test cho đoạn sắp refactor → viết test chốt hành vi hiện tại trước (dùng [`testing-strategy`](../testing-strategy/SKILL.md)), rồi mới refactor.
- **Từng bước nhỏ, chạy lại test sau mỗi bước** — không dồn nhiều kỹ thuật refactor vào một lần sửa lớn khó review.
- **Rule of Three** ([`rules/04`](../../rules/04-dry.md)): trùng lặp/code smell xuất hiện 2 lần có thể chấp nhận, lần thứ 3 mới refactor — tránh trừu tượng hóa sớm.
- **Giữ phạm vi** ([`rules/09`](../../rules/09-boy-scout-rule.md)): refactor trong đúng function/block đang sửa; code smell ở file/module khác không thuộc task hiện tại → báo lại, không tự ý mở rộng phạm vi.

## Code smell → kỹ thuật refactor

| Code smell | Kỹ thuật | Khi dùng |
|---|---|---|
| Hàm quá dài, làm nhiều việc (tên có "và": `validateAndSave`) | **Extract Method/Function** | Tách đoạn logic có thể đặt tên rõ thành hàm riêng ([`rules/02`](../../rules/02-readability.md)) |
| Biểu thức điều kiện/tính toán phức tạp khó đọc | **Extract Variable** | Gán biểu thức con vào biến có tên mô tả ý nghĩa, không cần comment giải thích |
| `if/else` lồng sâu nhiều tầng | **Decompose Conditional** / Guard Clauses | Tách từng nhánh thành hàm riêng hoặc dùng early return ([`rules/02`](../../rules/02-readability.md)) thay vì lồng tiếp |
| `switch`/`if-else` theo loại đối tượng, lặp lại ở **nhiều nơi** (≥3) | **Replace Conditional with Polymorphism** | Chỉ khi lặp thật ở nhiều nơi và có khả năng thêm loại mới — 1 nơi duy nhất thì giữ `if` theo [`rules/01`](../../rules/01-simplicity.md) |
| Số/chuỗi "ma thuật" lặp lại không rõ nghĩa (`if (status === 3)`) | **Replace Magic Number/String with Symbolic Constant** | Đặt tên hằng số mô tả ý nghĩa (`STATUS_SHIPPED = 3`) |
| Hàm nhận quá nhiều tham số cùng mô tả một khái niệm | **Introduce Parameter Object** | Gom tham số liên quan (`street, city, zip` → `Address`) thành một object/struct |
| Cùng một nhóm field + hàm xử lý chúng lặp lại ở nhiều chỗ (data clump) | **Extract Class** | Tách thành class/struct riêng mang đúng trách nhiệm ([`rules/03`](../../rules/03-separation-of-concerns.md)) |
| Biến tạm chỉ dùng để gọi lại một biểu thức một lần | **Replace Temp with Query** | Thay biến tạm bằng hàm tính trực tiếp — cẩn trọng nếu biểu thức là query nặng (DB/network), giữ biến tạm để tránh gọi lại nhiều lần |
| Comment giải thích "đoạn này làm gì" | **Extract Method + đặt tên rõ** | Tên hàm thay thế comment mô tả "cái gì" ([`rules/12`](../../rules/12-comments.md)) |

```javascript
// ❌ Code smell: điều kiện lồng sâu + magic number
function getShippingFee(order) {
  if (order) {
    if (order.status === 3) {
      if (order.weight > 20) {
        return 50000;
      }
    }
  }
  return 0;
}

// ✅ Guard clauses (Decompose Conditional) + Symbolic Constant
const STATUS_SHIPPED = 3;
const HEAVY_WEIGHT_KG = 20;
const HEAVY_SHIPPING_FEE = 50000;

function getShippingFee(order) {
  if (!order || order.status !== STATUS_SHIPPED) return 0;
  if (order.weight <= HEAVY_WEIGHT_KG) return 0;
  return HEAVY_SHIPPING_FEE;
}
```

## Khi áp dụng

- Thấy một code smell cụ thể ở trên trong đoạn code đang sửa — tra bảng để chọn đúng kỹ thuật, không áp kỹ thuật ngẫu nhiên.
- Trước khi refactor: xác nhận đã có test bao phủ hành vi hiện tại.
- **Không dùng** để refactor lan ra ngoài phạm vi task đang làm ([`rules/09`](../../rules/09-boy-scout-rule.md)), hoặc khi vấn đề thật ra cần một pattern kiến trúc mới (ví dụ cần swap nhiều implementation qua interface) — khi đó dùng [`design-patterns`](../design-patterns/SKILL.md).
