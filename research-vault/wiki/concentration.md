# Concentration & Breadth

Related: [[market-fragility]], [[ai-capex-cycle]], [[fragility-engine]].

> Firewall: DATA = measured. THESIS = interpretation.

## DATA (observed)
- ~11 names ≈ 40% of S&P 500 weight (2026-H1 session cells).
- **Top-10 ≈ 36–37% of the index (Slickcharts, ~2026-03-30): NVDA 7.0% (now #1), AAPL 6.3%, MSFT 4.6%
  (top-3 ≈ 18%).** Higher than the 2000 dotcom peak (top-10 was ~23%). [ICI/Slickcharts via WebSearch 2026-07-03]
- Top-10 weight share today vs prior peaks: session work compared *current* top-10 concentration
  to **2000 dotcom** and **2008 GFC** pre-crash setups; finding was today's top-10 is more
  concentrated than those prior peaks.
- Proxy for the [[fragility-engine]]: SPY/RSP ratio (cap-weight ÷ equal-weight); rising =
  narrowing. Percentile + slope computed live in the engine.

### ⚡ Top-10 YTD-2026 returns — the DE-concentration print (Colab/yfinance, run 2026-07-03)
YTD%s live (yfinance); weights approximate (mine, ~3mo stale, AVGO overstated post-drop) → aggregates ballpark.
| name | wt% | YTD% | contrib pts |
|---|---|---|---|
| NVDA | 7.0 | **+4.6** (stalled leader) | +0.32 |
| AAPL | 6.3 | **+13.7** | +0.86 |
| MSFT | 4.6 | **−18.9** | **−0.87** |
| AMZN | 4.0 | +5.1 | +0.20 |
| META | 2.8 | **−11.5** | −0.32 |
| AVGO | 2.5 | +4.5 | +0.11 |
| GOOGL | 2.3 | **+15.1** | +0.35 |
| TSLA | 2.0 | **−12.5** | −0.25 |
| GOOG | 1.9 | +13.7 | +0.26 |
| BRK-B | 1.7 | +1.0 | +0.02 |
- **Top-10 = 35.1% wt, equal-wt avg YTD +1.5%, cap-wtd contribution = +0.68 pts.** → the *other 490 names
  (65%)* carried nearly all of the S&P's 2026 gain. Breadth **broadened**; top 10 net-flat and internally split.

## THESIS (interpretation — NOT fact)
- *(analysis)* Extreme top-heavy concentration raises index fragility because a small number of
  correlated names carry the tape; a wobble in the leaders is a wobble in the index.
- *(analysis, 2026-07-03 — the DE-concentration read)* The 2023–24 "Mag-7 IS the market" regime is
  **already unwinding in the returns.** The heaviest weights are the year's *losers* (MSFT −18.9%,
  META −11.5%, TSLA −12.5%), NVDA has *stalled* (+4.6%), and only +0.68 index pts came from the top 10
  → **the other 490 carried 2026.** Concentration is falling *mechanically* (biggest weights = biggest
  losers shrink their share, ~37%→~35%), answering "is it unwinding from the March peak?" = **yes.**
- *(links [[ai-capex-cycle]] — builder vs monetizer, visible in the megacaps)* Within the top 10 the market
  is **discriminating capex-BUILDERS (MSFT/META, spending into <10% ROI → punished) from MONETIZERS
  (GOOGL/AAPL, light-capex / value-capture → rewarded).** The GPT-reframe's "value migrates OFF the
  infrastructure spenders" (fiber analog) is printing in the leaders, not just the semis/neocloud sleeve.
- *(⚠️ calibration — the side Jake under-weights, since this confirms his bearish lean)* The broadening may
  be the fragility **DEFUSING gracefully, not detonating**: the 2023-24 fear was "Mag-7 rolls over → index
  craters"; instead MSFT/META/TSLA rolled over and the index held on breadth = concentration risk resolving
  *without* a crash → arguably **bullish the index** even as it's bearish the AI names. **What keeps it
  bearish-consistent:** the [[rotation-stickiness]] scan says the breadth is **defensive-flavored** (gold/
  staples/healthcare, not cyclicals) = *risk-off hiding*, not *risk-on rotation*. Character of the "other
  490" leadership (defensive vs cyclical) is the tell that decides bullish-broadening vs bearish-hiding.
- *(analysis)* "Is an ATH a too-late or bullish signal?" — open question from the ATH study;
  distance-between-ATHs and forward-return event study were built but conclusions were
  data-dependent and not locked. Re-run before citing.

## Dry powder / re-concentration framework (2026-07-03)
### DATA
- **Money-market fund assets = record $7.95T (ICI, week ended 2026-07-01, +$47.7B and still rising).**
  60.2% institutional / 39.8% retail; 82.3% government funds. [ICI/Crane via WebSearch]
### THESIS (interpretation — NOT fact)
- *("cash on sidelines" is half a myth)* Every MMF dollar is already invested (T-bills/repo); it doesn't
  "flood into" stocks, it changes hands. $7.95T ≠ $7.95T of equity buying power. And the composition (60%
  institutional, 82% govt) = mostly corporate treasury/cash-mgmt, not retail dip-buying fuel.
- *(the switch is the FED, not the balance — ties [[new-economy-regime]] Fed Trap)* Cash earns ~4–5% risk-free;
  what dislodges it is the *yield dropping*. So Jake's two scenarios are **sequenced, gated by the Fed:**
  **hawkish (now) → parked → continued de-risking/selling; first cut → yield drops → re-concentration** (and
  since the index IS the top 10, that cash hunts the same names → violent melt-up). Parked now, weaponized on the cut.
- *(present flow supports the selling read)* MMF *rising* into 2026-07-01 *as semis sold* = the footprint of
  Jake's memory/semis profit-taking parking in **cash, not other equities** = risk-OFF, not rotation. Same
  de-risking impulse as the de-concentration + the [[rotation-stickiness]] defensive scan — one flow, three views.
- *(new leading indicator)* **ICI publishes MMF flows weekly (Thu).** Still rising = de-risking continues;
  first *sustained decline* = cash redeploying = re-concentration beginning. The public tripwire between Jake's two scenarios.

## ⚠️ methodology notes
- Survivorship bias: follow names even after they leave the index, and back before they joined,
  using point-in-time constituents (fja05680/sp500) — else results are biased.

## Sources
- Session breadth/concentration/ATH cells, 2025-Q4 → 2026-H1.
- Top-10 weights + YTD returns: Slickcharts/ICI (WebSearch) + Colab/yfinance run, 2026-07-03.
- MMF assets: ICI weekly (week ended 2026-07-01).
