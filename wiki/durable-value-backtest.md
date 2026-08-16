# Durable-Value Backtest — does "cheap for a good reason" beat "just cheap"? (2026-08-16)

Tool: `tools/durable_value_screen.py` (Colab; Yahoo prices × EDGAR XBRL, point-in-time).
Jake's spec, 2026-08-15: *"go back 5 years and locate 'cheap' stocks… low P/E ratios, but where both
the P&E are in historically tolerated ranges. Not where [E] is driving the low range by itself. Like a
quarter of crazy earnings, or depreciation pulled forward or an acquisition eats earnings… good balance
sheets, healthy growth (above 200 & 50 SMA), low P/E."*
Related: [[quiet-health-screen]] (the 2026-07-05 snapshot screen this tests), [[market-fragility]],
[[ai-capex-cycle]], [[consumption-vs-investment-crux]], [[colab-archive-audit]].

> Firewall: DATA = the run output (dated, reproducible). THESIS = the read. Descriptive, not advisory.

## THE CONSTRUCTION (so the numbers can be judged)
- **Point-in-time.** Every EDGAR fact is filtered on its `filed` date — only facts filed strictly BEFORE
  the formation date are used. No look-ahead.
- **7 formation dates, equal 3-year holds:** 2017-08-15 → 2023-08-15, each held to the same date 3 years
  later. **One date is one coin flip; the first version of this test used one date and was worthless.**
- **Cheap = bottom quintile of that date's OWN cross-section** (not a fixed multiple — see ⛔ below).
- **Durability = TTM diluted EPS ÷ median of the last 6 ANNUAL EPS prints.** Band 0.70–1.60.
  Below 0.70 = earnings collapsed. Above 1.60 = earnings spiked. Inside = "normal E."
- Universe ~330 today-listed US large/mid caps; **262–299 usable per date.**

## ⛔ DATA — THE HEADLINE RESULT, AND WHY IT IS NOT A RESULT
**Jake's FULL spec (cheap + durability + balance sheet + 50/200 SMA + positive growth + no prior loss):**

| formation | SPY | NAIVE spread | n | DURABLE spread | n | diff |
|---|---|---|---|---|---|---|
| 2017-08-15 | +36.6% | −12.1% | 5 | **+7.3%** | 3 | +19.4 |
| 2018-08-15 | +58.3% | +10.7% | 9 | **+143.0%** | 1 | +132.3 |
| 2019-08-15 | +50.7% | −19.3% | 2 | −59.2% | 1 | −39.9 |
| 2020-08-14 | +33.0% | +20.1% | 5 | **+57.5%** | 1 | +37.4 |
| 2021-08-16 | +23.7% | −1.2% | 10 | −38.5% | 2 | −37.3 |
| 2022-08-15 | +50.0% | −47.5% | 1 | *no names* | 0 | — |
| 2023-08-15 | +75.3% | −14.1% | 3 | *no names* | 0 | — |

- **DURABLE beats NAIVE by mean +22.4pp, median +19.4pp, winning 3 of 5.** ⛔ **DO NOT BELIEVE THIS.**
- **⛔ THE WHOLE NUMBER IS ONE STOCK.** Dick's Sporting Goods (DKS) was the **SOLE name** in the 2018
  durable bucket and returned **+201%**. **Drop that one date and the filter reads −5.1pp.**
- **The durable bucket averages 1.6 NAMES PER DATE and is EMPTY on 2 of 7 dates.** That is not a
  portfolio and not a backtest. **An effect that inverts when one observation is removed is not an effect.**

## ★★★ DATA — THE ISOLATION TEST (the one with enough sample to mean anything)
Every gate stripped except cheapness, then the cheap cohort split on durability alone. Same cheapness
rule, same dates, same universe — **the only difference between the columns is the thing being tested.**
**~55 cheap names per date; durable 27 vs spiky 28 on average.**

