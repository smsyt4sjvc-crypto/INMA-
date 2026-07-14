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
- *(participation decomposition, 2026-07-10)* The 61.5% / million-leavers headline splits three ways: (1)
  boomer aging (~0.2pp/yr structural drag — discount first); (2) **immigration policy — deportations +
  collapsed inflows shrink the labor force BY DESIGN, mechanically lowering the unemployment rate the
  administration touts while it needs weak numbers for cuts (the agendas fight inside the statistic)**;
  (3) discouraged/frozen-market exits (27% long-term unemployed → the +832K NILF = the Hollow Bottom's
  exit door). Second-order: **policy-shrunk supply drops NFP breakeven from ~180K (2023) to maybe 40-80K
  → +57K is weak demand AND possibly above breakeven simultaneously** = the rate is a broken gauge
  (numerator and denominator shrinking together); sticky +3.5% wages despite hollowing = supply-constrained
  stagnation = the Fed Trap's labor wing.

## 2026-07-10 addendum — GS puts a number on the Fed's "AI-related price pressures"
- **DATA (reported, `raw/2026-07-10-zh-memory-pce-electricity.md`):** GS note (via ZH): memory-driven
  electronics repricing (+5% to +25% realized/announced, PS5/MacBook/iPad/Xbox table) estimated to push
  **core PCE +0.5%** (⚠️ horizon unspecified in paste); separately, US wholesale electricity 24m forwards
  ≈ +25% vs Jan-25 on data-center demand while Germany/UK/Spain/France sit flat-to-down — a US-specific
  services-side impulse that pre-dates the Iran war.
- *(THESIS)* The 7/8 minutes named the cause; GS now sizes it, on both the goods channel (memory) and the
  services channel (power). Half a point of core PCE is roughly the whole distance between "cutting" and
  "a few wanted to hike." The trap's mechanism is no longer inferential — full write-up in
  [[ai-capex-cycle]] §2026-07-10.

## 2026-07-10 — Williams goes on record: AI demand could FORCE hikes (the troika speaks)
### DATA (`raw/2026-07-10-williams-ai-demand-hikes.md`, Bloomberg 7/9)
- NY Fed's Williams (permanent voter, troika): of all US inflation drivers he is **"most focused on demand
  driven by artificial intelligence"** — and if it persists, **"it could force the central bank to raise
  interest rates."** Direct quote: "you don't look through this."
- **June SEP: NINE policymakers penciled in ≥1 quarter-point HIKE in 2026** (of 19 participants).
  ⚠️ Upgrades the minutes' "a few saw a case for raising" — the hike faction is ~half the committee's
  dots, not a fringe.
- He kept the off-ramp: if benign, policy "well positioned." Conditional, not a pre-commitment.

### THESIS (interpretation — NOT fact)
- *(the escalation ladder, 3 rungs in 3 days)* 7/8 minutes: STAFF names "AI-related price pressures."
  7/10 GS: quantifies it (+0.5pp core PCE, both channels). 7/9 Williams: the SYSTEM's #2 says policy
  "would need to respond." This is no longer our inference about a doom loop — it is official
  communication of one. The Fed put isn't just absent; the Fed is pre-announcing the conditions for a
  Fed CALL on the AI trade.
- *("don't look through this" = the exemption revoked)* Central banks "look through" supply shocks
  (oil, tariffs). Williams explicitly frames AI as a DEMAND impulse — capex demand pulling on real
  resources (power, construction, memory) — which is exactly the shock type policy is REQUIRED to lean
  against. Jake's rent-vs-compute framing and the GS electricity forwards are the evidence under that
  classification.
- *(reflexivity, same page)* The very article carries "Nvidia's $1 Trillion Slide Sends Valuation to
  Pre-AI Boom Levels" (as-reported). The market repricing the builders WHILE the Fed reprices policy on
  the same phenomenon = both of the trade's supports (multiple expansion + easy money) tightening at
  once. Cross-ref [[buying-at-highs]] §3: NVDA's compressing multiple is not automatically "cheap" —
  the E-risk is growing as fast as the P falls.
- *(book relevance, descriptive)* A hike-leaning Fed into a 37%-concentrated index is the environment
  the SPY-put + cash posture was built for; SPAXX yield also rises with any hike. Not advisory — noting
  the alignment.

## 2026-06-30 (ingested 7/10) — Hammack: the FIRST rung, and the Warsh split goes public
### DATA (`raw/2026-06-30-hammack-ai-inflation-cnbc.md`, CNBC Sintra interview, Hammack = 2026 VOTER)
- "Insatiable" AI-infrastructure demand named as an inflation source; district evidence = a data-center
  **switchgear manufacturer**: hyperscalers "will pay almost any price for those inputs... need things
  built yesterday."
