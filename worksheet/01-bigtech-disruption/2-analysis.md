---
artifact: 2 — Phân tích case theo 4 câu hỏi + 5 chiều định lượng
bai-tap: 1 — Tìm 1 case bị ảnh hưởng bởi big tech AI (cá nhân)
phase: Vận dụng Lens 1 (Customer Expectations + Four Fits)
time: 15 phút
input: 1-research.md + prompts/02-four-fits-analysis.md
nop-cuoi: Không — file trung gian
---

# 2 — Phân tích Chegg vs ChatGPT/Google AI: Phần A + Phần B

---

# Phần A — 4 câu hỏi chiến lược

---

## Câu hỏi 1 — Trước AI, Chegg hoạt động dựa trên giả định gì?

### Trả lời

Trước ChatGPT (trước 11/2022), Chegg là **homework help leader** ở Mỹ:

- **Người dùng**: Sinh viên đại học Mỹ (18-24 tuổi), cần giải bài tập về nhà — STEM, business, social science.
- **Vấn đề người dùng cần giải**: "Giúp tôi giải bài tập này nhanh, đúng, và có lời giải từng bước để học theo".
- **Giá trị Chegg cung cấp**:
  - Kho **135 triệu Q&A** được expert (thường là sinh viên Ấn Độ) trả lời trước đó (data moat).
  - Service "Ask an Expert" — gửi câu hỏi mới, expert trả lời trong 30 phút.
  - Solutions Manual cho textbook chuẩn (ngàn cuốn).
- **Mô hình kinh doanh**: Subscription $19.95/tháng (Chegg Study).
- **Vì sao mô hình này hoạt động được 14 năm (2008-2022)**:
  - **Lý do 1**: Google trả lời tìm kiếm "calculus problem step by step" thì kết quả tự nhiên dẫn user vào trang Chegg → Chegg paywalled → mua subscription. **Distribution moat dựa hoàn toàn vào Google search referral.**
  - **Lý do 2**: Data moat — 135 triệu Q&A là kho khổng lồ, đối thủ mới khó tích đủ.
  - **Lý do 3**: Network effect mỏng — expert (Ấn Độ) ↔ student (Mỹ) — càng nhiều câu hỏi mới, càng có data để bán.

**Bằng chứng**:
- **S-08**: Doanh thu đỉnh $766.9M năm 2022 → mô hình từng cực hiệu quả.
- **S-19**: Giá $19.95/tháng → mô hình subscription rõ ràng.
- **S-18**: Trong đơn kiện Google 2/2025, Chegg công khai thừa nhận **135 triệu Q&A là tài sản chính** mà Google đã dùng để train AI Overviews.

---

## Câu hỏi 2 — Kỳ vọng người dùng đã thay đổi như thế nào? (7 Shifts)

### Trả lời

7 Shifts (nhắc lại):
1. Do the work for me (tool → teammate)
2. Custom made for me
3. Busy work done for me
4. Pay for output (not seat)
5. Expect it now (instant)
6. Interface adapts to me
7. Tool sees what I'm doing (context-aware)

Trong case Chegg, các shift quan trọng nhất là:

- **Shift 1 — Do the work for me**: trước kia sinh viên chấp nhận đọc lời giải step-by-step và tự hiểu. Sau ChatGPT, sinh viên gõ thẳng đề vào prompt → **ChatGPT trả lời ngay, giải thích, viết lại theo ngôn ngữ của em** → không cần "tham khảo lời giải" nữa.
- **Shift 3 — Busy work done for me**: viết essay, tóm tắt chapter, paraphrase — Chegg không làm; ChatGPT làm trong 10 giây.
- **Shift 5 — Expect it now (instant)**: Chegg "Ask an Expert" mất 30 phút; ChatGPT trả lời trong 2 giây.
- **Shift 2 — Custom made for me**: ChatGPT có thể giải lại bằng ngôn ngữ của sinh viên đó, theo trình độ đó. Chegg trả lời cố định theo lời giải đã có sẵn trong database.

So sánh kỳ vọng cũ và mới:

