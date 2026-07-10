# evolution — running log of how INMA has changed

> The timeline. Append here as the business and tools evolve, newest at top. Not a
> changelog of every commit — the *meaningful* shifts in how INMA works.

Related: [[state]] · [[architecture]] · [[offer-board]] · [[positioning]]
Source: [[2026-07-10-inma-baseline-ingest]]

## DATA (what happened)

### 2026-07 — the offer-board era
- [2026-07-10] Shipped the **auto-listing offer board** (`/offers/`): Jake exports
  a self-contained offer page, uploads it to the repo, and it appears on the board
  automatically — no spreadsheet. Replaced an earlier Google-Sheet-driven board.
  Pipeline proven with a photo dry-run, then cleared for a clean start.
  See [[offer-board]], [[architecture]].
- [2026-07-10] Reworked the old dual "field estimator" into a **Contractor Package
  Builder** (`field-estimate.html`): dropped the AI generation, added wall-by-wall
  photos+notes, line items, and "Export Offer Page" (offer HTML with a built-in
  Apply form → Formspree email + ImgBB photos, job-number-stamped).
- [2026-07-10] Hardened all builders for field use: **localStorage autosave**,
  **"+ New"** reset, reliable **Back buttons** on generated views, iOS
  octet-stream export ("Save to Files"), and vCard contact import. Fixed an iOS
  accept-checkbox render bug on offer pages.
- [2026-07-10] Renamed "Estimate" → **Offer Sheet**; added the INMA fee block
  (Subtotal → INMA Services % → New Subtotal → Sales Tax → Contractor Total) and a
  permitting footnote so contractors don't feel gouged.
- [2026-07-10] Added on-screen **signature pads** to the service agreement;
  consolidated duplicate agreement pages (old → redirect); made the notes page
  **page 2 of the estimate print**.
- [2026-07-10] Stood up this **vault** as INMA's persistent memory.

### Earlier this cycle (2026, pre-board)
- [2026-07] Marketing push around the homeowner-advocate pitch and fair-market
  framing ("cheapest isn't best, most expensive isn't best"). Built the `/welcome`
  mailer QR landing + a 20%-off Home Tune-Up offer banner; rebuilt the mailer back
  around the postage cutout.
- [2026-07] Side projects: `ioss.html` (policy proposal), `sim.html` ("Reality
  Check" simulator), `/showcase/` client-site demos (Right Now Exteriors, Elliott
  Elite Detailing).

## IDEAS & DIRECTION (what's next / being considered)
- [2026-07-10] Prove the **full live business loop**: a real homeowner retained →
  real offer posted → real contractor application lands in Jake's inbox → he
  forwards it. Mechanics work; the business loop is unproven. Tracked in [[state]].
- [2026-07-10] Client-site business (build → client owns it on pay) could become a
  repeatable product line if demand holds. See [[brand]].

## Superseded
- (none yet)
