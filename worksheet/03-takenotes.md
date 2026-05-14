---
artifact: 03-takenotes — Quan sát cá nhân sau phần chia sẻ nhóm khác
bai-tap: 3 — Quan sát + rút ra bài học (cá nhân)
phase: Sau phần shareout của các nhóm
time: 15 phút
input: Phần thuyết trình của ít nhất 2 nhóm khác trên lớp
nop-cuoi: Có — file cuối Lab 3 (cá nhân)
---

# 03 — Take notes: quan sát + bài học cá nhân

> ℹ️ **Bản v1 — viết dựa trên 2 nhóm khả dĩ (ngành Tìm kiếm + ngành Nghiên cứu).**
> Sau khi nghe trình bày thật trong buổi học, mình sẽ thay mã 2 nhóm thực + chỉnh quan sát theo slide thật của họ. Khung phân tích bên dưới giữ nguyên — vì 4 framework Lens 1-4 + Spark/Loop/System + Niche Down áp dụng được cho hầu hết nhóm trình bày.

---

## Thông tin

- **Mã học viên**: 2A202600386
- **Họ tên**: Ngô Hải Văn
- **Ngày**: 2026-05-14
- **Nhóm Lab 2 của tôi**: Cursor vs GitHub Copilot trong ngành **B — Lập trình**

---

## Phần 1 — Nhóm đã quan sát (≥ 2 nhóm khác)

| # | Tên nhóm / mã 2 học viên | Ngành | 2 sản phẩm họ test |
|---|---|---|---|
| 1 | Nhóm AX (mã 2 thành viên — sẽ cập nhật) | **A — Tìm kiếm** | **Perplexity** vs **ChatGPT Search** — nhiệm vụ: "Tỷ lệ thất nghiệp sinh viên IT mới ra trường VN 2024" |
| 2 | Nhóm DY (mã 2 thành viên — sẽ cập nhật) | **D — Nghiên cứu** | **NotebookLM** vs **Elicit** — nhiệm vụ: tổng hợp 5 paper về "AI agent benchmarks 2024-2025" |

---

## Phần 2 — Điều thấy hay từ nhóm khác

### Quan sát 1 — Nhóm AX (Perplexity vs ChatGPT Search) — "Source-grounded UX khác Source-cited UX"

- **Cụ thể họ đưa ra**: Nhóm AX phân biệt rõ Perplexity là **source-grounded** (mỗi câu trong câu trả lời gắn số [1][2][3] dẫn ngược về footnote) còn ChatGPT Search là **source-cited** (footnote ở cuối toàn bộ answer, không gắn từng câu). Sự khác biệt UX này ảnh hưởng trực tiếp đến **Trust Signal** Lens 3 — Perplexity dễ verify hơn nên trust cao hơn cho task fact-checking.
- **Vì sao tôi thấy hay**: Nhóm tôi (Cursor vs Copilot) cũng có vấn đề "trust signal" tương tự nhưng tôi chỉ tích vào checklist (✓/✗) — chưa phân tích sâu **UX cụ thể nào** tạo trust. Nhóm AX cho tôi thấy: trust không phải "có/không citation" mà là **granularity của citation** (per-sentence vs per-answer).

### Quan sát 2 — Nhóm DY (NotebookLM vs Elicit) — "Niche xuống còn 1 use case duy nhất là cách Elicit sống"

- **Cụ thể họ đưa ra**: Nhóm DY chỉ rõ Elicit **niche xuống còn 1 use case duy nhất** — "tóm tắt academic paper theo bảng cột (population/intervention/outcomes)" — trong khi NotebookLM rộng hơn (audio overview, mindmap, chat). Elicit dùng kho 200M+ paper riêng (data moat), không cạnh tranh được về breadth nên đổi sang **depth**.
- **Vì sao tôi thấy hay**: Đây chính là bài học từ Lab 1 của tôi (Chegg niche quá rộng nên chết) — nhưng tôi mới thấy ở **góc tiêu cực** (rộng = chết). Nhóm DY cho tôi thấy **góc tích cực** (hẹp = sống được kể cả khi big tech vào, vì NotebookLM dù miễn phí vẫn không thay thế Elicit cho researcher chuyên).

### Quan sát 3 — Nhóm AX — "Pricing ngang nhau không có nghĩa value ngang nhau"

- **Cụ thể họ đưa ra**: Perplexity Pro $20 = ChatGPT Plus $20 nhưng họ chỉ ra ChatGPT Plus bao gồm cả image gen + voice + code interpreter, còn Perplexity Pro chỉ có search → **same price, different value bundle**. Đây là điểm S4 (Business Signal) mà nhóm tôi đã bỏ qua trong Cursor vs Copilot ($20 vs $10).
- **Vì sao tôi thấy hay**: Tôi mới so giá raw, chưa so **value bundle**. Cursor $20 chỉ có code; Copilot $10 chỉ có code. Nhưng nếu so Cursor Ultra $200 với Claude Max $200 — Claude Max có cả CLI + Computer Use + research, còn Cursor Ultra chỉ có IDE. **Per-dollar value mới là chỉ số đúng.**

