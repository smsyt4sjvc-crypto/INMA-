# architecture — the running technical system

> How INMA's site and tools are actually wired, right now. One place to remember
> where things live and how data flows, so no session re-discovers it.

Related: [[state]] · [[offer-board]] · [[brand]] · [[evolution]]
Source: [[2026-07-10-inma-baseline-ingest]]

## DATA (what's true now)

### Hosting & repo
- [2026-07-10] Site is a **static site on GitHub Pages**, served from the `main`
  branch of `smsyt4sjvc-crypto/INMA-` (public repo) at **inmagent.com**. Pushing
  to `main` publishes; allow ~30–60s for Pages to rebuild.
- [2026-07-10] Domain registered at **Namecheap** (Jake's). Repo also has a Vercel
  deployment (`inma-five.vercel.app`) used for AI quote-analysis functions.
  Analytics: GA4.

### Public pages
- [2026-07-10] `index.html` (home), `work.html` (portfolio), `market-report.html`
  (Spokane fair-market pricing), `diy.html`, `consult.html`, `game.html`,
  `welcome` (mailer QR landing), `upload.html` (quote upload / contract audit),
  `contractor.html` (how working with INMA works).

### Internal tools (PWA-savable)
- [2026-07-10] `estimate.html` — Offer Sheet Builder (icon E).
- [2026-07-10] `field-estimate.html` — Contractor Package Builder (icon I); exports
  the contractor package + the self-contained offer page.
- [2026-07-10] `service-agreement.html` — Service Agreement builder (icon S), with
  signature pads.
- [2026-07-10] `estimate-blank.html` — blank Fair Market Estimate form.
- [2026-07-20] `measure.html` — **Wall Measure**, photo-first flow: snap every
  wall, then detail each one while looking at its photo (L×H + gable − openings,
  per-wall materials with one-tap accessory chips), then a combined rollup —
  identical items merged across walls + general lines (chips drop measured
  SF/LF in) → subtotal/tax/total + branded print sheet.
- [2026-07-10] All builders autosave to `localStorage` and have a "+ New" reset.
  Print outputs use `window.open('','_blank')` + `document.write` (must be
  synchronous from the click for iOS Safari) and carry Back buttons.

### Offer board data flow (no server)
- [2026-07-10] `offers/index.html` lists jobs by reading the **GitHub contents
  API** for the `/offers/` folder (public repo → no login), filtering
  `offer-*.html`, then fetching each file same-origin to read a
  `<script id="inma-offer-meta">` JSON block (type/city/price/scope). Falls back
  to a localStorage cache if the API is unavailable. Detail: [[offer-board]].
- [2026-07-10] Each exported offer page has a built-in Apply form → **Formspree**
  (`xgollken`) emails Jake; contractor photos upload to **ImgBB** (key
  `6bb4711623a05b2eb589a1d7cf3302f9`). Stamped with the job number.

### Integrations in play
- [2026-07-10] Formspree (form→email), ImgBB (client-side image host), Google
  Fonts, GA4, `inma-fb-rescue.js` (in-app-browser "open in Safari" banner).

### Repo branch landscape (checked 2026-07-21)
- [2026-07-21] Jake deleted a batch of old remote branches thinking they were
  stale uploads. **Audited: every deleted branch was fully merged into `main` —
  nothing was lost.** (Squash-merged PR branches show as "not merged" to git
  ancestry checks but their content is on main.)
- [2026-07-21] **`claude/sp500-intraday-low-timing-286y2r` is Jake's TRADING
  vault** (the other project), living as an unmerged branch in this same repo —
  active daily commits. **Never delete or merge this branch.**
- [2026-07-21] `archive-pre-may-2026-history` — new archive branch pointing at
  the old `claude/chat-v3-cw7r4` tip: the repo's **original Feb–Apr 2026
  history** (first site iterations, Review.html, game, consult tool, original
  AI field estimator, the $150 thermal-report CTA). Main's rewritten history
  starts 2026-05-08; this branch is the only copy of what came before. Keep.
- [2026-07-21] Remaining old feature branches (welcome-*, elliott-*, ioss-…) are
  all squash-merged into main — safe to delete anytime, no urgency.

### Accounts & ownership
- [2026-07-10] Domain **inmagent.com** registered at **Namecheap** (Jake's).
- [2026-07-10] Code + hosting: GitHub repo `smsyt4sjvc-crypto/INMA-` (public),
  served by **GitHub Pages** off `main`. **Vercel** deployment for AI functions.
- [2026-07-10] Client sites ([[showcase-clients]]) get their own GitHub repo +
  domain, owned by the client on payment; Jake holds credentials for management
  unless they ask for them.
- [2026-07-10] More public pages beyond the marketing set: `/thank-you.html`
  (Google Ads conversion), `contractor.html` (how working with INMA works).

## IDEAS & DIRECTION (thinking — not yet fact)
- [2026-07-10] The board depends on GitHub's unauthenticated API rate limit
  (60/hr per visitor IP). Fine at current traffic; if the board ever gets busy,
  revisit (cache harder, or generate a static index on upload).

## Superseded
- 🔄 UPDATED [2026-07-10]: The offer board originally read a **Google Sheet CSV**
  and showed sample offers. Replaced with the auto-listing GitHub-API approach so
  Jake just uploads a file and it appears — no spreadsheet. Source: commit
  `cd59348`.
