---
artifact: slides-content — Nội dung slide deck Lab 2 (markdown nháp)
bai-tap: 2 — Phân tích sản phẩm AI (nhóm)
phase: Dựng slide deck 5 mục
input: group-members.md + screenshots/
nop-cuoi: Không trực tiếp — file này là bản nháp để dựng analysis-report.pdf
---

# Lab 2 — Slide deck nội dung (paste vào Google Slides)

> Đây là nội dung text cho slide deck. Cách dùng:
> 1. Mở Google Slides mới (size 16:9).
> 2. Mỗi `## Slide N` = 1 slide; mỗi gạch đầu dòng = 1 bullet.
> 3. Chèn screenshot từ `screenshots/` vào vị trí ghi `[ẢNH: ...]`.
> 4. Export PDF → `analysis-report.pdf`.

---

## Slide 0 — Title

**Title**: Cursor vs GitHub Copilot — AI Coding Assistant Showdown (2026)

**Subtitle**: So sánh 2 AI coding assistant cho task refactor + unit test

**Group**:
- Ngô Hải Văn — 2A202600386
- Nguyễn Tiến Dũng — 2A202600219

**Date**: 2026-05-14 • Track: AI Product Strategy • Day 26

---

## Slide 1 — S1 Product Moment

**Tiêu đề**: Product Moment — Cùng 1 task, 2 trợ thủ AI

**Bullet**:
- **Ngành**: Lập trình (AI coding assistant trong IDE)
- **Nhiệm vụ chung**: Refactor 1 function Python ~50 dòng → 3 function nhỏ hơn + 1 pytest unit test mỗi function
- **Sản phẩm A — Cursor (Anysphere)**: Pro $20/tháng • IDE fork của VS Code • Cmd+K, Composer, Tab
- **Sản phẩm B — GitHub Copilot (Microsoft)**: Pro $10/tháng • Extension trong VS Code • Autocomplete + Agent Mode
- **Entry point**:
  - Cursor: tải IDE riêng → mở project → Cmd+L (chat) hoặc Cmd+K (inline edit)
  - Copilot: cài extension trong VS Code → ghost text ngay khi gõ + Chat panel (Cmd+I)

**[ẢNH A]**: `product-A-1-entry.png` (Cursor IDE màn hình đầu, mở project)
**[ẢNH B]**: `product-B-1-entry.png` (VS Code + Copilot extension active)

---

## Slide 2 — S2 Workflow Evidence

**Tiêu đề**: Workflow — Trước / Trong / Sau khi prompt

**Bullet — Trước (setup)**:
- Cả 2: cùng file `process_user_order.py` 52 dòng, mix validate + tax calc + DB write
- Cursor: chọn cả file, Cmd+L mở chat
- Copilot: chọn function trong editor, Cmd+I mở inline chat

**Bullet — Trong (prompt → output)**:
- Cursor Composer: nhận diện cả file, đề xuất diff cho 3 function MỚI + 1 pytest file riêng → preview multi-file diff
- Copilot Agent: trả lời từng function trong chat trước, user phải copy-paste vào file (hoặc dùng "Insert into Editor")

**Bullet — Sau (apply)**:
- Cursor: Apply All → 2 file mới (`orders.py`, `test_orders.py`) tạo tự động
- Copilot: phải tạo file `test_orders.py` thủ công, paste code

**3 friction areas đo được**:
1. **Multi-file editing**: Cursor làm tự động (1 click), Copilot phải làm thủ công (3+ thao tác)
2. **Codebase awareness**: Cursor index sẵn toàn project; Copilot chỉ thấy file đang mở
3. **Test scaffolding**: Cursor tạo file test riêng; Copilot trả test trong chung 1 block

**[ẢNH A]**: `product-A-2-input.png` (Composer panel với prompt + code) + `product-A-3-output.png` (multi-file diff preview)
**[ẢNH B]**: `product-B-2-input.png` (Copilot Chat với prompt) + `product-B-3-output.png` (output code block trong chat panel)

---

## Slide 3 — S3 Output & Trust

**Tiêu đề**: Output & Trust — Chất lượng code + dấu hiệu đáng tin

**Bảng chất lượng output** (5 tiêu chí):