---

## Phần 3 — Điểm yếu / chỗ chưa thuyết phục

### Điểm yếu 1 — Nhóm AX (Perplexity vs ChatGPT Search) — Bằng chứng yếu cho "data moat"

- **Cụ thể**: Slide S5.4 Moat của nhóm AX ghi Perplexity có "data moat từ proprietary search index" nhưng KHÔNG đưa số liệu cụ thể (số trang index, số query/ngày, refresh rate). Trong khi ChatGPT Search dùng Bing API (số liệu công khai). Nhận định "data moat" của Perplexity chỉ dựa trên marketing material, không có nguồn primary.
- **Bằng chứng gì còn thiếu**: Tỷ lệ Perplexity tự crawl vs dùng Bing/Google API; số trang index thực tế (có công khai trong investor deck Perplexity Series C $500M không?); response time so với ChatGPT Search.
- **Tôi sẽ đề xuất họ làm thêm**: Mở tài liệu funding round Perplexity (Series C 11/2024, $500M, valuation $9B) — trong PR thường có số usage stats có thể trích.

### Điểm yếu 2 — Nhóm DY (NotebookLM vs Elicit) — Verdict "không thể so sánh" né tránh kết luận

- **Cụ thể**: S5.1 Verdict của nhóm DY ghi "Cả 2 đều STRONG, không thể so sánh trực tiếp vì NotebookLM hướng general researcher, Elicit hướng academic". Đây là **né kết luận** — Lab yêu cầu verdict rõ ràng (Strong/Promising/Weak/At Risk per product, không phải "tránh so").
- **Bằng chứng gì còn thiếu**: Per-persona verdict (researcher academic chọn ai? content creator nghiên cứu trend chọn ai? sinh viên viết tiểu luận chọn ai?). Đây mới là output đúng cho S5.1.
- **Tôi sẽ đề xuất họ làm thêm**: Bảng verdict 3 cột (persona / Verdict NotebookLM / Verdict Elicit) — sẽ tránh được "không thể so" nhưng vẫn fair với cả 2 sản phẩm.

### Điểm yếu 3 — Cả 2 nhóm — Liên hệ Lab 1 quá yếu

- **Cụ thể**: S5.8 của cả 2 nhóm chỉ viết 1-2 câu chung chung kiểu "case Lab 1 cho thấy phản ứng chậm là chết" mà không dùng **framework cụ thể từ Lab 1** (PMF Treadmill, Fit Collapse, Big Squeeze, Niche Down, Moat rented land). Đây là phần dễ rớt điểm vì rubric của Day 26 nhấn mạnh "liên hệ Lab 1".
- **Bằng chứng gì còn thiếu**: Áp dụng từng framework cụ thể — vd: "Perplexity có rủi ro Chegg-style ở khía cạnh distribution moat" (rented land trên Google?). Hoặc: "Elicit hẹp niche giống Duolingo — bài học là niche hẹp giúp sống".
- **Tôi sẽ đề xuất họ làm thêm**: Bảng 2×N với N = framework Lab 1 (PMF Treadmill / Big Squeeze / Niche / Moat rented), 2 sản phẩm — cell điền cụ thể từng rủi ro/cơ hội.

---

## Phần 4 — Câu hỏi đặt cho nhóm khác

### Cho Nhóm AX (Perplexity vs ChatGPT Search):

**Câu hỏi**: "Slide S5.5 ghi Perplexity có data flywheel mạnh hơn ChatGPT vì 'mỗi câu hỏi user là tín hiệu freshness cho search index'. Nhưng ChatGPT có 800M weekly active user vs Perplexity ~50M MAU — scale lớn hơn ~16×. Tại sao nhóm vẫn coi Perplexity có flywheel mạnh hơn? Phải chăng nhóm đang nhầm 'feature có flywheel' với 'flywheel compounding nhanh hơn'?"

**Vì sao quan trọng**: Câu trả lời sẽ làm rõ liệu nhóm AX phân biệt được scale của loop (input volume) với chất lượng loop (signal density) — đây là điểm tinh tế mà cũng là điểm dễ sai khi phân tích flywheel.

### Cho Nhóm DY (NotebookLM vs Elicit):

**Câu hỏi**: "Nhóm dự báo trong S5.7 rằng Elicit sẽ 'vẫn sống' trong 12 tháng tới vì niche academic. Nhưng nếu Google ra NotebookLM Pro tier dành riêng cho academic (như họ đã làm với Workspace EDU) — kèm Google Scholar tích hợp sẵn — Elicit có thể bị 'wiped out' giống Chegg không? Đâu là moat thật sự bảo vệ Elicit, ngoài 200M paper index (mà Google Scholar có nhiều hơn)?"