| formation | SPY | cheap n | DURABLE-E spread (n) | SPIKY-E spread (n) | diff |
|---|---|---|---|---|---|
| 2017-08-15 | +36.6% | 55 | −31.7% (39) | −17.5% (12) | −14.2 |
| 2018-08-15 | +58.3% | 54 | −20.3% (15) | −30.4% (39) | +10.1 |
| 2019-08-15 | +50.7% | 57 | −4.8% (30) | **+52.0%** (26) | −56.8 |
| 2020-08-14 | +33.0% | 53 | +7.7% (33) | −1.3% (16) | +9.0 |
| 2021-08-16 | +23.7% | 58 | −21.5% (23) | +1.5% (35) | −23.1 |
| 2022-08-15 | +50.0% | 61 | −20.2% (25) | −34.9% (36) | +14.7 |
| 2023-08-15 | +75.3% | 60 | +7.4% (27) | −17.5% (31) | +24.9 |

- **DURABLE-E minus SPIKY-E: mean −5.0% · median +9.0% · durable wins 4/7.**
- **⛔ LEAVE-ONE-OUT SWINGS THE SIGN: −10.0% (drop 2023) to +3.6% (drop 2019).** The mean is dominated by
  a single date (2019, −56.8). No reliable edge in this sample.

## ⛔⛔ DATA — THE TEST DID NOT MEASURE WHAT IT CLAIMED TO. 7 DATES OUT OF 7.
**Before concluding anything about Jake's idea: check what the buckets actually contain.**
Median 3-year EPS CAGR of each bucket, at every formation date:

| formation | DURABLE median CAGR | SPIKY median CAGR | durable med durability | spiky med durability |
|---|---|---|---|---|
| 2017-08-15 | 6.4% | **29.1%** | 1.29 | 2.41 |
| 2018-08-15 | 6.6% | **26.7%** | 1.31 | 2.36 |
| 2019-08-15 | 9.5% | **27.1%** | 1.24 | 2.19 |
| 2020-08-14 | 14.3% | **26.7%** | 1.14 | 2.77 |
| 2021-08-16 | **−4.9%** | 11.2% | 1.26 | 2.24 |
| 2022-08-15 | 11.0% | **17.4%** | 1.27 | 2.66 |
| 2023-08-15 | 5.2% | **47.2%** | 1.21 | 2.80 |

**★★★ THE "SPIKY" BUCKET IS A GROWTH BUCKET. Every date, without exception.** And the arithmetic says it
must be — simulate a company with **ZERO spikes, ZERO cyclicality, nothing but steady compounding**:

| steady EPS growth | resulting "durability" | verdict under the 1.60 band |
|---|---|---|
| 5%/yr | 1.16 | passes as durable |
| 10%/yr | 1.33 | passes as durable |
| **17%/yr** | **1.60** | **the exact threshold** |
| 27%/yr | 2.03 | **REJECTED AS SPIKY** |
| 45%/yr | 3.00 | **REJECTED AS SPIKY** |

**⇒ `durability = TTM ÷ median(last 6 annual EPS)` IS VERY NEARLY A MONOTONE FUNCTION OF THE GROWTH RATE.
A flat median sits ~3 years back along a compounding series, so the ratio is approximately (1+g)³.
`DURABLE_HI = 1.60` does not mean "no one-off gain" — it means "REJECT ANY COMPANY COMPOUNDING EPS
FASTER THAN ~17%/YEAR."** The simulated values reproduce the observed bucket medians almost exactly
(spiky 2.2–2.8 ↔ 27–47% CAGR; durable 1.14–1.31 ↔ 5–14% CAGR).

**⇒ THE −5.0pp IS NOT EVIDENCE AGAINST JAKE'S HYPOTHESIS. It is the expected result of systematically
buying slow growers and shorting fast growers inside the cheap cohort over 2017–2026. JAKE'S ACTUAL
HYPOTHESIS REMAINS UNTESTED — the instrument never measured it.**

## ★★★ DATA — WHAT *IS* ROBUST: CHEAPNESS ITSELF LOST
- **BOTH halves of the cheap cohort underperformed SPY.** Mean 3-year spread vs SPY:
  **durable-E −11.9% · spiky-E −6.9%**, across 7 formation dates at ~55 names per date.
- **Bottom-quintile P/E underperformed on 5 of 7 formation dates for BOTH buckets.** Consistent sign,
  large n, no dependence on any single date. **This is the finding with actual support behind it.**
- Corroborates the standing line in [[quiet-health-screen]] written six weeks earlier: *"cheap-quality
  stayed cheap all of 2016–2020, and 'non-catalyst' means nothing forces the re-rating."*

