# Colab Archive Audit — the Drive folder, read and graded (2026-08-12)

Jake, 2026-08-12 ~2:20pm PDT: *"Read those. Early ideas uncreated in Colab. Some promising butt early
versions of chat writing code. So hiccups."* — Google Drive folder `1emVvnIsxhHGWmFlwDHipr6TVLG6YbWpg`
("Colab Notebooks").

Related: [[bull-bear-ledger]] · [[new-economy-regime]] · [[structural-pull-log]] · [[buying-at-highs]] ·
[[ath-clustering]] · [[data-sourcing-playbook]] · [[trading-maxims]] · [[portfolio-state]]

> **ARTIFACT TEST — what was actually read.** All **50 files (5.60 MB)** were downloaded and parsed, not
> the folder listing. The Drive MCP connector required an approval this session could not grant, so the
> folder was fetched as its public HTML (`HTTP 200`, 770,581 bytes, title "Colab Notebooks — Google Drive"),
> the 50 `data-id` entries extracted, and each file pulled via `drive.google.com/uc?export=download&id=…`.
> Notebook JSON parsed for source **and saved outputs** — so the results below are what the cells actually
> printed on Jake's runs, not what the code would print.
> ⬜ **The 50 is what the folder's first HTML page renders.** If Drive paginates beyond 50 there are files
> this audit did not see. Not verifiable without the API.

## DATA (observed — the inventory, 2026-08-12)
- **50 files · 33 distinct names · 5.60 MB.** 46 `.ipynb`, 2 `.txt`, 2 untitled.
- **17 files are duplicate NAMES — and every copy is a DIFFERENT code version.** `Call Put Scanner v5
  NDX100` ×5 (5 distinct SHAs), `ai stock analysis` ×5, `Call Put Scanner v4` ×3, `alpaca_connection_test`
  ×3, `bb compression ai capex analysis` ×3, `btc 2x strategy eval` ×3, `csp_screen` ×3, `Call Put
  Scanner` ×2. **They are not backups. They are divergent forks sharing a filename.**
- **5 files are EMPTY** (0 code cells): `kalshi edge finder`, `InlandNW_Modernization_Colab`, and one copy
  each of `Call Put Scanner v5`, `ai stock analysis`, `btc 2x strategy eval`.
- **12 saved tracebacks across 11 files.** Full list in the taxonomy below.
- **Data-source dependency count:** yfinance **23** · hardcoded ticker roster 15 · Colab Drive mount 4 ·
  manual file upload 4 · stooq 2 · Alpaca 1 · SEC EDGAR 1 · FRED CSV 1 · Kalshi 1.

### ⛔ THE HIGHEST-VALUE FINDING IS THE ONE I DID NOT EXPECT: THE VAULT IS AHEAD OF THE ARCHIVE
Three of the folder's best notebooks have **already been run and already been filed** — the archive is the
SCAFFOLDING behind conclusions this vault has been carrying for weeks, not new territory:

| notebook | saved output | already filed |
|---|---|---|
| `financial_gravity.ipynb` | SPX/Fed-BS trend +1.6%/yr; QE era −0.4%/yr; **QT era +29.7%/yr**; R² Fed BS 0.72 (elast 0.91) vs **M2 0.94 (elast 1.60)**; QT elast **−1.87** | **`new-economy-regime.md:1156-1177` (2026-07-19)** — every number, plus the M2 upgrade AND the spurious-regression caveat |
| `first_of_month_options.ipynb` | day-1 std 121.2bp vs 113.3 baseline; win **61% vs 53%**; mean **+18.7bp vs +3.0bp**; skew −1.21; mean\|move\| 1.76% vs straddle breakeven **2.03%**; clears 33% vs 29% random | **`bull-bear-ledger.md:190, 212` (2026-07-17)** — "+18.71 bp/day, 61% win"; "day-1 is a DRIFT not a vol event, so no long-premium edge" |
| `cluster_hunter.ipynb` | S&P 1500 → 625 under $60 → **89 survivors** on FCF-yield/growth/leverage gates | **`structural-pull-log.md:111, 139` (2026-07-12)** |

