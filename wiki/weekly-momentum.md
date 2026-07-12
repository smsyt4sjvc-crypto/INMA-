# Weekly Momentum Study — NDX top-5 weekly winners: carry, duration, threshold (2026-07-12)

Jake's question: "each week's top 5 pure returns (Mon open - Fri close), follow them the next week —
does momentum carry? For how long? Is there a threshold of initial return that suppresses forward
momentum?" Cell in chat 2026-07-12 (2016-present, alpha vs NDX-universe weekly average).
Related: [[runner-anatomy]], [[retail-edge]] (mechanisms-vs-parameters), [[_calibration]].

> Firewall: pre-registered BEFORE the run. Literature context (tier-3): 1-week horizon = the documented
> SHORT-TERM REVERSAL zone (Jegadeesh/Lehmann), not momentum (3-12mo formation); the effect is weakest/
> most-arbitraged in mega-cap liquid names; earnings-driven pops drift (PEAD), flow-driven pops revert.

## PRE-REGISTERED HYPOTHESES
- **H1:** Top-5 weekly winners carry ZERO-to-NEGATIVE next-week alpha vs the NDX average.
- **H2:** The threshold exists and is nonlinear: initial pops >+10% reverse harder than +2-6% pops
  (Jake's suppression intuition = the documented overreaction tail).
- **H3:** Any positive carry appears only at 3-4 week holds, not week one.
- **H4:** Bottom-5 losers BOUNCE next week (reversal stronger on the loser side).
- Regime block: effect expected weaker/flatter post-2023 (arbitrage + 0DTE-era flows) — the
  "mechanisms travel, parameters don't" doctrine tested live.
- ⚠️ Limits: survivorship (current roster backward); Mon-open→Fri-close convention ignores overnight
  weekend gaps between signal and entry; costs/slippage not modeled (5 names/week = high turnover —
  even positive alpha must clear ~0.1-0.2%/wk friction to be tradeable).

## RESULTS (run 2026-07-12, Jake's Colab — 549 weeks, 99 names, 2,725 top-5 events)
### DATA
- Week+1 alpha: **mean +0.05%, median −0.22%, win 48%.** Week+2: +0.13/−0.13/48%. Week+3: +0.16/+0.01/50%.
  Week+4: +0.40/+0.07/51%. (Per-week alphas; 4-week sum ≈ +0.74% BEFORE costs.)
- Threshold buckets (week+1): +2-5%: +0.14/−0.22/46% | +5-10%: −0.33/−0.32/46% | **+10-20%:
  +0.33/+0.13/51% (best bucket)** | **>+20%: mean +0.34 but MEDIAN −0.79, win 45%** (lottery skew:
  most fade, a few huge continuations drag the mean).
- Bottom-5 week+1: +0.20/−0.10/49% — no bounce.
- Regime: 2016-19 −0.00% | 2020-22 +0.03% | 2023-now +0.14%; win 47-49% in ALL eras.

### HYPOTHESES GRADED
- **H1 — CONFIRMED (as ZERO, not reversal):** no carry, no meaningful fade. Mean ~0, median slightly
  negative, coin-flip win rates. **The NDX is efficient at the weekly horizon — there is nothing here,
  in either direction.**
- **H2 — PARTLY, and non-monotonic:** suppression exists but only ABOVE ~+20% (median −0.79%, 45% win —
  the overreaction tail Jake predicted); the +10-20% bucket actually carried best (+0.13 median, 51% —
  likely earnings-gap/PEAD names). Moderate-big pops drift faintly; extreme pops fade; all magnitudes
  sub-cost.
- **H3 — WEAKLY CONFIRMED in direction, useless in size:** alpha grows with hold distance (wk4 best)
  but the 4-week sum (+0.74%) dies after ~0.1-0.2%/wk turnover friction.
- **H4 — REJECTED:** losers don't bounce. Reversal is as dead as momentum here.
- **Regime block:** no era had an edge — this wasn't arbitraged away recently; it's been flat since
  at least 2016 in mega-caps. Parameters AND mechanism absent at this cap size/horizon.

### THE VERDICT (what the study is FOR)
**Chasing weekly NDX leaders has zero expectancy before costs and negative after — in every era, at
every threshold.** The skew detail is the trap's anatomy: means > medians everywhere = rare big
continuations subsidize many small fades; the chaser eats the median, not the mean. This KILLS a whole
temptation class ($0 tuition, like the dip-buy study). Where edges actually measured out in our own
work, for contrast: small caps, panic windows, insider clusters, months-scale holds — never
mega-cap-weekly. Documented momentum lives at 3-12 MONTH formation; if the itch persists, that's the
horizon to test next.
