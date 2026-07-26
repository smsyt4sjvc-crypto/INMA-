# Growth-Ignition Anatomy — what the starts of 3x runs looked like (blind study)

Jake's commission (2026-07-25 ~7:21pm PT): map every ≥3x-in-2-3-years run in the S&P since 2015, extract the ignitions,
dissect with moving averages / oscillators / volume vs a CONTROL of random dates — "poke it from every angle." Sequel to
[[runner-anatomy]] (the 200%+/12-mo cohort); connects to [[deep-value-reclaim]] STUDY 2 and [[dip-buying-base-rates]].
Tool: `tools/growth_ignition_anatomy.ipynb`.

> Discipline: ANATOMY ≠ PREDICTION (episodes condition on a known future); survivorship (today's constituents) inflates
> everything; the base-rate cell is the honest number.

## DATA (observed — run 2026-07-25; 11y daily adj+volume, 502 names; ignition = trough launching ≥3x within ≤756 td)
- **573 ignitions across 284 stocks.** By year: crash years dominate — 2020 = 168, 2018 = 84, 2022 = 74 (57% combined);
  calm years thin (2024 = 16, 2025 = 18).
- **Ignition state vs control (median; control in parens):** 38.4% below ATH (10.6%) · **22.3% BELOW the 200-SMA** (+5.3%
  above) · 17.4% below 50-SMA (+1.2%) · **RSI-14 = 28.1** (52.5) · realized vol 44.2% (24.8%) · trailing 6-mo return
  −23.7% (+6.7%) · 200-SMA slope −0.5% (+1.0%) · **relative volume 121% of its 6-mo baseline** (99%).
- **First 6 months of the runs:** median +41.4% [IQR +21.7%, +72.3%] · worst pullback inside = **−18.1%** median
  [−25.4%, −12.5%] · 63.5% of days above the 20-SMA · **price reclaims the 200-SMA at median day 44**; ~100% reclaim
  within a year.
- **Crash vs calm split:** crash-year ignitions are the extreme form (−30.7% vs 200-SMA, RSI 25.8, relvol 1.33);
  calm-year ignitions are milder (−8.5% vs 200-SMA, RSI 30.7, relvol 1.06). Direction holds; magnitude is regime-scaled.
- **★ BASE RATE (the honest number):** all state-days matching the profile (RSI<35 AND ≤−15% vs 200-SMA AND relvol≥1.1):
  15,927. Of those, **18.0% went on to 3x within 3y — vs 9.8% for random stock-days.** Doubles the odds; fails ~4 in 5.

## THESIS (interpretation — NOT fact; analysis)
- *(ignition = capitulation, not breakout)* The 3x runs of the last decade did NOT start from quiet bases or new highs —
  they started deeply below every moving average, at RSI ~28, at double normal vol, ON ELEVATED VOLUME (the capitulation/
  accumulation print). The "early stage of the growth cycle" Jake asked to fingerprint IS the washout bottom.
- *(volume is the discriminator oscillators aren't)* Price-state (below MAs, low RSI) says "fallen"; relvol >120% at the
  low says someone is TAKING the other side in size. It's the one marker in the set that isn't just a restatement of "it
  went down a lot."
- *(the 200-SMA reclaim at day ~44 = the confirmation bridge)* Ties the studies together: PTJ's "nothing good below the
  200" catches these runs ~2 months in — sacrificing the bottom but buying confirmation; [[deep-value-reclaim]] STUDY 2's
  winner cohort (catalyst-crushed + reclaim) is the tradeable expression of this same anatomy.
- *(holding cost is the untold half)* Median −18% pullback INSIDE the first 6 months of eventual 3x runs — a
  correction-sized drawdown while being RIGHT. Sizing/stops that can't survive −18-25% get shaken out of the exact runs
  this study fingerprints.
- *(regime honesty)* 57% of ignitions live in crash years — the profile is substantially "crashes create 3x rebounds."
  Calm-year ignitions are milder pullbacks (−8% vs 200), so a screen tuned to the full-sample medians will sit empty in
  calm tapes and flood in crashes — which is itself the [[dip-buying-base-rates]] ladder conclusion from another angle.
- *(what it is and isn't)* A WATCHLIST-state definition (where 3x odds are ~2x base) + a confirmation sequence (volume at
  the low → 20-SMA hold → 200-SMA reclaim ~day 44). NOT a standalone buy signal: 82% of matching states don't 3x, and
  survivorship flatters everything here.

## Falsifier / regrade
- Forward test: profile states flagged from TODAY (notebook cell 6, editable thresholds) graded on realized 3y outcomes.
- Poke-from-more-angles queue: MACD/momentum-divergence at the trough; sector clustering of ignitions; gap-vs-drift
  overlay from [[deep-value-reclaim]]; fundamental overlay (revenue growth at ignition) via the SEC scanner.
