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