- Transmission: "I'm not seeing a lot of restraint... not hearing that interest rates or credit spreads
  are a reason why they're holding back" — policy is NOT restrictive for the AI complex.
- "Inflation... too high for the past five years... we may need to raise rates to bring that policy
  restraint in." Couched: "impacts in both directions."
- CNBC frames her view as running AGAINST Chair Warsh's AI-productivity-is-disinflationary doctrine.
- ⚠️ SEP discrepancy to resolve: CNBC says the June SEP "penciled in a quarter percentage point increase
  this year" (median-hike reading); Bloomberg 7/9 said NINE of 19 penciled ≥1 hike (not a median).
  Check the actual June dot plot before repeating either as the committee's central case.

### THESIS (interpretation — NOT fact)
- *(ladder re-sequenced — voters led, staff followed)* Corrected chronology: **Hammack (voter) 6/30 →
  minutes/staff 7/8 → Williams (troika) 7/9 → GS quantification 7/10.** Regional presidents were saying
  it on the record BEFORE the minutes printed. Four rungs in ten days; this is a communication campaign,
  not a stray remark.
- *(her evidence IS our bottleneck map)* A Fed president's hike case built on a switchgear order book is
  [[buildout-bottleneck-map]] confirmed from inside the system: switchgear sold out through 2028,
  price-insensitive hyperscaler bidding = both the inflation mechanism AND the unrepriced-shortlist
  demand thesis (VICR/VSH/ENS live in exactly that current). Same fact, two consequences: bullish the
  bottleneck sellers, hawkish the discount rate.
- *(transmission broken → the K-shaped hike)* If rates/spreads don't bite the hyperscalers (cash-flow
  funded + tight-spread AI debt, [[ai-financing-fragility]] loose 1.8x), then the hike sized to restrain
  THEM overshoots for everyone else — housing, small business, the Hollow Bottom get hit first and
  hardest. The instrument is aimed at the top of the K and lands at the bottom. Trade-down chain
  ([[trade-down-landing-pads]]) accelerates under that error.
- *(the Warsh split is the fight to watch)* Chair's doctrine (AI = disinflation eventually) vs voters'
  district-level physical evidence (AI = demand impulse now) — and the chair staffed his AI task force
  with industry (§Warsh task forces = "the pivot's paperwork"). Watch whether Warsh's escape hatch
  survives contact with his own committee's dots. The doctrine says look through; the voters say
  "you don't look through this" (Williams). Someone loses.

