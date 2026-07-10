# offer-board — the public jobs board at /offers/

> One concept: how INMA posts fully-scoped, fixed-price jobs for contractors to
> apply to. Detail + history live here; the current snapshot lives in [[state]].

Related: [[state]] · [[_calibration]]

## DATA (observed)
- [2026-07-10] Model: Jake scopes a full job, exports a self-contained offer HTML
  from `field-estimate.html` ("Export Offer Page"), uploads it to the `/offers/`
  folder on GitHub. The board (`offers/index.html`) reads the folder live via the
  GitHub contents API and renders a card for every `offer-*.html`. No spreadsheet.
  Source: commits on `main`, 2026-07-10.
- [2026-07-10] Each offer page carries its own Apply form. Submissions email Jake
  via Formspree (`xgollken`); contractor photos upload to ImgBB. Every application
  is stamped with the job number. Source: `field-estimate.html` exporter.
- [2026-07-10] Contractors **accept** the posted fixed price as-is — no bidding,
  no negotiating the homeowner's terms. Gate = credentials (license, bond,
  insurance) + references/photos; it is **free** to apply, not pay-to-play.
  Source: repo-root `CLAUDE.md` money-model discussion + this session.
- [2026-07-10] Homeowner name & full street address are **not** shown publicly;
  the card shows city only. The exporter parses city from the address and never
  emits the street line. Source: `field-estimate.html` `buildOfferPageHTML`.
- [2026-07-10] Confirmed working end-to-end with a photo dry-run offer
  (`offer-INMA-20260710-132.html`) that appeared on the board, then was cleared.
  Two earlier uploads landed as empty commits (nothing to show). Source: git log.

## THESIS (interpretation — NOT fact)
- [2026-07-10] The mechanical pipeline works, but the **business loop is unproven**:
  no real homeowner has retained + no real contractor application has landed in
  Jake's inbox from a live posted job. Verifying that full loop (post a real
  offer → contractor applies → email arrives → Jake forwards to homeowner) is the
  open item.
- [2026-07-10] Empty-upload risk: GitHub's web upload can silently commit nothing
  if "Commit changes" isn't pressed or the file lands at repo root. Worth a
  standing habit of eyeballing `/offers/` after each upload until Jake trusts it.
  Ties to [[_calibration]] "it shipped = it works."

## Falsified
- (none yet)