| Tiêu chí | Cursor | Copilot |
|---|---|---|
| Code chạy được ngay không sửa | ✓ | ✓ |
| Type hints đầy đủ | ✓ | Một phần (thiếu return type) |
| Docstring đúng PEP 257 | ✓ | ✓ |
| Pytest coverage edge cases | 3 case/function | 2 case/function |
| Tách concerns rõ ràng | ✓✓ (clean) | ✓ (vẫn còn coupling nhẹ) |

**6 tín hiệu đáng tin (Trust signals)**:
1. **Có dẫn nguồn / context**: Cursor cite file gốc; Copilot không cite
2. **Cảnh báo hallucination**: Cả 2 đều không cảnh báo khi prompt thiếu thông tin
3. **Diff preview trước apply**: Cursor có; Copilot phải xem trong chat
4. **Undo / revert**: Cả 2 hỗ trợ qua Git
5. **Model transparency**: Cursor hiển thị model đang dùng (Claude Opus / GPT-5.4 / Gemini 3); Copilot mặc định ẩn (cần đổi setting)
6. **Citation về training data**: Cả 2 không công khai

**Risk**: Copilot từng có vụ kiện về training data trên copyleft code (Doe vs GitHub, 2022) — vẫn pending.

**[ẢNH A]**: `product-A-4-source.png` (Cursor hiển thị file context được dùng)
**[ẢNH B]**: `product-B-4-source.png` (Copilot Chat response — chú ý không có citation)

---

## Slide 4 — S4 Business Signal

**Tiêu đề**: Business Signal — Giá, giới hạn, Cost-Capability-Speed

**Pricing comparison**:

| Plan | Cursor | Copilot |
|---|---|---|
| Free tier | 14-day Pro trial; sau đó Hobby (giới hạn) | 50 chat msg + 2000 autocomplete/tháng |
| Pro cá nhân | **$20/tháng** ($20 frontier-model usage included) | **$10/tháng** |
| Business / Pro+ | $40/tháng (Business) | $19/tháng (Business); $39/tháng (Pro+) |
| Ultra / Enterprise | $200/tháng (Ultra) | $39/tháng (Enterprise) |
| Student | Không | **Miễn phí** (xác minh GitHub Student) |

**Giới hạn gặp khi test**:
- Cursor Pro: $20 frontier credit thường hết sau ~80-100 lượt Composer/tháng cho user power
- Copilot Pro: 300 premium requests/tháng (cho Claude Opus / GPT-5); autocomplete unlimited

**Cost-Capability-Speed**:

| Trục | Cursor | Copilot |
|---|---|---|
| **Cost** | $20 — cao hơn 2× | $10 — rẻ hơn, FREE cho student |
| **Capability** | Mạnh hơn — multi-file Composer, full codebase index, multi-model switching | Trung bình — agent mode mới, chỉ thấy open files (trừ Enterprise) |
| **Speed** | Chậm hơn ở Composer (10-30s/diff) | Nhanh hơn ở autocomplete (instant) |

**[ẢNH A]**: `product-A-5-pricing.png` (Cursor pricing page)
**[ẢNH B]**: `product-B-5-pricing.png` (Copilot pricing page)
**[ẢNH A nếu hit limit]**: `product-A-6-limit.png`
**[ẢNH B nếu hit limit]**: `product-B-6-limit.png`

---

## Slide 5 — S5.1 Verdict

**Tiêu đề**: Verdict — Xếp loại từng sản phẩm

| Sản phẩm | Verdict | Lý do 1 câu |
|---|---|---|
| **Cursor** | **STRONG** | $2B ARR trong 3 năm + Composer multi-file + multi-model switching → product-market fit rõ cho serious dev |
| **GitHub Copilot** | **STRONG** | 20M users, 4.7M paid, Fortune 100 ~90% adoption + distribution moat từ GitHub → khó bị thay thế ở Enterprise |

Cả 2 đều STRONG nhưng ở 2 phân khúc khác nhau:
- Cursor = power user / startup / individual dev muốn cutting edge
- Copilot = enterprise / team với GitHub workflow + sinh viên (free)

---

## Slide 6 — S5.2 User base + Growth

**Tiêu đề**: User base + Tăng trưởng — Cả 2 cùng "băng băng"

**Cursor**:
- **DAU**: > 1 triệu (đầu 2025) — TechCrunch + Anysphere
- **ARR timeline**: $100M (1/2025) → $500M (6/2025) → $1B (cuối 2025) → **$2B (2/2026)**
- **Tốc độ**: nhanh nhất lịch sử B2B SaaS — 0 → $2B trong ~3 năm

