# Quiet-Health Screen — S&P 500 value x health x no-story (first run 2026-07-05)

Tool: `tools/sp500_health_screen.py` (Colab; Yahoo screen → EDGAR 10-K verification).
Screens for quality-adjusted cheapness with no catalyst attached: earnings/FCF yield × ROE/debt/
OCF>NI accruals × low-beta/no-big-52w-move, sector-neutral rank; top 20 verified against actual
filings (NI streak, OCF≥NI, revenue, share-count shrink).
Related: [[rotation-stickiness]], [[concentration]], [[ai-financing-fragility]], [[consumption-vs-investment-crux]], [[detachment-bid]].

> Firewall: DATA = the run output (dated). THESIS = the read. Descriptive, not advisory.

## DATA — EDGAR verification, top 20 (run 2026-07-05, Jake's Colab)
- **Four-green (NI+ streak, OCF≥NI, revenue up, shares shrinking):** PG, GILD, CME, GD, HIG, EA, FFIV,
  ULTA, GEHC *(3yr = full history, 2023 spinoff)*. WRB/REGN clean except no share-shrink.
- **Data artifacts (not signals):** CI "1yr" (Cigna→The Cigna Group entity/tag change 2023), ALLE revenue
  None + UHS shares None (XBRL tag misses).
- **Real flags:** BF-B (OCF<NI **and** revenue down — spirits demand sliding), CF + EOG (revenue already
  falling under fat trailing E = **peak-cycle-earnings caveat live**), PSA (REIT — P/E/OCF wrong metric
  class, strike from pool), SNA (OCF<NI — captive finance arm absorbing cash), RMD (OCF<NI — recheck; GLP-1 overhang).
- **Cohort composition:** healthcare (GILD, REGN, UHS, GEHC, RMD, CI), insurance/financial plumbing (HIG,
  WRB, CME), defense (GD), staples (PG, BF-B), boring industrial (SNA, ALLE), gaming (EA), networking (FFIV),
  beauty retail (ULTA), commodity (EOG, CF), REIT (PSA). **Zero AI / semis / mega-cap tech survived.**

## DATA — full screen output (run 2026-07-05, 503/503 pulled, 0 failed)
- **47 survivors of 503 = 9% pass rate.** Top-30 by sector-neutral score led by BF-B, CF, EA, EOG, FFIV,
  ULTA, PSA, SNA, GILD, UHS, REGN, CI, HIG, PG, RMD, CME, GD, WRB, ALLE, GEHC, then CBOE, CB, BKR, TGT,
  VLTO, JKHY, HII, KVUE, WTW, EXPD (+DVN in cheapest-15).
- **Cheapest health-passing name in the index: UHS 6.7x trailing (14.9% earnings yield, rev +9.6%).**
  HIG 9.9x/14.5% FCF yield; CI 12.2x/9.1% FCFy; CB 12.9x.
- Themes doubled: **exchanges CME + CBOE** both pass; **defense GD + HII** both pass; P&C insurance x4
  (HIG, WRB, CB, WTW).
- ⚠️ Artifacts: **divY% column inflated 100x** (yfinance returns % already — read 357 as 3.57%; fixed in
  tool). EA trailPE 58.6 vs fwd 21.5 = one-time-charge-depressed trailing E (EDGAR four-green; use fwd).
  DVN revG already **−0.8%** under an 11.5x P/E = peak-E deflation starting; CF 33% opm = fertilizer-cycle
  artifact. TGT passes but d/e 117 + discount-retail-to-the-squeezed-middle = Hollow-Bottom test name.

## THESIS (interpretation — NOT fact)
- *(9% pass rate)* 91% of the S&P fails at least one of cheap/healthy/no-story — the quiet-health cohort is
  a thin residue at this index valuation, concentrated exactly where the rotation is landing.
- *(themes > names)* A mechanical screen surfacing exchanges twice (CME+CBOE = two long-vol toll booths) and
  defense twice (GD+HII) is the screen talking. UHS cheapest-in-index + eds/meds carrying ALL job growth
  (June BLS) = the labor data and the value screen agreeing on where the real economy is.
- *(the headline — three-tool convergence)* The quiet-health cohort **IS the defensive cohort the
  [[rotation-stickiness]] candle scan showed money landing on** (health/defense/staples/insurance), and the
  mirror of the [[concentration]] de-concentration print (the "other 490" carrying the index). Value, flow,
  and filings now point at the same cohort — the market is rotating INTO the quietly-healthy cheap stuff.
- *(CME — the barbell name)* An exchange is a **toll booth on volatility**: volumes/earnings spike when
  markets break → a "non-catalyst" name that benefits from the exact catalyst the book hedges. Cheap +
  cash-backed + shrinking shares + structurally long-vol.
- *(ULTA vs LULU — the price-point K)* ULTA passes everything while LULU's op income fell 37% → the
  **lipstick effect**: the $15 indulgence holds while the $120 leggings crack. The discretionary crack is at
  the PRICE-POINT tier (aspirational-stretch), not the category level. Discriminating datapoint for the
  Hollow-Bottom K-shape and for Burry's LULU negative-bezzle bet.
- *(SNA — a Hollow-Bottom canary)* Snap-on's OCF<NI likely = its captive finance book (tools-on-credit to
  mechanics) absorbing cash. Working-class credit strain would show in its financing receivables EARLY.
  Watch item, not a call.
- *(insurers — same label, opposite risk)* HIG/WRB are P&C underwriters, NOT the PE-owned life/annuity/
  Bermuda chain in [[ai-financing-fragility]]. The screen's insurance is the boring clean kind. Distinguish.
- *(⚠️ calibration)* This is a **regime-change portfolio**: if the melt-up resumes, it lags — cheap-quality
  stayed cheap all of 2016–2020, and "non-catalyst" means nothing forces the re-rating. The screen says
  where healthy cash flow is cheap, not when anyone will care. One week of defensive flow ≠ a regime.

## Live benchmark — the paper basket (started 2026-07-07)
Jake built the screen's list as a Fidelity paper watchlist (1 share each — ⚠️ price-weighted like the Dow;
ULTA/CBOE dominate the Total row, read per-name %). **Basis date 2026-07-07 = a clean falsifiable test:
quiet-health cohort vs SPY from 7/7.** Basket beats SPY over weeks → rotation had legs (sticky wins);
chips V-bounce + basket bleeds flat while SPY rips → flush (base rate wins). Day 1: basket **+1.31%** vs
chip-wreck 2.0 (SMH −5.7) — exchanges led (CBOE +5.0, CME +3.0 = the long-vol toll booths paid same-day);
defense (the 7/3 leader) was the only red = rotation eating its own front rank.

## Refresh
Re-run both cells any time (~20 min); paste top-30 + EDGAR lines back → I update this note dated.

## Sources
- Jake's Colab run 2026-07-05 (EDGAR verification output pasted in chat); `tools/sp500_health_screen.py`.
