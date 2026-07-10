# Runner Anatomy — what 200%+ 12-month runners looked like at IGNITION (study, 2026-07-10)

Jake's challenge: "take every stock that ran over 200% in a 12 month period back to 2020...
see where the runs began... flag each commonality. Trailing P/E? FCF? Revenue/capex? Were they cheap?"
Tool: `tools/runner_anatomy.py` (Colab: yfinance + EDGAR + OpenInsider, 4 cells).
Related: [[quiet-health-screen]], [[buying-at-highs]], [[rotation-stickiness]], [[_calibration]].

> Firewall: nothing below is a result yet. This note exists to PRE-REGISTER the hypotheses before the
> data comes back, so we can't hindsight-fit the story to the output.

## Design
- Universe: current S&P 500 + 400 + 600 (~1,500 names). Run = rolling 252-trading-day return ≥ 200%
  any time since 2020-01. Episodes deduped (>180d gap = new run). Run START = the price low in the
  12 months before the first crossing.
- At-start measurements: drawdown vs prior 2y high (cheap-on-PRICE), trailing-FY P/E and P/S off actual
  EDGAR 10-K figures + split-safe market cap (cheap-on-EARNINGS/SALES), FCF yield, revenue YoY,
  capex/revenue, buybacks/mcap, insider net buys in the 6 months pre-start (OpenInsider).
- ⚠️ Known limits, logged up front: (1) **survivorship** — current index members only; runners that later
  collapsed out of the indices are invisible, so results = "index-quality runners," biased toward
  happy endings. (2) Fundamentals = last FISCAL YEAR filed before start, not TTM (robustness > precision
  across 1,500 filers). (3) Run-start = price low, a hindsight construct — nobody can buy the low;
  the question is what the PROFILE was, not the tick.

## PRE-REGISTERED HYPOTHESES (written before any run, 2026-07-10 — analysis, falsifiable)
- **H1:** The single most common trait is a DEEP DRAWDOWN, not a cheap multiple — majority start ≥30%
  below prior high; "cheap on price" beats "cheap on earnings."
- **H2:** Valuation at ignition is BIMODAL, not cheap: one cluster of single-digit-P/E left-for-dead
  cyclicals (energy '21, etc.) and one cluster of unprofitable/expensive hypergrowth (2020-21 tech,
  2023-25 AI). The median P/E will mislead; the distribution is the answer.
- **H3:** Ignition dates CLUSTER in a handful of macro windows (≈ Apr 2020, Nov 2020 vaccine rotation,
  late 2022 / spring 2023 AI, 2024 power/AI adjacents). Runners are cohort events — the regime picks
  the sector, then the sector picks the stocks. Stock-picking explains less than cohort membership.
- **H4:** Buybacks are NOT a common precursor (runners were mostly conserving or burning cash);
  insider buying is elevated pre-start in the value/cyclical cohort and largely ABSENT in the
  hypergrowth cohort (mirrors the current "corporately all-in, personally de-risked" split).
- **H5 (the uncomfortable one):** The [[quiet-health-screen]] profile (steady FCF, low beta, no story)
  will describe FEW of the runners. The screen finds compounders/mean-reverters, not 3x rockets —
  different animal, different job. If H5 holds, the basket's benchmark is SPY+alpha, and 3x outcomes
  were never on its menu; expecting them from it would be a category error.

## What would CHANGE behavior if the data says so
- If most runners WERE four-green-cheap at ignition → the quiet-health basket is also the rocket pad;
  weight it up in the core.
- If runners are drawdown+catalyst creatures → the hunting ground for tactical 3x candidates is the
  bombed-out cohort with a fresh demand shock (today's analog candidates live in
  [[buildout-bottleneck-map]] and fallen-tech, not the health screen).

## RESULTS (run 2026-07-10, Jake's Colab — 588 run events, 485 tickers, 1,504 names priced)

### DATA — the commonality block
- **Drawdown at start: median −63%. 90% were ≥30% below their prior 2y high; 75% were ≥50% below.
  Only 5% were cheap on none of price/earnings/sales.**
- Profitability: 68% had positive FY net income at ignition. Trailing P/E of the profitable: median
  **7.7x**, 68% under 15x, only 12% over 40x. P/S median 0.66, 60% under 2x. FCF yield median +6.9%,
  only 18% FCF-negative. Revenue YoY median +7.5% (27% shrinking). Capex/rev median 3.5%.
- Size: **median mcap at start $1.1B; 80% under $10B.** Mega-cap ignitions rare (NVDA Oct-2022 at
  $276B = the exception).
- WHEN: ignitions cluster in ~4 panic windows — **2020Q1+Q2 = 345 events (59%)** (COVID crash),
  2022Q2–2023Q1 ≈ 43 (bear bottom), 2023Q4 = 24 (rate-cut pivot), **2025Q2 = 75 (April tariff crash)**.
  Quiet quarters produce ~0–7 ignitions each.