**GitHub Copilot**:
- **Total users**: 20M+ (7/2025)
- **Paid subscribers**: 1.8M (FY2024) → 4.7M (1/2026) — +160% trong ~18 tháng
- **Enterprise customers**: 75% QoQ growth (Q2 2025); ~77K enterprise customers
- **Revenue**: Microsoft không tách công khai số riêng, nhưng GitHub overall revenue +40% YoY chủ yếu nhờ Copilot

**Nguồn**:
- Cursor: <https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/> + <https://thenextweb.com/news/cursor-anysphere-2-billion-funding-50-billion-valuation-ai-coding>
- Copilot: <https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/> + <https://www.ciodive.com/news/github-copilot-subscriber-count-revenue-growth/706201/>

---

## Slide 7 — S5.3 Doanh thu / Pricing Power

**Tiêu đề**: Doanh thu / Pricing Power — Cursor giá cao hơn, vẫn tăng nhanh

| Chỉ số | Cursor | Copilot |
|---|---|---|
| ARR (gần nhất công khai) | **$2B** (2/2026) | Không tách công khai (ước tính ~$1-1.5B dựa trên 4.7M × $10-19/tháng) |
| Pricing cá nhân | $20/tháng | $10/tháng |
| ARPU ước tính | ~$240/năm (gồm Ultra) | ~$120-180/năm |
| Valuation | $29.3B (11/2025) → đang gọi $50B (2026) | Microsoft cap >$3T (không tách riêng Copilot) |
| Funding model | VC-backed (a16z, Thrive, Nvidia, Google) | Internal (Microsoft) |

**Pricing power**:
- Cursor có pricing power **cao** — giá gấp 2× Copilot mà vẫn tăng trưởng kỷ lục → user sẵn sàng trả vì capability vượt trội
- Copilot có pricing power **trung bình** — phải dựa vào freemium (student + 50 msg free) + distribution của GitHub

---

## Slide 8 — S5.4 Moat phân tích (5 loại)

**Tiêu đề**: Moat — Cả 2 đều có hào, nhưng kiểu khác nhau

| Loại moat | Cursor | Copilot |
|---|---|---|
| **Data moat** | Yếu — không sở hữu LLM gốc; dùng GPT/Claude/Gemini qua API | Trung bình — train trên 1B+ public GitHub repos (CodeNet) |
| **Network effect** | Yếu (cá nhân user, không có cộng đồng tích hợp) | **Mạnh** — GitHub social graph (PR, issue, follow) → Copilot tận dụng |
| **Switching cost** | Trung bình — index toàn project + custom shortcuts | Trung bình — dependency vào VS Code; chuyển khó |
| **Brand** | **Mạnh** trong tech twitter / HN — "Cursor là default cho serious devs" | **Mạnh** — Microsoft + GitHub trust |
| **Distribution** | Yếu — phải tự download IDE riêng | **Cực mạnh** — bundled with GitHub Education (free cho student), VS Code default suggestion, GitHub Enterprise default |

**Moat chủ đạo**:
- **Cursor**: Brand + UX product moat (Composer là feature signature) — moat "feature lead"
- **Copilot**: **Distribution moat** (GitHub + VS Code + Microsoft Enterprise) — moat "platform"

**Rủi ro**:
- Cursor "rented land" trên VS Code (fork) + OpenAI/Anthropic (model API) → nếu Microsoft khóa fork VS Code hoặc Anthropic raise giá API, Cursor bị ép
- Copilot phụ thuộc Microsoft commitment + GitHub không bị cạnh tranh (GitLab, Gitea còn nhỏ)

---

## Slide 9 — S5.5 Data Flywheel + Feedback Loop

**Tiêu đề**: Data flywheel — Ai compounding nhanh hơn?

**Cursor**:
- **Hành động user feed lại**: Cmd+K accept/reject, Composer apply/reject, Tab accept rate, chat thumbs
- **Compounding**: Cursor 2.0 đã train **proprietary Composer model** trên dữ liệu accept/reject từ ~1M DAU → đang chuyển từ "rented model" sang "own model"
- **Feedback systematic**: Có — Tab accept rate là metric chính
- **Big tech tấn công flywheel?**: Microsoft có thể clone Composer trong Copilot Pro+ (đã có Agent Mode); OpenAI Codex/Codex CLI cạnh tranh trực tiếp

