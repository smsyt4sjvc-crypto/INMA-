# AI-Infra Allocation Map — tonight's names, sorted

Consolidation of the 2026-07-01 session's investable output. Related: [[ai-capex-cycle]],
[[power-scarcity-equities]], [[nuclear]], [[power-not-petroleum]], [[portfolio-state]], [[_calibration]].

> **This is a coverage map + entry framework, NOT a buy list.** Descriptive construction; sizing
> and execution are Jake's. Firewall: DATA = what's held / what's factual. THESIS = the framing.

## The one thing that matters (read first)
**Everything below is ONE trade** — the AI-capex / memory / power complex, all correlated. So:
1. Size the **whole cluster as a single exposure**, not each name on its own.
2. **Jake already owns most of it** (see "held" tags) — so the marginal decision is *gaps + timing*,
   not "buy everything." "Invest all of that" = maxing a position he's already heavy in and hedged
   against. The barbell (cash + SPY Dec puts) is the counterweight; don't spend it into the top.
3. Most names are **already extended** → limit/ladder entries on flushes, not market buys.

## Tier 1 — CORE (cash-flowing, readiness/toll-adjusted; own the toll)
- **MU** *(held, 28% trading basket)* — memory shortage confirmed & durable near-term; ⚠️ all-in on
  the cycle (killed Crucial), cyclical-top + efficiency-whipsaw risk. Watch the retail-pricing flip.
- **GEV** *(held)* — most-advanced *investable* SMR (BWRX-300) + grid; the toll, not the lottery.
- **AVGO, MRVL** *(held)* — storage controllers/connectivity = the memory-overflow "get by" layer.
- **VST, CEG** *(held)* — merchant IPPs capturing record PJM capacity prices (nuclear-heavy).
- Toll energy *(LNG/VG held)*: **WMB, LNG, KMI, TPL** — midstream/export/royalty > producers.

## Tier 2 — CYCLICAL beneficiaries (real, but late & P&S-cliff exposed)
- **STX, WDC** — HDD duopoly, sold out 2026. *(GAP — not held)* The purest "old-school gets bid."
- **SNDK** — pure NAND *(GAP)*. **SIMO** — pure NAND controller *(GAP)*. **ALAB** — CXL memory expansion *(GAP)*.
- Cooling *(VRT/FIX held)*: **AAON**. Grid *(POWL/PWR/ETN/MYRG held)*.
- ⚠️ All = AI-capex derivatives → same cliff. **LRCX/AMAT/KLAC** (fab equip) highest-beta; **AMAT = Burry short.**

## Tier 3 — OPTIONALITY (pre-revenue / pre-readiness; small, Tier-C sizing)
- **OKLO, SMR, NNE** *(OKLO/NNE held)* — SMR developers; valuations ahead of NRC reality. Optionality only.
- **XE** — WATCH, don't chase: Apr-2026 IPO, −40%, **Sept-1 lockup** overhang → entry *after* the flush.
- Tape/cold overflow: **IBM** (quality), **QMCO** (distressed spec). Fuel: **CCJ** *(GTC pending)*, **LEU**.

## Entry windows (buy the flush, not the top)
- **Late July 2026:** opex (Jul 17) + mega-cap earnings + FOMC (Jul 28-29) cluster → possible rollover.
- **Sept–Oct 2026:** midterm-cycle low *and* XE lockup expiry overlap → the "flush is the entry" window.
- Mechanism already set: the **semis GTC ladder** (AMD/NVDA/MRVL/TSM/MU rungs) catches the flush —
  VERIFY those GTCs are live/vol-calibrated (the one PENDING item).

## Leading-indicator triggers (the edges found tonight)
- **Memory:** retail "request-pricing / sold-out" → "in-stock / listed / **falling**" = MU cycle turning,
  *before* earnings. Check from a retail page.
