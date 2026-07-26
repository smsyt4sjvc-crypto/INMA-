# Deep-Value Reclaim — furthest under the 200-SMA, back above the 20-SMA

Jake's screen (2026-07-25, built ~6:48pm PT): buy the S&P names FURTHEST below their 200-day SMA that have reclaimed
their 20-day SMA — deep drawdown + a trend-turn trigger. Note the tension: it INVERTS the Tudor Jones 200-day rule
("nothing good happens below the 200-day" — [[defense-not-offense]], [[trading-maxims]]) on the position axis, while
using a Jones-style trend trigger (the 20-day reclaim) as the entry catalyst. Tool: `tools/deep_value_reclaim.ipynb`.
Companions: [[dip-buying-base-rates]], [[median-line-dip]], [[seeing-vs-predicting]].

## DATA (observed — backtest run 2026-07-25, Yahoo v8 adjusted closes, 10y, 502 current S&P constituents)
- Method: monthly rebalance (last trading day), eligible = close < 200-SMA AND close ≥ 20-SMA, rank by %-below-200,
  buy deepest N=10 equal-weight, hold 1 month. Since 2017-06. No costs/taxes.
- **Strategy: 21.0% CAGR · −45.8% maxDD · 26.1% vol · Sharpe 0.86** (growth of $1 → $5.62)
- **Same screen WITHOUT the 20-SMA filter: 18.2% CAGR · −57.8% maxDD · 43.1% vol · Sharpe 0.58**
- **SPY same dates: 15.0% CAGR · −23.9% maxDD · 15.9% vol · Sharpe 0.95** ($1 → $3.54)
- N=20 variant: 19.1% CAGR, −37.4% maxDD, Sharpe 0.87. Weekly rebalance ≈ monthly (20.8% CAGR) — robust to frequency.
- Beats SPY in only **54% of months** (corr 0.76). Monthly mean +1.86% vs SPY +1.26%; best +22.9% / worst −26.1%
  (SPY: +12.7% / −12.5%) — the edge is fat right-tail months, not consistency.
- By year: **wins are recovery-year concentrated** — 2020 +54.7% (SPY +18.3), 2023 +65.0% (SPY +26.2), 2019 +42.0;
  **crushed in sustained bears** — 2022 −34.3% (SPY −18.2), 2018 −10.7% (SPY −4.6). 2026 YTD +22.1% vs SPY +8.9%.
- ⚠️ artifact — **SURVIVORSHIP BIAS, and it flatters THIS strategy specifically**: universe = TODAY'S constituents, so
  every deeply-fallen pick is a known survivor; real-time deletions/zeros are invisible. Every bias in the test points UP.

## THESIS (interpretation — NOT fact; analysis)
- *(the filter is the finding)* The 20-SMA reclaim requirement added ~3 points of CAGR while CUTTING vol nearly in half
  (43%→26%) and maxDD by 12 points vs raw knife-catching. Jake's "catalyst" leg is doing real work — the naked
  "deepest under 200" screen is mostly uncompensated volatility.
- *(what the strategy IS)* A crash-recovery harvester: it buys washed-out survivors once they stabilize, so it prints in
  V-recovery years (2020/2023) and bleeds in grinding bears (2022: 20-day reclaims inside downtrends = bear-market
  rallies, the classic trap). Higher CAGR than SPY, WORSE Sharpe — you're being paid in extra return for carrying nearly
  double the drawdown, not getting a free lunch.
- *(fits the vault's dip law)* Same shape as [[dip-buying-base-rates]]: sign is a coin flip (54% monthly hit rate),
  magnitude is fat-tailed. The edge concentrates exactly where the ATH-drawdown ruler says to deploy powder — AFTER
  washouts — which the survivorship caveat also inflates most.
- *(honest read)* Real-world (survivorship-corrected, costs, taxes) this likely lands near-SPY return with double the
  pain — UNLESS deployed selectively in post-washout regimes, where its documented edge lives. As a standing always-on
  system: no. As a recovery-regime playbook: the numbers justify a second look.

## Falsifier / regrade
- Rerun the notebook anytime (today's-screen cell shows current picks). If a real historical-constituent universe ever
  gets tested and the edge survives deletions, the survivorship caveat softens; until then treat reported CAGR as ceiling.