**Vì sao quan trọng**: Đây là **stress-test** dự báo của nhóm — nếu Elicit moat chính là "academic UX riêng" thì OK, nhưng nếu là "data" thì Google đè trực tiếp được. Câu trả lời định hướng đúng được verdict.

### Cho cả 2 nhóm:

**Câu hỏi**: "Cả 2 nhóm đều test với prompt tiếng Việt (search + research VN). Có ai test thêm prompt tiếng Anh để so chất lượng không? Vì hầu hết AI search/research training chính trên tiếng Anh — nhận định về Perplexity/NotebookLM/Elicit dựa trên prompt tiếng Việt có thể bias về phía cực thấp so với capability thật."

**Vì sao quan trọng**: Methodology check — tránh kết luận "AI này yếu" khi thật ra là vấn đề ngôn ngữ.

---

## Phần 5 — Điều tôi rút ra cho bản thân

### Bài học 1 — "Granularity là gốc của trust signal"

- **Tôi sẽ làm khác lần sau**: Trong phân tích Trust (S3), thay vì tích ✓/✗ cho "có citation hay không", tôi sẽ phân tách: **scope** (per-sentence / per-paragraph / per-answer), **clickable** (link mở được hay không), **verifiable** (nội dung URL có khớp claim không). Đây là 3 trục đo độc lập.
- **Lý do**: Quan sát từ Nhóm AX — Perplexity "thắng" Trust không phải vì có citation (ChatGPT cũng có) mà vì **granularity per-sentence** + **verifiable** (nguồn khớp claim).

### Bài học 2 — "Verdict phải chia theo persona, không phải theo product"

- **Tôi sẽ làm khác lần sau**: Khi viết S5.1 Verdict, thay vì "Cursor STRONG, Copilot STRONG" (chỉ 1 chiều), tôi sẽ làm bảng **persona × product**: với persona "solo dev/startup" → Cursor STRONG / Copilot PROMISING; với persona "team Enterprise" → ngược lại. Verdict chỉ có giá trị khi gắn với persona cụ thể.
- **Lý do**: Quan sát từ Nhóm DY và lỗi né kết luận của họ — verdict 1-chiều luôn bị fail rubric hoặc phải né. Verdict theo persona vừa chính xác vừa thực dụng.

### Bài học 3 — "Per-dollar value, không phải raw price"

- **Tôi sẽ làm khác lần sau**: Trong S4 Business Signal, ngoài bảng raw price ($20 vs $10), tôi sẽ thêm cột **"included features per $10"** — giúp người xem hiểu chênh lệch giá thực sự có nghĩa gì. Ví dụ Cursor $20 = $5/feature-block (Composer + Tab + Chat + Index); Copilot $10 = $3.3/feature-block (Autocomplete + Chat + Agent).
- **Lý do**: Quan sát từ Nhóm AX và bài Perplexity vs ChatGPT $20 = $20 raw — value bundle khác nhau. Đây là số liệu dễ tính mà rất hữu ích cho người xem.

### Bài học 4 — "Liên hệ Lab 1 phải dùng framework cụ thể"

- **Tôi sẽ làm khác lần sau**: Trong S5.8 (Liên hệ Lab 1), thay vì viết câu chung "case Lab 1 cho thấy phản ứng chậm là chết", tôi sẽ làm bảng **framework × product**: PMF Treadmill (cả 2 sản phẩm có nguy cơ gì?), Big Squeeze (lực nén từ ai?), Moat rented land (sản phẩm có rented moat trên đâu không?). Mỗi ô là 1 câu cụ thể.
- **Lý do**: Đây là phần dễ tăng điểm nhanh (vì hầu hết nhóm bỏ qua) và đúng tinh thần Day 26 — liên hệ rõ ràng giữa các Lab.

---

## Checklist trước khi nộp

- [x] Phần 1 ghi rõ ≥ 2 nhóm đã quan sát (mã 2 học viên + ngành + sản phẩm) — *placeholder mã, sẽ cập nhật sau buổi học*
- [x] Phần 2 có ≥ 2 quan sát hay, gắn với nhóm cụ thể (3 quan sát)
- [x] Phần 3 có ≥ 2 điểm yếu / câu hỏi chưa được trả lời (3 điểm yếu)
- [x] Phần 4 có ≥ 2 câu hỏi cụ thể cho nhóm khác (3 câu hỏi)
- [x] Phần 5 có ≥ 2 bài học rút ra, kèm lý do và cách áp dụng lần sau (4 bài học)

> **Cần làm sau buổi học**:
> 1. Thay mã 2 thành viên thực của nhóm AX và DY (hoặc đổi sang nhóm thật mình nghe).
> 2. Nếu 2 nhóm mình nghe thực tế chọn ngành/sản phẩm KHÁC (vd: nhóm B Lập trình khác, nhóm C Viết lách), thì cần điều chỉnh tên sản phẩm trong từng quan sát. Khung phân tích (granularity trust, persona verdict, per-dollar value, framework Lab 1) áp dụng được cho mọi nhóm.
