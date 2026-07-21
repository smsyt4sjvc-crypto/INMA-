# state — canonical truth, right now

> THE single snapshot of what is actually true this moment. Only verified reality
> lives here — nothing speculative. When reality changes, this file is corrected
> **first**, then the detailed note gets its dated correction. Last full review
> date is tracked at the bottom.

Related: [[_persona]] · [[_guardrails]] · [[architecture]] · [[positioning]] · [[brand]] · [[evolution]] · [[decisions]] · [[marketing]] · [[door-knock-thermal]] · [[showcase-clients]] · [[side-projects]] · [[offer-board]]

## DATA (observed) — Business
- [2026-07-10] INMA = homeowner-advocacy / buyer's-agent service for exterior
  remodels. Owner: Jake Bishop, Spokane WA. Fee 10–15% of the offer, paid by the
  homeowner, carved out of the offer as a contract debit. INMA is not a contractor.
  Source: repo-root `CLAUDE.md`.
- [2026-07-10] Contact: (509) 251-7792 · jake@inmagent.com · inmagent.com ·
  WA UBI #606 027 063. Source: repo-root `CLAUDE.md`.

## DATA (observed) — Site & tools (live on inmagent.com, GitHub Pages, main)
- [2026-07-10] `estimate.html` — Offer Sheet Builder. Autosave + vCard import +
  INMA fee block + notes page 2. Live.
- [2026-07-10] `field-estimate.html` — Contractor Package Builder. Now has
  autosave, a "+ New" button, reliable Back buttons on generated views, iOS
  octet-stream export, and "Export Offer Page" that embeds card metadata. Live.
- [2026-07-10] `service-agreement.html` — Service Agreement builder with on-screen
  signature pads + autosave + vCard import. Live.
- [2026-07-10] `estimate-blank.html` — blank Fair Market Estimate form. Live.
- [2026-07-21] `measure.html` — Wall Measure tool, photo-first: snap walls (any
  number of photos per wall, filename → wall label on Files import) → detail
  each while viewing its photos: sizes, gables as base×rise×count, openings,
  per-wall trim (LF by type/stock size, auto-suggested from dims), materials
  via accessory chips → combined rollup (square/gable SF segregated, trim
  merged by type+size) + totals + print. Photos auto-compress (~1600px) so
  drafts persist for days; .vcf contact import fills the job header. Live.
- [2026-07-10] `/offers/` — Offer board. Auto-lists every `offer-*.html` uploaded
  to the folder by reading the public GitHub contents API (no spreadsheet).
  Caches last-good load. Cleared to empty on 2026-07-10 for a clean start. Live.
  See [[offer-board]].
- [2026-07-10] Offer pages carry a built-in Apply form → emails Jake via Formspree
  (`xgollken`) with photos via ImgBB. Accept-checkbox iOS render bug fixed
  2026-07-10. Source: this session's commits on `main`.

## DATA (observed) — Session pickup
- [2026-07-10] Root `CLAUDE.md` (auto-loads every session) has a "READ FIRST"
  pointer at the top directing a new session to read `vault/CLAUDE.md` then this
  file. So a fresh chat picks up the running memory automatically — no need to
  paste or remember a kickoff line.

## DATA (observed) — Pipeline
- [2026-07-10] Offer board is empty (test files cleared). No live real offers
  posted yet. No contractor applications recorded in the vault yet.

## IDEAS & DIRECTION (thinking — not yet fact)
- [2026-07-10] The self-upload offer pipeline (build → export → upload to
  `/offers/` → auto-lists) is confirmed working end-to-end via a photo dry-run,
  but has **not** yet been proven with a real homeowner + real contractor
  application landing in Jake's inbox. That full live loop is the next thing to
  verify. → tracked in [[offer-board]].

## Falsified
- (none yet)

---
_Last full review: 2026-07-10_
