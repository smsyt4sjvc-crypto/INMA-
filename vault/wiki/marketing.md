# marketing — assets, channels, campaigns

> What INMA has out in the world to bring in homeowners, and what's been tried.

Related: [[brand]] · [[evolution]] · [[architecture]] · [[state]]
Source: [[2026-07-10-git-history-ingest]]

## DATA (what exists / what's been done)

### Direct mail (EDDM)
- [2026-05-09] EDDM mailer artwork built: 3 PNGs + 3 QR codes + a build script.
- [2026-06-24] Mailer QR codes point to **`/welcome`** — a landing page built so
  the codes resolve (they weren't before). `qr-welcome.png` is the code.
- [2026-06-26] **Mailer back-v2**: full-bleed two-column design, laid out around
  the postage cutout.

### Mailer result — first drop (measured)
> 🔄 CORRECTED [2026-07-22]: the "~0 scans / flopped" read below was WRONG — I
> was looking at the page-path report (/welcome) instead of source/medium.
> GA4 Traffic-acquisition (Jun 15–Jul 20) shows **welcome / mailer = 21
> sessions** (of 155 total). That's ~8% of the 250 pieces — well above the
> 1–2% direct-mail norm. **The mailer WORKED.** (Tagged traffic landed on the
> homepage, which is why /welcome page-path looked empty.) Also that window:
> direct/none 68 · welcome/mailer 21 · m.facebook.com/referral 20 ·
> google/organic 16. Facebook pulled 20 with little posting = cheap upside;
> direct 68 = word-of-mouth/brand is the biggest driver.
- [2026-07-20] **250 pieces** sent to a **highly targeted list** (Jake's count).
- [2026-07-20] GA4 (page path, Jun 15–Jul 20): **`/welcome` did not register** —
  below `/game.html` (3) and `/index.html` (2), i.e. ~0–2 views. So ~0 trackable
  QR scans from the drop.
- [2026-07-20] `/welcome` URL confirmed **live/working** (inmagent.com/welcome →
  HTTP 200; GitHub Pages serves welcome.html at the clean path). The zero is real
  traffic, not a broken link.
- [2026-07-20] Site overall in that window: 292 views (homepage 120, diy 42,
  market-report 33, work 33) — traffic exists, just not from the mailer.

### The /welcome landing (mailer destination)
- [2026-06-24] Full advocate-pitch welcome block with bear logo, sticky Home
  banner, contact buttons.
- [2026-06-26] **20%-off Home Tune-Up** floating offer banner pinned to top
  (earlier iteration was 15%). Live on `/welcome` and `work.html`.

### Paid + analytics
- [2026-05-08] GA4 conversion tracking site-wide. [2026-05-15] `/thank-you.html`
  for Google Ads conversion tracking; ad-ready renders (square/landscape/portrait).
- [2026-06-08] Three social-media post images; earlier social images too.

### On-site conversion pieces
- [2026-05] `market-report.html` (Spokane fair-market pricing — the FMV proof),
  `work.html` (portfolio/proof zone), `game.html` (lead game, 3 plays/day, with a
  "skip the game — book directly" shortcut), `upload.html` (quote upload / contract
  audit).
- [2026-06-03] Home Tune-Up strapline **"Inspect · Seal · Clean · Report."**

### In-app browser rescue
- [2026-06-19] `inma-fb-rescue.js` — shared banner telling users in
  Facebook/Instagram in-app browsers to open in Safari/Chrome (those browsers
  can't do print/PDF or signature canvases).

## IDEAS & DIRECTION (thinking — not yet fact)
- [2026-07-10] The offer board is itself a contractor-acquisition channel (free to
  apply, credential gate) — not just homeowner-facing marketing. See [[offer-board]].
- [2026-07-20] **Mailer read (Jake + Claude):** 250 pieces is too small a sample
  to judge from QR scans, and QR is the highest-friction ask on a postcard. Mail
  converts on **calls/typed URLs and repetition**, which GA4 can't attribute (a
  phone call is invisible). So ~0 scans ≠ ~0 value. Jake: "there's value in the
  idea, gotta keep after it." Levers to try: (1) lead the CTA with **call/text +
  offer**, QR secondary; (2) **repeat** to the same 250 in 3–4 wks; (3) add a
  **"mention this card"** code so a phone call becomes countable; (4) **UTM** the
  QR so scans label as "mailer" in GA4. Not yet acted on.

## Superseded
- 🔄 UPDATED [2026-07-10]: Home Tune-Up mailer offer was **15% off** initially
  (2026-06-24) → bumped to **20% off** (2026-06-26).
