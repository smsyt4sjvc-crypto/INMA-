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

## Sources
- 2026-07-01 session; portfolio memory `data/jake-bishop-project-memory.csv`.
- 2026-07-26: `raw/archive/2026-07-26-micron-meta-lpddr-dc-whitepaper.pdf` (Micron/Meta LPDDR5X white paper, Rev A 07/2026).