- **Nuclear:** first-concrete / NRC approval milestones, NOT siting announcements.
- **Oil:** Cushing draw + crude backwardation → the demand-destruction/short-oil lean weakening.
- **Detachment Bid:** 0DTE %, lottery-stock premium, crypto flows roll over while index holds → melt-up
  losing its buyer → puts nearer.
- **Fragility engine** composite + trigger panel ([[fragility-engine]]).

## What this does NOT change
Barbell stays: cash dry powder + SPY Dec 745 puts as the hedge; QLD as the leveraged long. The map is
for deploying *deliberately, on flushes,* into gaps — not for going all-in at a documented top.

## 2026-07-26 ~9:45pm PT — Micron+Meta white paper: LPDDR5X qualified for hyperscale servers (the memory demand SECOND LEG, in writing)
Source: `raw/archive/2026-07-26-micron-meta-lpddr-dc-whitepaper.pdf` (Micron white paper Rev A 07/2026,
co-authored by 4 Meta hardware engineers). Vendor collateral — read DATA as "what the paper claims."
### DATA (as-published, vendor benchmark)
- What it is: Micron + Meta jointly characterize **LPDDR5X (mobile-class memory) for datacenter servers**
  using **DCPerf — Meta's own benchmark suite, used internally "for product evaluation, platform
  configuration, and procurement decisions."** Test platforms are **ARM 72-core/socket** servers.
- Configs: SKU1 = 512GB/socket @ 6400 MT/s (4-rank); SKU2 = 256GB/socket @ 8533 MT/s (2-rank) —
  rank count trades capacity vs speed.
- **Power (the headline):** LPDDR5X ≈ **1/3 the power of DDR5**; measured **6.8% of total system power**
  under the memory-heaviest workload; prior Micron study: up to **75% lower DRAM power vs DDR5**.
- Bandwidth: 8533 vs 6400 MT/s → +13% delivered bandwidth → +11% AI-pipeline throughput (Tensor
  Rebatching), +18% IPC on Deserialization. Latency: ~9% lower P99 tail on Meta's web-serving benchmark.
- **Capacity is the multiplier:** 2x DRAM (512 vs 256GB) → **2.8–3.5x Spark SQL throughput; 38.75x on the
  shuffle stage** once spill-to-disk is eliminated. Paper's words: "memory capacity is the decisive
  performance factor."
- Form factor: **SOCAMM2 modules kill LPDDR's soldered-down constraint** — 256GB module, **up to 2TB
  LPDDR5X per CPU socket**; signaling roadmap toward 9600 MT/s. Opening premise of the whole paper:
  datacenters face "increasingly daunting power and thermal constraints."
### THESIS (interpretation — NOT fact) — Independence: 1/5 (single vendor-published source; Meta co-authorship is the only external anchor)
- *(analysis — what survives the marketing discount)* The NUMBERS are vendor-picked; the durable signal is
  the **customer's fingerprints**: Meta engineers co-authoring, Meta's procurement benchmark as the yardstick,
  ARM platforms = what public qualification of a new memory class for fleet buying looks like. This is the
  **second demand leg for DRAM made explicit** — LPDDR migrating into GENERAL-PURPOSE hyperscale servers
  (Spark, web serving — zero GPU involved), on top of HBM-for-accelerators.
- *(analysis — razor support)* Directly supports the 7/17 razor observation in [[compression-thesis]]:
  memory demand tracks deployment/data volume, not GPU efficiency. Capacity-as-multiplier (38x) is the
  engineering argument for MORE DRAM per socket regardless of what happens to the GPU bill.
- *(analysis — the power hook)* The pitch is WATTS, not speed: vendor+customer co-writing "memory as
  power-budget relief" = the power ceiling ([[power-scarcity-equities]], [[buildout-bottleneck-map]] PJM
  section) is now a stated procurement axis. DRAM watts saved = accelerator watts freed → memory efficiency
  monetizes THROUGH power scarcity. Also the benign face of the [[compression-thesis]] heal: input deflation
  (bandwidth-per-watt) via SUBSTITUTION, where the same oligopoly sells the substitute — heals the payer
  without killing the seller.
