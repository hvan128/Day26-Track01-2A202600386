---
artifact: group-members — Danh sách thành viên nhóm Lab 2
bai-tap: 2 — Phân tích sản phẩm AI (nhóm)
phase: Khai báo nhóm
nop-cuoi: Có — bắt buộc (nộp kèm analysis-report.pdf)
---

# Thành viên nhóm Lab 2

---

## Danh sách thành viên

| # | Mã học viên | Họ tên đầy đủ | Phân công chính |
|---|---|---|---|
| 1 | 2A202600386 | Ngô Hải Văn | Test + screenshot **Cursor**; viết S2 Workflow + S5.4 Moat + S5.5 Data flywheel |
| 2 | 2A202600219 | Nguyễn Tiến Dũng | Test + screenshot **GitHub Copilot**; viết S3 Output & Trust + S5.6 Niche + AI Feature Map + S5.7 Spark→Loop→System |

Phân công chung (cả 2): chốt nhiệm vụ + prompt, dựng S1 Product Moment, S4 Business Signal, S5.1 Verdict, S5.2/S5.3 số liệu, S5.8 Liên hệ Lab 1.

---

## Nhiệm vụ thử nghiệm chung

**Nhiệm vụ**: Refactor 1 function Python dài (~50 dòng) thành 3 function nhỏ hơn, dễ test, kèm 1 unit test cho mỗi function.

**Prompt chính xác** (nhập y hệt vào cả 2 sản phẩm):

```
Refactor function `process_user_order` dưới đây thành 3 function nhỏ hơn:
1) validate_order_input(...)
2) calculate_total_with_tax(...)
3) save_order_to_db(...)

Mỗi function phải có docstring và 1 unit test với pytest.
Giữ nguyên logic và behavior. Code phải chạy được trên Python 3.10+.

[Dán nguyên function process_user_order ~50 dòng vào đây]
```

**Code mẫu**: xem file [`process-user-order.py`](./process-user-order.py) trong folder này — function ~55 dòng mix 3 concerns (validation + tax calculation + DB write), không type hints, lồng if/else. Cả 2 thành viên paste y hệt file này vào prompt của Cursor/Copilot.

**Ngành chọn**: **B — Lập trình**

**Sản phẩm A**: **Cursor** — <https://www.cursor.com>  (Pro plan $20/tháng — dùng 14-day Pro Trial)
**Sản phẩm B**: **GitHub Copilot** — <https://github.com/features/copilot>  (Pro plan $10/tháng — dùng gói student xác minh hoặc 30-day free trial)

Cả 2 đều dùng phiên bản trả phí cá nhân (Pro tier) để so sánh fair — không dùng Enterprise.

---

## Phân chia screenshot

- **Sản phẩm A (Cursor)** → Ngô Hải Văn phụ trách (chạy trên máy của Văn, đăng nhập tài khoản Pro Trial).
- **Sản phẩm B (GitHub Copilot)** → Nguyễn Tiến Dũng phụ trách (chạy trên VS Code, đăng nhập tài khoản student hoặc 30-day trial).

Mỗi người chụp ≥ 3 ảnh bắt buộc + 3 ảnh khuyến khích, đặt tên theo quy ước `product-[A|B]-[số]-[mô tả].png`.

---

## Ghi chú

- Mỗi thành viên copy folder `02-product-comparison/` (đã hoàn thiện) vào repo cá nhân của mình (`Day26-Track01-2A202600386` và `Day26-Track01-2A202600219`).
- Slide deck `analysis-report.pdf` và `analysis-report-link.md` là sản phẩm chung — 2 thành viên cùng tên trong credits.
- File `group-members.md` này phải giống nhau ở cả 2 repo cá nhân.

---

## Cấu trúc Analysis Report — S5 mở rộng

Slide deck Analysis Report có 5 mục bắt buộc (S1 → S5). Mục S5 mở rộng thành 8 mục con:

- **S5.1 Verdict** — Strong / Promising / Weak / At Risk + lý do 1 câu.
- **S5.2 User base + tăng trưởng** — MAU, DAU, paid users, growth rate + nguồn.
- **S5.3 Doanh thu / pricing power** — ARR/MRR; pricing strategy.
- **S5.4 Moat phân tích** — 5 loại moat (data / network / switching / brand / distribution).
- **S5.5 Data flywheel + feedback loop** — hành động user → model; compounding.
- **S5.6 Niche Down + AI Feature Map** — User Value / Alignment / Business Value.
- **S5.7 Spark → Loop → System** — giai đoạn nào; dự báo 12 tháng.
- **S5.8 Liên hệ Lab 1 case** — rủi ro disruption-style; bài học áp dụng được.

Nhóm bắt buộc xong S5.1, S5.6, S5.7, S5.8. S5.2–S5.5 là phần mở rộng để đạt nhóm Khá.