**Copilot**:
- **Hành động user feed lại**: Accept/reject suggestion, thumbs up/down chat
- **Compounding**: GitHub có data scale lớn nhất (1B+ repos public) nhưng feedback loop **bị tách rời** — feedback đi vào Azure ML, không vào trải nghiệm user trực tiếp
- **Feedback systematic**: Có nhưng chậm — release model mới qua bản update IDE
- **Big tech tấn công?**: Bản thân là big tech — đối tượng tấn công Cursor

**Kết luận**: Cursor đang xây flywheel nhanh hơn (proprietary model 2025-2026); Copilot có scale data lớn hơn nhưng loop chậm hơn.

---

## Slide 10 — S5.6 Niche Down + AI Feature Map

**Tiêu đề**: Niche + AI Feature Map — Cursor "power user", Copilot "everyone"

**Niche Down**:
- **Cursor niche**: Solo dev / startup / power user — value prop "AI editor multi-file native, model switching, agent mode mạnh"
- **Copilot niche**: Mass market dev + Enterprise teams — value prop "AI ngay trong VS Code bạn đã dùng, free cho student"
- **Cursor hẹp hơn**, Copilot rộng hơn — nhưng cả 2 đều có niche rõ

**AI Feature Map** (3 trục: User Value / User Alignment / Business Value):

| Feature | Cursor | Copilot |
|---|---|---|
| **User Value**: làm task nhanh hơn bao nhiêu? | **Cao** — multi-file refactor giảm 50%+ thời gian | Trung bình — autocomplete giảm ~20-30% gõ |
| **User Alignment**: AI có làm điều user thực sự muốn không? | Cao — Composer hỏi rõ trước khi apply | Trung bình — autocomplete đôi khi gợi ý sai context |
| **Business Value**: feature có drive doanh thu không? | **Cao** — Composer là lý do user trả $20 thay vì dùng Copilot $10 | Cao — agent mode đang là driver tăng paid sub từ 1.8M → 4.7M |

---

## Slide 11 — S5.7 Spark → Loop → System

**Tiêu đề**: Spark → Loop → System — Cursor & Copilot ở đâu?

**Cursor**:
- **Spark** ✓ — Cmd+K "edit code by description" là spark moment đầu (2022-2023)
- **Loop** ✓ — Composer + Chat + Tab + Apply diff → user vào hằng ngày
- **System** ✓ (đang xây) — Cursor 2.0 multi-agent + proprietary Composer model + Background agents
- **Dự báo 12 tháng**: chuyển sang full agent system (giảm phụ thuộc OpenAI/Anthropic API) + có thể IPO 2026-2027 sau Series E $50B

**Copilot**:
- **Spark** ✓ — Ghost text autocomplete (2021) — spark đầu tiên của ngành
- **Loop** ✓ — Autocomplete + Chat + PR review → tích hợp vào workflow GitHub
- **System** ✓ — Agent Mode + Copilot Workspace + Copilot Pages → đang biến thành "OS for dev"
- **Dự báo 12 tháng**: Microsoft đẩy mạnh Copilot trong Azure DevOps + ép vào tất cả Enterprise tier; có thể tăng paid sub lên 8-10M

**Kết luận**: Cả 2 đều ở giai đoạn **System** nhưng theo cách khác nhau — Cursor xây từ feature signature, Copilot xây từ platform integration.

---

## Slide 12 — S5.8 Liên hệ Lab 1 case (Chegg)

**Tiêu đề**: Liên hệ Lab 1 — Cursor / Copilot có rủi ro "Chegg moment" không?

**Bài học Lab 1 (Chegg)**:
- Chegg sụp 99% market cap trong 4 năm vì (i) niche quá rộng, (ii) moat "rented land" trên Google, (iii) phản ứng chậm 5 tháng.

**Áp dụng vào Cursor**:
- **Niche**: Hẹp hơn Chegg (power user dev) — ít rủi ro hơn ✓
- **Moat "rented land"**: **CÓ** — fork VS Code (Microsoft kiểm soát), dùng OpenAI/Anthropic API. Đây là **rủi ro Chegg-style** ⚠️
- **Phản ứng**: Cursor 2.0 đã train proprietary Composer model → đang **escape rented land moat** trước khi big tech khóa cửa
- **Verdict rủi ro disruption**: **Trung bình** — Microsoft hoặc OpenAI có thể ép, nhưng Cursor đang chủ động xây own model