### ⚠️ RESOLVED (2026-07-10, WebSearch vs actual June SEP) — the dot-plot discrepancy
- **DATA (June 17 2026 SEP + press reports):** Current target range **3.50–3.75%**, held. **Median 2026
  dot = 3.8%** — i.e., ONE quarter-point HIKE above current — revised UP from **3.4% in March** (which had
  implied a CUT). Distribution: **18 dots** — 8 no change, 1 cut, **9 with ≥1 hike** (of those: 3 at one
  quarter-point, 5 at a half-point per TradingKey). **Chair Warsh did NOT submit a dot** ("I, however,
  have refrained from offering any projections of my own, consistent with my long-held views").
  SEP medians: PCE 2026 3.6%, core PCE 3.3%; GDP 2.2%; U3 4.3%.
- Both prior reports were correct: CNBC's "penciled in a quarter-point increase" = the MEDIAN; Bloomberg's
  "nine penciled at least one hike" = the distribution. 9 of 18 = literally half the committee; the median
  sits on a knife-edge — one dot from neutral.
- *(THESIS)* Three upgrades to the trap read: (1) **The median flipped from cut to hike in ONE SEP**
  (~40bp swing March→June) — the fastest hawkish revision of this cycle, contemporaneous with the AI-demand
  language. (2) **Five participants project a HALF-POINT of hikes** — the hawk tail is deeper than "one and
  done." (3) **The chair abstained** — so the committee-median-says-hike EXCLUDES the one man holding the
  AI-disinflation doctrine. The Warsh split isn't rhetorical; it's structural: his committee's central dot
  contradicts his framework and he declined to put a number against them. The dot plot is the committee
  voting against the chair's escape hatch.

## 2026-07-10 — housing bill held hostage (Jake detail: supply-side cost-reduction bill; Trump won't
## sign unless Congress passes the "Save America Act" — contents unknown to vault)
- *(THESIS)* The inconsistency is the datapoint: shelter is the LARGEST sticky core component (~42% of
  core CPI), and supply-side housing relief is the only lever that actually disinflates it — hikes make
  it WORSE (starts fall → less supply). So the administration is pulling the FAST optics lever (oil
  suppression into midterms, visible at the pump in weeks) while holding the SLOW structural lever
  (housing supply, years) hostage for unrelated legislation. Politically rational, economically
  incoherent — and it leaves the Fed alone against sticky shelter with a tool that suppresses supply.
  The trap's division of labor: White House manages headline, Fed stuck with core, housing fixable by
  neither. Bottom-of-K squeeze deepens ([[trade-down-landing-pads]] tailwind).
- Open item: Save America Act contents — needed before reading the hostage price.

## 2026-07-11 — debt math logged: +$2.99T/yr, interest ~$1.2T/yr (ZH 5-charts)
- *(THESIS — THE collision, now numerically explicit)* $1.2T annual interest vs 9 dots leaning HIKE:
  every 25bp raises the Treasury's refi bill by tens of billions while AI cost-push demands the hike.
  The newsletter's conclusion ("rates to near-zero even with above-target inflation") IS fiscal
  dominance — the Sargent/White wing of Warsh's own task forces. The Fed Trap's two exits: hike into
  the debt spiral, or cut into the inflation. Debasement bid ([[gold-flows]], COT gold longs building)
  = the market pricing the second exit. Silver datapoint filed: 4x then −50% — the violence of the
  debasement trade's corrections; ratio vs S&P still far under 2011.

## 2026-07-12 — Jake's "inflate it away" scenario: the policy valve as the answer to the well-duh riddle
### THESIS (user's thesis, logged in substance)
- *(the scenario)* The simplest resolution to the negative-FCF/circular-financing setup isn't a crash —
  it's accommodation. Warsh states: **"AI is deflationary; easing increases supply-side production and
  lowers prices even if there's a short-term inflation cost"** → the capex, the circular money, the whole
  AI bet gets a longer runway. Jake: this wouldn't raise an eyebrow. And it's not a stretch — it's the
  chair's EXISTING doctrine (the Warsh split, above), and **he abstained from his own committee's dots**,
  keeping exactly this optionality.
- *(analysis — why it's the modal historical outcome)* Every "well duh" setup that DIDN'T complete was
  rescued by this valve: 1998 LTCM cuts into a boom (→ 1999 melt-up → bigger 2000 bust), 2008 QE/ZIRP,
  2019 repo, 2020 everything. The valve is WHY doom signals have a low unconditional hit rate.
- *(analysis — the valve-status refinement; upgrades the planned false-positive study)* Crash signals
  aren't predictive ALONE because the outcome depends on a policy variable: **is the valve available?**
  Valve OPEN (inflation at/below target) → signals fire, Fed rescues, "false positive." Valve JAMMED →
  the crash completes: 1929-32 (gold standard), 1973-74 (CPI), 2022 (Fed HIKING into the derate — the one
  recent decline that ran unimpeded). Study design: condition every signal-firing on valve status.
  Predicted result: near-zero completion valve-open; high completion valve-jammed.
- *(analysis — why the valve is jammed-ish NOW, the counterweight)* The last use (2020) CREATED the jam:
  5 years above target (Hammack), 9 hike dots, $1.2T interest bill. And uniquely, the thing being rescued
  is itself COST-PUSH inflationary in household essentials (electricity, DRAM passthrough, the bipartisan
  bill-grievance ratchet) — easing into the AI buildout bids up the exact bottlenecks a Fed voter already
  cites as her hike case. Easing can't print electrons or transformers; it prints DEMAND for them. Warsh's
  doctrine vs Hammack's channel = whether the valve physically works when the bubble's inputs ARE the inflation.
- *(the check that didn't exist in 2008 — the long end)* 2008 easing → duration rallied (deflationary
  bust). Easing into 3%+ inflation + ~$3T deficits → term-premium/vigilante veto: the bond market can put
  the tightening in the 10-30yr regardless of the funds rate. **The tradeable tell is not the doctrine but
  the long end's (and gold's) REACTION to it:** Warsh talks AI-deflation and the 30yr rallies = market
  grants the runway (melt-up branch); long end sells off / gold rips = the valve leaks straight into
  debasement pricing.
- *(book sort — this scenario IS [[detachment-bid]]/debasement, the standing bull)* Inflate-away ≠
  "no crash"; it means the crash arrives in REAL terms, slowly, denominated in purchasing power. Both
  branches sort the book the same way: hard assets / bottleneck tolls / gold long, long-duration nominal
  claims avoided, equity puts kept SMALL (the valve is exactly what makes shorting the nominal price
  dangerous). 1998→2000 precedent: the rescue extends the runway AND raises the terminal altitude.
- **LIVE TEST: Warsh's first congressional testimony Tuesday 7/14, same day as CPI.** Watch for "look
  through," "supply side," "productivity," any AI-disinflation framing under oath — then watch the
  10yr/30yr and gold in the following hour, not the equity tape.

## 2026-07-12 — the 2026 YTD run-rate (Jake's Q: "on the year, not the sum of the parts")
### DATA (WebSearch 7/12: BLS/CNBC/TradingEconomics/Morningstar monthly prints, compounded Jan–May 2026)
- Monthly m/m prints 2026 — **CPI headline (SA): Jan +0.2, Feb +0.3, Mar +0.9 (largest since Jun-2022),
  Apr +0.6, May +0.5.** Core CPI: Jan +0.3, Feb +0.2, Mar +0.2, Apr +0.4, May +0.2. **PCE headline:
  Jan +0.3, Feb +0.4, Mar +0.7, Apr +0.4, May +0.4.** Core PCE: Jan +0.36 (supplied by Jake 7/12 —
  resolves the prior ⚠️ est. +0.3; "slightly hotter than expected," YoY 3.1%), Feb +0.4, Mar +0.3,
  Apr +0.2, May +0.3.
- **Compounded YTD (5mo) → annualized: CPI headline +2.52% → 6.2% ann. Core CPI +1.31% → 3.2% ann.
  PCE headline +2.22% → 5.4% ann. Core PCE +1.57% → 3.8% ann.** (core PCE revised up from ~3.7% est.
  when Jan's exact print landed)
- YoY prints for reference: CPI 4.2% (May, highest since Apr-2023; energy +23.5% YoY, >60% of May's
  monthly increase), PCE 4.1%, core PCE 3.4% (highest since Oct-2023). Jan YoY was 2.4% — i.e., **the
  entire resurgence happened INSIDE 2026** (2.4→4.2 in four prints).
- Arithmetic vs the SEP: headline PCE landing the June-SEP 3.6% Dec/Dec median now requires the
  remaining 7 months to run **~2.3% annualized** — a full disinflation to target starting immediately.
### THESIS (interpretation — NOT fact)
- *(what the YoY hides)* The 4.2%/4.1% YoY prints UNDERSTATE the current tape — they average in soft
  late-2025 months. 2026's own run-rate is a 5-6 handle on headline. The valve-jam is quantitative now:
  Warsh would have to sell AI-deflation easing over a 6%-annualized headline tape.
- *(composition = the war + the buildout)* Headline−core gap (6.2 vs 3.2 CPI) ≈ energy war premium —
  reversible if [[demand-destruction]]'s suppression stack holds. Core 3.2-3.7% ann. = the sticky part,
  and June (Tuesday) carries the first memory-electronics pass-through test (GS +0.5pp core-PCE claim).
- *(the dots vs the tape)* March's SEP median implied a CUT with Jan running 2.4% YoY; June's implied a
  hike at 3.5% YoY. If June/July prints hold the 2026 run-rate, the September SEP pressure is toward
  MORE hike dots — the trap tightening on schedule, unless the war premium unwinds first.

## 2026-07-12 — the THIRD exit: redefine the yardstick (Jake's thesis — VERIFIED as announced program)
### DATA (WebSearch 7/12: PIMCO/RBC/Chase/CNBC recaps of June 17 FOMC, Warsh's first meeting)
- Warsh announced a **task force to "examine the drivers of inflation, first principles, and weigh the
  full range of ideas for delivering price stability in a changing economy"** (noting inflation "uneven,"
  housing disinflationary) AND a **second task force to review "the data sources and analytical methods
  the Fed uses to assess the economy."**
- Warsh abstained from the dots; quote: his dot **"is not helpful in the conduct of policy"**; expects
  **"by year-end... a review about communication broadly, press conferences, dots, meetings, and the
  like."** PIMCO's headline label: "Hawkish-Leaning Committee, Reform-Minded Chair."
- Prior related datapoint (Aug 2025): BLS commissioner fired over jobs revisions — statistical-agency
  politicization already live on the executive side.
### THESIS (user's thesis + analysis)
- *(user's thesis, stated before verification)* Warsh's incentive fork: two years of constant Trump
  pressure (hiking into the debt spiral), or "revolutionize" inflation measurement — defining technology
  + outdated tools + bet that AI is the productivity exponential — and never have to choose between his
  president and his committee. Jake called the program from behavior alone; the June FOMC transcript
  confirms both legs (new metrics task forces + projection-apparatus review).
- *(analysis — the base rate favors it: every US inflation crisis produced a new, LOWER-reading yardstick)*
  Burns 1970s: invented "core" by excluding food/energy exactly when food/energy WERE the inflation.
  1983: house prices → owners'-equivalent rent (asset inflation removed from CPI permanently). 1996
  Boskin Commission: substitution/hedonics, ~1.1pp shaved, explicitly under fiscal (COLA) pressure.
  2000: Fed switches preferred gauge CPI→PCE (reads ~0.3-0.4pp lower). 2022: Powell's "core services
  ex-housing" supercore, invented mid-fight. Redefine-not-defeat is the documented playbook, not paranoia.
- *(analysis — why it's respectable, which is what makes it work)* The tools genuinely ARE outdated:
  CPI can't see AI consumer surplus, free digital services, quality-adjusted deflation. A "modernized"
  index is a defensible methodological argument deployed at a convenient time — not fraud, selective
  truth. The audition is **Greenspan 1996**: override the staff models on a productivity-mismeasurement
  hunch (he was RIGHT; longest expansion followed). Difference in stakes: Greenspan bet with ~2.5-3%
  headline + budget heading to surplus; Warsh would bet with a **6.2% annualized YTD headline run-rate
  + ~$3T deficits + the grievance anchored in essentials** (electric bills, groceries, memory
  passthrough) that no index revision lowers.
- *(analysis — the tell that it's political, not just methodological)* The year-end review targets the
  FORWARD apparatus — dots, pressers, SEP — i.e., the instrument that publishes his committee's
  disagreement (9 hike dots). Killing the dot plot doesn't change measurement; it removes the visible
  evidence that half the committee opposes the chair's doctrine.
- *(analysis — what cannot be redefined = where the trade lives)* TIPS breakevens, the long end, gold,
  and the household's lived prices. The bipartisan ratchet runs on the electric bill, not the index —
  a yardstick change that reads as "they changed the numbers" AMPLIFIES the grievance. And if both the
  measurer (BLS, post-firing) and the interpreter (Fed, under review) are restructured within 18 months,
  **official-inflation credibility itself becomes the traded variable** — which IS the debasement bid.
  The third exit doesn't escape the trap; it re-denominates it. Same book sort as the valve scenario:
  the referee that doesn't accept re-denomination is gold.
- **Watch:** Tuesday 7/14 testimony — task-force framing, "changing economy"/"measurement" language,
  dots skepticism under oath; any NAMED new gauge (the supercore pattern) = the scenario going live;
  year-end communication-review deliverable; breakevens/gold reaction to each.

### 2026-07-12 — the LABOR leg of the third exit (Jake's extension: "wages > inflation" by composition)
#### DATA (WebSearch 7/12: June jobs report, CNBC/BLS/Fox)
- June: payrolls **+57k** (vs 115k consensus; May revised DOWN 43k to 129k, April down 31k to 148k).
  **Participation fell 0.3pp to 61.5% — lowest since Mar-2021** (pre-pandemic 63.3%); emp-pop ratio
  down 0.2pp to 59.0%. **Unemployment DROPPED to 4.2%** — mechanically, via the participation exit.
  **AHE accelerating: 3.4% → 3.5% YoY** ($37.64). Fox headline the same day: "added jobs at a steady pace."
- Composition-bias precedent: **April 2020 AHE spiked ~+8% YoY** purely because low-wage workers were
  fired en masse — averages rise when the bottom leaves the sample. The Atlanta Fed Wage Growth Tracker
  (median, matched persons) and the ECI (fixed job-mix) exist specifically to correct this artifact.
- Vault priors: Amazon −16k workers Jan citing AI; June construction still adding (specialty +14.1k)
  while residential sheds.
#### THESIS (user's thesis + analysis)
- *(user's thesis)* Pair the redefined inflation gauge with AI-driven labor-force exit: participation
  falls but headline payrolls look "steady"; jobs consolidate into AI-supplementary/supervisory/HITL
  roles at much higher wages → **average wages rise by composition, not raises** → "wages > inflation"
  prints, and the chair's prosperity story completes.
- *(analysis — June ALREADY has the signature)* Every element printed at once: exits (61.5%),
  "steady" framing, unemployment falling FOR THE WRONG REASON, AHE accelerating. Not alleged
  engineering — the composition effect is mechanical as displacement proceeds; the POLICY choice is
  merely which series to cite (AHE not ECI/median; U-3 not participation; core not headline). Burns
  didn't fake data either — he chose the exclusions.
- *(analysis — the yardstick choice flips the sign of real wages TODAY)* AHE 3.5% vs headline CPI 4.2%
  = real wages NEGATIVE. Same 3.5% vs core CPI 2.9% = POSITIVE. "Look through energy" is not framing —
  it is the difference between rising and falling real wages in the current prints. The redefinition
  leg and the wage leg NEED each other; that's why it's a package.
- *(analysis — the productivity double-headline)* Unit labor costs = compensation/output. AI raises
  output per remaining worker → ULC can FALL (Warsh's disinflation doctrine confirmed) while average
  wages RISE (composition). Both headlines print simultaneously, both arithmetically true, from the
  same displacement. The chair gets disinflation AND prosperity from one phenomenon.
- *(analysis — the statistical laundering of the Hollow Bottom)* The displaced appear NOWHERE: not
  unemployed (stopped looking → out of U-3), not in the wage average (not employed). The K's bottom leg
  exits the aggregates entirely — [[consumption-vs-investment-crux]] made invisible by sample attrition.
  The grievance doesn't exit the electorate, though: it reappears as the bipartisan ratchet and the
  trade-down tape ([[trade-down-landing-pads]]).
- *(un-gameable checks — the series that can't be composition-laundered)* **Prime-age (25-54) emp-pop
  ratio** (bodies/population, no wage or participation definitions); **ECI vs AHE spread** (fixed mix vs
  drifting mix — divergence = the fingerprint); **Atlanta Fed median tracker vs AHE average**;
  **aggregate real labor income** (hours × jobs × wages — can stagnate while the average rises); real
  consumption at the median vs trade-down volume. If AHE accelerates while ECI/median/prime-age EPOP
  stall → the "wages > inflation" print is composition, not raises.

### 2026-07-12 — the FISCAL ledger (Jake: "it shows up in SS, SNAP and housing subsidies")
#### DATA (WebSearch 7/12)
- **Social Security applications jumped ~11% in 2025 YoY**; as of mid-2026, **26% of new beneficiaries
  claim at 62** (accepting up to −30% permanent haircuts); notably higher-income people — those most
  able to delay — increasingly claiming early. Attributed to fear about the program's future + SSA
  upheaval. [IndexBox/AARP/Yahoo]
- **The intake aperture is being narrowed simultaneously: SSA cut 7,100+ jobs (13%+ of workforce,
  largest staffing cut ever)**, offices closed, **AI tools now analyzing medical evidence** for
  disability claims — delays/denials expected to rise, appeals to lengthen. [Parriva/CO disability law]
- SNAP 2026 enrollment trend: not cleanly retrieved (⚠️ open item — and the 2025 reconciliation bill's
  SNAP work-requirement expansion is a policy confound: rolls can FALL while need rises).
#### THESIS (user's thesis + analysis)
- *(the conservation law)* The laundered displaced don't vanish — they cross ledgers: out of the labor
  statistics, into the fiscal accounts (early SS, SSDI, SNAP, housing assistance). Labor stats can be
  composition-gamed; enrollment counts and outlay dollars are appropriations-grade arithmetic. The
  transfer rolls are the shadow labor report.
- *(analysis — but the aperture is being narrowed at the same time)* SSA staff −13%, AI denial tooling,
  SNAP work requirements, housing-voucher funding pressure: the administrative state is shrinking the
  very ledgers that would register the displacement. Where the aperture closes, the displaced disappear
  from BOTH ledgers — official statistics go fully dark, and the residual detectors become PRIVATE
  series: **credit/auto delinquencies (NY Fed), food-bank volumes, BNPL growth, the trade-down tape in
  corporate earnings** (WMT/dollar-store mix — companies cannot redefine their customer composition).
- *(analysis — the exception that can't be gated)* **Early retirement claiming is a birthday
  entitlement** — no medical review, no work requirement, no caseworker. That's why it's the ledger
  already visibly filling (+11%), and the −30% haircut acceptance is the tell: people locking in
  nominal dollars NOW rather than trusting the future promise = **a slow-motion run on the entitlement,
  debasement psychology at the household level** (same instinct as the gold bid, expressed in benefits).
- *(analysis — the loop closes into the trap)* Transfer absorption raises mandatory outlays → deficit →
  issuance → the $1.2T interest bill → the Fed Trap tightens. And the third exit's yardstick leg CUTS
  these same transfers' real value (COLA = CPI-W; Boskin's explicit purpose was COLA savings). Full
  pipeline: launder the labor stats → displaced flow to transfers → narrow the aperture → redefine the
  COLA gauge to shrink what remains. Each leg documented separately; together = the Hollow Bottom
  pipeline, fiscal edition. The grievance compounds at every stage and surfaces only at the ballot.

## 2026-07-12 ~10pm PT — Timiraos pre-testimony frame: a JULY HIKE is in play; Williams sets a
## numeric tripwire; the Fed names the AI buildout as the restrainable inflation source
### DATA (`raw/2026-07-12-timiraos-warsh-first-call.md` — WSJ full text)
- July 28-29 FOMC: hike live (undo last year's last two cuts); **Waller flipped** dove→hawk
  ("risks completely flipped"); real rates ~zero/negative vs realized 3-4% inflation; Friday MPR:
  wages "roughly consistent with 2%" (first time in 5 yrs); Kashkari: the tools start in the labor
  market and the labor market isn't causing the inflation.
- **WILLIAMS TRIPWIRE (vice chair): H2 monthly core CPI ≤0.2% = stay well-positioned; faster =
  "monetary policy would need to respond."** Williams on AI: chip/electrical-gear prices =
  "hockey sticks"; sustained buildout demand-pull = the kind you DON'T look through — and the one
  inflation source rates CAN restrain (vs tariffs/oil).
### THESIS (interpretation — NOT fact)
- *(the tripwire vs our own tape — THE Tuesday number)* 2026 core CPI monthly: 0.3, 0.2, 0.2,
  0.4, 0.2 — averaging 0.26, NOT ≤0.2, and June carries the memory-electronics passthrough.
  **June core ≥0.3% trips the vice chair's own stated framework** two hours before Warsh's House
  testimony. The swing vote pre-committed publicly; the print grades him in real time. (Set #2
  registration input.)
- *(the biggest line for the book: the Fed just aimed at the buildout)* Williams articulated what
  Hammack implied: tariffs and oil can't be restrained by rates — **datacenter capex CAN.** A hike
  cycle framed this way is a hike AT the $996B. Stack the weekend: token revenue −21% + credit
  window narrowing (Papai) + now the Fed contemplating rates aimed at capex demand = the third
  policy leg of the squeeze. Stage-2 pressure now comes from Constitution Ave too.
- *(Kashkari + the wage certification = the third exit's intellectual preconditions, delivered)*
  The Fed ITSELF now says: models can't parse this inflation, wages aren't causing it. That is
  precisely the doctrinal opening Warsh's task forces need — "the tools are outdated" is no longer
  a chair's heresy, it's the committee's own lament (and the wage line ironically certifies the
  composition-flattered wage tape as target-consistent). The redefinition path got easier tonight.
- *(structure read)* Williams pre-dismissing the "credibility hike" publicly = the vice chair
  boxing the new chair in before his first testimony. Warsh's real choice: hold with hawk dissents
  (weak chair optics) or own a hike his doctrine disbelieves. Either way, the July 28-29 meeting
  prices as live — and **GEHC's Q2 earnings land on FOMC decision day (Jul 29)**: Jake's position
  reports into a Fed-decision tape.
- Calendar lock: CPI Tue 8:30am ET → Warsh House 10am → PPI/Beige Book/Senate Wed → TSMC Thu →
  FOMC Jul 28-29. The Williams tripwire is the connective number through all of it.

## 2026-07-13 ~11:45am PT — WALLER, CPI EVE: "near-term hike possible" — Treasuries fall, GOLD −3%
- DATA (ZH flashes): **Waller (the FLIPPED dove): "near-term hike possible"** + "not obvious our
  balance sheet causing problems" (QT can run). Market: Treasuries fell, **gold −3%**, on the eve
  of CPI + Warsh's debut. ZH gloss: "rate hike to contain DRAM."
- *(THESIS)* The committee is PRIMING the hike the day before the print — Waller's conversion
  completing in public (led last year's cuts; now pre-endorsing the reversal, per the Timiraos
  frame). Gold −3% on hike talk = the valve-jam trade in miniature: hawkish surprise hits the
  debasement bid FIRST (the 7/01 Goldman debasement-unwind pattern). Tomorrow's reaction map
  sharpened: hot CPI now lands on a market pre-warned of hikes — less surprise premium on the
  hawkish branch, MORE on the dovish (a soft print now moves further than a hot one). Watch
  Warsh's distance from Waller under oath.

## 2026-07-13 ~1:15pm PT — the WALCL chart + Waller's defense: the two-handed policy, quantified
### DATA (FRED WALCL chart, Jake upload + ZH flash)
- **Fed total assets: QT trough ~$6.53T (Dec-2025) → ~$6.73T now = +$200B in ~7 months ≈
  +$29B/month ≈ $350B/yr pace.** The decline stopped cold at year-end 2025; steady climb Feb→Jul
  2026 (with a year-end TGA/repo spike artifact at Jan-1). This DETAILS the Act-3 line ("QT looks
  done") — it's not done, it's REVERSED.
- Same hour: **WALLER: "NOT OBVIOUS OUR BALANCE SHEET CAUSING PROBLEMS"** — defending the
  expansion — while ALSO saying "near-term hike possible" (gold −3%).
### THESIS (interpretation — NOT fact)
- *(the two-handed policy, now in one frame)* Hike talk with the RATE hand; +$29B/month with the
  LIQUIDITY hand. Tightening the PRICE of money while growing its QUANTITY = the fiscal-dominance
  signature: $2.99T/yr of Treasury issuance (+ the AI IG wave) needs an absorber, and reserve
  scarcity broke repo in 2019 — so the balance sheet CANNOT shrink, and all "tightening" must be
  performed by the rate tool alone. The debasement base case doesn't need the valve to open;
  the quantity hand is already easing while the price hand talks tough. "Inflation is the policy,"
  hawkish face edition.
- *(the Warsh irony for tomorrow)* Warsh built his reputation as THE balance-sheet hawk (years of
  op-eds against QE bloat) — he now presides over renewed expansion his own governor defends as
  harmless. Under-oath question to watch Tue/Wed: anyone forcing Warsh to reconcile hike talk with
  +$350B/yr of balance-sheet growth. His answer (or dodge) = the third-exit tell in miniature.
- *(market mechanics)* The Feb→Jul climb IS the "not-QE" liquidity under the melt-up (Act-3 fuel):
  detachment-bid supportive near-term, debasement-confirming long-term. Watch: whether the pace
  accelerates when the AI-IG issuance wave meets the Papai ceiling — the Fed as the marginal
  absorber of last resort is the endgame branch.

### 2026-07-13 ~5:30pm PT — prediction market prices July FOMC: 66% hold / 34% hike (Jake's print)
### DATA (observed)
- Jake pastes event-market odds, eve of CPI: **Jul 29 FOMC — "maintain" 66% (1.46x payout),
  "hike 25bps" 34% (2.81x payout).** Vig ≈ small (implied 68.5% + 35.6%).
- Calendar between now and decision: CPI 7/14 (tomorrow, ~12h), Warsh House 7/14 + Senate 7/15,
  PPI 7/15, retail sales 7/17, FOMC blackout ~7/18, decision 7/29 10am PT. June PCE lands 7/31
  — AFTER the meeting. Tomorrow's CPI is the only major inflation print the committee sees.
### THESIS (interpretation — NOT fact)
- *(analysis)* This market is currently a CPI DERIVATIVE with a two-week tail: hot core (≥0.3)
  likely reprices hike toward ~50-60%; soft (≤0.2, Williams's tripwire) collapses it toward
  10-15%. Buying either side tonight = a leveraged CPI bet, overlapping the straddle's branches.
- The strongest single base rate: **the modern Fed does not act at 34% priced.** Since the
  mid-90s it pre-telegraphs until the market prices ≥~70% before moving (it treats surprise
  itself as a policy cost). For hike-at-2.81x to pay, tomorrow must print hot AND the committee
  must spend its 4 pre-blackout days ramping expectations (Timiraos/Waller are arguably already
  the ramp). Absent the ramp, hawk-talk into a hold is the two-handed pattern already logged
  (hike TALK + balance sheet EXPANDING +$29B/mo).
- Vault tension, stated honestly: the hawkish tape (Waller flip, Williams tripwire vs 0.26 avg,
  6.2% ann. headline) argues hike risk is real; the structural spine (third exit, valve thesis,
  WALCL, Warsh building machinery to AVOID hiking) argues the talk is the tool and the hold is
  the act. The vault's own macro read → "maintain" is modestly underpriced at 66% IF the valve
  thesis is right — but every input here is public; the edge is interpretive, not informational.
- Surprise-rule check: "what does the market believe (34% hike), what do we know that's
  different?" — no differential FACT, one differential FRAME (third exit). Thin edge; the same
  view is already expressed cheaper in gold/duration reactions. Sizing, as ever, Jake's.
- Links: [[market-fragility]] (event-vol), [[retail-edge]] (surprise rule).
- **Addendum ~5:40pm PT — Jake's registered view (user's thesis): "34% chance of a hike is
  lower than reality."** I.e., true P(hike) > 34% → the 2.81x side is value. Gradeable two ways:
  (a) do the odds trade materially higher post-CPI/testimony this week; (b) does the Fed hike
  7/29. Decomposition at registration (analysis): P(hike) = P(hot core)·P(hike|hot) +
  P(soft)·P(hike|soft) ≈ 0.45·0.60 + 0.55·0.08 ≈ 31% — market ≈ fair on those inputs; Jake's
  edge must live in P(hot) > 45% (run-rate 0.26 + oil $85) or P(hike|hot) > 60% (Waller ramp
  already underway). Trade construction note: Kalshi positions can be SOLD before settlement —
  the repricing (34→50-60 on a hot print) is capturable without the hike ever happening.