- *(steelman — against reading this as MU-bullish confirmation)* (1) **Not a Micron moat**: Samsung/SK Hynix
  ship LPDDR and SOCAMM-class modules too — this is a DRAM-industry demand story; Micron just wrote it up
  first. (2) **Margin question open**: LPDDR displacing DDR5/RDIMM server sockets can be mix-dilutive if it
  prices like mobile product — content growth ≠ profit growth until proven in gross margin. (3) **Timing
  flag**: a vendor publishing the more-memory-per-server gospel during the exact hoarding/pull-forward stage
  the vault flagged (IBM front-running, 7/14) is ALSO what late-stage demand marketing looks like — texture
  for the near-term hold-side runway on MU *(held, 28%)*, touches NOTHING in the 2028-glut / Burry-short
  medium-term caution. Both stand. [[portfolio-state]], [[_calibration]].
- *(Jake's catch, 2026-07-26 ~10pm PT — the white paper is the DEMAND side of the lawsuit's story)* The 6/25
  DRAM class action ([[ai-capex-cycle]] 7/7 cluster) alleges the big 3 starved commodity DDR3/DDR4 "under the
  pretext of the HBM transition" — datacenter demand eating consumer memory. This paper is the NEXT chapter of
  the same crowding-out, published proudly: hyperscalers qualifying **LPDDR — mobile's own memory class
  (iPhone/M-series Macs/Android are the incumbent buyers)** — for fleet deployment at up to 2TB/socket. If it
  scales, AI demand collides with Apple/OEMs *in their own product class*, not just adjacent to it. Cuts three
  ways: near-term MORE pricing power (tighter LPDDR = bull the runway); politically it worsens the exact
  "AI capital outbidding consumers" optics the complaint weaponizes (phones priced out by datacenters = the
  ratchet's next exhibit); legally it fattens the dormant WHALE claims — Apple already has self-documented
  damages (its June price raise) and is the vault-tagged clean claimant that monetizes leverage in the GLUT,
  when allocation risk no longer mutes it. Firewall note: the paper is demand-side marketing, not evidence of
  supply fabrication — the collusion allegation stays unproven; parallel oligopoly conduct isn't per se illegal.

## 2026-07-26 ~10pm PT — VERIFIED: Apple lobbying Trump admin for CXMT/YMTC access; MICRON LOBBYING AGAINST — the whale squeeze is LIVE, in front of the White House
### DATA (WebSearch verified 7/26; multi-outlet)
- **Apple is testing CXMT (ChangXin) DRAM** for China-market devices and **Cook + top execs have pitched
  Trump, Lutnick (Commerce), Bessent (Treasury)** on using **CXMT + YMTC** memory in Apple products sold
  **outside the US**. Timeline: petition reported 6/29 → active lobbying 7/1 → testing confirmed 7/8 →
  **7/24: "Apple and Micron clash before Trump"** (9to5Mac) — **Mehrotra (MU CEO) directly warning Lutnick
  et al against allowing CXMT/Chinese memory into US supply chains.**
- Blockers: CXMT is on the **Pentagon 1260H military-linked list**; House China Committee (Moolenaar) +
  Foreign Affairs (Mast) call any CXMT/YMTC sourcing a "grave mistake"; lawmakers urging an outright BAN
  on Chinese memory.
- Context in the coverage: consumer DRAM prices ~4x over recent quarters on the HBM capacity shift; Apple's
  late-June price raises ($100–500 across Macs/iPads) explicitly framed as memory-cost passthrough;
  iPhone 18 Pro memory cost reported as threatening to ~triple.
### THESIS (interpretation — NOT fact) — Independence: 3/5 (multi-outlet trade press, single underlying report chain; no primary docs)
- *(Jake's frame, sharpened — the three-lever whale squeeze)* Apple is running a classic procurement squeeze
  on the oligopoly: **Lever 1 = the China valve** (CXMT/YMTC petition — live); **Lever 2 = the dormant legal
  claim** (the 6/25 class action is the roadmap; Apple's June price raise = self-documented damages);
  **Lever 3 = the historical prepay-for-priority playbook.** Jake's chain: petition FAILS → the legal
  *threat* activates to extract priority pricing "once again." Refinement: the levers compound rather than
  queue — the petition is doing leverage work NOW (Micron fighting it publicly proves the threat is priced
  as real; you don't spend CEO political capital against a bluff), and the legal threat's cheap form
  (private, paired with lobbying) works pre-glut even though the CLAIM monetizes best post-flip
  (whale-timing, [[ai-capex-cycle]]). Apple v. Qualcomm precedent: Apple will go to war with a sole-source
  supplier while still dependent.
- *(the fork is an event for MU either way)* **Approve** (even ex-US-only): the captive-customer premium
  cracks, CXMT gets qualified/legitimized by the world's cleanest OEM = the 2028 glut leg ACCELERATES
  (Burry's short thesis gets its demand-side confirmation early). **Deny**: Apple stays captive in the
  shortage (near-term bullish MU pricing) BUT the damages narrative strengthens ("we tried to escape; the
  state locked us in with the profiteers") → feeds the whale claim + the political ratchet, and BOM-driven
  consumer price raises keep the "AI outbidding consumers" politics loud. Either branch: **memory pricing is
  now arbitrated in Washington, not the market** — the designated-champion umbrella ([[buildout-bottleneck-map]]
  7/11) colliding with the champion's own biggest customer. Watch: the admin decision, any 1260H/Commerce
  action, a YMTC(NAND)-vs-CXMT(DRAM) split compromise, MU lobbying disclosures.
- *(Jake's premium read, logged)* "Any Mag-7 not buried in AI capex is viewed as a premium" — the
  [[compression-thesis]] smallest-capex-gap discrimination, restated from the tape (AAPL raised prices
  publicly, ripped anyway, took #1). Vault adds the falsifier: the premium is the market's CURRENT sign on
  capex, not a law — same capex-light fact traded as a DISCOUNT in the "Apple behind on AI" tape. ~~Flip tell:
  a hyperscaler prints capex-UP + stock-UP → the discrimination is reversing.~~
  > 🔄 CORRECTED [2026-07-26 ~10:05pm PT — Jake's catch]: that flip-tell was STALE against the vault's own
  > record — the test already RAN 7/22 and fired BEARISH (GOOGL: Cloud crushed, $205B naked capex raise,
  > −3.85% AH; escape hatch FAILED; graded "my miss, Jake's hit" in [[compression-thesis]]). The venue for
  > the flip-tell MOVED from the income statement to the FINANCING tape — see the razor's terminal form in
  > [[compression-thesis]] (2026-07-26 addendum): earnings prints lost evidentiary value (circular revenue +
  > paper gains), so the discrimination reverses only via the CREDIT channel — AI-complex spreads tightening
  > + a mega AI debt raise that prices tight/oversubscribed AND the stock rallies ON the raise.

## Sources
- 2026-07-01 session; portfolio memory `data/jake-bishop-project-memory.csv`.
- 2026-07-26: `raw/archive/2026-07-26-micron-meta-lpddr-dc-whitepaper.pdf` (Micron/Meta LPDDR5X white paper, Rev A 07/2026).
- 2026-07-26: WebSearch — 9to5Mac 7/24 (Apple/Micron clash before Trump), Electronics Weekly 6/29 (CXMT petition), MacDailyNews 7/1+7/8 (lobbying, testing), wccftech (iPhone 18 memory costs), cryptobriefing (lawmakers urge ban).