| Trước ChatGPT (kỳ vọng cũ) | Sau ChatGPT (kỳ vọng mới) |
|---|---|
| Chấp nhận đợi 30 phút cho expert | Đợi >5 giây đã quá lâu |
| Đọc lời giải có sẵn, tự hiểu | "Giải lại theo cách em hiểu được" |
| Trả $20/tháng cho thư viện lời giải | Trả $0 (ChatGPT free) hoặc $20 nhưng cho **mọi thứ** (không chỉ homework) |
| Mở Chegg cho mỗi môn riêng | 1 chatbox duy nhất cho mọi môn + cả viết essay + cả code |

**Bằng chứng**:
- **S-04**: ChatGPT 100M MAU trong 2 tháng — kỳ vọng "instant + do the work" lan cực nhanh.
- **S-12**: Chegg subscriber Q4 2024 còn 3.6M (-21% YoY) — người dùng RÚT THẬT, không phải churn theo mùa.
- **S-19**: Giá ngang nhau ($19.95 vs $20) — bỏ Chegg KHÔNG vì giá mà vì **value perception**.

---

## Câu hỏi 3 — Giả định nào của Chegg đã không còn đúng? (Four Fits)

### Trả lời

Bốn Fit của Chegg trước ChatGPT:

- **Product Market Fit (PMF)**: sinh viên cần giải bài tập → Chegg có 135M Q&A → khớp.
- **Product Channel Fit (PCF)**: Google search "[problem] step by step" → kết quả Chegg → click vào trang Chegg paywalled.
- **Channel Model Fit (CMF)**: Google free traffic + subscription $19.95/tháng = CAC thấp, LTV cao.
- **Model Market Fit (MMF)**: sinh viên Mỹ có ngân sách $20/tháng + nhu cầu định kỳ trong học kỳ.

**Trình tự Fit vỡ:**

1. **Fit vỡ ĐẦU TIÊN: Product Market Fit (PMF)** — vì kỳ vọng người dùng nhảy bậc.
   - Người dùng không cần "kho lời giải có sẵn" nữa; họ cần "AI giải bài này cho tôi, theo cách tôi hiểu".
   - Bằng chứng **S-05**: cổ phiếu sập -48% ngày 2/5/2023, CEO Rosensweig công khai nói "spike in student interest in ChatGPT since March" làm chậm new customer growth → PMF đã vỡ từ Q1 2023, chỉ ~3 tháng sau ChatGPT ra mắt.

2. **Fit vỡ THỨ HAI: Product Channel Fit (PCF)** — Google AI Overviews cướp traffic referral.
   - Ngày 14/5/2024 Google AI Overviews ra mắt rộng → kết quả tìm kiếm trả lời thẳng câu hỏi của user, không cần click vào Chegg nữa.
   - Bằng chứng **S-13**: traffic non-subscriber sụp dần: -8% (Q2/24) → -19% (Q3/24) → **-49% (1/2025)**. Đây không phải PMF problem nữa — đây là **kênh phân phối bị Google cắt**.
   - Bằng chứng **S-18**: Chegg kiện Google 24/2/2025 chính vì điều này → công ty thừa nhận PCF đã vỡ.

3. **Fit vỡ THỨ BA: Channel Model Fit (CMF)** — không có Google free traffic, subscription model không CAC-positive nổi.
   - Khi traffic referral sụp, Chegg phải mua quảng cáo trả phí → CAC tăng → subscription $19.95/tháng không đủ trả CAC + COGS + expert payouts.
   - Bằng chứng **S-15, S-16, S-17**: 3 đợt sa thải liên tiếp (21% → 22% → 45%) là phản ứng đối với unit economics đã âm.

4. **Fit vỡ THỨ TƯ: Model Market Fit (MMF)** — thị trường homework help giờ giá thấp + chất lượng AI tốt hơn.
   - Sinh viên có lựa chọn miễn phí (ChatGPT free / Gemini free) chất lượng cao → trả $19.95 cho Chegg không hợp lý nữa.
   - Bằng chứng **S-12**: subscriber giảm từ ~7.8M (2021) → 3.6M (Q4 2024) — mất >50% trong khi giá KHÔNG đổi.

