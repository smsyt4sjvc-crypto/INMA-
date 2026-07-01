# New-Economy Regime — the macro database read

Interpretation of `data/macro_2019_present.csv` (live FRED, monthly 2019→2026-06, pulled via
Colab 2026-07-01; sanity-checked: SP500 2026-06 = 7,499.36 matches live). Related:
[[consumption-vs-investment-crux]], [[market-fragility]], [[detachment-bid]], [[portfolio-state]].

> Firewall: DATA = the series. THESIS = the read (Jake's Fed Trap / debasement, labeled).
> ⚠️ Column `fed_assets_pct_gdp` is BAD (ChatGPT copied WALCL raw, didn't divide by GDP) — ignore it.

## DATA (the three acts, from the series)
**Act 1 — the flood (2020–21).** Fed funds 2.4→0.05; balance sheet (WALCL) $4.04T→$8.94T peak
(2022-04); M2 $14.5T→$21.5T (+~40%). Real fed funds ~ −5%. → the asset-inflation that births the
Hollow Bottom.
**Act 2 — the tightening that didn't break it (2022–23).** Fed funds →5.33%; **M2 actually
contracted** (YoY −4%, first since the 1930s); curve inverted to −1.06 (2023-06). The
"should-have-been" recession — deferred, not taken.
**Act 3 — the re-acceleration (2024→now).** Fed funds eased 5.33→**3.63** (2026-06). And into
that easing:
- **M2 back to a record $23.05T** (2026-06), YoY **+5.6%** (2026-05) — reaccelerating from
  negative.
- **Balance sheet ticking UP again**: $6.66T (2025-06) → $6.74T (2026-06). QT looks done.
- **Inflation reaccelerating**: CPI YoY 2.4% (2024) → **4.2%** (2026-05); core PCE YoY →**3.4%**
  (2026-05), both back above target.
- **Real fed funds compressing toward zero**: +2.5% (2024) → **+0.2–0.5%** (2026).
- Curve dis-inverted/steepening (T10Y2Y +0.30 to +0.74); **HY credit spreads tight** (~2.8% OAS)
  — no stress priced. Unemployment drifting 3.5→4.3. Federal debt **$22T→$39T** (+77% in 7yr).
  S&P 2,704→7,499.

## THESIS (interpretation — NOT fact)
- *(Jake's Fed Trap, Vector 7 — now with a fingerprint)* Act 3 is the trap made visible: the Fed
  is **easing into reaccelerating inflation** — cutting while CPI runs 4% and core PCE 3.4% — because
  the $39T debt can't be serviced at 5%+. Real rates being pushed back toward zero/negative while
  M2 makes new highs and the balance sheet turns up = **"inflation IS the policy,"** not a failure
  to control it. The debasement base case ("he'll inflate anyhow") is in the series, not a vibe.
- *(links [[consumption-vs-investment-crux]])* Act 2 is the deferral in the data — they had the
  tightening teed up (M2 contracting, curve inverted = the recession signal) and **blinked**. The
  can-kick is measurable.
- *(links [[detachment-bid]])* Tight HY spreads + VIX ~17 + S&P at 7,499 into 4% inflation = the
  complacency/risk-seeking the Detachment Bid describes. No stress priced while liquidity re-flows.
- *(links [[market-fragility]])* Liquidity turning back ON (M2 record, WALCL uptick, real rates
  falling) is fuel under the melt-up — the "not-QE" Jake flagged. Bullish near-term, worse tail.

## Post-COVID (2022-base) — wages, energy, frozen labor (added 2026-07-01)
Source: `data/postcovid_2022.csv` (2022-01 base) + chart `raw/postcovid-2022-wages-labor.jpeg`.

### DATA (2022-01 → 2026-05)
- **Wages:** nominal median +19.1% (1037→1235); CPI +18.2% (282.5→334.0); **real median wage
  +3.6%** (363→376) — but **stalled since late 2024** (~+0.5% in 18 months), and was *underwater*
  (below base, to 359) in mid-2022.
- **Energy:** CPI energy +25.3% (270→339), incl. a sharp **+19% spike Feb→May 2026** (283→339)
  while WTI is only ~$79 → the surge is **electricity/gas, not crude** → ties [[power-not-petroleum]].
- **Frozen labor:** hires 4.3→3.3, quits **2.9→1.9**, layoffs 0.9→1.1 (~flat), median weeks
  unemployed **9.9→11.6** (+1.7, step-up late 2025). Unemployment rate 4.0→4.3.

### THESIS (interpretation — NOT fact)
- *(Jake, confirmed)* The frozen market (low-hire / low-quit / low-fire) **is the wage-stall
  mechanism**: quits collapse → no job mobility → no raises. The rate (4.3%) hides it; rising
  duration is the tell.
- *(correction to earlier)* Crude "median real wages were crushed" is **FALSE** (real +3.6% from
  2022, +5.9% from 2019). The Hollow Bottom is NOT a median-wage story — it's stall + freeze +
  energy(electron) bite + the (unshown) 25th-pct / asset-lockout leg. Sophisticated version intact,
  strawman version dead.
- *(links [[market-fragility]])* Edge cluster mid-2026: energy spike **and** unemployment-duration
  spike together, inside the July/midterm window → live stress signal for the fragility engine.
- *(links [[detachment-bid]])* Frozen labor = can't get ahead through work → rational to gamble in
  markets → feeds the risk-seeking bid.

## Bottom basket vs CPI — the deflator test (added 2026-07-01)
Source: `data/bottom_basket.csv`, chart `raw/bottom-basket.png`. Tests whether CPI understates
the bottom's inflation (Jake's "income-specific CPI" / moving-target idea).

### DATA (2019-01 → 2026-05, indexed)
- rent +37.3%, groceries +32.8%, **energy +65.7%**, medical +21.0% | discretionary: apparel
  **+10.1%**, used cars +26.6% | **headline CPI +32.2%** | median wage +36.5%.
- **Bottom necessities basket +38.5%** (realistic lowest-quintile weights: rent .40/food .15/
  energy .10/medical .08) — ~**6 pts hotter than headline CPI**.
- **Real median wage: +3.2% vs CPI, but −1.5% vs the bottom basket.** (Sign flips with the ruler.)

### THESIS
- *(Jake's method CONFIRMED)* CPI understates the bottom's inflation by ~6 pts; on the bottom's
  own basket the median real wage is **negative (−1.5%)**. And discretionary deflates (apparel
  +10% over 7yr ≈ −20% real) and drags headline CPI down — demand-destruction-as-distress, visible.
- *(calibration — don't overclaim)* The gap is **modest** (a ~5-pt swing, not −15%), and **energy
  (+66%, the electron spike) drives most of it**. So wage-vs-basket alone does NOT explain "can't
  afford anything."
- *(RELOCATION — the real finding)* The bigger "broke" driver is **off this chart**: the
  **balance sheet** — housing ~+50% (asset lockout), debt serviced at ~20% (crater-era borrowing),
  lost COVID transfers. The Hollow Bottom is confirmed but is **more a balance-sheet story
  (assets + debt) than an income-statement story** (wages ≈ flat vs basket). Next cut:
  wealth-by-quintile.

## Falsifiers (watch in the monthly refresh)
- M2 YoY rolls back negative / WALCL resumes falling → liquidity tightening, debasement read weakens.
- Real fed funds climbs (inflation falls faster than cuts) → Fed NOT trapped, they have room.
- HY OAS blows wider → the complacency breaks; Detachment Bid fading.

## Refresh
Re-run the Colab cell (in `data/README` / playbook) monthly; overwrite the CSV; re-read Act 3 lines.

## Sources
- `data/macro_2019_present.csv` (FRED via Colab, 2026-07-01).
