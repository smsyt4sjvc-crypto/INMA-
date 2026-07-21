# measure-tool-product — gate Wall Measure & charge contractors

> Idea logged 2026-07-21 (Jake): once mastered on real jobs, gate the Wall
> Measure tool and charge contractors for it. Comp: Hover at ~$150/job.

Related: [[architecture]] · [[offer-board]] · [[evolution]] · [[state]] · [[brand]]

## DATA (what's true now)
- [2026-07-21] The tool exists and is deep: photo-first flow, gable geometry
  from base+pitch (per-gable override), siding-standard presets (window 5×4 /
  door 3×7 3-side casing, belly band 5/4×8 auto-Z, frieze = soffit run ÷2 for
  the 5/4×4 rip), header/Z-flash math, learning trim library, IndexedDB photo
  persistence, vCard import, branded print. See [[architecture]].
- [2026-07-21] Hover (hover.to) charges contractors roughly $85–150 per
  measured job; per-job measurement spend is a normal contractor expense.
- [2026-07-21] As built it CANNOT be gated: static HTML on a public GitHub
  Pages repo — source is one View-Source away. Jake's Vercel account (already
  hosting the AI functions) is the natural home for a gated version.

## IDEAS & DIRECTION (thinking — not yet fact)
- [2026-07-21] Positioning: NOT a Hover replacement (it doesn't measure from
  photos) — it's the **siding takeoff brain**: trade-correct math + order
  sheet. Price accordingly: ~$20–30/mo unlimited or small per-job fee, pitched
  against one $150 Hover job.
- [2026-07-21] Two-tier fits the existing funnel: **free for INMA's vetted
  network** (perk that makes the [[offer-board]] network sticky) · **paid for
  everyone else** (revenue + recruiting magnet).
- [2026-07-21] Brand caution: paid pro version likely wants a neutral product
  name — contractors may balk at running numbers through the homeowner
  advocate's branded app. Free-tier INMA branding is fine goodwill.
- [2026-07-21] Needed to charge: accounts + Stripe + private serving (Vercel);
  later, cross-device sync/backup (first thing paying users will ask for).
- [2026-07-21] Sequencing (Jake's call): master it on real jobs first — dogfood
  is the QA and the demo. First customers could be offer-board applicants.
- [2026-07-21] **Jake's v0 gate idea: rotating URL, pay-as-you-go** ("change the
  URL a digit daily, charge for the day's link"). Viable with two patches:
  (1) paid file must live OUTSIDE the public repo — file lists + rename history
  are visible there; use a separate PRIVATE repo deployed on Vercel;
  (2) rotate a RANDOM slug, not an incrementing digit (guessable). Then:
  Stripe payment link + manually texting the day's link = zero-infra v0.
  Browser storage is origin-scoped, so customers' drafts survive daily URL
  changes. Accepted leak: payers can share the day's link — tolerable at
  validation scale. Ladder: v0 manual → v1 auto-rotate slug → v2 real accounts
  if demand proves.
- [2026-07-21] **Timed-access tiers** (Jake: "they're paying for timed access"):
  each horizon = its own route on its own rotation clock — day pass (~$10–15,
  rotates nightly), week pass (~$35–50, rotates Mondays; a siding job ≈ a week,
  the natural unit), month pass (~$75–100, rotates the 1st, best-value anchor),
  network tier free/rarely-rotated for vetted crews. One Stripe payment link
  per tier. Leakage scales with horizon → sell day/week to strangers, keep
  month semi-invite until real accounts. Under v2 accounts, a tier is just a
  license expiry date — the structure carries over unchanged. Drafts are
  origin-scoped so an expired customer keeps their job history: renewal hook.
- [2026-07-21] Status: NOT building yet — Jake mastering it on real jobs first.

## Superseded
- (none yet)
