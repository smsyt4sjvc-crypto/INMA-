# top10_band_test.py — is the S&P top-10 cohort's movement predictable? (Colab cell)
# Jake's question 2026-07-09: top-10 by weight (~35-40% of index), 1yr back, find bands/patterns,
# measure predictability. Design: falsifiable tests, not chart-shapes —
#   (1) daily-return autocorrelation (near 0 = noise = the honest usual answer),
#   (2) 20d ±2σ band-touch events -> forward 5/10/20d returns + win rates (n will be small — thin-sample
#       warning built in; rerun period='5y' before trusting anything),
#   (3) THE RATIO top10/RSP = the concentration oscillator — levels trend (bands break), spreads
#       mean-revert (bands hold); if structure exists it's likely here, and it times the
#       de-concentration thesis ([[concentration]]),
#   (4) SPY as control (if top-10 tests no better than SPY, concentration adds no predictability).
# Caveats: today's weights applied backward; ~dozen events/yr can suggest, never prove.
# Full cell lives in chat 2026-07-09; paste output back for the read.
#
# RESULT (run 2026-07-09, 5y backtest, Jake's Colab) — STRATEGY KILLED:
#   Top-10 composite dip-buy (sell +3% or 5d): avg trade NEGATIVE at all depths
#   (-2%: -0.05 | -3%: -0.22 | -5%: -0.40), hit rates 32-41%, worst trades -9 to -10.6%.
#   Deeper dips = worse expectancy → MEGA-CAPS TREND; dips continue more than they bounce in 5d.
#   QQQ: one marginal green cell (-5%: +0.26 avg, 35% hit) = noise (1 of 6 configs) ≈ +2.3%/yr gross
#   with a -7% tail — SPAXX beats it. On 5y of mostly-bull data: definitive NO.
# KEPT: the movement ruler — top-10 unit: ~1.0%/day typical (2.95% = 90th pct day),
#   ~2.4%/wk typical (6.2% big week); +3% weeks 24% vs -3% weeks 16% = the edge is the DRIFT,
#   captured by holding, not timing. Composite more volatile than QQQ (1.00 vs 0.79%/day) with
#   worse dip stats — concentration adds vol without adding mean-reversion.
# ⚠️ Do not knob-turn until a cell goes green (data-mining). Legit iterations only: 200dma trend
#   filter, or weeks-months horizons. First backtest = first kill = the machine works.
