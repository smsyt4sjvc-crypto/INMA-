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
- **Addendum ~5:40pm PT — [WITHDRAWN 7/14 at Jake's request: a passing Kalshi-hike speculation was
  logged here as a "view"; Jake reclassified it as offhand speculation, not a registered prediction,
  and asked it removed. Not on the calibration scoreboard. Neutral market data (Kalshi 66/34) stays
  in the 5:30pm entry above; the personal-view framing is gone.]**

### 2026-07-13 ~5:50pm PT — AI cost-push INTO the CPI: the channel map (Jake's Q: "electronics, autos, etc.")
### DATA (observed, weights/precedents from public BLS structure + vault sensors)
- Vault sensors already showing the push at the component layer: server DDR5 $78-133/GB vs $3-5
  pre-shortage (DigiKey census 7/13); Samsung Gen-5 SSDs at Gen-4 retail parity (consumer shelf
  flip, 7/13); GEHC $250M memory-driven cost cut (the industrial receipt).
- Rough core-CPI goods weights (BLS, approximate): new vehicles ~3.5-4%, used vehicles ~2.5%,
  household furnishings/appliances ~4%, IT commodities (PCs/phones/TVs) ~1%. Electricity ~2.5%
  (services side). Fed has already named DC capex as inflation it does NOT look through
  (semis/electrical gear "hockey sticks" — logged 7/12).
- Precedent: 2021 chip shortage → used-car CPI +~45% peak, THE single largest driver of the
  2021 core spike. Cars carry $500-1,500 of semi content; memory rides in infotainment/ADAS.
### THESIS (interpretation — NOT fact)
- *(analysis)* Four channels, ordered by arrival time:
  1. **Electricity — already in the prints.** AI load growth → power prices; most direct and
     most visible channel; runs through services, not goods.
  2. **Consumer electronics — arriving NOW (his SSD sensor = the leading edge).** Key mechanic:
     BLS hedonic quality adjustment made electronics a structural DEFLATION category (−5-10%/yr
     for PCs historically). Same-spec hardware costing more = pure price increase hedonics
     can't offset. A category that mechanically subtracted from core for 30 years flipping to
     ADD is a sign-change the models aren't built for. Small weight (~1%) but the swing is big.
  3. **Appliances/furnishings — 1-2 quarters out** (contract repricing lag from the $102/GB
     industrial layer, per the Advantech→GEHC chain).
  4. **Autos — 2-4 quarters out, biggest weight.** 2021 showed the transmission works and is
     violent. If memory stays tight into model-year 2027 pricing, this is the H1-2027 core story.
- Timing verdict: adds LITTLE to tomorrow's June print (shelf prices flipped this week, June
  data closed in June) — adds a LOT to H2-2026/2027 core persistence. So it strengthens the
  hawkish-persistence case mainly via the committee reading persistence AHEAD, not
  via tomorrow's number. It is also the anti-Kashkari inflation: not labor-caused, and the only
  Fed tool that touches it is making the capex itself more expensive (the fourth blade of the
  funding squeeze).
- **The yardstick collision:** this is exactly where the third exit will be fought. Warsh's
  "inflation in a changing economy" + data-methods task forces could EXPAND hedonics/"look
  through supply factors" to define AI cost-push away — the same categories, opposite sign.
  Whether AI shows up as inflation may end up a MEASUREMENT decision, not a market fact.
- Links: [[ai-capex-cycle]] (memory sensors), [[buildout-bottleneck-map]], [[power-scarcity-equities]] (electricity).
- **Addendum ~6pm PT — Jake: "Apple, Microsoft already raised prices. Others probably have as
  well, just with less coverage."** (Jake's recall, specifics unverified ⚠️ — worth a Perplexity
  census: which consumer-tech names have ANNOUNCED increases, on what products, effective when.)
  Two upgrades to the channel map if it holds: (1) MID-CYCLE price increases on unchanged
  hardware are the hedonics-proof pure signal — nothing for quality adjustment to absorb;
  (2) Microsoft raising SUBSCRIPTION prices = a fifth channel: software/cloud passing compute
  costs through as SERVICES inflation — and its twin is the GPT-5.6 nerf, price-per-unit-of-
  cognition rising with the sticker unchanged. CPI cannot see the nerf at all: cognitive
  shrinkflation is measurement-invisible, which means the AI-services channel is UNDERSTATED
  in any official print by construction.
