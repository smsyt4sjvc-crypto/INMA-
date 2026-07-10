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

## Warsh / Fed Trap update (2026-07-01, Sintra) — HAWKISH, corrects the intraday "dovish" read
- ⚠️ **Correction:** an early headline ("inflation risks have come down") read dovish/cut-lean. The FULL
  Sintra readout is **hawkish**: "prices are too high," "we're going to deliver price stability," **won't
  tolerate inflation >2%**; forward guidance abandoned. Market: **~70% odds of a HIKE by Sep**, 9/18 officials
  see rates higher by end-2026, two hikes priced by Q1 2027. So "he's gonna cut / Trump gets his way" is
  **contradicted** — hikes are still priced. `raw/2026-07-01-macro-scan.md`.
- *(inverts the Fed-put read)* Hawkish Fed **into** the AI-capex crack = **NO Fed put right now** → growth
  scare AND policy both bearish → strengthens the drawdown/puts scenario, kills "a cut cushions the dip."
- *(Fed Trap, live)* "Won't tolerate >2%" = the *can't-ease* horn; $39T debt = the *can't-tighten* horn.
  Warsh is talking the hawkish horn — either he means it (hikes → bust) or folds later. Still trapped.
- *(escape hatch + Jake's rebuttal)* Warsh's out: AI capex "expands the supply side" (productivity →
  immaculate disinflation → avoids the choice). Bull counter to [[cepi]]. **Jake's rebuttal (sharp):** the
  binding inflation is *essentials* (rent/food/energy), not compute — AI productivity in compute doesn't
  lower rent, so the escape hatch is a category error re: the Hollow Bottom.

## ⚠️ Debasement-unwind headwind (2026-07-01, Goldman via ZH Korea note)
- Goldman attributes part of the Korea/won move to the market **"unwinding debasement trades" while USD stays
  resilient** → USDKRW grinds higher. `raw/2026-07-01-korea-liquidity-goldman.md`.
- *(near-term counter to the debasement lean)* A debasement-trade *unwind* + strong USD is a **short-term
  headwind to the gold/hard-asset side of the barbell** — mild tension with gold +1.6% (2026-07-01). Watch
  whether it persists: if debasement-unwind + strong-USD holds, hard assets face a near-term drag even as the
  *structural* debasement thesis ([[consumption-vs-investment-crux]], Fed Trap) stays intact. Positioning vs structure.
- Reinforces **global hawkish CB** (BOK hiking July + Warsh hawkish) = no central-bank put; strong USD is the tell.

## June-2026 jobs — Hollow Bottom confirmed, Fed Trap deepened (2026-07-02)
Source: `raw/2026-06-jobs-report-empsit.md` (Jake's verbatim BLS extraction).
- **Stall-speed headline over a hollowing core:** NFP +57k, unemployment 4.2% — but the rate fell for the
  *wrong* reason (participation −0.3pp → 61.5%, not-in-labor-force +832k, employed-HH −507k). Serial DOWN
  revisions (−74k Apr+May). Long-term unemployed 1.9M (27.3%); involuntary part-time series-high (+201k);
  full-time −514k. The frozen-labor / duration thesis, confirmed and deepening.
- **Hollow Bottom cross-confirmed from a 2nd dataset:** discretionary/cyclical *sheds* (leisure & hosp −61k,
  retail −7.5k) while eds/meds/social-assistance carry the entire gain. Prices *and* jobs now print the same
  two-economy split. Ties [[consumption-vs-investment-crux]].
- **Fed Trap deepened, July FOMC reopened two-sided:** weak labor = cut ammo (counters yesterday's hawkish-
  Warsh read) BUT wages +3.5% y/y = cover to dismiss it. "He's gonna cut" isn't dead — it's now a race between
  labor deterioration and inflation stickiness; this report tilts labor-weak, not decisive.
- **Checkpoint:** Aug-28 **QCEW/UI benchmark revision** (near-universe, Jake's 941 cross-check) — given the
  down-revision trend, likely reveals MORE hollowing. ⚠️ Payroll 90% CI ±122k → +57k ≈ noise; read composition.

## Falsifiers (watch in the monthly refresh)
- M2 YoY rolls back negative / WALCL resumes falling → liquidity tightening, debasement read weakens.
- Real fed funds climbs (inflation falls faster than cuts) → Fed NOT trapped, they have room.
- HY OAS blows wider → the complacency breaks; Detachment Bid fading.

## Refresh
Re-run the Colab cell (in `data/README` / playbook) monthly; overwrite the CSV; re-read Act 3 lines.

## Sources
- `data/macro_2019_present.csv` (FRED via Colab, 2026-07-01).

## FOMC minutes 2026-07-08 — the Fed names AI; the doom loop documented
- **DATA:** June-meeting minutes: staff attributes core-goods inflation "largely" to "tariffs and **AI-related
  price pressures**" (first official naming). "Some participants" cite eventual AI productivity disinflation
  "though... would likely take time." **"A few" wanted to HIKE in June; "majority" fear higher inflation.**
  (`raw/2026-07-08-zh-feed-ceasefire-over.md`)
- *(THESIS — the reflexive loop, now official)* The AI trade sits on BOTH sides of the Fed's ledger: ~37% of
  the index (what a put would protect) AND a named cause of the inflation that prevents the put. **AI capex
  manufactures its own monetary headwind.** The Warsh escape hatch (supply-side someday) is deployed in the
  same minutes that book the cost-push today — policy is set on today. Jake's rent-vs-compute rebuttal stands
  unaddressed inside their own framework. No-put + live hike faction into the oil/diesel CPI impulse and
  de-anchoring expectations = the trap's horns at their tightest reading yet.
- *(political link)* The Fed NAMING AI as an inflation source = citable ammunition for the first candidate who
  runs on "AI raises your prices and takes your job" — the monetary and political ratchets linked.

## Warsh's task forces (2026-07-09, Fed press release — primary source, Jake paste)
Five task forces "to advance the conduct of monetary policy." The COMPOSITION is the document:
- **Productivity & Jobs (the AI panel — the headline):** Andreessen (a16z, admin ally) + Charles Jones
  (Stanford, ON LEAVE AT ANTHROPIC — disclosed in the release) + a Microsoft EVP. **3/3 industry-aligned,
  zero AI-productivity skeptics** — the panel exists to evaluate Warsh's own escape hatch (AI expands supply
  side → immaculate disinflation) and is staffed by people whose employers need the answer to be yes.
  Source-correlation at the institutional level. Jake's rent-vs-compute rebuttal structurally unrepresented.
  *(THESIS — the market translation)* **The pivot's paperwork, drafted in advance:** when this panel reports
  AI-as-disinflationary, Warsh gains intellectual cover to ease INTO the capex boom without citing the debt —
  "inflation is the policy" gets its official absolution. The debasement thesis handed its mechanism.
- **Inflation Frameworks (cuts the OTHER way):** Mankiw + **Sargent** ("unpleasant monetarist arithmetic" =
  the founding text of the Fed Trap / fiscal-dominance thesis) + **William White** (BIS, pre-2008 warner).
  The fiscal-dominance realists brought inside: either the trap gets acknowledged in an official framework,
  or their credibility gets borrowed to bless ~3% tolerance. Watch which.
- **Data:** Chetty (real-time card spend) + McMillon (ex-Walmart CEO — the bottom-80% consumption window) =
  the reported-vs-physical discipline institutionalized; the Fed admitting official data is too slow/revised
  (the −74k saga). If it works, the Fed sees the Hollow Bottom in near-real-time.
- **Balance Sheet:** Rajan/Stein/Dynan — QE's sharpest internal critics reviewing "the current regime."
  Watch for the "not-QE" backstop architecture (Jake's political-economy read) redesigned under this banner.
- **Communications:** King/Fisher/Fraga — consistent with forward-guidance abandonment (Sintra).
- *(context)* Released ONE DAY after the minutes named "AI-related price pressures" as an inflation driver —
  the Fed's internal AI fight (cost-push today vs supply-side salvation tomorrow) now has org charts, and
  the salvation side got the friendlier judges. Timeline: reports in quarters-to-years — regime architecture,
  not a near-term rate signal.
- *(2026-07-09 same-day exhibit — the conflict compounds)* The MSFT exec named to the Productivity & Jobs
  panel runs Xbox, which is cutting **1,600 jobs** (4,800 MSFT-wide) while the company holds **2,273 H-1B
  approvals** this year — the panel assessing AI displacement co-led by an executive executing it. Threads:
  (1) layoffs-fund-capex mechanism (Jul-6/7 log) + the visa-substitution spread routed to GPUs; (2) the
  POLITICAL FUSE gets a legislative vehicle — Trump's $100K H-1B fee struck down as a tax only Congress can
  levy → relocated into Congress in an election year; the fact-pattern (layoffs + visas + record capex + a
  Fed advisory seat) = ready-made midterm ammunition; (3) Xbox squeezed both ends in one month: prices +$150
  (memory passthrough) AND 1,600 cuts = the Hollow Bottom trifecta inside one business unit. ⚠️ Approvals ≠
  1:1 replacement (framing is polemical) — but veracity ≠ effect, and the effect is radioactive.

## The layoffs-vs-jobs-numbers reconciliation (permanent explainer, 2026-07-10)
Jake's question: mega-layoffs weekly, NFP "fine" — who's lying? Answer: nobody has to be; four mechanics:
1. **Scale illusion:** ~5M separations + ~5M hires EVERY month; all 2026 tech layoffs ≈ 150-200K = a bucket
   vs the river. Feeds sample the salient; NFP nets the flow (JOLTS layoff rate near historic lows).
2. **Composition (Jake's own June extraction = the answer):** severance keeps the laid-off "on payroll";
   gig/labor-force exit hides them (+832K NILF, participation −0.3pp, full-time −514K, involuntary PT at
   series highs). The net stays fine while the KIND of employment degrades.
3. **Jobs-that-aren't-jobs, documented:** birth-death imputation (overcounts at turning points → the huge
   negative QCEW benchmarks → the Aug-28 checkpoint exists for this), record multiple jobholders (1 person
   = 2 entries), involuntary part-time (a count, half a livelihood).
4. **Revisions pattern = mechanics first, politics real second:** CES response rates collapsed (~60%→40s) →
   first prints are imputation-heavy and assume trend-continuation → in deceleration, prints are
   SYSTEMATICALLY high and revise down. No dial-touching required. BUT distrust is rational: the BLS
   commissioner was FIRED over a report (2025) = institutional-pressure risk is real; and **Warsh's Data
   task force (Chetty card data + Walmart's ex-CEO) = the Fed itself no longer trusting official timeliness.**
**Method: route around the contested number** — QCEW (tax records), Treasury daily withholding, 941s, and
the trade-down tape itself (ROST +17% comps IS labor data). Cultural marker: displacement-anxiety sales
funnels (Kiyosaki-class "safe job = dangerous") = the political fuse's kitchen-table layer, monetized.
