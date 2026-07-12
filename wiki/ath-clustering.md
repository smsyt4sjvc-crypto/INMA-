# Record-High Study — do ATH clustering/spacing/droughts predict? (2026-07-12)

Jake's question: "record highs — if the distance between them, or if they cluster, and the time
distance between them, predict anything." Cell in chat 7/12 (^GSPC 1950-present).
Related: [[buying-at-highs]] (ATH ≈ average forward returns, already logged), [[market-fragility]],
[[retail-edge]] (mechanisms-vs-parameters).

> Pre-registered BEFORE the run. Literature context (tier-3): ATHs cluster in decade-scale regimes;
> the documented signal is DROUGHT-EMERGENCE (first ATH after a long dry spell = strong forward —
> 1980/2013-class breakouts); cluster ENDINGS are not identifiable in real time.

## PRE-REGISTERED HYPOTHESES
- **H1:** ATHs cluster far beyond random (quantify: share with another ATH within 30 prior days).
- **H2:** First ATH after >1yr drought = ABOVE-average forward 12m (the breakout effect).
- **H3:** ATH DENSITY (trailing-1y count) has little forward power — hot-count periods are mid-regime,
  not tops; expect no monotonic decay, possibly mild softness at extreme density but not tradeable.
- **H4:** Within-cluster spacing adds nothing; the information lives at drought-emergence only.
- ⚠️ Limits: index-level only (the [[buying-at-highs]] aggregation-artifact caveat applies — 2026's
  cluster rides on narrow leadership; density can't see breadth); 1950-present ≈ mostly two great
  ATH regimes, so n at the drought tails is small; forward windows overlap (autocorrelated samples).

## RESULTS (run 2026-07-12 — 19,251 days, 1,534 ATH closes = 8.0% of days)
### DATA
- All ATH days fwd-12m: **+9.8% mean / +10.8% median / 75% win** vs all-days baseline +9.4% —
  buying at highs ≈ average-or-slightly-better, now confirmed in our own run ([[buying-at-highs]] ✓).
- Gaps: median 2 days, mean 18, max 2,744 (7.5yrs). ⚠️ MY BUG: the printed "random ~239%" comparison
  was garbage math; correctly, iid-at-8% implies ~92% would have an ATH within 30 prior days — same
  as observed — so the 30-day stat does NOT demonstrate clustering. Clustering shows in the gap
  SHAPE (median 2 vs ~8 iid-geometric) and is partly MECHANICAL (post-ATH you sit at the max, so
  near-term repeats are definitionally likelier). H1 stands but weaker than the printout implied.
- **H2 — THE FINDING: first ATH after a 1-3 YEAR drought: n=11, mean +17.6%, median +14.1%,
  win 11/11 (100%).** Same effect from the density side: "first ATH in a year" n=16: +15.1%, 94% win.
  (>3yr breaks: n=4, +5.6% — poisoned by the 2007 break→GFC; too few to read.) These 11 events are
  decades-apart = a rare NON-overlapping clean sample.
- **H3 — CONFIRMED: density predicts nothing.** Hot (46+ ATHs/yr): +9.1%/75% ≈ baseline; no monotonic
  decay anywhere. "Too many highs" is not a top signal. Sparse (1-10, early-regime): best at +12.0%/85%.
- Context: latest ATH 2026-06-02 at density 59 (hot bucket = historically benign); current drought
  38 days — if a new high prints soon it lands in the 30-180d bucket (+7.3%/71%, slightly soft).

### GRADED
H1 PARTLY (real but partly mechanical; my comparison stat was wrong — logged per calibration).
H2 CONFIRMED STRONGLY. H3 CONFIRMED. H4 supported (cluster members ≈ baseline).

### THE KEEPER (standing rule derived)
**The drought-break entry: the first new ATH after a 1-3 year dry spell has been a 100%-win, +14-18%
fwd-12m signal across 76 years (n=11).** It fires ~once per 7 years — i.e., at the exit of the NEXT
bear market. Pairs with [[fear-duration]] rule 3 (episode-end = positive-expectancy re-entry) and the
[[runner-anatomy]] ignition window: three independent recovery detectors now aimed at the same future
moment. Density tells you nothing about when the current cluster dies; the aggregation caveat
(narrow-breadth 2026 cluster) stands unmeasured by this study.

## Part 2 — cluster LIFESPANS (run 2026-07-12; 16 clusters, 365d separator)
### DATA
- **Median cluster lifespan: 2.2 years** (range 0.4–5.5). Only two clusters ever exceeded 5 years
  (1995-2000, 2016-2022) — both ended in 20%+ bears.
- **Forward 12m by cluster AGE at the ATH print — NON-MONOTONIC with a mortality valley:**
  <6m: +14.8%/87% win | 0.5-1.5y: +10.5%/79% | **1.5-3y: +3.9% mean, +0.9% MEDIAN, 52% win (the
  danger zone)** | 3-5y: +10.9%/85% (survivors' second wind) | **5y+: −14.3%, 0% win (n=37 — the
  1999-2000 and 2021 blow-off tails).**
- Hazard: **P(cluster dies within a year | reached age 2) = 4/9 ≈ 44%** — the mortality peak
  (age 1: 10%; age 5: 2/2).
- **TODAY: the current cluster began 2024-01-19 — age 2.5 years, 120 highs, last high June 2,
  38-day drought running. Sitting in the exact center of the mortality valley.**
### GRADED (pre-registration went ~1-for-3 — the data beat the priors)
- H1 WRONG on duration: clusters are SHORTER than the "decade regime" framing — median 2.2y (the
  365d separator splits the long eras at their crashes, correctly).
- H2 WRONG in the useful direction: age DOES carry structure — not decay, a VALLEY at 1.5-3y.
- H3 PARTLY WRONG: the hazard curve has a real peak at age ~2.
### HONEST MECHANISM (before anyone panics)
The 1.5-3y valley is substantially DEFINITIONAL: if the median cluster dies at ~2.2y, then highs
printed at age 1.5-3 are, on average, near a death — their forward windows mechanically contain the
post-cluster drawdown. This is a BASE RATE (typical lifespan), not an age-curse. And the 3-5y bucket's
strength is survivorship: clusters that clear 3 are the great regimes — unknowable in advance which
kind this one is.
### THESIS
- **This is the first index-level study that AGREES with the internals evidence.** Density said benign;
  age says: 2.5-year-old cluster, 52% historical win rate on new highs from here, ~44% one-year
  cluster-mortality hazard — a coin flip, priced at all-time highs. Harmonizes with breadth (48% in
  drawdowns), the vol gap, insider distribution, and the two-bucket posture — without predicting a date.
- Milestones derived: (1) a fresh ATH before ~June 2027 keeps the cluster alive; surviving past age 3
  (Jan 2027+) historically flips the base rate friendly again (85% win). (2) If the current 38-day
  drought stretches past 365d, the cluster retroactively DIED June 2, 2026 — and the NEXT drought-break
  entry (the 11/11 signal from Part 1) goes on watch. The two studies chain: cluster death → drought →
  drought-break = the highest-conviction entry in the entire vault's arsenal.