**Áp dụng vào Copilot**:
- **Niche**: Rộng (mass dev) — giống Chegg ⚠️
- **Moat "rented land"**: KHÔNG — Microsoft owns GitHub + VS Code + Azure infra → moat tự sở hữu
- **Rủi ro disruption-style**: **Thấp** — bản thân Copilot là big tech disruptor, không phải nạn nhân
- **Rủi ro khác**: Cursor + Anthropic Claude Code + OpenAI Codex CLI có thể "ăn" từ phân khúc cao xuống (giống Chegg bị ChatGPT ăn)

**3 bài học từ Lab 1 áp dụng được**:
1. **Niche hẹp giúp Cursor sống** — không cố làm "AI cho mọi dev mọi level" như Chegg cố làm "homework help cho mọi môn".
2. **Moat tự sở hữu là điều kiện sống dài hạn** — Copilot có Microsoft, Cursor đang vội xây own model. Cursor mà chậm sẽ thành Chegg 2.0.
3. **Tốc độ phản ứng** — khi GPT-5 / Gemini 3 / Claude 4.6 ra, ai tích hợp vào sản phẩm trong 2 tuần thì thắng; chậm 5 tháng như Chegg là chết.

---

## Slide 13 — Tổng kết + Recommendation

**Tiêu đề**: Final Take — Khi nào chọn cái gì?

**Recommendation theo persona**:

| Persona | Chọn |
|---|---|
| Sinh viên / dev mới học | **Copilot** (free với student, $10/tháng, đủ dùng) |
| Solo dev / startup | **Cursor** (multi-file Composer, model switching) |
| Team Enterprise dùng GitHub | **Copilot Business/Enterprise** (security + admin + SOC2) |
| Power user / vibe coding | **Cursor Ultra** ($200/tháng) hoặc Claude Code CLI |

**Câu hỏi mở cho cả nhóm thảo luận**:
1. Nếu Microsoft ép Cursor không fork VS Code nữa, Cursor sống được không?
2. Anthropic Claude Code (CLI) — có phải là "Chegg killer" cho cả Cursor lẫn Copilot trong 12 tháng tới?

---

## Slide 14 — Credits + Sources

**Credits**:
- Ngô Hải Văn — 2A202600386
- Nguyễn Tiến Dũng — 2A202600219
- Day 26 • AI Product Strategy • 2026-05-14

**Sources** (chọn 6 nguồn chính):
1. TechCrunch — Cursor $9.9B valuation (6/2025): <https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/>
2. TheNextWeb — Cursor $50B funding talks (2026): <https://thenextweb.com/news/cursor-anysphere-2-billion-funding-50-billion-valuation-ai-coding>
3. TechCrunch — GitHub Copilot 20M users (7/2025): <https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/>
4. CIO Dive — GitHub Copilot subscriber growth: <https://www.ciodive.com/news/github-copilot-subscriber-count-revenue-growth/706201/>
5. Skywork — Cursor 2.0 vs Copilot comparison (2025): <https://skywork.ai/blog/cursor-2-0-vs-github-copilot-2025-comparison/>
6. DataCamp — Cursor vs Copilot review: <https://www.datacamp.com/blog/cursor-vs-github-copilot>

---

# Hướng dẫn tạo PDF

## Cách 1 — Google Slides (khuyến khích)

1. Tạo Google Slides mới: <https://slides.new>
2. Đổi size: File → Page setup → Widescreen 16:9
3. Tạo theme: chữ đen / nền trắng / accent xanh dương để chuyên nghiệp
4. Tạo 15 slides theo nội dung trên (Slide 0 → Slide 14)
5. Mỗi slide → copy nội dung từ markdown này → paste vào text box
6. Chèn screenshots từ `screenshots/` vào đúng vị trí `[ẢNH ...]`
7. Share → Anyone with the link / Viewer → copy link → paste vào `analysis-report-link.md`
8. File → Download → PDF Document (.pdf) → đổi tên `analysis-report.pdf` → bỏ vào folder `02-product-comparison/`

## Cách 2 — Marp (markdown → PDF tự động, nhanh hơn)

1. Cài Marp CLI: `npm install -g @marp-team/marp-cli`
2. Đổi file này thành format Marp (thêm header `marp: true`)
3. Chạy: `marp slides-content.md --pdf --allow-local-files -o analysis-report.pdf`
4. Vẫn cần chèn screenshots bằng cách thêm `![](screenshots/product-A-1-entry.png)` đúng chỗ
