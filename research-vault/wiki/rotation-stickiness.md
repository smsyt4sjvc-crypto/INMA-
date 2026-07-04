# Rotation Stickiness — when a tech→defensive rotation persists vs snaps back

The framework for judging whether a "money leaving tech, into defense/gold/healthcare" day is
the start of a regime or a 48-hour flush. Built 2026-07-03 off the candle-scan below.
Related: [[market-fragility]], [[concentration]], [[new-economy-regime]], [[detachment-bid]],
[[live-flow-trackers]], [[portfolio-state]].

> Firewall: DATA = the scan + observable base rates. THESIS = the stickiness model (analysis).

## DATA — the triggering scan (2026-07-03, candle scan, `tools/flow_trackers.py`-style)
- **Clean one-way de-risking day.** Sector roll-up (avg % move): Defense **+4.7**, Gold **+3.7**,
  Health **+3.0**, Staples **+3.0** at the TOP; Semis **−4.2**, AIinfra **−4.7**, Power **−1.1** at the BOTTOM.
- **Conviction confirmed by close-location:** greens closed at/near highs (Defense/Health/Staples
  clsLoc ~0.95–1.00 = bought all day); reds closed at/near lows (MRVL 0.21, NBIS 0.28, META 0.08,
  TSLA 0.10 = sold all day, no dip-buying). Directional, not chop.
- **Volume caveat:** rvol mostly ~1.0 (normal, not a panic spike) → orderly de-risking, not capitulation.
  ⚠️ MRVL −9.8% on rvol **0.6** (below-avg volume) = thin/gappy, trust that specific size less.
- **Base rates (observable history):** sharp-tech-down/defensive-up days occur many times per bull
  market; the majority resolve as V-bounces within 1–3 weeks (e.g. 2018-Q4 flushed then fully
  recovered; 2023–24 wobbles same). The minority that mark true tops (2000, 2007, 2022) → defensives
  led for quarters-to-years. Day-1 looks identical in both.

## ⚠️ Correction to prior read (firewall rule 4 — wrong reads stay)
- **2026-07-02/03 WebSearch sector read was YTD-lagged and wrong for the current tape.** It reported
  Healthcare *weakening*, Defense *underperforming*, Energy/Industrials/Materials *leading* (reflation).
  The bottoms-up candle scan says the **opposite**: Defense/Gold/Health/Staples leading, Energy/Indu
  middling, Semis/AIinfra dumping (**risk-off**, not reflation). The tape beat the search — same
  "go to the source" lesson as the ChatGPT stale-macro catch. Weight direct scans over search for *current* momentum.

## THESIS (the stickiness model — NOT fact)
- *(analysis, the core model)* **Valuation sets the DEPTH. Catalyst + Fed set the TIMING & stickiness.
  Concentration sets the TAIL.** Overvaluation only says how far it *can* fall — never that it starts now
  or persists. The rotation itself isn't sticky; the **earnings deceleration under it** is.
- *(analysis)* Stickiness lives on the **funding side** (tech bleeding), not the destination side
  (defensives ripping). In an over-owned, concentrated regime the unwind self-feeds (crowded exit →
  CTA/passive de-gross → [[concentration]] / Vector 11) → tech downside has a mechanical tail even if
  the defensive upside is modest.
- *(calibration — the side Jake under-weights)* "Usually sticky" **overstates the base rate.** On any
  single day, mean-reversion/bounce is the majority outcome; P(sticky) is LOW unconditionally, HIGH only
  *conditional on a real top* — and you cannot tell which from the rotation alone. One clean day ≠ regime.
- *(analysis — why THIS one has better-than-base odds)* Three stickiness conditions are unusually present:
  1. **Real catalyst** (Meta capex cut / compute-crack / memory+H100 pricing — [[ai-capex-cycle]]) — earnings
     decel is the ingredient that turns flush→regime. Present, not proven.
  2. **Hawkish Fed = no put** ([[new-economy-regime]], Warsh) — removes the #1 killer of defensive rotations
     (Fed blinks → tech V-bounces). Biggest structural point in favor.
  3. **Record concentration** — the mechanical tail is loaded.
  → Conditional, not confirmed. **The confirm is the leading-indicator set, not today's candles:** H100
  rental, DDR5 pricing, Aug-28 QCEW, next earnings guides. Roll → sticks. Hold + Fed dovish hint → flush.
- *(analysis — persistence ranking of the destinations)* **Gold is the stickiest leg** (real rates /
  debasement / CB buying = structural, multi-quarter, not positioning; rarely reverses in days).
  Defense & healthcare give more back on a tech bounce. If weighting which defensive *holds*: gold > defense/health.

## Book implication (descriptive, not advice — [[portfolio-state]])
- Jake's heavy sleeve (Semis: MU/MRVL/NVDA-adj; AIinfra: NBIS/CRWV) **is the funding source** — bottom of
  the scan. SPY Dec puts favored by exactly this tape. LLY (Health) on the right side today.
- ⚠️ **Power sleeve traded as AI-beta, not defensive** (Power −1.1, SMR −3.8 closed at low) — GEV/VST/OKLO/SMR
  correlated to the thing cracking, NOT hedged against it. Contradicts the "utilities improving" search read.

## Falsifiers (what kills the sticky read)
- Tech V-bounces within 1–3 weeks on no fundamental change → it was a flush (base-rate outcome).
- Fed hints at a cut → rotation likely ends (removes condition #2).
- H100 rental / DDR5 pricing hold firm + earnings guides don't cut → no earnings decel → flush.

## Sources
- Candle scan 2026-07-03 (`tools/flow_trackers.py`); session discussion 2026-07-03.