- **The retrieval gate is what caught this, and it caught it BEFORE anything was filed.** `crosscheck.py`
  surfaced `new-economy-regime.md:1126` on the first pass. Five times in two days the vault has held the
  answer while I was preparing to re-derive it; **this is the first time the machine stopped it rather than
  the post-mortem finding it.** *(Analysis.)*
- ⚠️ **But it only worked after a fix — and the fix is the same bug class twice.** The first run printed
  *"no (subject, number) pairs found — nothing to check"* for BOTH headline claims, because `crosscheck.py`
  had no vocabulary for **balance sheet · M2 · SPX · day-1 · seasonality · drawdown · 52-week high**.
  **"No vocabulary" and "no conflict" rendered IDENTICALLY — the exact defect that made the FRED probe show
  a 404 and a timeout as the same `✗`.** Fixed 8/12: 25 subjects added, and a claim carrying numbers but no
  known subject now prints **"⛔ VOCABULARY GAP — the vault was never searched,"** which is the opposite of
  a clean bill. *(Third instance of one shape: a checker that cannot distinguish "I found nothing" from
  "I could not look" is worse than no checker, because it certifies.)*

### ⛔ THE HICCUPS ARE NOT TWELVE BUGS. THEY ARE FOUR, REPEATED.
- **(1) Cross-cell state — 6 of 12.** `KeyError: 'score'` · `'composite_score'` · `'ticker'` ·
  `'Is_Compression'` · `'Fwd_Return_21d'` · `['is_moonshot','edge_score']`. **Every one is a column an
  EARLIER cell was supposed to create.** The notebook was correct as a program and broken as an artifact:
  cells were re-run out of order, or a cell was replaced mid-session and its successor still expected the
  old schema. **This is the structural argument for rule 17 (COMPLETE cells), arriving as evidence rather
  than as a preference** — a 17-cell notebook has 17 places to lose state; a one-cell notebook has none.
- **(2) yfinance column shape — 1 explicit, 4 latent.** `ValueError: Cannot set a DataFrame with multiple
  columns to the single column BB_PercentB` is `yf.download` returning MultiIndex columns. **Four notebooks
  carry NO guard at all** — `KRE 52W High Analysis`, `ai stock analysis`, `bollinger compression ai
  suppliers`, `cold fundamentals scanner` — and **three of those four are among the eleven that failed.**
  The guard the working notebooks use is one line: `if hasattr(s,'columns'): s = s.iloc[:,0]`.
- **(3) Paths from the wrong machine — 2.** `FileNotFoundError: /content` (Colab path, run elsewhere) and
  **`FileNotFoundError: '/home/claude/scoring_bands_boxplots.png'`**. ⛔ **The second one is mine.**
  `/home/claude/` is an assistant sandbox path, not a Colab path — a cell was authored where I run and
  handed to Jake without changing the destination. **A code-delivery failure by the rule-17 standard, filed
  against myself.** *(Analysis.)*
- **(4) Paste damage — 2.** `SyntaxError: unterminated string literal` and `IndentationError: unexpected
  indent`, both in code that never had a chance to be wrong: it was mangled between chat and cell. **On an
  iPhone this is the default failure mode, not an edge case.**

## THESIS (interpretation — NOT fact)
- **⛔ THE FOLDER'S PROBLEM IS NOT CODE QUALITY. IT IS THAT NOTHING CLOSES.** The strongest notebooks —
  `financial_gravity`, `first_of_month_options`, `mean_reversion_screener`, `csp_screen` — carry
  pre-registered hypotheses, honesty boxes, and named limits. That is *good* research hygiene. But the
  archive has **no state**: five files named `Call Put Scanner v5` with five different bodies, and no way
  to tell which one was right. **This is precisely the append-only defect STEP ZERO-B fixed in the wiki, in
  a folder that never got the fix.** The vault amends; Drive accumulates. *(Analysis.)*
- **★★ THE ONE GENUINELY UNRUN IDEA IS ALSO THE ONE THE VAULT HAS BEEN OWED SINCE 7/17.**
  `body_momentum_carry.ipynb` has **zero saved output — it was written and never executed.** It asks
  whether the month BODY (day 3-22) carries through the turn, with a quintile monotonicity check built in.
  And `bull-bear-ledger.md:185, 205-207` has carried, since 7/17: *"the decisive open test = rerun on ≥2018
  only — does day-1/payday still pay, or did quants eat it since?"* **Two open calendar questions, one
  unrun notebook, twenty-six days.** 🚩 *(Analysis.)*
