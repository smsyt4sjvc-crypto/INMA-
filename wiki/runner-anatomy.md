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

## RESULTS
*(pending — Jake runs the 4 cells in Colab and pastes Cell-1 event table, Cell-2 fundamentals,
Cell-3 insider table, Cell-4 commonality block back; then this section gets filled and the
hypotheses above get graded pass/fail, visibly.)*

## Sources
- `tools/runner_anatomy.py`; session 2026-07-10.
