# decisions — calls made, and why

> The reasoning behind the choices that shaped INMA, so we don't relitigate them.
> Each is a settled call with its rationale. If one reverses, mark it Superseded —
> don't delete it.

Related: [[positioning]] · [[_guardrails]] · [[offer-board]] · [[architecture]] · [[evolution]]
Source: [[2026-07-10-git-history-ingest]] · build sessions

## DATA (decided)

### Positioning & liability
- [2026-06-10] **"Homeowner Advocate," not "Remodeling Agent."** Cleaner, avoids
  implying INMA is part of the crew. Rebrand applied site-wide.
- [2026-06-08] **Buyer's-agent framing everywhere, GC-safe.** How-It-Works and all
  copy reworded so INMA never reads as controlling/guaranteeing the work — that
  would create general-contractor liability. The licensed contractor is
  responsible for the work. Enforced by [[_guardrails]].
- [2026-06-13] **The estimate is the homeowner's "offer," not a binding bid.**
  Disclosure reframed to "INMA presents this as YOUR offer." Stripped
  signatures/validity/hidden-conditions/permits from the estimate doc.

### Money
- [2026-07-06] **Money is one-directional: homeowner pays INMA's fee upfront.**
  Contractor's number is already net of the fee (the "contract debit"); INMA never
  collects/holds/disburses construction funds. Chosen deliberately to keep INMA
  clear of GC/fiduciary exposure. ("I gotta be careful how I accept money.")
- [2026-07-06] **Fee shown in the open, deducted dollar-for-dollar**, not added on
  top — homeowner's total cost doesn't increase. Permitting kept in the
  contractor's terms via a footnote so the homeowner doesn't feel gouged.

### Offer board & contractor gate
- [2026-07-10] **Self-upload over a Google Sheet.** Jake is fluent uploading files;
  the board auto-lists `offer-*.html` from the repo via the GitHub API — no
  spreadsheet dependency. See [[offer-board]], [[architecture]].
- [2026-07-10] **Contractors ACCEPT a fixed price — they don't bid.** The homeowner
  picks from qualified applicants. Keeps it "the homeowner's offer," not a reverse
  auction.
- [2026-07-10] **Contractor gate is credential-based and FREE, not pay-to-play.**
  License + bond + insurance required, plus references/photos. Free-to-apply chosen
  over pay-to-play to avoid taking money from contractors (liability) and to give
  the homeowner equal packages.
- [2026-07-10] **Photos/references encouraged, not required** — framed as "a
  complete application improves your odds," so applying is low-friction but strong
  applicants stand out.

### Tools & UX
- [2026-07-05] **No forced/required fields anywhere** — every document generates
  blank so Jake can fill by hand on-site and move freely.
- [2026-06-13] **Logos embedded (base64) or served from `/bear-logo.jpg`** — plain
  cross-origin URLs fail in iOS PWA/about:blank print contexts.
- [2026-07-05] **Notes page is page 2 of the estimate print**, not a standalone
  page (removed `/notes.html`).

## IDEAS & DIRECTION (unsettled)
- [2026-07-10] Homeowner fee mechanics floated as "$300 upfront OR deduct the full
  ~12%" — confirm the final numbers before baking into copy. See [[positioning]].

## Superseded
- 🔄 UPDATED [2026-07-10]: Offer board was first built **Google-Sheet-driven**
  (2026-07-09). Superseded by self-upload auto-listing (2026-07-10) once it was
  clear Jake would rather upload a file than maintain a sheet.