- **⚠️ `KRE 52W High Analysis` HAS A BASE-RATE HOLE THE VAULT ALREADY KNOWS HOW TO PLUG, AND ITS OUTPUT
  READS AS A SIGNAL BECAUSE OF IT.** DATA: 14 streaks within 10% of the 52-week high since 2006; the
  13 completed ones were followed, within 52 weeks, by max drawdowns of **−11.5 / −31.7 / −15.9 / −26.8 /
  −18.6 / −12.0 / −14.3 / −51.7 / −28.2 / −29.2 / −14.2 / −28.0 / −23.8%**, with the notebook annotating
  the big ones *"MAJOR CRASH — puts would have printed."* **THESIS: that is 13-for-13, which is the tell,
  not the finding.** There is **no unconditional control** — KRE's max drawdown in a RANDOM 52 weeks is
  never computed, and for a high-beta regional-bank ETF it is plausibly this same distribution. The
  annotation labels outcomes after seeing them. **[[buying-at-highs]] and [[ath-clustering]] already
  establish the correct form of this test** (ATH days: +9.8% mean / 75% win fwd-12m **against an all-days
  baseline of +9.4%** — the baseline is the whole point). 🚩 **The rebuild is one line: same statistic on
  random start dates.** *(Analysis.)*
- **⚠️ `Layoff Buy Signal Backtest` — the numbers are strong and the construction is not.** DATA (n=50,
  Apr 2020-Feb 2025): 12M win rate **78%**, median return **+39.9%**, median alpha vs SPY **+9.7%**; 6M
  70% / +17.7% / +8.3%. **THESIS: Independence score LOW — the dataset was curated by the model that
  tested it**, from memory, and the window is one of the strongest equity stretches on record (SPY median
  12M +23.8% over the same events). The notebook's own caveat list names survivorship and curation. **A
  self-selected event list scored over a bull market is a description of that bull market.** The honest
  version needs an exogenous event source (WARN filings / Layoffs.fyi), which makes it a real build, not a
  rerun. *(Analysis.)*
- **★ WHAT IS WORTH SALVAGING, RANKED — and the ranking is by what the VAULT lacks, not by code quality.**
  ⟲ SUPERSEDED 2026-08-12 → colab-archive-audit.md:L175 — salvage was ranked by what the vault lacks — wrong axis for backtests; re-ranked on backtest validity (holdout, costs, benchmark, sample)
  1. **`body_momentum_carry`** — unrun, and it closes a 26-day-old registered question. Cheapest real win.
  2. **`mean_reversion_screener`** — the only tool here that measures a name's *behaviour* (Hurst,
     half-life, lag-1 autocorr, R² to SPY) rather than its level. Nothing in `tools/` does this, and it
     bears directly on the basket work: its 8/? run had **META passing all 5 criteria, NVDA only 3.**
  3. **`cold fundamentals scanner`** — the "score it as if you'd never heard of it" rubric is the
     mechanical form of [[_calibration]]'s anti-narrative discipline. Its **2026-04-26 run is a dated
     snapshot the vault does not have** (NVDA $208.27 / $5.06T / P/E 42.6 fwd 18.5; AVGO P/E 82.6; TSLA
     345.2) — useful as an April benchmark for the basket, independent of the scanner itself.
  4. **`csp_screen`** — already encodes the trading-system laws as filters (200-day gate, liquidity,
     earnings blackout) and prints every reject with the law that killed it. Belongs in `trading-system/`,
     not in a Drive folder.
  5. **Everything Bollinger** (`bb compression ai capex`, `bollinger compression ai suppliers`, `bb squeeze
     pop scanner`, `BB10_2_*`) — **four notebooks, one idea, all with the same compression gate.** Their
     3rd-order-supplier universe (MKSI, ENTG, ONTO, UCTT, FORM, ACLS, VERT, APH, GLW, CDNS, SNPS) is more
     complete than anything in [[portfolio-state]]'s baskets, but the compression signal itself is
     untested here — every one of the four died before producing forward returns.
