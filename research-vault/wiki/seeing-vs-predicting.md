# Seeing vs predicting price movement — the capstone

The sentence to read before building the next clever visualization. Answers Jake's real question behind the
whole median-line / fan / brain / follow-the-money arc (2026-07-18/19): *can we see in real time where price
is moving, and how reliable is that movement as a predictor?*

Related: [[where-the-edge-is]] (the structural conclusion), [[how-to-get-paid]], [[rotation-stickiness]],
[[median-line-dip]], `tools/sector_brain.ipynb`, `tools/follow_the_money.ipynb`.

## The two-part answer (THESIS — but evidence-backed below)
1. **Seeing WHERE price is moving = solved, free, real-time, and therefore edgeless.** Relative-strength ratios,
   sector heatmaps, the sector-brain network all show it instantly. No edge, *because* everyone sees the same map
   → it's already in the price.
2. **Movement as a DIRECTION predictor = weak-to-zero.** Public current movement is already priced, so it carries
   almost no forward edge about *which way next*. Daily return autocorrelation ≈ 0 ([[bull-bear-ledger]] /
   `top10_band_test`). The market is a near-random walk in the short run *by construction*.

## The reliability hierarchy — what price movement predicts (worst → best)
- **Next move's direction:** ~zero. Near-random. The layer most retail tools pretend to crack.
- **Short-term mean reversion (days):** weak, regime-dependent. Works in ranges, dies in trends (mega-caps trend;
  dips continued in `top10_band_test`).
- **Momentum (3–12mo):** real but small, crowded, decaying — a *factor premium* (paid for crash risk), not a free
  lunch.
- **Correlation / regime persistence:** medium. Stress (and coordinated moves) cluster for a few days.
- **Volatility / MAGNITUDE:** HIGH — the one reliable thing. Big moves cluster; today's vol forecasts tomorrow's.
  **Price movement reliably predicts SIZE, coin-flips DIRECTION.** This is *why* the vault's edge is VRP /
  vol-selling gated by regime ([[where-the-edge-is]]) and not direction prediction.

## The real-time penalty (THESIS)
Real-time is the WORST signal-to-noise you'll ever have: the most recent move is the least-confirmed. Reliability
only appears *with confirmation/persistence* — and by then it's neither real-time nor news. This is structural,
not a tooling gap you can engineer around.

## DATA — the sector-brain run that confirmed it (Jake, SPY/sectors, Jan 2025 → 2026-07-17)
- **Magnitude-not-direction, printed:** **XLE and XLK top BOTH the leader AND laggard frequency lists** (XLE 86
  lead / 66 lag; XLK 78 / 58). The highest-magnitude sectors are most often the best AND the worst — size is
  where they live, direction is a coin flip.
- **⚠️ Leadership "persistence" was a NULL-MODEL ARTIFACT (correction to the tool, 2026-07-19).** The notebook
  first reported 14% vs a naive 1/N = 9% null → "+5% momentum." But leadership is concentrated (XLE 22%, XLK 20%
  of days), so the correct **concentration-adjusted null = Σpᵢ² ≈ 13.0%.** Observed 14% vs 13% = **+0.6σ = noise.**
  **Sector leadership does NOT persist day-to-day beyond what concentration explains.** Tool null fixed to Σpᵢ².
- **Connectedness ≠ crash:** the 5 most-"wired" days (avg_corr ~0.84) were all late-April-2025 and tagged **BROAD
  risk-ON** (breadth 90-100%) — the rebound off the tariff crash. Correlations went to 1 on the way UP. "Everything
  correlates" = a big *coordinated* move, direction-agnostic — magnitude again, not sign.
- **Noise is the base rate:** 208 of 384 days (54%) tagged "mixed/quiet."

## THESIS — the synthesis (why the book is built the way it is)
Every viz we built *shows WHERE* (free) and none reliably *predicts DIRECTION*. The only reliable prediction from
price movement is **magnitude** — and that is the edge the book already harvests (VRP / the wheel, regime-gated by
the 200-day). **You can't predict the direction of the fire; you can reliably predict the building is flammable, and
get paid to insure it.** Use real-time movement for **regime/context** (risk-on/off, where the stress is), never as
a direction signal. This is the lens to apply to the *next* clever tool before expecting it to forecast direction:
it won't — but it will tell you the weather, and weather sizes the vol you sell.