**Tốc độ Fit Collapse**:
- Từ ChatGPT (30/11/2022) đến khi Chegg mất 50% subscriber: ~24 tháng (đến Q4 2024).
- Từ ChatGPT đến khi cổ phiếu mất 50% giá trị: ~5 tháng (2/5/2023).
- Pre-AI: Kodak, Blockbuster, Yahoo mất ~5-10 NĂM để rơi tương tự.
- **Kết luận**: Chegg đã trải qua **Fit Collapse compressed** — 4 Fit vỡ trong 24 tháng. Cái mất nhiều năm để xảy ra giờ rút gọn còn vài tháng (PMF Treadmill).

**Bằng chứng**:
- **S-05**: -48% giá cổ phiếu trong 1 phiên (2/5/2023).
- **S-12**: subscriber -21% YoY Q4 2024.
- **S-13**: traffic -49% YoY tháng 1/2025.
- **S-17**: sa thải 45% workforce tháng 10/2025.

---

## Câu hỏi 4 — Chegg có thể cứu vãn? Hay đã quá muộn?

### Trả lời

So sánh Chegg vs Duolingo (đối thủ cùng partner OpenAI nhưng phản ứng tốt):

| Yếu tố | Chegg | Duolingo |
|---|---|---|
| Đối tác AI | OpenAI (GPT-4) | OpenAI (GPT-4) |
| Thời gian ra sản phẩm AI | CheggMate công bố 17/4/2023 (5 tháng sau ChatGPT); tích hợp sâu phải đến 2024 | Duolingo Max ra 3/2023 (4 tháng) |
| Giá sản phẩm AI | $19.95 Chegg Study (không tăng) | Duolingo Max $30/tháng (premium tier MỚI, tăng ARPU) |
| Tích hợp với sản phẩm cũ | CheggMate là **add-on** rời rạc; user vẫn đi tới Chegg để xem lời giải có sẵn | Duolingo Max **tích hợp thẳng** vào bài học (Explain My Answer, Roleplay, Video Call) |
| Mô hình kinh doanh | Vẫn subscription homework help | Subscription + freemium + AI tier mới |
| Niche moat | "Homework help" — quá rộng, trùng 100% với ChatGPT | "Language learning gamified" — niche hẹp + UX riêng |
| Network effect | Expert (Ấn Độ) ↔ student (Mỹ) — mỏng | Streak / leaderboard / friends — mạnh (gamification + social) |

**Big Squeeze trên Chegg (3 lực nén)**:

- **Lực 1 — Doanh nghiệp lớn sao chép**:
  - OpenAI + ChatGPT: trả lời homework free.
  - Google + AI Overviews (14/5/2024): trả lời ngay trên SERP → cắt referral traffic (bằng chứng **S-13, S-14, S-18**).
  - Microsoft + Copilot (tích hợp Office, Edge): student dùng cho essay.

- **Lực 2 — Startup khác xây nhanh hơn**:
  - Brainly (Ba Lan) tích hợp AI sớm + mua Quizlet AI features.
  - Khan Academy + Khanmigo (powered by GPT-4) — content giáo dục có nguồn gốc, miễn phí.

- **Lực 3 — Platform AI gom người dùng**:
  - ChatGPT (5/2025: ~800M weekly active users) trở thành "1 destination cho mọi nhu cầu" — sinh viên không còn lý do mở Chegg riêng.

**Đánh giá của tôi**:

- **Chegg có cứu vãn được không?**: **Quá muộn cho mô hình homework help cũ.** Có thể tồn tại như công ty nhỏ B2B skilling, KHÔNG còn quay lại $14B market cap.

- **Lý do**:
  1. **Data moat hỏng**: 135M Q&A của Chegg đã bị Google train vào AI Overviews (bằng chứng **S-18** — đây là gốc rễ vụ kiện). Moat thành **dữ liệu chùa** mà big tech ăn.
  2. **Distribution moat hỏng**: 80%+ traffic Chegg đến từ Google search → khi Google trả lời ngay trên SERP, Chegg mất kênh duy nhất (bằng chứng **S-13**: traffic -49%).
  3. **Niche quá rộng**: "Homework help" trùng 100% với use case mặc định của ChatGPT — không có ngách để defend.