- The Apr-2025 cohort is the live one and it is Jake's memory/optics complex: SNDK +5,004%, LITE
  +1,708%, WDC +1,177%, MU +1,029%, STX +777%, CIEN +823%, INTC +556% — all ignited 2025-04-04/22.
- Buybacks: 39% bought back >1% of mcap in the prior FY (mostly legacy behavior of mature cheap names).
- ⚠️ Artifacts (do not read as signal): CHRD "+147,479%" (merger-adjusted penny series), TRIP mcap
  $0.00 / buyback 415,224%, AMRX FCF 1,471,889%, TCBI P/S 6,528, MTRN/PATK share-count glitches —
  a handful of rows are garbage; medians are robust to them.

### ⚠️ CORRECTION (my bug, Cell 4) — insider stats understated
The printed "insider buying: any 7%" is wrong: only the top 60 events were sampled in Cell 3, but the
Cell-4 mask counted every unsampled event as "no buying." **Within the sampled 60: ~53% had at least
one insider buy in the 6 months pre-start; ~17% had >$1M net.** And the split is stark: heavy
open-market buying in the value/cyclical ignitions (MTDR 46 filings/$2.9M, OVV 23/$1.3M, SEZL 14,
REZI 14, CALX 10, CELH $9.6M, CAR $15.0M) vs **zero buys and heavy selling in the momentum/tech
ignitions** (PLTR $136M sells, APP $66M, STX $20M, SMCI $10.8M, LITE $9.6M, MU $8.1M, WDC $7.9M —
all 0 buys).

### HYPOTHESES GRADED (against the pre-registration above)
- **H1 — CONFIRMED, emphatically.** Deep drawdown is THE commonality: 90% price-cheap vs 40%
  earnings-cheap. You don't find 3x in strength; you find it in wreckage.
- **H2 — PARTLY.** Both clusters exist (32% unprofitable + a >40x tail vs 68%-of-profitables under
  15x), but the value hump dominates this survivor universe — median P/E 7.7 is cheaper than
  hypothesized. (Survivorship trims the hypergrowth hump: the 2021 meme cohort that later delisted
  is invisible.)
- **H3 — CONFIRMED.** ~80% of all ignitions sit in four macro panic windows. Runners are cohort
  events; the regime picks the moment.
- **H4 — HALF WRONG, HALF CONFIRMED.** Buybacks were present in 39% (more than hypothesized, though
  as mature-value legacy, not a trigger). The insider half confirmed strongly with corrected numbers:
  buying concentrates in value-cohort ignitions, absent-with-heavy-selling in growth ignitions —
  the "corporately all-in, personally de-risked" signature visible back to 2020.
- **H5 — CONFIRMED.** The runner profile = SMALL ($1.1B) + CRUSHED (−63%) + still-functioning
  (profitable, FCF+, revenue growing). The [[quiet-health-screen]] deliberately excludes crushed and
  small (low-beta/no-big-move filters, S&P 500 only) — right VALUATION profile, wrong STATE. The
  basket's job is compounding; 3x was never on its menu.

### THESIS (interpretation — NOT fact)
- **The formula the data spits out:** the modal 3x runner is a profitable, FCF-positive, revenue-growing
  small-cap whose PRICE was destroyed by a systemic panic while its BUSINESS stayed intact — bought at
  maximum fear, median 63% off its high, at ~8x trailing earnings. "Cheap" at ignition means cheap
  because broken price, not because the market overlooked a healthy chart. The edge is distinguishing
  broken price from broken business INSIDE the panic — the reported-vs-physical discipline in equity form.
- **Timing implication:** the future-runner list is written in crash windows (~4 in 6 years) and almost
  never between them. Between panics the job is watchlist-building and holding the option on clarity
  (cash/hedges); inside panics the job is deploying into intact businesses. Jake's current posture maps
  onto this cleanly — the hedge's deepest function is FUNDING the next ignition window.
- **Live confirmation:** the April-2025 tariff-crash cohort (memory/optics) is a textbook instance —
  crushed 40–70%, profitable or near it, then repriced by a demand shock ([[ai-capex-cycle]] scarcity).
  The study says the NEXT cohort forms in the next panic; today's analog watchlist = intact businesses
  in [[buildout-bottleneck-map]] + whatever the AI-capex unwind crushes indiscriminately if Stage 2 hits.
- Insider tell, refined: in a panic window, insider cluster-buys mark which crushed names' operators
  believe the business is intact (MTDR's 46 filings at the COVID low). In momentum ignitions insiders
  sell the whole way up — insider silence is normal there and not disqualifying, but it means YOU carry
  the E-risk they're shedding.

## Sources
- `tools/runner_anatomy.py`; session 2026-07-10.