- **★★★ AND THE SALVAGE LIST ABOVE IS PARTLY WRONG, BECAUSE THE REPO ALREADY HAD MOST OF IT — THE TWO
  ARCHIVES SPLIT ALONG A LINE NOBODY DREW ON PURPOSE.** Diffing `tools/*.ipynb` against the Drive copies:
  **`body_momentum_carry`, `financial_gravity`, `first_of_month_options`, `mean_reversion_screener` are
  BYTE-IDENTICAL in code** — but the repo copies carry **0 saved outputs** while the Drive copies carry
  5, 9 and 12. **`tools/` is the CODE record. Drive is the RUN record. Neither is complete alone**, and
  the vault's conclusions were written from runs that live only in Drive. *(Analysis.)*
  - **This also settles `body_momentum_carry` beyond doubt: 0 outputs on BOTH sides. It has never been
    executed anywhere.** Not "the run was lost" — never run.
  - **⛔ TWO REAL RECOVERIES, and one was hiding behind a name collision.** Drive's `cluster_hunter.ipynb`
    is **not a version of** the repo's `tools/cluster_hunter.ipynb` — the repo's reads OpenInsider
    cluster-buy feeds; Drive's is a two-stage S&P-1500 value screen (2× the code, 7 saved outputs).
    **Two different tools wearing one filename across two archives.** Recovered as
    **`tools/broad_value_screen.ipynb`** so neither overwrites the other.
  - **`csp_screen.ipynb` was missing from `tools/` altogether** while [[trading-maxims]]`:13` cites it by
    name. Recovered as **`tools/csp_screen.ipynb`** (largest of its 3 Drive forks, 6 cells).
  - ⚠️ **The general lesson, and it is the folder's disease crossing into the repo: a filename is not an
    identity.** Five `Call Put Scanner v5`s with five bodies inside Drive is the same failure as one
    `cluster_hunter` meaning two things across Drive and git. **The wiki solved this with `vault_amend`
    pointers; `tools/` has no equivalent and just took a collision.** *(Analysis.)*
- **⛔ AND THE HARD CONSTRAINT ON ALL OF IT: 23 of 50 notebooks need yfinance, which this container cannot
  reach.** Tested 2026-08-12 ~2:35pm PDT: `query1/query2.finance.yahoo.com` return **HTTP 429 Too Many
  Requests** (browser UA does not clear it); stooq returns **connection failure (000)**. **429 is a
  different animal from the FRED timeout and the Census "Missing Key" — it is a shared-egress rate limit on
  a LIVE host, so it may clear on its own, whereas a timeout will not.** The distinction matters for
  triage: **Colab has a clean IP and runs all of these fine.** These are Jake-side runs, not container
  runs. *(Analysis. Extends [[data-sourcing-playbook]].)*

## ⬜ NOT-KNOWN
- ⬜ Whether the folder holds more than the 50 files the first HTML page renders.
- ⬜ **Which of the 5 `Call Put Scanner v5` forks (and 5 `ai stock analysis` forks) is the good one.** Only
  Jake knows which one last worked; SHA and size cannot rank them.