- **Điều Chegg đáng lẽ phải làm khác** (trong 6 tháng đầu sau ChatGPT, từ 12/2022 đến 5/2023):
  1. **Niche xuống**: pivot sang 1-2 môn cụ thể (vd: USMLE prep, AP exam prep) với UX và data riêng biệt, KHÔNG cố giữ "homework help cho tất cả".
  2. **Tích hợp AI vào core trước, không launch sản phẩm rời**: CheggMate đáng lẽ phải là Chegg Study v2.0 chứ không phải add-on.
  3. **Đối tác AI khác Google** (vd: Anthropic) để giảm rủi ro Google "tham" data; hoặc tự train model nhỏ trên 135M Q&A độc quyền.
  4. **Đổi mô hình kinh doanh sang B2B**: bán Chegg API cho trường đại học, không bán B2C subscription cạnh tranh trực tiếp với ChatGPT.

**Bằng chứng**:
- **S-20**: Duolingo +41% revenue, +451% net income → cùng partner OpenAI nhưng adapt đúng cách. Vấn đề KHÔNG phải AI, mà là niche + tốc độ + moat.
- **S-17**: Sa thải 45% workforce + thay CEO 10/2025 → công ty đã ở chế độ survival, không còn "cứu vãn" mà là "thoát thân".

---

# Phần B — 5 chiều phân tích định lượng

## B1 — User base

| Chỉ số | Trước AI shock | Sau AI shock | Nguồn |
|---|---|---|---|
| Người dùng trả tiền (paid subscribers) | ~7.8M (2021) | 3.6M (Q4 2024, -21% YoY) | S-12 |
| Tổng subscribers (Chegg Services + Busuu) | ~7.8M (2021) | 6.6M (FY 2024, -14.2% YoY) | S-12 |
| Non-subscriber traffic (visit/month) | baseline 100% | -49% YoY (1/2025) | S-13 |
| MAU / DAU | Không công khai cụ thể | Không công khai cụ thể | — |

**Nhận định**: Tệp paid subscriber sụt nhanh nhất (-55% từ đỉnh 2021 đến Q4 2024). Tệp non-subscriber (free traffic search) sụt còn nhanh hơn (-49% chỉ trong 9 tháng cuối 2024) — do Google AI Overviews. **Cả funnel TOP (Google traffic) và BOTTOM (paid sub) đều sụp đồng thời.**

## B2 — Tốc độ tăng trưởng

| Giai đoạn | Tốc độ tăng trưởng | Nguồn |
|---|---|---|
| 2020–2021 (pandemic boom) | +50%/năm revenue (đỉnh) | MacroTrends (S-08) |
| 2022 (đã chậm) | -1.21% YoY | S-08 |
| 2023 (sau ChatGPT) | -6.6% YoY | S-09 |
| 2024 | -13.78% YoY | S-10 |
| Q4 2024 | -24% YoY (quý sập sâu nhất) | S-11 |
| Thời điểm đảo chiều | Q1 2023 (3 tháng sau ChatGPT) | S-05 |

**Nhận định**: Chegg đã thật sự quay đầu giảm, không phải chậm lại. Tốc độ giảm **gia tốc**: 2023 -6.6% → 2024 -13.8% → Q4 2024 -24%. Curve đi xuống dốc hơn theo thời gian — dấu hiệu Fit Collapse hoàn toàn.

## B3 — Doanh thu / valuation

| Chỉ số | Trước AI shock | Sau AI shock | Nguồn |
|---|---|---|---|
| Annual revenue | $766.9M (2022) | $617.6M (2024) | S-08, S-10 |
| Quarterly revenue | $205.2M (Q4 2022) | $143.5M (Q4 2024, -30%) | S-11 |
| Market cap | ~$14B (2/2021 đỉnh) | ~$90M (5/2026) | S-01, S-02 |
| Sụt giá trị thị trường | — | **-99.4%** | derived |
| ARPU (rough estimate) | ~$98/year ($766.9M / 7.8M sub) | ~$172/year ($617.6M / 3.6M sub) | derived |

**Mức công khai**: Cao — Chegg niêm yết NYSE, có 10-K filings + earnings releases hàng quý trên investor.chegg.com.

**Nhận định**: Mất $13.9 tỷ vốn hoá trong ~4 năm — một trong những vụ "wipeout" lớn nhất do AI gây ra cho công ty niêm yết. ARPU tăng (vì giữ giá nhưng mất subscriber) nhưng tổng revenue vẫn giảm — dấu hiệu **bóp tệp khách hàng còn lại** thay vì grow lại.

## B4 — Moat strategy

