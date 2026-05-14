---
artifact: slides-content — Nội dung slide deck Lab 2 (markdown nháp)
bai-tap: 2 — Phân tích sản phẩm AI (nhóm)
phase: Dựng slide deck 5 mục
input: group-members.md + screenshots/
nop-cuoi: Không trực tiếp — file này là bản nháp để dựng analysis-report.pdf
---

# Lab 2 — Slide deck nội dung: Google Antigravity vs GitHub Copilot

> **File này là bản tóm tắt.** Nội dung slide đầy đủ (15 slide) là `analysis-report-source.html` trong cùng folder — đó là nguồn được dùng để export `analysis-report.pdf`.
>
> Nếu muốn dùng Google Slides thay vì HTML/PDF:
> 1. Mở Google Slides mới (size 16:9).
> 2. Copy text/bảng từ `analysis-report-source.html` từng slide (mở file trong browser).
> 3. Chèn screenshot từ `screenshots/` vào vị trí ghi `[ẢNH: ...]`.
> 4. Export PDF → đè lên `analysis-report.pdf`.
> 5. Share link Google Slides → paste vào `analysis-report-link.md`.

---

## Outline 15 slide

| # | Mục | Nội dung chính | Screenshot cần |
|---|---|---|---|
| 0 | Title | Tên nhóm + sản phẩm + ngành | - |
| 1 | **S1 Product Moment** | Nhiệm vụ refactor `process_user_order` + giới thiệu 2 sản phẩm | `product-A-1-entry.png`, `product-B-1-entry.png` |
| 2 | **S2 Workflow Evidence** | Trước/trong/sau prompt — 3 friction areas (autonomy, multi-agent, codebase awareness) | A-2/3, B-2/3 |
| 3 | **S3 Output & Trust** | Bảng 5 tiêu chí code quality + 6 trust signals | - |
| 4 | **S4 Business Signal** | Pricing (Antigravity FREE vs Copilot $10/$39), giới hạn (rate limit drama 3/2026), Cost-Cap-Speed | A-5, B-5 |
| 5 | **S5.1 Verdict** | Antigravity = PROMISING, Copilot = STRONG + per-persona verdict | - |
| 6 | **S5.2 User base + Growth** | Antigravity ra 18/11/2025 + hype; Copilot 20M user / 4.7M paid | - |
| 7 | **S5.3 Pricing Power** | Antigravity loss-leader, Copilot freemium | - |
| 8 | **S5.4 Moat (5 loại)** | Antigravity moat = Distribution Gmail + Data Gemini; Copilot = Distribution GitHub + Network effect | - |
| 9 | **S5.5 Data Flywheel** | Antigravity unique (browser interaction data); Copilot scale lớn nhưng loop chậm | - |
| 10 | **S5.6 Niche + Feature Map** | Antigravity = agent power user (hẹp), Copilot = mass market (rộng) | - |
| 11 | **S5.7 Spark→Loop→System** | Antigravity ở Spark, Copilot tới System | - |
| 12 | **S5.8 Liên hệ Lab 1** | Cả 2 KHÔNG có Chegg moment (đều big tech, moat tự sở hữu); Antigravity rủi ro Stadia-style; Copilot rủi ro chậm phản ứng | - |
| 13 | **Final Recommendation** | 5 persona × sản phẩm | - |
| 14 | **Credits + Sources** | 6 nguồn chính | - |

---

## Highlights (tóm tắt thông điệp chính)

### Cùng task, 2 paradigm khác nhau
- **Antigravity**: agent-first — Mission Control dispatch agent tự verify, có thể dùng browser
- **Copilot**: editor-first — inline chat trong VS Code, user vẫn lái mỗi bước

### Pricing đảo trục
- Antigravity FREE preview (gồm Claude Opus 4.6) vs Copilot $39 Pro+ cho Claude Opus
- Đây là chiến lược "loss leader" của Google để giành share trước Microsoft

### Rate limit drama 3/2026
- Antigravity Pro $19.99 advertise 5-hour refresh, thực tế user báo 7-day lockout
- Điểm trừ lớn nhất của Antigravity ở thời điểm hiện tại

### Verdict không phải về AI quality
- Cả 2 đều generate code chạy được; khác biệt nằm ở **autonomy** (Antigravity tự verify) vs **ổn định** (Copilot không drama)

### Liên hệ Lab 1
- Cả 2 đều là big tech, KHÔNG có rủi ro "Chegg moment" do moat tự sở hữu
- Copilot có rủi ro "chậm phản ứng" — nếu không leap sang full agent mode, có thể trở thành "Chegg của AI IDE"

---

## Cách re-export PDF sau khi có screenshots

Sau khi Hải Văn (Antigravity) + Dũng (Copilot) chụp đủ ảnh:

```bash
cd worksheet/02-product-comparison/

# Sửa analysis-report-source.html: thay
#   <div class="placeholder-image">[ẢNH: ...]</div>
# bằng
#   <img src="screenshots/product-X-N-name.png" style="max-width:100%; max-height:280px; border:1px solid #ccc; border-radius:4px;">

# Re-export PDF
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --print-to-pdf=analysis-report.pdf "file://$(pwd)/analysis-report-source.html"
```
