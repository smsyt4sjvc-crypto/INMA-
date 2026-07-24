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

## Analyst layer — estimate revisions + targets (Cell 3 run 2026-07-07)
Consensus current-yr EPS revisions (90d), price targets, buy%. ⚠️ This is the REPORTED layer — herds and
lags; weight revisions (direction) > targets (lag price) > buy% (contrarian texture).
### DATA
- **CBOE: +14.9% revisions, +23% upside, 24% buy** — estimates rising hard (vol revenue repricing into
  consensus), cheap, under-recommended. Best profile in the table. **CME +1.0%/+24%/56%.** Exchange theme
  now confirmed by a 4th independent tool (screen, EDGAR, rotation tape, revisions).
- Ignored value: UHS −0.1%/+32.7%/40%; HII −0.1%/+32.7%/42% — flat estimates, big gaps, Street not looking.
- Loved-but-flat: CI +0.2%/+18.6%/**83% buy** (most-recommended); GEHC **−3.8% cuts** but 72% buy (China/
  imaging — know why before funding); ULTA +0.9%/+38.7%/70% (⚠️ target-lag inflates the gap).
- Fully-priced per Street (target ≤ price): FFIV, WRB, CB. **EA = weakest profile on the list: −2.4% cuts,
  zero upside, 6% buy, near 52w high** → the drop candidate if trimming the basket.
- **⚠️ HIG −4.9% cuts — real flag, not artifact** (P&C cat losses or pricing cycle rolling?). Check why
  before sizing past equal weight; revision data favors WRB/CB stability among the insurers.
- **GILD −109% = ARTIFACT, resolved (verified 7/7):** $11.5B acquired-IPR&D charges (Arcellx $7.8B + Ouro +
  Tubulis) flip the GAAP guide to a loss; **ex-items EPS guide unchanged $8.45–8.85 and sales guidance
  RAISED to $30.0–30.4B.** The scary GAAP headline is part of why GILD screened cheap = fallen-quality
  optics event, not deterioration. (Same lesson as EA's trailing-PE artifact: one-time charges lie.)
### Diligence honesty (what the stack still hasn't done)
Screen + EDGAR + analyst layer ≠ underwriting: no guidance calls read, no name-level risk work (GILD patent
cliff, CI PBM regulation, UHS Medicaid/labor, HIG cat book, EA pipeline), revenue check is endpoint-to-
endpoint, 10-K data lags. Before real dollars beyond an equal-weight tracking basket: name-level dives on
whatever gets sized up (priority: UHS/CI/GEHC + HIG's why).

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

## GEHC — the 8-buyer cluster, detail (2026-07-12, WebSearch corroboration of the NDX scan hit)
### DATA (StockTitan Form-4 coverage + QuiverQuant, May-2026 buys, verified names)
- **CEO Peter Arduini: 4,169 sh @ $59.93 (~$250K)** → 259,424 directly held. **CFO bought May 1.**
  **GC Frank Jimenez: 1,750 sh (~$105K).** Directors: **Kevin Lobo (Stryker's sitting CEO): 10,000 sh
  (~$600K+)**; **William Stromberg (ex-T. Rowe Price CEO): 1,000 @ $61.69**; **Rodney Hochman
  (ex-Providence CEO): 1,618 @ $62.03 via family trust**; plus **one unidentified director: 80,805
  shares (~$4.8M — the bulk of the $6.42M)**. Prices paid ~$59.93–62.03.
- QuiverQuant (dated recently): "GEHC rises as investors weigh fresh FDA clearance, insider buying,
  and a steadier growth backdrop."
### THESIS (interpretation — NOT fact)
- **This passes every quality test the vault has:** varied sizes ($62K → $4.8M — the anti-EPAM
  signature), varied dates across May, top-of-house titles (CEO + CFO + GC = operations, numbers, and
  legal all buying), and two PROFESSIONAL allocators among the directors (a sitting med-tech CEO and
  a former T. Rowe Price CEO buying personally). Not a program, not theater.
- The basket's flagged worry (−3.8% estimate cuts, China/imaging) now has: 8 insiders' money against
  it + an FDA-clearance catalyst + basing-to-rising tape. The "know why before funding" gate from the
  diligence-honesty section is now half-answered by the people who know why.
- OPEN: identity of the 80,805-share whale; whether buying continued into Jun/Jul; exact cluster
  total/dates → Colab detail parse. Name-level work (China exposure sizing, imaging cycle) still
  required before sizing past basket weight.

### GEHC cluster — COMPLETE FILE (2026-07-12, Jake's EDGAR detail parse, 120d window)
- **The $4.8M whale = H. LAWRENCE CULP JR: 80,805 sh @ $61.88 on 5/6 = $5,000,076** — a deliberately
  round $5M personal check. Culp = GE Aerospace CEO, architect of the GE breakup and of the GEHC
  SPINOFF ITSELF — arguably the single most structurally informed person on this asset alive.
- **The sequence (a story in dates):** GC Jimenez + CEO Arduini 4/30 ($106K + $250K) → CFO Saccaro 5/1
  ($201K) — management inside 48hrs, classic post-earnings open window → Stromberg + CULP $5M 5/6 →
  Yang Watkin 5/8 ($63K) → Hochman 5/12 ($100K) → **Lobo (Stryker CEO) 5/22: $642K @ $64.18 — buying
  HIGHER after the rise** (insider buying INTO strength — the rare variant). Prices $59.93 → $64.18,
  escalating as the stock recovered. **Zero sells in 120 days**; everything else in the window =
  routine annual director grants (5/7 cycle) + one tax-withholding.
- **Verdict: A-grade, artifact-checked, complete.** All quality tests passed: varied sizes ($62K–$5M),
  varied dates, escalating prices, C-suite + GC + professional allocators + THE ARCHITECT. The
  strongest name-level insider signal in the vault, attached to a four-green basket name.
- Remaining gate before sizing past basket weight: name-level fundamentals (China/imaging exposure,
  replacement cycle, the −3.8% estimate-cut anatomy). Options chain untradeable (OI 14) — this is an
  EQUITY signal, not a CSP candidate.