## DATA — THE MECHANISM IS REAL AT THE NAME LEVEL (it just does not aggregate)
- **REGN, formation 2021-08-16: P/E 11.3, durability 3.86** — trailing EPS inflated by COVID antibody
  revenue. **Returned +27.8% against SPY's +73.7% over 5 years: −45.9pp.** It was the ONLY name that
  passed the naive full-spec screen at that date, and the durability filter vetoed it.
- **MPC, formation 2021-08-16: P/E 5.0, durability 2.55** — trailing EPS inflated by the Speedway sale
  gain against a FY2020 print of **−15.13**. The lowest multiple in the cohort, manufactured by the E.
- **⇒ Individually verifiable, not fitted. The trap Jake described EXISTS. What the test cannot show is
  that a mechanical band around it sorts returns over a 3-year horizon.**

## ⛔ DATA — SEVEN DEFECTS FOUND AND FIXED IN THE TOOL (the run before this one was unreportable)
**Four in the EPS layer, all concealed by EDGAR's own labels:**
1. **Quarterly facts wearing annual clothes.** Valero tags its quarterly-EPS footnote `form="10-K"`;
   keying on `end` let **Q4-2019 (2.58) overwrite FY-2019 (5.84)**. VLO's "annual history" was **five
   consecutive QUARTERS posing as five YEARS.** Chevron's 10-K carries no quarterly facts, so Chevron
   looked clean. **⇒ COMPANY-DEPENDENT. A one-name spot check could not find it.**
2. **Year-to-date summed with discrete quarters** — a Q2 10-Q carries both, and `fp` says "Q2" for both.
3. **Q4 discrete EPS is NEVER published in a 10-Q.** Summing four 10-Q quarters can never span a fiscal
   year-end. **Not patchable by filtering forms** — TTM must be built by cumulative arithmetic:
   `latest FY + current-FY YTD − prior-FY YTD`. Hand-verified: **CVX −2.96 + 2.32 − (−2.51) = +1.87**
   (P/E 54.0, was `nan`); **VLO −3.50 + (−1.34) − (−1.48) = −3.36**, genuinely loss-making (was a 109.4 P/E).
4. **The split bug, a second time, INSIDE the EPS history.** EDGAR restates comparatives only in filings
   made AFTER a split, so AAPL returned `[9.22, 8.31, 9.21, 2.98, 2.97, 3.28]` — three pre-split, three
   post. **The median of that list is what durability divides by.** Fixed → durability 0.88 → **1.94.**

**Three in the screen calibration, and these were MINE, not EDGAR's:**
5. **Absolute P/E ≤ 15 cut 149 of 175 names.** A fixed multiple is not a cheapness test, it is **a bet on
   the ERA** — 15× is near the median in 2011 and near the bottom decile in 2021. Now a percentile.
6. **Leverage measured as `Liabilities / Equity`** — that is the entire right-hand side of the balance
   sheet (payables, deferred revenue, pension, leases). An ordinary industrial runs 1.5–2.5× on it with
   **no borrowings at all**; the gate cut 14 of the 26 P/E survivors. **INSTRUMENT MISMATCH.**
7. **⛔⛔ STALE REFERENCE VALUE — THIRD INSTANCE OF THIS CLASS IN THREE DAYS.** `instant()` returned the
   newest fact carrying a tag *however old it was*, and **filers abandon tags**. Marathon last used
   `LongTermDebtNoncurrent` on **2012-03-31**; the screen reported a **nine-year-old** figure as its 2021
   debt and derived leverage of 0.11. Ford's last use was a $0.29B fragment. **Same shape as
   `meta.chartPreviousClose` (8/14) and the Jane Street 2024 denominator (8/14): THE VALUE IS CORRECT AND
   THE DATE IS NOT.** Facts are now rejected on AGE — which protects every balance-sheet read, not just debt.

**Plus a silent drop:** the 3-year EPS CAGR raised a negative float to the ⅓ power. Python returns a
**complex number**; `growth <= 0` then raised `TypeError`, and a bare `except` turned it into `r = None`.
**Every company with a negative latest annual EPS was being dropped by an exception, not by a filter.**

