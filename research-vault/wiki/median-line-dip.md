# The median line as a dip trigger — study result

Tests Jake's "median price line" (a straight **median/LAD regression** through log-price, walk-forward, no
lookahead) as a dip-buy signal vs the 200d SMA, %-off-52w-high, and the 200d rolling median.
Tool: `tools/median_line_dip_study.ipynb`. Related: [[where-the-edge-is]], [[defense-not-offense]],
[[portfolio-state]] (the *rolling*-median regime jurisdiction — a DIFFERENT use, see note below).

> Firewall: DATA = the run's numbers. THESIS = the mechanism read + what it means for the book.

## DATA (observed — Jake's run 2026-07-18 ~9pm PT; ⚠️ TEST RUN, ~29 names / 72,906 name-days, 50% common support)
Matched-frequency (each signal fires on top 15% most-dipped name-days, common support). EDGE = median fwd
return minus all-days baseline. Survivorship-conditioned (current members followed back).

| horizon | MEDLINE edge | SMA200 | PCT_off_high | ROLLMED | winner |
|---|---|---|---|---|---|
| 21d (1mo)  | **+1.15%** | +0.27% | +0.07% | +0.47% | **MEDLINE** |
| 63d (3mo)  | **+1.35%** | −0.18% | −0.29% | −0.05% | **MEDLINE** (only positive) |
| 126d (6mo) | +2.51% | +1.99% | **+6.46%** | +1.63% | PCT |
| 252d (12mo)| +7.85% *(last)* | +13.61% | **+21.50%** | +12.31% | PCT |

Win rates: MEDLINE 60%/63% at 21/63d vs 54-56% for the rest. Per-name (fwd_63, matched 15%): **MEDLINE beats
SMA200 in 17/29 (59%), beats ROLLMED 17/29 (59%), beats PCT_off_high 13/29 (45%).**

## THESIS (interpretation — NOT fact)
- *(the finding — real but horizon-specific)* **The median line is a genuinely better SHORT-horizon (1–3 month)
  dip trigger** than the moving-average family. At 63d it is the ONLY signal with positive edge — buying below
  the SMA, below the rolling median, or X% off the high all UNDERperformed baseline at 3 months, while below the
  median line beat it (+1.35%). Per-name it beats SMA and rolling-median ~59% (not a pool artifact). At 1 month
  it's ~4× the next-best edge with a 60% win rate.
- *(the honest other half)* **At 6–12 months it loses, and at 12 months it's the WORST.** "% off the 52-week
  high" dominates the long horizons (+21.5% edge at 252d). Do not bury this — the median line is not a
  long-hold entry signal.
- *(mechanism — why the split, and it's coherent)* Each signal's *normalization* decides what it catches.
  **MEDLINE** = deviation from a robust trend, normalized by recent scale → fires on **shallow, fast-reverting
  dips inside uptrends** → pays quickly (1–3mo), fades as a 12mo signal. **PCT_off_high** = raw drawdown from the
  high → fires on **deep crashes** → for names that *survived to still be in the index today*, deep crashes
  resolve into huge 12mo rebounds. So MEDLINE = "buy the small dip while the trend holds"; PCT = "buy the deep
  crash and wait a year."
- *(⚠️ the survivorship flag points AT PCT's win, not MEDLINE's)* PCT's long-horizon dominance is the **most
  survivorship-contaminated cell in the table** — it's the signal that most directly exploits "deepest drawdown
  in a name that we KNOW survived → biggest rebound." MEDLINE's short-horizon edge is about oscillation around
  trend and is **less survivorship-dependent** → arguably the more transportable/real edge of the two. Read the
  table with that asymmetry: MEDLINE's win is cleaner than PCT's.
- *(why it fits Jake specifically)* Jake's stated lane is swing/mean-reversion, **NOT** 20-year buy-and-hold
  ("I'm 42, I need an edge in *trading*"). The horizon where the median line wins (1–3mo) is exactly his lane.
  The 12mo cell where it loses is the horizon he isn't trading. So the result is *better* aligned to the book
  than a flat "PCT wins" headline would suggest.
- *(does NOT invalidate the existing rolling-median jurisdiction)* [[portfolio-state]] uses the *rolling* median
  as a **regime filter** (invested/cash, judged by drawdown-avoidance / MAR — Faber-style), a different question
  than "forward return after a dip." ROLLMED looking mediocre HERE doesn't touch that use. Two different tools.

## Owed / next (before this becomes a standing signal)
1. **Full S&P run** (`LIMIT_NAMES=0`) — this was ~29 names; need the whole index + more per-name votes.
2. **LINE_METHOD robustness:** rerun `"lad"` vs `"theil"` vs `"ols"`. If the short-horizon edge holds as LAD/
   Theil but dies as OLS → the *robustness* (median-not-mean) IS the edge. If it wins regardless → it's just
   trend proximity, and cheaper tools suffice.
3. If it survives both: the median-line z is a candidate **entry-timing overlay** for the regime-gated wheel /
   CSP screen — buy the shallow below-line dip on quality names while above the 200-day.