- **Addendum ~6:15pm PT — the census came back (raw/2026-07-13-ai-price-increase-census-perplexity.md):
  VERIFIED, channel 2 has arrived.** Apple ~20% (June, verbatim reason: "could no longer absorb
  component inflation"); Dell ~17% (Mar 30 — already inside Q2 prints); Lenovo (June); Cisco
  (Mar); Hetzner cloud up to 37% (Apr); IBM ~6%; Microsoft commercial M365 up to 33% (Jul 1).
  *(analysis)* Reads:
  · **The stated-reason split is the tell:** hardware names say COSTS out loud (DRAM/NAND/AI);
    software names say VALUE ("AI features") — same pass-through, cost-push wearing a
    monetization costume on the services side.
  · **Landing spots differ:** Apple/Dell/Lenovo consumer hardware → CPI (Dell's March raise is
    already in prints; Apple's June raise enters June/July collection — possibly a trace in
    TOMORROW'S print). Microsoft COMMERCIAL licenses + Hetzner/Cisco → PPI — landing in
    WEDNESDAY'S print (7/15), the day after CPI. This week reads both ends of the pipe.
  · **Arithmetic honesty:** IT commodities ≈ 1% of CPI; +20% passed through ≈ +0.2pp on the
    index spread over months — a few bp/month directly. The direct math is small; the SIGNAL is
    the sign-flip (a 25-30pt swing vs the −5-10%/yr hedonic norm) and the breadth (7 majors in
    6 months). The big weights (autos) haven't moved yet — that's the 2027 leg.
  · **The not-yet list is the frontier:** streaming/consumer subs (Netflix, Spotify, Prime)
    unraised — DRAM-light businesses, no cost excuse yet. If THEY start raising citing "AI
    features," that's opportunistic breadth (1970s-style), not cost-push — a regime-worse signal.

### 2026-07-14 ~4:28am PT — Ericsson refines the AI-inflation channel map: pricing power decides CPI-vs-margin
### THESIS (interpretation — NOT fact) — extends the 7/13 channel map + price census
- *(analysis)* Ericsson (memory margin warning, see [[ai-capex-cycle]]) reveals the memory
  cost-push has TWO transmission paths, and CONTRACT STRUCTURE / PRICING POWER decides which:
  · **Short product cycles + pricing power → CONSUMER PRICE (CPI).** Apple, Dell raise stickers
    ~17-20% (price census 7/13); the consumer pays; shows in CPI.
  · **Long-term fixed contracts + weak pass-through → MARGIN COMPRESSION (earnings).** Ericsson,
    GEHC eat it; the SHAREHOLDER pays; shows in EPS, not CPI.
- **The sequencing insight (leading indicator):** the SAME memory inflation hits OEM MARGINS
  FIRST (now — GEHC, Ericsson, guiding into 2027) and CONSUMER PRICES LATER (as long-term
  contracts renegotiate and new tenders reprice — 2027, Citi's timeline). So **industrial-OEM
  margin compression LEADS the memory-inflation CPI leg by quarters.** That's why the OEM
  equity casualties are cracking NOW while electronics CPI is barely moving. Watch OEM gross
  margins (GEHC, Ericsson, Nokia, medical/industrial) as the leading gauge of the eventual
  consumer-price leg — earnings calls front-run the CPI print.
- Reinforces the yardstick-war stakes: a cost-push that first appears as MARGIN (not price) is
  even easier for a measurement task force to keep out of the official inflation number — it's
  not in CPI yet by construction; it's in corporate earnings.
- Links: [[ai-capex-cycle]] (Ericsson/GEHC/DigiKey), [[cluster-shortlist-workup]] (GEHC Q2).

### 2026-07-14 ~5:30am PT — CPI PRINTS COLD: core 0.0% below the tripwire (the relief branch)
### DATA (observed) — ZH wire, 8:30am ET release
- CPI −0.4% MoM (exp −0.1%) — outright DEFLATION, 0.3pp below.
- **Core 0.0% MoM (exp 0.2%)** — FLAT, below Williams's 0.2% tripwire, well below the 2026 core
  run-rate avg 0.26. 0.2pp below.
- CPI 3.5% YoY (exp 3.8%, 0.3pp below). Core CPI 2.6% YoY (exp 2.8%, 0.2pp below).
- Every line printed below consensus. June collection period.
### THESIS (interpretation — NOT fact)
- *(analysis)* **The VALVE gets a green light.** Core 0.0% < the 0.2% tripwire = the Fed has cover
  to NOT hike and even to ease WITHOUT Warsh needing to redefine anything — the number came in soft
  on its own. Kills the July-hike case; the "inflate-it-away / longer-AI-runway" scenario ([[new-economy-regime]]
  valve thesis) gets fuel. Hike odds should collapse toward ~10-15%; "maintain" toward ~85-90%.
- (The July-hike case is dead on this print — core 0.0, not ≥0.3. No position was taken; the
  "reprice after the print / maintain gets fat on a soft print" read was the correct one.)
- **Forward thesis INTACT — the sequencing holds.** This is JUNE data: BEFORE the July $85-Brent
  war spike AND before the memory cost-push reaches consumer prices. Per the 7/14 Ericsson/GEHC
  sequencing ([[ai-capex-cycle]]): memory inflation hits OEM MARGINS first (now, in earnings),
  CONSUMER PRICES later (2027). A soft June CPI is CONSISTENT with — even confirms — that timing:
  the cost-push isn't in CPI yet, exactly as predicted. Soft print ≠ cost-push refuted; it = the
  margin damage leads the price damage by quarters. The Ericsson margin warning and this soft CPI
  are the SAME thesis at two points on the lag.
- **Gold:** the debasement bid returns off the $4,000 ledge (the asymmetry logged 7/13 — Waller
  knocked it down positioning for hawkish; a soft print sends it back violently). Watch it rip.
- **Warsh testifies 7am PT into a SOFT print** = maximally easy setup — he can lean dovish without
  fighting the data; watch whether he still pushes the task-force/measurement language anyway
  (would signal the third exit is structural, not just data-driven).
- Set #2 grade note: this fires the "core ≤0.2 asymmetric relief rip +1.5-2.5%" KILL SWITCH — the
  modal gap-DOWN shape call is falsified; direction is UP. Grade full set #2 vs closes later.
### For the book (descriptive — sizing/execution Jake's)
- The SPY Jul-15 750 straddle: soft-CPI surprise = relief RALLY = the CALL leg is the payer. The
  overnight/pre-open gap is captured automatically at 6:30am. Mechanics per [[retail-edge]] gap-at-2DTE
  entry: gamma pays the move, vega is dead, IV CRUSH hits at the open — so the payoff is the GAP,
  not the hold. Breakevens ~743.5/756.5 (±0.87%); needs SPY through ~756.5 (~+1%) for a clear win.
  Pre-committed exit = "big move → close whole by mid-morning"; the relief gap is the sell, not the
  hold-for-Warsh (theta + crush eat continuation). Whether the gap clears breakeven = the open tells.
- **Addendum ~5:35am PT — WARSH: "Fed has 'NO TOLERANCE' for persistently high inflation"** (prepared
  remarks ahead of the 7am House hearing). *(analysis)* Reads hawkish; is mostly COSTLESS table-stakes.
  · TIMING: lands right after core 0.0% — sounding tough on inflation the hour inflation printed
    SOFT = free credibility. The word "PERSISTENTLY" is the hedge: core 0.0 says it's not persistent
    now, so "no tolerance for persistently high inflation" is fully compatible with NOT hiking.
  · Every new chair's first testimony REQUIRES the anti-inflation credential (esp. a Trump-adjacent,
    dovish-suspected one) — this is boilerplate, not news; the market knows it.
  · NOT a contradiction of the third-exit thesis — it's the COVER for it. The third exit isn't
    "tolerate inflation," it's "redefine the yardstick so measured inflation is at target." A chair
    pursuing it would SAY exactly this — under the new measure, inflation won't BE persistently high.
    Hawkish rhetoric + yardstick redefinition are complementary. The two-handed pattern (hawk talk +
    balance sheet expanding) continues.
  · WATCH THE Q&A (the real signal): does he pivot "no tolerance" → "so we must MEASURE it correctly"
    (task forces / data-methods)? That's the redefinition tell. Prepared line = credibility; Q&A = intent.
  · Book: a hawkish-sounding header could TRIM the relief rally (minor fade risk to the straddle's call
    leg) — reinforces "take the gap at the open, don't hold for the full 7am testimony; Warsh can
    SUBTRACT from the rally, not just add." Live example of why hold-for-Warsh is the wrong exit.
- **Addendum ~5:40am PT — Jake's catch: "isn't it still 3.5% YoY? Isn't that persistent?"** *(user's
  insight — sharp)* Correct: 3.5% headline / 2.6% core YoY, above 2% target for YEARS = persistent by
  the plain meaning; that reading would DEMAND a hike. The reconciliation IS the third exit on one word:
  · "Persistent" is undefined → two clocks. LEVEL/DURATION (2.6-3.5%, years, above target — Jake's read,
    demands action) vs MOMENTUM (recent MoM pace, core 0.0%, decelerating — Warsh's read, permits holding).
    The soft print hands him the momentum clock; base effects (hot mid-2025 months rolling off) let YoY
    drift down mechanically = "clear path to target" narrative even at an elevated level.
  · He said "persistently high," NOT "high" — the qualifier is a DOVISH tell in hawkish costume: it
    commits him to react to TRAJECTORY not LEVEL → pre-authorizes sitting at 3.5% indefinitely as long as
    each MONTH behaves. Permission to run hot as long as it's not accelerating.
  · **This is the yardstick redefinition operating on a single ADJECTIVE** (not CPI methodology) — Jake
    watched the definitional escape hatch work live. Strengthens the third-exit thesis: the ambiguity of
    "persistent" is the micro-mechanism; the task forces are the macro version. Same move, two scales.
- **Addendum ~5:45am PT — CPI composition (ZH breakdown):** the −0.4% headline was ENERGY-DRIVEN
  (largest energy decline since Aug-2022; June oil tumble). **Core SERVICES still rose modestly** —
  the STICKY part did NOT disinflate; GOODS deflation carried core to 0.0%. Refinements:
  · **The soft headline is a backward-looking oil-dip artifact that REVERSES next month.** June oil
    tumbled; JULY oil is $85 (war). So the July CPI (reported Aug) gets the OPPOSITE energy push —
    this −0.4% is likely a one-month LOW, not a trend. Don't extrapolate "deflation is here."
  · Composition SUPPORTS the cost-push-not-in-CPI-yet thesis: core services sticky-positive, goods
    still deflating (old hedonic regime), memory cost-push absent (the 2027 leg). Exactly the lag
    the Ericsson/GEHC sequencing predicted.
  · Moderates the dovish read slightly: sticky core-services + reversing energy = the disinflation
    is less clean/durable than the headline. For TODAY'S tape though, headline soft + core 0.0
    dominate = relief rally.
  · **JPMorgan traders' est: +1-1.5% stocks** = ~756-760 SPY. Straddle breakeven ~756.5 → JPM's
    expected move lands RIGHT AT the breakeven; a clear straddle win needs the HIGH end (+1.5%/~760).
    Live but not fat; the opening gap decides. Waller walk-back watch (his hawkish panic vs this print).
- **CORRECTION/refinement ~5:50am PT — component chart (ZH):** MoM contributions — Energy −0.445
  (THE driver), Food +0.028, Core Goods −0.016, Core Services +0.019, **SUPERCORE −0.206**. YoY —
  Core 2.594, Supercore 3.172, Energy +1.013, Core Services 1.915, Core Goods 0.158.
  · **Corrects my 5:45am "core services rose, sticky part intact":** core services rose ONLY on
    SHELTER — SUPERCORE (core services EX-housing, the Fed's most-watched wage-driven gauge) was
    NEGATIVE −0.206 MoM. The sticky-ex-housing part DID disinflate this month. More dovish
    composition than I said. (Firewall: overstated the sticky read; the chart falsifies it.)
  · BUT the level/momentum split (Jake's catch) HOLDS and sharpens: even supercore momentum went
    negative WHILE supercore YoY is still 3.17% (elevated/persistent). Momentum soft in the
    stickiest component now → makes Warsh's momentum-clock read EASIER, the relief rally more
    justified today; the LEVEL (3.17%) still above target = Jake's persistence point intact.
  · Cost-push thesis STILL confirmed: Core Goods −0.016 (goods DEFLATING, not memory-inflating) —
    the cost-push is absent from CPI exactly as the Ericsson/GEHC 2027-lag predicts.
  · Net: a genuinely soft-composition print (supercore negative), but energy-led and one-month;
    July's $85 oil + the eventual goods cost-push are the reversers. Dovish today, not a trend.
- **Addendum ~5:52am PT — supercore drill-down (ZH chart):** Supercore CPI −0.206 MoM (biggest drop
  since COVID) LED BY Education & Communication Services −0.144 and Transportation Services −0.084
  (Medical Care Services −0.032). Two tempering reads the headline hides:
  1. **The drivers are VOLATILE components, not broad sticky cooling.** Transportation services
     (airfares, insurance) and Education & Communication are among the JUMPIEST supercore
     sub-lines — airfares swing ±several % monthly. A −0.2 led by these can BOUNCE next month;
     it's not evidence the wage-driven core is broadly rolling over. Less durable than "biggest
     since COVID" implies.
  2. **Supercore PCE proxy DIVERGED — stayed elevated (~+0.5 on the chart's magenta line) while
     supercore CPI plunged to −0.206.** The Fed TARGETS PCE, not CPI. The categories that fell
     (education/comm, transport) are weighted MORE in CPI than PCE; PCE weights medical (which
     didn't fall much) far heavier. So the dovish CPI-supercore may NOT replicate in the Fed's
     preferred gauge (core PCE for June prints Jul 31, AFTER the FOMC). ⚠️ verify the 0.501 PCE
     reading, but the divergence direction is the watch: soft CPI-supercore ≠ soft PCE-supercore.
  · Net refinement: dovish for TODAY'S tape (relief rally justified), but a WEAKER durable Fed
    signal than the headline — volatile drivers + CPI/PCE divergence. Supercore YoY still 3.172%
    (persistence intact, Jake's point). ZH framing technically true, composition less durably dovish.

### 2026-07-14 ~5:55am PT — "money about to rip again?" (Jake: mini-cycle-within-the-cycle)
### THESIS (interpretation — NOT fact)
- *(Jake's frame, affirmed)* Big cycle = AI-capex supercycle; mini-cycles = the oscillations
  inside it (memory dip, Korea flush, CPI risk-on/off swings). Soft CPI = the kind of trigger
  that fires an UP-swing. Near-term the rip is ON: valve green-lit (core 0.0 < tripwire), JPM
  +1-1.5%, dovish-lean, banks say no recession → the [[detachment-bid]] / valve melt-up setup.
- **What rips:** dovish print → yields down → the BEATEN-DOWN long-duration complex bounces
  hardest — the megacap drawdown names (MSFT −32%, META −25% off highs, ModestWallet chart) +
  the AI-capex complex (lower rates = funding squeeze eases at the margin = relief in exactly
  what FELL on funding fear) + gold (debasement bid off the $4,000 ledge). Relief rally COVERS
  the fear; doesn't RESOLVE the fundamental.
- **The catch — the fuel is thin (why it's a rip with a short fuse, not a clean secular leg):**
  1. Energy-LED, REVERSES next month ($85 July oil → August CPI bounces).
  2. Supercore PCE diverged — the Fed's own gauge may not confirm the dovishness (prints Jul 31).
  3. Warsh "no tolerance" + Waller's hawkish talk = Fed may lean AGAINST the dovish rip for
     credibility, not validate it.
- **The bigger frame (the peer-check on "money rips"):** a rip HERE, with Roberts' scorecard at
  3-4 horsemen + 2 end-signals flashing ([[bull-bear-ledger]]), risks being the BUY-THE-RIP
  melt-up — the FINAL FOMO leg before the credit event — not a healthy new advance. The valve
  opening EXTENDS the runway (bullish near-term) but does NOT defuse the capex squeeze
  (IBM/Ericsson/memory, the funding cliff). Rip now, break later — Jake's own "position for
  both conservatively until something breaks" resolution.
- **Rising-amplitude tell inside the frame (a state, not a timer):** the mini-cycles are getting
  SHARPER and MORE FREQUENT — Korea cascade, IBM −23%, bank vol-harvest, now a CPI rip, all inside
  DAYS. Rising amplitude + frequency of the oscillations = the "high volatility" horseman = a
  warning condition (elevated forward-drawdown odds), NOT a dated top. Money can rip AND the chop
  can be the warning; neither times the turn — a trigger does.
- Links: [[detachment-bid]], [[bull-bear-ledger]], [[market-fragility]], [[ai-capex-cycle]].
- **Addendum ~6:12am PT — Jake: "and the soft CPI runs for a month."** *(user's thesis — sound)*
  The soft print clears the single biggest SCHEDULED overhang (the inflation data point) until the
  next CPI ~mid-Aug (July data, w/ $85 oil). That's a DATED runway, not vague "room" — which is
  exactly what the expiry-matching rule wants: a dated catalyst → a dated instrument with the exit
  at the catalyst. Jake's full 3-message framework now coheres: momentum PAYS (retail push is real
  flow) + buy-the-dip regime intact (Roberts' terminal flip hasn't fired) + DATED ~1-mo runway =
  ride the melt-up via a DATED instrument, ENTERED on a dip (his own regime call), EXITED at/before
  the next print, SIZED with a stop (not share-concentration held through the break). That single
  structure honors the momentum thesis + the buy-the-dip entry + expiry-matching + capped concentration.
- *(the refinement — clear of CPI ≠ clear of RISK):* the month is empty of the CPI PRINT but FULL
  of other catalysts: **PPI TOMORROW (7/15) is the immediate test — and PPI is where the memory/
  producer cost-push (Ericsson) shows up FIRST, before CPI.** So "soft inflation" gets its first
  challenge in ~24h, not a month. Then TSMC Thu, tech earnings late July, FOMC 7/28-29 (inside the
  runway) — and the whole time $85 July oil visibly LOADS the August reversal (market may price it
  before the print). The stop is for the NON-CPI catalysts; the runway is only inflation-print-clear.
- Links: [[retail-edge]] (expiry-matching, two-population), [[bull-bear-ledger]] (Roberts scorecard), [[detachment-bid]].
- **Addendum ~7:06am PT — Warsh headline now "no tolerance for ELEVATED inflation" (was "persistently
  high").** *(analysis)* "Elevated" speaks to the LEVEL (3.5%) — closer to Jake's persistence point,
  a notch harder than "persistently high" (which hedged on trajectory). Still mostly costless post-
  soft-print, but the wording drift toward the level is worth tracking (ZH paraphrase vs exact quote
  ⚠️). Straddle relevance: hawkish-ish Warsh talk could CAP the relief rally → keeps SPY muted → works
  AGAINST the straddle's need for a big index move. + Hassett "gasoline deflation to $3" = if real,
  extends the soft-CPI energy runway (vs my $85-oil-reverses-August-CPI flag) — spot-vs-forecast battle.

### 2026-07-14 ~8:47am PT — rate-hike odds: soft CPI knocked them down but SMART money holds them up
### DATA (observed) — ZH feed
- Sept hike odds: jumped to ~60% on Waller's hawkish Monday → soft CPI today knocked them DOWN.
  Now **Polymarket 40% vs SOFR futures 52% = a 12-pt arb/gap.** (SOFR = institutional rate hedging;
  Polymarket = retail betting.)
- Warsh: "Fed is RACING to put out GENIUS Act [stablecoin] rules by Saturday." (+ US-UK joint
  stablecoin statement, US Treasury — coordinated stablecoin-reg push this week.)
- Citigroup −5.5% DURING its earnings call (outlook/guidance-driven, not the print).
### THESIS (interpretation — NOT fact)
- **Retail vs smart-money hike-odds gap (observation):** Polymarket (retail) 40% < SOFR futures
  (institutional) 52% = a 12-pt spread. Retail prices the Sept hike LOWER than institutions — a
  recurring pattern worth watching (retail tends to underprice hawkish tails). Descriptive market
  data, not a graded call.
- **The bigger tell: hike odds did NOT collapse to 10-15% on a soft CPI — SOFR holds 52% for Sept.**
  = the market (like the vault) reads the softness as ENERGY-LED/TEMPORARY (July $85 oil reverses it)
  and keeps a real Sept-hike probability. Confirms the "soft print ≠ dovish regime, it's a one-month
  runway" read. If Jake trusts SOFR over Polymarket, buying "hike" at 40% (Polymarket) vs 52% (SOFR)
  = the measurable edge — but Sept is far, cross-venue arb has friction; descriptive, not a call.
- Warsh racing GENIUS Act rules by Sat + US-UK stablecoin statement = the tokenization/stablecoin
  regulatory plumbing accelerating hard ([[buildout-bottleneck-map]] tokenization crossing).
- Links: [[market-fragility]], [[demand-destruction]] (oil-into-CPI).

### 2026-07-14 ~7pm PT — Gundlach: 30Y at 5.10% bumping ~2-decade-high resistance, "unlikely to hold"
### DATA (observed) — ZH feed, evening
- Gundlach: generic 30Y US Treasury yield **5.10%**, <10bps below the ~2-decade high, "keeps bumping
  against resistance... seems unlikely to hold. Even Lacy Hunt has turned bearish."
- Day's tape (ZH summary): "Big-Banks Good, Breadth Bad, Big-Blue Ugly; Bitcoin, Bullion & Bonds Bid
  on Benign-Flation" (BTC/gold/bonds bid on the soft CPI; banks up; breadth narrow; IBM ugly).
### THESIS (interpretation — NOT fact)
- *(analysis)* **The long-end is the debasement/fiscal tell.** 30Y pressing a 2-decade-high with
  Gundlach flagging the resistance breaks UPWARD = the market demanding more term premium (fiscal
  deficits + sticky inflation, Dimon's "tectonic plates"). Lacy Hunt — the dean of bond bulls / secular
  deflationists — CAPITULATING to bearish is a notable regime marker (the last deflation holdout turning).
- **Today's cross-current:** soft CPI gave bonds a SHORT-term bid ("benign-flation") — yields down on
  the day — but Gundlach's STRUCTURAL call is yields BREAK higher. Short-term bid vs structural bear:
  the soft print bought a day; the 30Y at 5.10% says the fiscal/inflation term-premium pressure is the
  bigger force. If the 30Y breaks the 2-decade high, that's a TRIGGER (a real event) — reprices duration,
  pressures equity multiples, and is the "valve jammed" signal (can't ease into a bond revolt).
- Links: [[market-fragility]] (duration/multiple), [[bull-bear-ledger]].

### 2026-07-14 ~8:30pm PT — Warsh FULL testimony (primary source): the third-exit machinery, stated
### DATA (observed) — raw/2026-07-14-warsh-house-testimony-full.md (federalreserve.gov)
- Rates HELD 3.50–3.75% (June). "No tolerance for persistently ELEVATED inflation" (the exact hedge
  phrase — confirms Jake's "persistently" catch: 3.5% YoY IS elevated, but "persistently" lets him
  weigh trajectory).
- "AI investment will soon be called just 'investment.'" Equipment capex +8% (4q), high-tech +25% (4q).
- Two task forces NAMED: (1) balance-sheet policy (ample-reserves regime + asset composition +
  "alternatives"); (2) productivity & jobs — "changes of a DIFFERENT ORDER... implications for the
  Fed... in pursuit of our inflation mandate." Productivity "strong, predating AI." Labor "broadly stable."
- Framing: "courage to revisit our prior views," "fresh look," "point the institution forward."
### THESIS (interpretation — NOT fact) — the vault's Warsh theses, now strongly supported by his own words
- **THIRD EXIT / yardstick redefinition — explicit machinery:** the productivity-&-jobs task force
  ("changes of a different order" + "implications for the inflation MANDATE") is the intellectual
  vehicle to reframe inflation via AI productivity — if productivity is structurally higher, the same
  growth is non-inflationary and above-target inflation becomes "productivity-adjusted fine." "Courage
  to revisit prior views" + "fresh look" = reform intent, not stewardship. This is the third exit in
  soft language.
- **VALVE / runway — confirmed:** "AI investment will soon be called just investment" = the chair
  BLESSING the capex boom, refusing to lean against it. Directly contradicts the staff-hawk framing
  (7/12: "DC capex = restrainable inflation, you don't look through"). The CHAIR came down on
  "it's productive investment" = dovish-for-capex = the melt-up runway has Fed cover.
- **TWO-HANDED policy — confirmed:** hawkish MOUTH ("no tolerance," "we will get it right," "restore
  price stability") + dovish FRAMEWORK (bless capex, productivity task force to justify running hot,
  balance-sheet review that can re-expand). Credibility layer over reform substance.
- **Steelman (per [[_calibration]] — argue the under-weighted side):** a HAWK reading is available —
  "no tolerance / resolute commitment / restore price stability" could be sincere, and the task forces
  genuine institutional review, not a redefinition scheme. The text is Rorschach-ish. The TELL is
  actions, not remarks: does he HOLD/EASE while blessing capex (third exit) or actually HIKE (sincere
  hawk)? June = hold. Watch the next moves + whether the task forces produce a framework revision.
- Labor note: benign read ("kept pace with the workforce") skips the participation/composition issues
  the vault flagged (June participation 61.5% low; composition bias). The un-gameable checks still apply.
- Links: [[market-fragility]] (WALCL/balance sheet), [[ai-capex-cycle]] (capex blessed), [[detachment-bid]].

### 2026-07-14 ~8:40pm PT — Jake's SIGN-FLIP insight: in THIS regime, HIKING is the "for the people" move
### THESIS (interpretation — NOT fact)
- *(Jake's insight)* Historically low rates = "for the people" stimulus. Now it feels inverted —
  RAISING would be the pro-worker move, because letting it run further DETACHES the capex economy from
  the working/production economy.
- *(analysis — why the sign flipped)* The "easy money = pro-worker" valence was a DEMAND-DEFICIENT-WORLD
  artifact (2008-2021 secular stagnation: cheap money → hiring → jobs). In a SUPPLY-CONSTRAINED,
  capex-boom, inflationary world the TRANSMISSION changed: cheap money now flows to ASSETS + the CAPEX
  complex FIRST (Cantillon effect — those closest to the printer benefit first: Mag7, datacenters,
  asset owners), while WORKERS eat the inflation (the most regressive tax; real wages lag). So easy
  money now = pro-asset-owner + anti-worker; tight money = real-wage defense. **The tool didn't change;
  the WORLD did, so its distributional SIGN flipped.** Jake intuited the flip.
- **This is the debasement thesis from the WORKER'S side — the missing distributional dimension:** the
  third exit / valve ("inflate it away / bless the capex / run hot," Warsh testimony 8:30pm) is a WEALTH
  TRANSFER from labor to capital. Political irony: low rates are FRAMED as populist ("for the people")
  but are anti-populist in EFFECT — the framing is INVERTED from the effect. Warsh's "no tolerance for
  inflation (but AI-investment-is-just-investment, run hot)" = technocratic dressing on a distributional choice.
- **Volcker rhyme:** sometimes tight money IS the pro-worker move — Volcker hiked to 20%, hated then
  (recession/unemployment), vindicated later (killed the inflation destroying real wages). "Pain now for
  real-wage restoration." Jake's intuition rhymes.
- **Honest counter (per [[_calibration]]):** hiking isn't CLEANLY pro-worker — the Fed cools inflation by
  cooling the LABOR MARKET (Kashkari: "tools start in the labor market"), so you'd hit workers (jobs) to
  fix a CAPEX-caused problem; and hikes hurt DEBTORS (mortgages/credit = working-class). So "hike = for
  the people" is true on the inflation/savings axis, false on the employment/debt axis. Cleanest pro-worker
  move may be NEITHER pure easing nor hiking but targeting the capex/asset detachment directly (fiscal,
  antitrust) — but within the rates-only toolkit, Jake's inversion is directionally right.
- The takeaway: the "for the people" valence of monetary policy is REGIME-DEPENDENT. Jake supplied the
  distributional/political-economy layer the debasement + third-exit theses were missing.
- Links: [[consumption-vs-investment-crux]] (capex vs production detachment), [[detachment-bid]], [[bull-bear-ledger]].
- **Addendum ~8:45pm PT — Jake's riff (bracketed "another space"): direct capex→worker distribution,
  no inflation, skip the bureaucratic vig.** *(analysis — the useful loop-back)* The "no inflation" is
  economically CORRECT *if* it's a real productivity dividend: inflation = money chasing UNCHANGED supply;
  distributing a genuine productivity gain = distributing NEW supply, so no inflation (the catch = telling
  real productivity from financial inflation = the utilization question again). Lineage: sovereign-wealth/
  citizen dividends (Alaska Permanent Fund, Norway), UBI (why tech/Altman push it — they see AI displacing
  labor), the "ownership economy" (give workers equity in the capex). The "govt vig" critique = public-choice
  (capture, means-testing overhead) — exactly why direct mechanisms exist (Friedman's negative income tax,
  Alaska's automatic dividend). **THE PERSONAL PUNCHLINE:** since the direct-distribution won't happen, the
  individual's rational response to a labor→capital transfer is to OWN THE CAPITAL SIDE — which is literally
  what Jake's portfolio is doing. The AI-capex trades ARE his private "distribution" — capturing the
  productivity dividend as an owner because it won't come as a worker. [[detachment-bid]] has a political-
  economy root: own the assets that absorb the transfer.

### 2026-07-15 ~7:14am PT — PPI soft → July hike off the table → runway EXTENDS (but energy-led again)
### DATA (observed) — ZH feed, Wed AM
- "July rate-hike OFF THE TABLE after PPI drops most since COVID." PPI final-demand goods −1.4% June;
  **nearly 2/3 of that drop = GASOLINE −12.0%.** PPI final-demand SERVICES ROSE: 60%+ of the advance =
  final-demand TRADE SERVICES MARGINS +1.1%.
- WILLIAMS: shelter inflation "on downward path"; expects overall inflation to FALL to 3.25% by year-end.
  HASSETT: "data shows no excuse for raising rates." BANK OF CANADA drops reference to consecutive hikes.
### THESIS (interpretation — NOT fact)
- **The PPI "first test" (flagged 7/14) came SOFT → the one-month runway CONFIRMED near-term.** July hike
  dead; Williams (the tripwire-watcher) + Hassett + BoC all dovish. Valve stays open; the melt-up runway holds.
- **BUT the SAME energy-artifact + sticky-services pattern as CPI:** the PPI drop is ~2/3 GASOLINE (−12%,
  the June oil dip) — reverses with July's $85 oil. And services MARGINS are RISING (+1.1% trade services) =
  the sticky/pricing-power tell UNDER the energy mask. So: soft HEADLINE (energy), firm CORE (services margins).
  Same as CPI — the cost-push isn't in the goods PPI yet (per the Ericsson 2027-lag), and gasoline is
  flattering both prints on a one-month oil dip that's already gone.
- Net: runway extended (near-term dovish confirmed), fuse unchanged (energy reverses; services margins the
  sticky tell; the memory cost-push still ahead). Watch the NEXT prints once July oil hits.
- Links: [[demand-destruction]] (oil/gasoline), [[ai-capex-cycle]] (cost-push lag).

### 2026-07-15 — Beige Book (July): the margin-vs-price tell RESOLVES "margins, not prices — so far"
Source: July 2026 Beige Book (`raw/2026-07-15-beige-book-july.md`; Layer-1 official, data through July 6).
This is the qualitative cross-check I flagged the July book would settle: has AI/input cost-push landed in
CPI, or in margins?
#### DATA (observed)
- Prices up **moderately: 9 Districts moderate, 2 robust, 1 slight; vs prior period price growth was
  "the same or slower in ALL Districts"** → NOT accelerating.
- **"A couple of Districts reported that selling prices grew less than input costs over the period,
  crimping margins."** Pass-through explicitly MIXED, firm-by-firm (Cleveland: some pass all, some part,
  some none "for fear of losing customers").
- **Richmond (numbers):** service price growth **<3.5% YoY**; service non-labor input costs **>5.5%**;
  manufacturing input costs **~7%** but "prices received by manufacturers remained relatively the same."
- **Kansas City:** "Inflationary pressures continued to compress profit margins."
- Dominant cost driver named = the Middle East conflict (fuel/freight/petrochem/fertilizer) + tariffs.
- ⚠️ The book's *price-relief* optimism (Dallas "agreement to reopen Strait of Hormuz → gasoline falling";
  Chicago "blockages eased") is a **July-6 snapshot of a truce that has since REVERSED** (Jake's 7/12–13
  feeds: blockade reinstated, Brent ~$85). Treat the "falling fuel" expectation as stale by ~a week.
#### THESIS (interpretation — NOT fact)
- *(analysis)* **The tell resolved: cost-push is showing up as a MARGIN squeeze, not (yet) as consumer
  pass-through.** Input 5.5–7% vs selling <3.5% (Richmond); manufacturers eating ~3+ points. Warsh's
  "persistently elevated" is real in INPUT costs but the bottom-half consumer is too price-sensitive to
  pass it to — so it lands in margins, not CPI. **This is dovish for the July-29 CPI-vs-margin read but
  BEARISH for margins** (the [[ai-financing-fragility]] / earnings side).
- *(analysis)* Consistent with the same-story CPI/PPI reads above: soft headline (energy, now reversing),
  firm underlying (services margins / input costs). The memory cost-push ([[ai-capex-cycle]], Ericsson
  2027-lag) is still AHEAD of the goods PPI — and the Beige Book already shows memory-component inflation
  at the contact level (NY). **Watch the flip:** if firms stop eating it and start passing → CPI channel
  opens. The Beige Book is where that flip shows up first.
- Links: [[consumption-vs-investment-crux]] (capex-driven economy), [[ai-financing-fragility]] (margin
  squeeze = earnings risk), [[demand-destruction]] (Hormuz reversal), [[ai-capex-cycle]] (memory cost-push).

### 2026-07-16 eve — Fed turns HAWKISH; long end UP → cuts against the back-door-easing bull
Source: scanner digest (`raw/2026-07-16-scanner-digest-eve.md`).
- DATA: Dallas Fed **Logan calls for "modestly higher" rates**; **Schmid** — inflation above 2% target, cuts
  DELAYED, "one CPI won't force a cut"; **30-yr mortgage 6.55% = 1-yr HIGH.**
- *(THESIS)* The [[compression-thesis]] "coerced-Treasury-buying → lower long end → back-door easing" bull
  (Jake, 7/16) needs the LONG END to FALL. Today it ROSE (mortgages 1-yr high) and the Fed leaned hawkish.
  = the bear's "objection migrates to the rate / long end won't cooperate" + war→inflation→can't-cut,
  printing. The easing mechanism is directionally LOSING right now (a warning, not yet a verdict — one day).

### 2026-07-17 ~11:50pm PT — Labor market FREEZING (JOLTS-vs-hiring); a viral "cover-up" claim, filtered
Source: **Jake's OWN post** (revealed 7/17 — "that's me, it was a post lol"; originally logged as a viral
paste). Numbers CLAIMED, NOT independently verified here. Logging the STRUCTURE + the real signal. NOTE: the
stock/flow correction below stands regardless of author — the analysis was run blind before attribution.
#### DATA (observed / as-claimed)
- Video's frame: openings 6.9M/hires 5.5M (Mar), openings 7.6M/hires 5.2M (Apr), ~46% "gap" held (May) →
  "openings 146% of hires = fake jobs cover-up." **⚠️ CLAIMED figures, unverified.**
- The part that's structurally solid regardless of the exact numbers: **net job growth 214k (Mar) → 148k
  (Apr) → 129k (May) → 50k (Jun) — a collapsing hiring trend.**
#### THESIS (interpretation — NOT fact)
- *(correction of the video's math)* **Category error: openings is a STOCK** (unfilled positions on the
  last business day) **vs hires is a FLOW** (total over the month). Comparing them as a "gap %" is
  units-mismatched (reservoir level vs monthly tap flow). Openings > monthly-hires has been the OPENLY
  DISCUSSED regime since 2021; the ratio PEAKED ~1.8x in 2022 and 1.46 is **DOWN from peak = normalizing**,
  not a hidden record. "Record highs / cover-up" is likely wrong on the level.
- *(filters, live application of [[_assumption-filters]])* **Goodhart bites FOR the video:** ghost/evergreen
  postings are real — once openings became a watched "strength" metric it decoupled from hiring. So "some
  postings aren't real" = TRUE. **But Occam + Hanlon kill the CONSPIRACY:** stock/flow units + banal stale
  reqs + a cooling hire rate explain every number without coordinated intent; thousands of firms
  independently leaving reqs up is emergent mess, not a plot. Verdict: **fake postings yes, cover-up no.**
- *(the signal that matters for US)* The buried trend — **net job growth collapsing 214k→50k** — is the real
  tell: the hiring engine is FREEZING ("no-hire/no-fire," labor hoarding). Two vault linkages:
  1. **Fed Trap sharpens** ([[market-fragility]]): a cracking labor market is normally the disinflation that
     LETS the Fed cut (the bull rescue). Cracking WHILE war/oil inflation runs = Fed **can't cut into it** =
     stagflation-lite tighter. This is the labor face of the GDP decel (2.9→1.3%).
  2. **Demand-side vote on the [[compression-thesis]] razor:** falling hiring → softer consumer → inputs
     cheapening because DEMAND fell to meet supply (the BEAR branch), not supply catching up (benign). A
     frozen labor market is a point for the bear's reading of the razor.
- ⚠️ Calibration: one post + unverified figures; the hiring-trend collapse is the durable part and worth its
  own data pull. WARNING (a cooling STATE), not a dated TRIGGER — labor can freeze for quarters.

### 2026-07-17 ~7:13am PT — UMich sentiment bounce is a STALE truce-window snapshot (survey timing trap)
Source: ZeroHedge (Jake paste), UMich prelim July.
#### DATA (observed)
- Headline sentiment **49.5 → 54.4** (exp 51.0), highest since Feb; 2nd straight ~10% monthly jump. Rebound
  off record 46-yr June low. All 5 components up; **durables buying conditions +20%, yr-ahead biz +20%.**
- Driver (Hsu, Dir. of Surveys): **easing pump prices** in recent weeks. Gains pervasive across
  age/income/wealth/party, **particularly strong among consumers WITHOUT a bachelor's** (the bottom-half,
  gas-sensitive cohort). **Yr-ahead inflation expectations 4.6% → 4.2% (still elevated).**
- Hsu's own caveat: momentum "difficult to sustain if recent declines in gas prices continue to reverse."
- **⚠️ THE KEY LINE: interviews Jun 23–Jul 13, but >70% completed BEFORE the Jul 7 resumption of US strikes
  and the subsequent gas-price rise.** The print measures the PRE-escalation calm.
#### THESIS (interpretation — NOT fact)
- *(analysis)* **Backward-looking, gas-driven, and already reversed.** Same staleness pattern as the Beige
  Book "Hormuz reopening → falling gasoline" (flagged stale by ~a week): this is a snapshot of the truce
  window, and 70%+ of it predates the 6th-night escalation + gas re-rise now on the tape. Next month faces
  Hsu's own reversal headwind. **Do not read this as "the consumer is fine NOW."**
- *(analysis, the tension that matters)* **Sentiment bounced (backward, gas) while the labor market is
  FREEZING (forward, net job growth 214k→50k above).** Feel-good coincident print vs deteriorating forward
  crack — classic divergence. The sentiment is the lagging pump-price feel; the jobs data is the leading
  break. Weight the jobs.
- *(razor / Fed)* The whole bounce rode ONE input (gas = a supply/price variable), now reversing → the
  demand-side support is fragile ([[compression-thesis]] razor: is consumer strength real or just cheap
  gas?). Inflation expectations easing (4.6→4.2) is a dovish crumb, but still-elevated + war-gas reversal
  threatens to re-lift it = the [[market-fragility]] Fed-Trap "can't-cut" thread intact.
- ⚠️ Calibration: near-zero actionable; a stale coincident print. Logged for the timing trap + the
  sentiment-vs-labor divergence, not the headline beat.

### 2026-07-18 ~7:54am PT — foreclosures +21% H1 but STILL below normal: warning, not crisis (base-rate trap)
Source: ATTOM via Epoch Times/ZH (Jake paste). July-16 ATTOM report.
#### DATA (observed)
- **227,548 US foreclosure filings H1-2026, +21% YoY, +28% vs 2yr ago.** **0.16% of all housing units** (FL
  worst 0.27%, SC 0.26%). State YoY leaders: **Idaho +59%, Colorado +57%, Georgia +52%, NC +47%.**
- **⚠️ CONTEXT that guts the scare:** 2021 was the pandemic-MORATORIUM low (foreclosures artificially crushed);
  rising since. BUT **every first-half 2008–2019 was HIGHER than 2026** — still BELOW the pre-COVID baseline.
  ATTOM CEO: "gradually returning to more TYPICAL patterns." 30yr mortgage **6.55% (1-yr high)**; Redfin: demand
  subsiding on cost.
#### THESIS (interpretation — NOT fact)
- *(base-rate trap, same as insider-selling / JOLTS)* "+21%!" is measured off a **moratorium-suppressed floor**
  and the ABSOLUTE level is still below every boring pre-pandemic year. **Normalization, NOT a new crisis;**
  0.16% of units is tiny. **WARNING (a state), not a TRIGGER** — not 2008, not close. Don't trade the headline.
- *(the real, slow undercurrent — on-thread)* Direction is up + mortgage 6.55% (1-yr high) + demand backing off
  = the **consumer/housing leg of the slowdown**, slotting next to the labor-freeze (JOLTS 214k→50k) + GDP
  decel. The **Fed Trap in households:** rates can't fall (can't-cut into war/oil inflation) → housing stress
  *grinds* higher. Demand-side softening = a point for the [[compression-thesis]] BEAR branch (consumer strain).
- *(regional tell)* Biggest jumps = Idaho/Colorado/GA/NC = the **pandemic BOOMTOWNS** normalizing hardest =
  froth mean-reverting, not a nationwide break.
- Net: a warning-grade consumer-stress brick in the slowing-economy/can't-cut-Fed wall; NOT a fired trigger. Book unchanged.

## 2026-07-19 ~10pm PT — "Financial gravity" (SPX / Fed balance sheet): the debasement spine, and its honest bounds
Source: Jake paste — viral "financial gravity" quote + Bloomberg chart (SPX Index / FARBAST, 1995-2024). Tool: `tools/financial_gravity.ipynb`.
### DATA (observed — from the Bloomberg chart)
- SPX / Fed balance sheet (FARBAST): **high 0.0026 (Mar 2000), low 0.0003 (Nov 2008), ~0.0007 (2024), avg 0.0011.**
- → From the **2008 low the ratio rose ~2.3x** (0.0003→0.0007). The 2022-2024 leg rose to new post-2008 highs
  **during QT** (balance sheet shrinking). Over the full 1995-2024 window the ratio is BELOW its pre-2008 avg
  (balance sheet grew faster than stocks across the whole period).
### THESIS (interpretation — NOT fact; calibration: monotone-confirming ideological claim → push hard)
- *(the LEGIT kernel — concede)* QE was a huge 2009-2021 tailwind; it inflated asset prices and **widened wealth
  inequality** (asset owners/elites) — the distributional critique is solid/mainstream. A large share of NOMINAL
  gains is debasement/liquidity — the "own the numerator" spine. This note's whole reason for being.
- *(the chart REFUTES its own caption — 3 ways)* (1) **"Flat since 2008" is a Y-AXIS ILLUSION** — the 2000 spike
  (0.0026) compresses 2009-2024 into a low flat-looking band; the actual move is a **2.3x UPTREND**. Zoom to
  2009-2024 = clear rising trend. (2) A rising ratio = **stocks OUTPACED the balance sheet** since 2008; if it were
  all QE the ratio would be FLAT. (3) The 2022-2024 rise happened **during QT** → directly refutes "maintained
  through QE."
- *("correlation nearly 1" = spurious)* Two upward-trending (non-stationary) series always correlate ~1 in LEVELS
  (shared trend — Fed BS also "correlates ~1" with pizza sales). Honest test = correlation of CHANGES (returns vs
  BS changes) = weak, regime-dependent. Classic spurious-regression trap. "Plugged directly into equities"
  overstates the plumbing (Fed buys Treasuries/MBS, not stocks; transmission is INDIRECT via discount rates).
- *("entire rally is an illusion" = refuted)* Ratio rose 2.3x + S&P earnings ~tripled since 2009 (real cash flows)
  + QT-era rally. Nominal ≠ illusion. **The rally is PART liquidity (big, 2009-2021) + PART real (earnings + the
  non-Fed 2022-2024 melt-up).**
- *(the real question it throws back)* Financial gravity is a real force stocks have been ESCAPING, esp. 2022-2024
  — and whether that escape is real earnings or a bubble (private credit / AI capex) IS the [[market-fragility]]
  question. Not "it's all the Fed," which the chart quietly disproves. `financial_gravity.ipynb` quantifies the
  QE-flat vs QT-breakout split + the R² (how much of SPX the balance sheet actually explains).
- *(firewall note — the mirror of tonight's HF error)* Data (Bloomberg chart) = real; THESIS (caption "entire
  rally illusion") = overreach. Honor the data, check the claim — the discipline running the correct direction.

### RESULT — financial_gravity.ipynb run (Jake, 2026-07-19 ~10pm PT). Prior CONFIRMED; thesis upgraded to M2.
#### DATA (observed — the run)
- **SPX/Fed-BS ratio trend:** full +1.6%/yr; **QE era (pre-6/22) −0.4%/yr (≈flat)**; **QT era (6/22→) +29.7%/yr,
  moved 2.40x.** SPX/M2 trend +4.2%/yr (moved 1.72x).
- **R² of log-SPX on log-denominator (levels):** Fed BS 0.72 (elasticity 0.91); **M2 0.94 (elasticity 1.60)**;
  Fed BS QE-era 0.69 (elast 0.74); **Fed BS QT-era 0.91 but elasticity −1.87** (BS down while SPX up = inverse).
#### THESIS (interpretation — NOT fact)
- *(prior graded — landed)* Predicted flat-QE / break-up-QT + M2-fits-better: all confirmed. QT elasticity −1.87 =
  the Fed *drained* while stocks rose → hardest refutation of "maintained through QE."
- *(⚠️ apply the spurious-correlation caveat to the tool's OWN R²)* All three R²s are LEVELS regressions of
  non-stationary (trending) series → absolute values INFLATED by shared trend (same trap as "correlation ~1").
  Valid = the RELATIVE ranking (M2 0.94 > Fed BS 0.72). Overstated = reading "94%" as explained *returns*. v2:
  regress weekly RETURNS for the honest predictive R². QT R²=0.91 is the most trend-contaminated (short window,
  two opposite drifts fit a line trivially) → read as "DECOUPLED," not negative causal elasticity.
- *(the upgrade — the defensible version of "financial gravity")* It's not the Fed BALANCE SHEET, it's **broad money
  (M2)** — and **stocks are ~1.6x levered to it** (elasticity 1.60). M2 = Fed + bank credit + fiscal, which is why
  it kept lifting stocks through QT when the Fed's own sheet shrank. The narrow gauge (Fed BS) has been actively
  MISLEADING since 2022; M2 (better: global M2) is the gauge that tracks. Debasement spine, sharpened: equities =
  a levered claim on the money supply.
- *(the original claim's honest bounds)* "Flat since 2008" = RIGHT for 2009-2021 (QE, −0.4%/yr) and WRONG for
  2022-2026 (the 2.4x QT breakout). A true statement that expired mid-2022. The 4-yr decoupling (rally on broad
  money + earnings + AI capex, NOT the Fed) IS the [[market-fragility]] question, now quantified.

## 2026-07-23 ~8:35am PT — tariffs = a SECOND inflation input stacking on oil into a boxed Fed (higher-for-longer reinforced)
Source: Jake tariff briefing (as of 7/23/26). The 2025 IEEPA reciprocal/fentanyl tariffs were TERMINATED Feb 2026 (legal
defeat); current = a temporary 10% global Section-122 surcharge + narrower 232/301/338 tariffs.
### DATA (as-reported)
- **10% global surcharge EXPIRES 12:01am ET Jul 24 (tonight)** unless extended/replaced. USTR Section 301 replacement (10%
  / 12.5% on 60 economies, forced-labor basis) is teed up as successor — hearings done, no effective date.
- Sector tariffs in force: **steel 50% / aluminum 25% (deriv) / copper 15%**; autos+parts 25%; **softwood lumber 10%**;
  **cabinets/vanities 50%** (up from 25%); upholstered wood 30%. **AI chips 25%** (H200/MI325X) but BROAD exemptions (US
  data centers, R&D, startups, public-sector) = gutted. **Brazil 25%** (active 7/22). **Canada +50%** on selected goods
  (autos/dairy/alcohol + cement, wine, etc.) from **Aug 19** (energy/potash/critical-minerals/232 excluded).
- **Patented pharma 100%** default from Jul 31 (large-co annex) — **but 0% thru 2029 for onshoring+MFN, 20% onshoring-only,
  15% EU/JP/KR/CH, 10% UK; generics/biosimilars EXEMPT.** → **LLY** (book) likely exempt/reduced via onshoring, NOT the 100%.
### THESIS (interpretation — NOT fact)
- *(the inflation stack)* Tariffs = a SECOND inflation impulse layered on oil-$100 + war, right as 10Y/2Y hit YEAR HIGHS
  and the Fed is boxed (jobless claims 1969-low, Warsh no-cuts). Reinforces higher-for-longer from a second source →
  tightens the screw on the debt-funded AI buildout ([[compression-thesis]] means-of-financing; [[ai-financing-fragility]]).
- *(tonight's binary)* A CLEAN lapse of the 10% surcharge (no replacement) = the disinflationary surprise (mild oil offset);
  a Section-301 replacement = tariff-regime swap, inflation persists. Base case = swap, not tariffs-off. Watch for a
  proclamation tonight. *(AI-chip tariff = non-event, exemptions gut it; discount for the capex thread.)*
- *(real-economy tie — Jake's contracting COGS)* aluminum (window frames)/copper/steel/lumber/cabinets + the Aug-19 Canadian
  cement list = direct input-cost creep on his bids. The same impulse spiking the 10Y lands on his material invoices — a
  descriptive real-economy read, not a market call.

## 2026-07-23 ~8:50am PT — Jake's run-hot/debasement synthesis (+ the jobless-claims correction + the tariff-dollar Triffin trap)
Jake: low jobless = compressed denominator? "lie about jobs and cut to run hot"; debt+Iran-war spend looming; "tariffs +
shrinking trade deficit keeps the dollar afloat?"
### DATA / mechanics (the corrections)
- **Claims ≠ the rate (⚠️ Jake conflated).** Initial jobless claims = a FIRING/benefit-filing FLOW; you can't hide
  discouraged workers out of it (they were never in it). The DENOMINATOR/discouraged-worker critique = the unemployment
  RATE (unemployed/labor force), NOT claims. Valid claims critique instead: **LOW-FIRE/LOW-HIRE freeze** (claims see only
  firings; a frozen market = low claims + soft) + gig/self-employed excluded + benefit exhaustion → "lowest since 1969" =
  apples-to-oranges. Right skepticism, wrong lever.
- **"Lie about jobs":** hold "lie" as interpretation (unfalsifiable, info-war discipline). Documented version = initial
  prints run hot → revised down hard + real politicization risk (BLS-commissioner firing). Skepticism warranted; fabrication unproven.
### THESIS (interpretation — NOT fact)
- *(run-hot = inflate-away-the-debt, the coherent core)* A sovereign with this debt BENEFITS from moderate inflation (erodes
  real debt) — arithmetic, not conspiracy. Trump's REVEALED preference (Fed pressure to cut, tariffs, fiscal/war expansion,
  explicit weak-$-for-exports) = a mix that PRODUCES inflation regardless of stated preference. This IS the debasement regime.
- *(the tariff→dollar question — weak + partly BACKWARDS: the Triffin trap)* The channel that DOES support $: tariffs →
  inflation → Fed can't cut → rate differential (short-term $-positive; also today's DXY +0.5% = mostly HAVEN flight, not tariffs).
  But "shrink the trade deficit → support $" is BACKWARDS: the US deficit is the flip side of the capital surplus — it's HOW
  the world gets dollars to recycle into TREASURIES. Shrink it via tariffs → less foreign Treasury demand → yields UP → a
  FUNDING problem for the war/debt (Triffin). And the DOMINANT vector is $-NEGATIVE (run-hot/inflate/weak-$-preference).
- *(the synthesis — afloat AND debased, different channels)* The $ stays afloat NOMINALLY (rate differential + haven) while
  DEBASED in REAL terms — not contradictory. new-economy-regime/financial-gravity: the $ needn't CRASH to be debased; just
  lose purchasing power faster than exchange rate. **GOLD is the referee** — DOWN today (real rates/haven-$ up) = a rates-fear
  day, NOT a debasement day. Debasement tell = gold + $ rising TOGETHER, or gold ripping vs unjustified real yields. Watch the
  PAIR, not DXY alone. [[gold-flows]], [[demand-destruction]] (oil-inflation), [[compression-thesis]] (means-of-financing/rates).