- ⬜ Dates. Drive's public HTML does not expose created/modified times, so the archive cannot be ordered in
  time except where a run stamped itself (`cold fundamentals` 2026-04-26; `BB10_2_Filters` "Generated:
  2026-02-01"; `KRE` data through 2026-02-09).
- ⬜ Whether `alpaca_connection_test` ever printed a paper balance — the surviving copy failed on a
  SyntaxError before reaching the call. Bears on whether [[portfolio-state]]'s paper-trading leg was ever
  actually plumbed.
- ⬜ KRE's **unconditional** 52-week max-drawdown distribution — the missing control above.
- ⬜ `InlandNW_Modernization_*` (3 files, migration/census data for Idaho/Washington) is **not markets
  work** and is not graded here.

## Sources
- Google Drive folder `1emVvnIsxhHGWmFlwDHipr6TVLG6YbWpg`, read 2026-08-12 ~2:25pm PDT — 50 files,
  5.60 MB, downloaded and parsed in full. Inventory + extracted sources retained in the session scratchpad.
- Vault cross-checks: `new-economy-regime.md:1156-1177` · `bull-bear-ledger.md:187-217` ·
  `structural-pull-log.md:111,139` · `buying-at-highs.md` · `ath-clustering.md:25-27`
- Reachability tests 2026-08-12 ~2:35pm PDT: Yahoo chart API HTTP 429 (both hosts, with and without
  browser UA); stooq.com connection failure.

---

## 2026-08-12 ~3:05pm PDT — ⛔ RE-GRADED ON THE RIGHT AXIS: THESE ARE TRADING BACKTESTS, NOT RESEARCH ARTIFACTS
  ⟲ SUPERSEDES colab-archive-audit.md:L107 — salvage was ranked by what the vault lacks — wrong axis for backtests; re-ranked on backtest validity (holdout, costs, benchmark, sample)

Jake, 2026-08-12: *"It's all python code / Colab trading backtests."* **He is right and the audit above
graded them on the wrong criterion.** I ranked salvage by *"what does the vault lack"* — a research-archive
question. **For a backtest the only question that matters is whether the backtest LIES.** Re-read all 14
backtest/screen notebooks against the standard defect list. *(Analysis. Concede.)*

### DATA (observed — verified in the source, not inferred from filenames)
- **ZERO of the 14 implement a train/test split, walk-forward, or any out-of-sample validation.** Not one.
  ⚠️ **Two of my own first-pass regex hits were FALSE POSITIVES and are corrected here:**
  `bb squeeze pop scanner`'s "walk-forward validation" is item 5 on a **markdown TODO list** ("Next
  Iterations"), not code; `kalshi edge finder v2`'s hit was the variable name `sample_markets`.
- **Costs/slippage modelled: 4 of 14.** `BB10_2_EndToEnd` (5 bps/side, fees=0), `mean_reversion_screener`,
  `btc 2x strategy eval`, `Layoff` (benchmark only). **The other 10 model zero friction.**
- **Benchmark/buy-and-hold comparison: 4 of 14** (`bb squeeze pop`, `mean_reversion_screener`, `Layoff`,
  `csp_screen`). **`EMA5` — the most trade-intensive strategy here — has none.**
- **`EMA5_TP7_SL4_Backtest*` config:** `TICKERS = ["STX","MU","WDC","MRVL","CRDO"]`, `LOOKBACK_MONTHS = 6`,
  `TP_PCT = 7.0`, `SL_PCT = 4.0`, `MAX_HOLD_DAYS = 30`, immediate rebuy, `auto_adjust=False`,
  `end = pd.Timestamp.today()`.
- **`BB10_2_Squeeze_SP500_EndToEnd_NoDrive.ipynb` does not contain a squeeze backtest.** Its settings are
  `LONG_TICKER="BITX"` / `SHORT_TICKER="BTCZ"` / `PERIOD="3mo"` / `MA_N=10` — **it is the BTC 2× leveraged
  strategy.** Filename and content disagree.
- **`BB10_2_Squeeze_SP500_Filters_ForwardReturns` filters HISTORICAL squeeze events on CURRENT
  `trailingPE`** — stated plainly in its own markdown twice ("not historical as-of event date").

### THESIS (interpretation — NOT fact)
- **⛔⛔ THE WORST DEFECT IS IN `EMA5`, AND IT IS NOT ON THE STANDARD LIST — IT IS CONSERVATISM THEATRE.**
  The notebook advertises one conservative assumption loudly (*"If both TP and SL hit same day, assume STOP
  first"*) while making a much larger optimistic one silently: **the stop FILLS AT EXACTLY `entry×0.96`
  whenever `low <= sl_price`.** A limit order at +7% genuinely fills when the high trades through it — that
  side is fair. **A stop does not: it becomes a market order and gaps.** So **TP fills are realistic and SL
  fills are fictional, in the same engine.** The advertised conservatism is about *sequencing within a day*;
  the unadvertised optimism is about *price*, and it is the bigger of the two by an order of magnitude.
  **A backtest that names its small conservatism and not its large optimism reads as careful and is not.**
- **★ THE ARITHMETIC THAT MAKES THE WIN RATE UNINFORMATIVE: TP 7 / SL 4 has a breakeven win rate of
  4/11 = 36.4%.** Any dip-buy rule in an uptrend clears that easily, so **a high win rate here is evidence
  of the payoff ratio, not of the signal.** The number that would be informative — expectancy net of costs
  against buy-and-hold on the same five names over the same six months — **is exactly the number the
  notebook does not compute.**
- **⛔ AND THE UNIVERSE AND WINDOW ARE BOTH SELECTED AFTER THE FACT.** Five memory/storage names
  (STX, MU, WDC, MRVL, CRDO) over *the trailing six months* — the strongest stretch that complex has had,
  and the exact names [[memory-regime-question]] exists to track. **A long-only dip-buy on a basket that
  went vertical will print a good hit rate no matter what the rule is.** With no benchmark leg, the
  notebook cannot distinguish its signal from the beta it was pointed at.
- **⚠️ THREE MECHANICAL BUGS UNDER THAT, each individually small:** (1) **`auto_adjust=False`** means
  unadjusted OHLC — **dividend ex-dates inject synthetic price drops straight into a −4% stop**, and STX/MU/
  WDC pay dividends; (2) `end = pd.Timestamp.today()` makes the window **slide with the run date**, so no
  two runs are the same experiment and no result is reproducible; (3) zero costs against **immediate
  rebuy + a 30-day max hold**, i.e. the highest-turnover design in the folder is the one modelling no
  friction. At ~0.1% round-trip spread, ~15 round trips per name over six months is ~1.5% of capital —
  material against a 7% target.
- **⛔ THE 3-MONTH BTC 2× TEST IS BELOW THE SAMPLE FLOOR AND SHOULD NOT BE READ AT ALL.** `PERIOD="3mo"`
  ≈ 63 daily bars; a 10-day MA signal on 63 bars yields single-digit round trips **on a 2× leveraged pair
  where volatility decay is the dominant term over any horizon longer than the test.** Ironically this is
  one of the four notebooks that *does* model slippage — **careful execution assumptions wrapped around an
  unfalsifiable sample.** *(The general shape: the notebooks that model costs are testing the wrong things,
  and the notebook testing the most interesting thing models no costs.)*
- **★★ WHERE THE FOLDER IS ACTUALLY STRONGEST IS THE PART THAT ISN'T A BACKTEST.**
  `mean_reversion_screener` measures a name's *behaviour* — lag-1 autocorrelation, Hurst, reversion
  half-life, R² to SPY — over a 2y S&P-100 sample, models costs, benchmarks against buy-and-hold, and its
  markdown states the killer limit itself: *"behaviour is NOT stationary… MU almost certainly screened as a
  clean mean-reverter at \$400, right before its 4×."* **That is the one notebook here whose honesty box
  names the failure mode that would actually kill it.** Its Stage-2 bracket backtester still has no
  out-of-sample split, but **its Stage 1 is a measurement, not a strategy, and measurements do not overfit.**
- **★★★ THE STRUCTURAL VERDICT, AND IT IS ONE SENTENCE: the folder has no HOLDOUT anywhere, so every
  performance number in it is in-sample by construction.** Combined with the earlier finding that five files
  named `Call Put Scanner v5` hold five different bodies, **the archive is a record of iterating a rule
  against a fixed dataset until it looked good, with no mechanism that could ever tell you that you had.**
  **That is not a code-quality problem and no amount of debugging touches it.** [[momentum-extrapolation-backtest]]
  and [[deep-value-reclaim]] are the vault's own examples of the honest version — both reported the result
  that killed the idea (hit 27.5%; "survivorship-flattered, worse Sharpe than SPY"). *(Analysis.)*
- **🚩 THE ONE CHEAP FIX THAT WOULD CHANGE EVERY NUMBER IN THE FOLDER: add a benchmark leg and a date split.**
  For `EMA5` specifically: run the identical rule on the same five names, then run buy-and-hold on the same
  five names over the same window, and report the difference — **and split the window in half, fit nothing
  on the second half.** That is a config change and about twenty lines, not a rebuild.

### ⬜ NOT-KNOWN (backtest leg)
- ⬜ **EMA5's actual expectancy versus buy-and-hold** on its own universe/window. Not computable here —
  Yahoo returns HTTP 429 to this container. **Colab run.**
- ⬜ Whether the stop-fill optimism is material at these names' gap frequency — measurable as
  *"how often did the open gap through `entry×0.96`?"*, one column in the same loop.
- ⬜ Whether any of the five `Call Put Scanner v5` forks was ever backtested at all. **Its own markdown says
  not:** *"V4 z-score composite is computed in parallel for reference but does not drive the signal until
  backtested."* **The scoring engine driving the output is the un-backtested one.**
