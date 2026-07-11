# Fear Duration Study — does how LONG the market stays afraid predict bear vs recovery? (2026-07-11)

Jake's question: "if there's a way to gauge base market fear through actionable events, how much time
passes in that state — does the length of time correlate with an actual bear or contraction vs
compression and recovery?"
Tool: chat cell 2026-07-11 (VIX episodes 1990-present). Related: [[market-fragility]],
[[runner-anatomy]] (panic windows = these episodes' bottoms), [[_calibration]].

> Firewall: nothing below is a result. Pre-registered BEFORE the first run.

## Design
- Fear state = VIX episode: opens on cross ≥25, closes after 5 consecutive days <20 (hysteresis).
- Per episode: PEAK (intensity), DURATION (days), INTEGRAL (area above 20 = intensity x time),
  drawdown during, forward S&P 3m/12m from episode END, bear label (≥20% dd within 18m of start).
- ⚠️ Sample honesty: VIX exists from 1990 → only ~6-8 consequential episodes. Suggestive, never proof.

## PRE-REGISTERED HYPOTHESES
- **H1:** Peak VIX does NOT separate bears from recoveries (2020: peak 82, V-recovery; 2022: peak <40,
  grinding -25% bear).
- **H2:** DURATION separates: <~30 days → compression-and-recovery; >~90 days → bear/contraction.
- **H3:** The INTEGRAL beats either single measure.
- **H4 (limitation, stated up front):** duration confirms with a LAG (by day 60-90 much drawdown is in) —
  the signal's value is RE-ENTRY GOVERNANCE, not top-calling: short fear = buy the recovery early;
  long fear = the first rally is usually a trap. A don't-buy-the-first-dip detector.
- **H5:** Time-to-recover scales NONLINEARLY with fear duration.
- If validated → second regime instrument beside the median filter: price line governs core pace;
  fear-duration state governs dip treatment under stress (different failure modes: median whipsaws in
  fast crashes; fear duration can't be faked by a quiet grind).

## RESULTS
*(pending — Jake runs the cell, pastes episode table + test block; hypotheses graded visibly.)*