## THESIS (interpretation — NOT fact)
- ***(⛔ THE VERDICT, AND IT IS NOT THE ONE THE RUN APPEARED TO GIVE)*** **The instrument was wrong, so the
  result is void — in BOTH directions.** The +22.4pp headline was one stock; the −5.0pp isolation figure
  is an inverted growth screen. **Neither number says anything about whether inflated trailing earnings
  are a trap. Jake's hypothesis is UNTESTED, not disproven.** ⚠️ **The dangerous version of this note is
  the one that reports −5.0pp as "we tested it and it does not work."** Measuring the wrong thing
  precisely is worse than not measuring, because it produces a number, and numbers get quoted.
- ***(why a flat median cannot detect a spike)*** A median is a **level** statistic applied to a series
  with a **trend**. On any compounding series the median sits ~3 years back, so `TTM ÷ median` measures
  how far the company has travelled, not how far it has deviated. **To detect a deviation you need a
  model of the trend to deviate FROM.** ⬜ **THE FIX: fit a regression through the annual prints and
  score TTM against the FITTED value, not the median. NOT RUN — registered, not claimed.**
- ***(and the fix has a known failure mode too, so register it now)*** A trend fit will treat a genuine
  step-change in earnings power — an acquisition that permanently raises EPS, exactly one of the cases
  Jake named — as a deviation. **Detecting "temporary" requires distinguishing a spike from a re-basing,
  and no single ratio does that.** The honest instrument is probably the SOURCE of the earnings (one-off
  gains, asset sales, tax items) read from the filings, which is a text problem, not a ratio problem.
- ***(why the full-spec screen returns 1-3 names)*** Stacking six gates on a 20% cheapness cut leaves
  nothing. **A screen that returns 1.6 names is not measuring the market, it is measuring the screen.**
  The isolation design — one gate, one split — is the only version of this that can carry a conclusion.
- ***(★★★ THE ONLY FINDING THAT SURVIVES, and it is not the one we set out to test)*** **Cheapness was the
  losing bet of 2017–2026, robustly, at large n.** ⚠️ It survives precisely BECAUSE it does not depend on
  the broken durability measure: it is the cheap cohort vs SPY, both buckets, 7 dates, ~55 names. That is the value factor's known drought, and it sits
  directly alongside the vault's concentration work: this is the same period in which the index return
  was carried by the top names. **A low multiple was not a discount in this era; it was a classification.**
- ***(⚠️ what survivorship does and does not spoil)*** The universe is today's listed set at every
  formation date, so failures are absent from **both** columns. It inflates every absolute return here,
  **including SPY's.** It hits the durable and spiky buckets alike and **largely cancels in the DIFFERENCE**
  — which is why the spread between columns is the only number worth reading, and the absolute levels are
  not evidence of anything.

## ⬜ NOT KNOWN / NOT RUN
- 🚩🚩🚩 **TREND-FITTED DURABILITY instead of median-fitted — this is now the whole test.** Until it runs,
  the vault has NO evidence either way on Jake's actual claim. Everything else here is scaffolding.
- ⬜ **Growth-neutral variant:** split the cheap cohort on durability WITHIN growth deciles, so the two
  buckets are matched on EPS CAGR. If the effect is real it must survive holding growth constant.
- ⬜ **The source-of-earnings read** (one-off gains, asset sales, tax items from the filings) — the
  instrument that would actually distinguish a spike from a re-basing. Text work, not a ratio.
- ⬜ **Point-in-time index membership.** Without it, survivorship is bounded but not removed.
- ⬜ **Longer holds (5yr) at every formation date** — only the 2021 date has a full 5 years to 2026.
- ⬜ **Sector-neutral cheapness.** The bottom-quintile P/E cohort is structurally energy/financials-heavy,
  so the test may be measuring sector timing rather than valuation.
- ⬜ **Dividends.** All returns here are PRICE ONLY; the cheap cohort yields more than SPY, so the cheap
  cohort's underperformance is **overstated** by an unmeasured amount.

## Sources
- `tools/durable_value_screen.py`, runs of 2026-08-16 ~10:00am–12:30pm PDT (full spec + isolation).
- SEC EDGAR XBRL `companyfacts` API; Yahoo Finance chart API (prices + split events).
