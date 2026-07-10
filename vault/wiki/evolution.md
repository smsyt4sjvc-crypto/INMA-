# evolution — running log of how INMA has changed

> The timeline, newest era at top. Append the *meaningful* shifts, not every
> commit. Backed by the full git history (2026-05-08 → present).

Related: [[state]] · [[architecture]] · [[decisions]] · [[marketing]] · [[offer-board]] · [[showcase-clients]] · [[side-projects]] · [[positioning]]
Source: [[2026-07-10-git-history-ingest]] · [[2026-07-10-inma-baseline-ingest]]

## DATA (what happened)

### Jul 2026 — the offer-board era
- [2026-07-10] Shipped the **auto-listing offer board** (`/offers/`): export an
  offer page, upload it, it appears — no spreadsheet. Replaced the earlier
  Google-Sheet-driven board. Proven with a photo dry-run, then cleared clean.
  See [[offer-board]].
- [2026-07-10] Hardened all builders for the field: autosave, "+ New", reliable
  Back buttons, iOS octet-stream export, vCard import; fixed an iOS accept-checkbox
  render bug.
- [2026-07-09] Reworked the old dual field estimator into the **Contractor Package
  Builder** (AI generation removed); added "Export Offer Page" (offer HTML with a
  built-in Apply form → Formspree email + ImgBB photos, job-number-stamped).
- [2026-07-06] **CLAUDE.md business brain** created, then sharpened: money model +
  §3a operational model, §8a document brand kit. Estimate → **Offer Sheet**
  (INMA fee block, autosave, contact import). Permitting footnote added.
- [2026-07-10] Stood up this **vault** as INMA's persistent memory.

### Jun–Jul 2026 — tools, forms, and going GC-safe
- [2026-07-05] On-screen **signing** on the agreement; **dropped all required-field
  blocking** (every doc generates blank to fill by hand); notes → page 2 of the
  estimate; added `estimate-blank.html`; retired `/agreement.html` (redirect).
- [2026-06-17] `service-agreement.html` builder shipped: Import from Contacts,
  signature pads. Fixed the script-killing nested `</script>` bug and the iOS PWA
  logo. See [[decisions]].
- [2026-06-13] `estimate.html` 2-step builder shipped: stripped
  signatures/validity/permits language; disclosure reframed to "INMA presents this
  as **YOUR** offer"; bear logo inlined as base64 (fixed broken image).
- [2026-06-08/10] **GC-safety + rebrand**: reframed How-It-Works to buyer's-agent
  language; added the Leverage Flip section and the Four Ways tier menu (10–15%);
  **renamed "Your Remodeling Agent" → "Homeowner Advocate."**

### May–Jun 2026 — launch, marketing, and copy
- [2026-06-01/03] De-seasonalized Home Tune-Ups (year-round); added the
  **"Inspect · Seal · Clean · Report"** strapline; game tweaks (3 plays/day,
  skip-to-book).
- [2026-05-15] `/thank-you.html` for Google Ads conversion + ad-ready renders.
- [2026-05-08/09] **Site launch era**: GA4 tracking site-wide; homepage bio + copy
  passes (Reality section, FMV-as-truth, About/CTA); windows card with Jake's
  14-yr McVay Brothers / Coeur d'Alene Window history + Avista rebate; **EDDM
  mailer artwork** (3 PNGs + QR + build script); tool PWAs with custom letter
  icons. See [[marketing]].

## IDEAS & DIRECTION (what's next / being considered)
- [2026-07-10] Prove the **full live business loop**: real homeowner retained →
  real offer posted → real contractor application in Jake's inbox → forwarded.
  Mechanics work; the loop is unproven. Tracked in [[state]].
- [2026-07-10] Client-site business ([[showcase-clients]]) could become a
  repeatable product line if demand holds.

## Superseded
- 🔄 UPDATED [2026-07-10]: Earlier vault version of this note only covered Jul 2026.
  Extended back to launch (2026-05-08) from the full git history.
