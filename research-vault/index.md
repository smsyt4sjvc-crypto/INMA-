# Vault Index — the map (read after CLAUDE.md)

Table of contents for the `wiki/`. Read `CLAUDE.md` first (identity + rules), then this (what exists + where).
43 notes, 66 raw sources, 27 tools. Last built: 2026-07-18. Regenerate when notes are added/renamed.

> Two domains, two brains: THIS vault = markets research. The **trading system** is a SEPARATE repo
> (`Alpaca-Claude`) with its own `CLAUDE.md` — staged in `trading-system/` (one domain per vault).

## ⭐ Read-first / meta
- [[_persona]] — response contract (how to engage Jake: no pandering, peer not cheerleader)
- [[_calibration]] — the pushback filter (argue the side he's under-weighting)
- [[_origin-assessment]] — the first-message ChatGPT profile of Jake, graded against months of reality
- [[_assumption-filters]] — pre-flight for any load-bearing thesis (Goodhart/Hanlon/Occam/Chesterton + narrative-tiers)
- [[data-sourcing-playbook]] — offload heavy fetching, keep the chat lean

## 🧭 The thesis spine (start here)
1. [[consumption-vs-investment-crux]] — THE top question: did post-COVID borrowing build or drink?
2. [[new-economy-regime]] — the macro-database read (Fed Trap / debasement in the series)
3. [[market-fragility]] — the top-level regime read (narrow-market STATE, timed by triggers)
4. [[ai-capex-cycle]] → [[cepi]] — the fragility's fundamental driver (Capex→Earnings→Price Intensity)
5. [[power-not-petroleum]] → [[demand-destruction]] — the energy rotation / oil
6. [[fragility-engine]] — the code that scores it all into one number
7. [[portfolio-state]] — the running truth of the book (+ account constraints)

## 🤖 AI capex / compression / financing
- [[ai-capex-cycle]] — the buildout cycle
- [[compression-thesis]] — Jake's positive spine: how the AI-capex corner resolves (input-deflation heal; the razor)
- [[ai-financing-fragility]] — the debt leg (private credit → the funding squeeze; the tripwire)
- [[ai-infra-allocation-map]] — the names, sorted
- [[buildout-bottleneck-map]] — the next unrepriced layer
- [[cepi]] — Capex → Earnings → Price Intensity
- [[trade-down-landing-pads]] — who catches the falling customer
- [[concentration]] — concentration & breadth

## ⚡ Power / energy / oil
- [[power-not-petroleum]] — the core energy-rotation thesis
- [[power-scarcity-equities]] — the three tiers (and the bottleneck≠hedge correction)
- [[nuclear]] — the AI-power sleeve
- [[demand-destruction]] — oil / war fuse (Hormuz, Red Sea, the buffered-shortfall thread)
- [[civilian-infra-strike-log]] — dated ledger, both sides: non-military / civilian-impact strikes (power/water/telecom)

## 🩻 Fragility / regime / breadth
- [[market-fragility]] — the regime read
- [[fragility-engine]] — "the brain" (the score)
- [[new-economy-regime]] — the macro-DB read
- [[detachment-bid]] — the standing bull vector
- [[bull-bear-ledger]] — the whole debate, counted honestly (+ the mechanical-bid & VRP studies)
- [[buying-at-highs]] — the ATH framework
- [[ath-clustering]] — do all-time-high clustering/spacing/droughts predict?
- [[fear-duration]] — does how LONG the market stays afraid predict bear vs recovery?
- [[rotation-stickiness]] — when a tech→defensive rotation persists vs snaps back

## 💰 Where the edge is (→ the trading system)
- [[how-to-get-paid]] — the four buckets, and which one is Jake's (keystone)
- [[where-the-edge-is]] — get PAID to bear risk, don't predict (keystone; the VRP verdict lives here)
- [[defense-not-offense]] — the Tudor Jones discipline anchor (the behavioral half: survival, not prediction)
- [[trading-maxims]] — the sticky one-liners, each mapped to a validated law/study (Buffett, PTJ)
- [[retail-edge]] — retail-edge doctrine ("most successful retail system for straight ROI?")

## 🪙 Gold / debasement / flows
- [[gold-flows]] — central-bank vs ETF-tourist flows (the debasement referee)
- [[live-flow-trackers]] — MOSO + RVOL (free)
- [[structural-pull-log]] — weekly positioning/filings baseline

## 🔬 Studies / screens / synthesis
- [[who-gets-paid-12m]] — the next-12-months synthesis
- [[cluster-shortlist-workup]] — E-path workup on the 15 names
- [[quiet-health-screen]] — value × health × no-story
- [[runner-anatomy]] — what 200%+ 12-mo runners looked like at ignition
- [[weekly-momentum]] — NDX top-5 weekly winners: carry, duration, threshold
- [[median-line-dip]] — the median/LAD line as a dip trigger (wins 1-3mo, loses 12mo; test-run result)

## 📜 Process / policy
- [[ioss-proposal]] — iOSS policy project (Jake's)
- [[data-sourcing-playbook]] — (also under meta)

## 🛠 Tools (`tools/`, 27 files — run in Colab, token-free)
Edge/premium: `vol_risk_premium.ipynb`, `vol_risk_premium_decay.ipynb`, `passive_bid_fingerprint.ipynb`,
`mechanical_bid_patterns.ipynb`, `first_of_month_options.ipynb`, `momentum_through_first.ipynb`,
`body_momentum_carry.ipynb`, `sma_20_50_regime_backtest.ipynb`, `memory_intraday_close.ipynb`,
`median_line_dip_study.ipynb` (straight LAD/median trend vs SMA/%-off-high/rolling-median as a dip trigger).
Screens/scanners: `insider_trading_scanner.ipynb`, `vault_headline_scanner.ipynb`, `mean_reversion_screener.ipynb`,
`spy_weekly_poc_scan.ipynb`, `power_equipment_screen.ipynb`, `sp500_health_screen.py`, `cluster_hunter.ipynb`,
`ignition_filter.py`, `runner_anatomy.py`, `follow_the_money.ipynb`, `structural_pulls.py`, `flow_trackers.py`,
`monday_flows.py`, `top10_band_test.py`, `weekly_stack.ipynb`, `cluster_backtest.ipynb`, `insider_pull.py`.

## 🎯 Predictions (`predictions/`) — the calibration engine
Nightly point + 80% range + direction + kill-switch for the core five; graded next session → `_scoreboard.md`.

## 📁 Trading system (`trading-system/` → transplants to repo `Alpaca-Claude`)
`constitution.md` (constraints→vehicle→laws→roadmap), `CLAUDE.md` (the 8 laws), `README.md`,
`alpaca_connection_test.ipynb`, `.gitignore`, `.env.example`. Separate domain, own brain.