| Loại moat | Mức mạnh trước AI | Bằng chứng cụ thể |
|---|---|---|
| Data moat | **Mạnh** (135M Q&A) | S-18: được Chegg công khai trong đơn kiện Google |
| Network effect | Yếu (expert-student mỏng, không two-sided sticky) | Expert là contractor, không invest vào platform |
| Switching cost | Yếu (subscription tháng, không có data user lock-in) | Sub hủy bất kỳ lúc nào, không export-import gì |
| Brand | Trung bình (sinh viên Mỹ biết Chegg nhưng không "yêu") | Không có brand premium |
| Distribution | **Mạnh nhưng phụ thuộc** (Google search referral chiếm 80%+ traffic) | Khi Google đổi thuật toán, Chegg hứng đòn |

- **Moat chủ đạo trước AI**: **Distribution moat via Google search** + **Data moat (135M Q&A)**. Cả hai đều phụ thuộc Google.
- **Big tech AI tấn công moat nào**: **Cả hai** — ChatGPT tấn công data moat (làm 135M Q&A trở nên thừa vì AI tự generate được); Google AI Overviews tấn công distribution moat (cắt referral traffic).
- **Moat còn lại sau AI**: Brand yếu, switching cost gần bằng 0. **Gần như không còn moat nào.**

**Nhận định**: Cấu trúc moat của Chegg là **moat "rented land"** — cả data + distribution đều dựa trên việc Google cho phép. Khi Google quyết định cạnh tranh trực tiếp (AI Overviews), Chegg không có hào nào tự mình kiểm soát được.

## B5 — Data flywheel + feedback loop

- **Hành động người dùng feed lại sản phẩm**: Sinh viên hỏi câu mới → expert trả lời → lưu vào DB → câu sau có lời giải → kéo user mới (qua Google search) → trả tiền → trả tiền cho expert → vòng tròn.
- **Loop có compounding không?**: **Một phần.** Amplification factor mỏng — 1 câu hỏi mới chỉ phục vụ thêm vài chục user khác có cùng đề. Không compounding theo cấp số nhân (như ChatGPT — 1 conversation training data → cải thiện cho tất cả).
- **Sản phẩm có thu feedback systematically?**: **Có thu nhưng không dùng tốt** — thumbs up/down trên lời giải có, nhưng không retrain mô hình AI (vì không có mô hình AI riêng, dùng GPT-4 raw).
- **Big tech AI vô hiệu hoá flywheel ở đâu?**:
  1. **Đầu vào**: Google AI Overviews cắt câu hỏi mới (user không cần vào Chegg để hỏi nữa) — S-13.
  2. **Đầu ra**: Google + ChatGPT có thể tự generate lời giải mới, không cần kho 135M Q&A của Chegg — bằng chứng S-18 (đơn kiện Chegg vs Google nêu rõ Google đã train trên Q&A của Chegg).

**Nhận định**: Khi Google AI Overviews + ChatGPT vô hiệu hoá cả input (câu hỏi mới từ user) và output (lời giải), Chegg còn lại **kho 135M Q&A tĩnh** — tài sản lịch sử nhưng không tự sinh sôi. **Flywheel đã ngừng quay.**

---

## Tổng kiểm tra

| Phần | Đã trả lời? | ≥ 2 bằng chứng? |
|---|---|---|
| A1 — Giả định cũ | ✓ | ✓ (S-08, S-19, S-18) |
| A2 — Kỳ vọng người dùng | ✓ | ✓ (S-04, S-12, S-19) |
| A3 — Fit nào vỡ | ✓ | ✓ (S-05, S-13, S-15, S-17, S-18) |
| A4 — Cứu được không | ✓ | ✓ (S-20, S-17) |
| B1 — User base | ✓ | ✓ (S-12, S-13) |
| B2 — Tốc độ tăng trưởng | ✓ | ✓ (S-08 đến S-11) |
| B3 — Doanh thu / valuation | ✓ | ✓ (S-01, S-02, S-08, S-10, S-11) |
| B4 — Moat strategy | ✓ | ✓ (S-18, S-13) |
| B5 — Data flywheel | ✓ | ✓ (S-13, S-18) |

→ Chuyển sang `3-FINAL-case-analysis.md` để viết bản nộp.
