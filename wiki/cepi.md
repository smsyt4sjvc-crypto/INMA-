# CEPI — Capex → Earnings → Price Intensity

A measure the **user invented** to gauge AI-capex fragility. Related: [[ai-capex-cycle]],
[[market-fragility]], [[fragility-engine]].

> Firewall: DATA = what the measure literally computes + observed inputs. THESIS = what a
> given CEPI reading is claimed to *mean*. The construct itself is the user's idea, not an
> established/consensus metric — flag it as such wherever cited.

## DATA (definition — what it computes)
- Universe treated as one "sector": Mag-7 + MU + ORCL (NVDA, MSFT, GOOGL, AMZN, META, AAPL,
  AVGO, MU, ORCL).
- Inputs per name (annual, current-cycle): capex, net income, revenue, price.
- Core ratios:
  - **Air gap** = (sector capex YoY growth) − (sector earnings YoY growth). >0 = capex
    outrunning earnings.
  - **Intensity** = sector capex / sector net income.
- Data source for current cycle: **yfinance annual** financials (clean). EDGAR quarterly is
  the higher-resolution upgrade but has XBRL tagging inconsistencies (YTD-vs-discrete,
  company-specific tags) — see ⚠️ below.

## ⚠️ artifact notes (do not treat as clean)
- EDGAR quarterly pull gave ORCL intensity 2.82, AMZN/NVDA empty, capex/revenue distorted —
  cause was per-company XBRL tagging (some report discrete 3-month, some YTD cumulative).
  CEPI for the *current* cycle was therefore pivoted to yfinance annual. EDGAR only for the
  harder multi-year cloud-era baseline, and only with tag normalization.

## THESIS (interpretation — NOT fact)
- *(user's thesis)* Capex growing faster than the earnings it's supposed to produce (positive,
  widening air gap) is the tell of a late-stage capex bubble; price is discounting returns
  that the cash flows don't yet support. When intensity is high AND price is at highs, the
  setup is fragile.
- *(analysis)* CEPI is a *leading* lobe of [[fragility-engine]] because fundamentals lead
  price — weight it heavily, but it is a bespoke construct, not a validated factor. Treat its
  output as a structured opinion, not a reading off an instrument.

## Sources
- User's v2 memo (CEPI framework). Session EDGAR/yfinance pulls, 2026-H1.

---

## 2026-08-07 ~1:55pm PDT — ★★★ CEPI GETS AN INSTRUMENT: `tools/cepi_tracker_cell.py` (Jake's spec: *"take capex:earnings… scale down and create a running E/C ratio"*)

**THE HONEST ANSWER TO "CAN WE REASONABLY RIGHT NOW": THE FRAMEWORK YES, THE NUMBER NO — AND THE CELL
PROVES IT BY PRINTING ITS OWN COVERAGE.** Seeded with everything the vault holds, the tracker returns
**ONE company-quarter (SPCX 2026Q2) filling 1 of 4 ratio cells.** Not a series — a seed. *(This note
had a thesis and no instrument for six weeks; it now has the instrument and a measured data gap.)*

### THE DESIGN — why FOUR ratios, not one (analysis)
- **E/C = net income ÷ capex** — Jake's ask; GAAP profit per dollar of capex.
- **★ OCF/C = operating cash flow ÷ capex — THE LINE THAT MATTERS. Below 1.00 the buildout is NOT
  self-funded** (FCF<0 ⟺ OCF/C<1). **The vault already has this firing at the aggregate: Alphabet's
  first negative-FCF quarter since its 2004 IPO, and the GS chart's five-hyperscaler combined negative.**
- **C/R = capex ÷ revenue** — intensity. Vault comparators: **SPCX 2.35x · ORCL ~1.0x · MSFT ~0.7x.**
- **DA/C = D&A ÷ capex** — the CATCH-UP ratio.
- **★★★ THE TRAP E/C ALONE WALKS INTO, AND WHY DA/C IS MANDATORY: earnings are AFTER depreciation, so
  as the 2024-26 wave depreciates, E/C falls for TWO reasons at once — capex UP and earnings DOWN.
  DA/C separates them: rising DA/C = the old capex hitting the P&L (mechanical, expected); FLAT DA/C
  with falling E/C = earnings deteriorating for a REAL reason.** **That is the difference between a
  depreciation wave and a demand problem, and E/C alone cannot see it.** *(Analysis.)*
- **⚠️ AND THE MEASUREMENT TRAP: headline "capex" from a press release often EXCLUDES FINANCE-LEASE
  ADDITIONS — where much AI infrastructure sits.** Use the **cash-flow-statement line + the lease
  footnote.** *(The vault caught exactly this once: MSFT $196.6B stale vs $329.1B actual — a $132B gap
  inside one number.)*
- **⚠️ WHAT THE RATIO IS AND IS NOT: capex spent in 2026 produces earnings in 2028-2030, so a
  CONTEMPORANEOUS E/C is NOT a return-on-investment measure.** It measures **how much current profit is
  being consumed by forward bets** — which is exactly the CEPI question ("is price discounting returns
  the cash flows don't support"), but it must never be described as ROI.

### 🚩 THE FETCH THAT TURNS THE SEED INTO A SERIES — per company, per quarter, from the 10-Q
  ⟲ SUPERSEDED 2026-08-07 → cepi.md:L82 — fetch RETURNED 2026-08-07: 11 company-quarters loaded; flag closed, series exists
**MSFT · GOOGL · AMZN · META · ORCL** (+ SPCX's missing lines), **2026Q1 and 2026Q2** to start:
1. **Revenue** · 2. **Capex** = *purchases of property & equipment* (cash flow statement) **PLUS
finance-lease additions** (state them separately) · 3. **Net income (GAAP)** · 4. **Operating cash
flow** · 5. **D&A** · 6. *(optional)* **remaining performance obligations / purchase commitments.**
**Six lines × 5 companies × 2 quarters = 60 numbers, and the series exists.**

**Links:** [[ai-capex-cycle]] · [[ai-financing-fragility]] · [[fragility-engine]] · [[compression-thesis]] ·
[[new-economy-regime]] (the 8/7 productivity entry — the macro-side version of the same question)

---

  ⟲ SUPERSEDED 2026-08-07 → cepi.md:L174 — aggregate crossing decomposed: 3/5 diffusion, only GOOGL on both blades, META's fall is pure capex step-up
## 2026-08-07 ~5:00pm PDT — ★★★★ THE SERIES EXISTS: 11 COMPANY-QUARTERS, AND THE COMPLEX CROSSED THE SELF-FUNDING LINE IN CALENDAR Q2
  ⟲ SUPERSEDES cepi.md:L70 — fetch RETURNED 2026-08-07: 11 company-quarters loaded; flag closed, series exists
**Closes the 🚩 fetch flag above.** Jake returned the digest (`raw/sec-line-items-2026Q1-Q2-handoff-reply-2026-08-07.docx`
+ `.txt`). Both traps the handoff was built around were handled by the source: **finance leases stated separately
from headline capex**, and **Oracle's fiscal quarters explicitly labelled as NOT aligning to calendar quarters.**
`tools/cepi_tracker_cell.py` rebuilt to v2 and run. **The digest forced a FIFTH ratio.**

### DATA (observed — from the digest; $M, per quarter; ratios computed on TRUE capex = headline + finance leases)
| tkr | qtr | C/R | E/C | OCF/C | DA/C | CQ |
|---|---|---|---|---|---|---|
| MSFT | 2026Q1 | 0.43 | 0.89 | 1.31 | 0.29 | 1.47 |
| MSFT | 2026Q2 | 0.46 | 0.86 | 1.34 | 0.27 | 1.79 |
| GOOGL | 2026Q1 | 0.33 | 1.74 | 1.28 | 0.18 | **−2.59** |
| GOOGL | 2026Q2 | 0.38 | 2.46 | 0.86 | 0.16 | **−10.29** |
| AMZN | 2026Q1 | 0.25 | 0.66 | 0.57 | 0.41 | **−0.22** |
| AMZN | 2026Q2 | 0.27 | 1.14 | 0.83 | 0.36 | **−0.86** |
| META | 2026Q1 | 0.34 | 1.41 | 1.70 | 0.32 | 0.91 |
| META | 2026Q2 | 0.50 | 0.53 | 1.06 | 0.21 | 2.52 |
| ORCL ⚠️ | 2026Q1 | 1.08 | 0.20 | 0.38 | 0.14 | 1.34 |
| ORCL ⚠️ | 2026Q2 | 0.94 | 0.24 | 0.81 | 0.16 | 3.62 |
| SPCX | 2026Q2 | 2.35 | −0.03 | 0.13 | 0.16 | 1.04 |

- **⭐ THE SELF-FUNDING LINE WAS CROSSED. Dollar-weighted OCF/C, the four calendar-aligned hyperscalers
  (MSFT+GOOGL+AMZN+META): 2026Q1 = 1.106 → 2026Q2 = 0.999.** Below 1.00 means the complex no longer funds
  its buildout out of the business; the marginal dollar comes from a bond desk or a share sale.
- **⚠️ AND 0.999 IS A CEILING, NOT A POINT ESTIMATE. META's finance-lease additions are NOT DISCLOSED**
  in either quarter, so its true capex is a FLOOR and the aggregate OCF/C is an upper bound. The real
  number is at or below 0.999.
- **THE FINANCE-LEASE CORRECTION IS NOT COSMETIC — it is the difference between two verdicts.** MSFT Q2:
  headline capex 35,802 + **5,600 of finance leases** = 41,402 true (+15.6%); OCF/C 1.55 → **1.34**.
  Q1: 30,876 + 4,700 = 35,576; 1.51 → 1.31. ORCL Q2: 16,493 + 1,527 = 18,020; 0.89 → **0.81**.
  Across the two quarters, disclosed lease additions add **$14.9B** of capex that headline numbers omit.
- **E/C AND OCF/C MOVED IN OPPOSITE DIRECTIONS Q1→Q2. Aggregate E/C ROSE 1.11 → 1.32 while OCF/C FELL
  1.106 → 0.999.** On E/C alone the complex looks like it got *more* profitable per dollar of capex.
- **DA/C aggregate = 0.31 (Q1) → 0.26 (Q2).** The 2024-26 capex wave has barely begun hitting the P&L.
- **⭐ THE CASH-QUALITY SCREEN SPLITS THE COMPLEX IN TWO, AND THE SPLIT IS NAME-SPECIFIC, NOT SECTOR-WIDE.**
  CQ = (OCF − NI) / D&A. A capital-intensive company should generate MORE cash than accounting profit, by
  roughly D&A ⇒ CQ ≥ 1.0 is normal. **Negative in BOTH quarters: GOOGL (−2.59, −10.29) and AMZN (−0.22, −0.86).
  Clean in every quarter: MSFT (1.47, 1.79), META (0.91, 2.52), ORCL (1.34, 3.62), SPCX (1.04).**
- **GOOGL 2026Q2 is the extreme: net income 112,193 against operating cash flow 39,069. OCF − NI = −73,124** —
  $73.1B of reported earnings that generated no cash. Reported revenue that quarter was 119,796, i.e. a
  **93.6% net margin.**
- **MSFT DISCLOSED A USEFUL-LIFE EXTENSION: effective 2026-07-01, datacenter/office-building lives 15 → 25
  years** (explicitly NOT servers/network equipment). It lands in **calendar Q3 2026**, not in the data above.
- **⚠️ artifact — ORCL:** fiscal ≠ calendar (FY26Q3 = Dec-Feb; FY26Q4 = Mar-May). Its capex, OCF, D&A and
  Q2 leases are all **DERIVED by period subtraction** (9M − 6M, FY − 9M), not disclosed quarterlies. Excluded
  from every calendar aggregate above and reported on its own line.
- **⚠️ artifact — D&A is not like-for-like:** GOOGL's CF line is **depreciation only** (amortization not
  disclosed ⇒ its DA/C is understated); AMZN's **includes capitalized content costs and operating-lease
  assets** (⇒ its DA/C is overstated). Do not rank DA/C across those two names.
- Coverage gaps remaining: finance leases for META (both quarters), ORCL Q1, SPCX Q2.

### THESIS (interpretation — NOT fact)
- *(analysis)* **THE FIFTH RATIO EXISTS BECAUSE THE DATA DEMANDED IT, AND IT IS THE ONE THAT PROMOTES AN
  8/6 CLAIM UP THE EVIDENCE LADDER.** The vault logged the Goldman piece on 8/6 — *"half the S&P's 'record'
  earnings growth is just Big Tech marking up its own stock portfolio"* — as **REPORTED**. CQ **MEASURES**
  it from the cash flow statements, and measurement adds something the assertion did not have: **it is two
  names, not the complex.** GOOGL and AMZN carry the negative CQ; MSFT, META, ORCL and SPCX are clean.
  A claim about "Big Tech" is, in the numbers, a claim about the two holders of the largest private-AI
  equity stakes. → [[ai-financing-fragility]], [[new-economy-regime]].
- *(analysis)* **THE MECHANISM IS INFERRED, NOT PROVEN BY THIS DATA.** CQ detects that earnings exceed cash;
  it does not name the cause. Unrealized marks on equity stakes is the standing hypothesis (and it fits: the
  gains are subtracted back out in the OCF reconciliation, which is exactly the signature). But this digest
  does not contain the equity-securities line, so **the cause remains THESIS.** The gap itself is DATA.
- *(analysis)* **THIS IS THE ENTIRE ARGUMENT FOR BUILDING FOUR RATIOS INSTEAD OF ONE, AND IT PAID OFF ON THE
  FIRST REAL RUN.** E/C rose while OCF/C fell. Jake's original ask — a running E/C — would, read alone, have
  reported the complex getting *more* profitable per dollar of capex in the exact quarter it stopped funding
  itself. **E/C is currently flattered at BOTH ends: non-cash gains inflate the numerator (CQ), and the
  depreciation wave has not yet arrived to deflate it (DA/C 0.26).**
- *(analysis)* **THE DATING: the crossing is MEASURED one quarter EARLIER than the GS chart PROJECTED.**
  The 8/6 GS/FactSet chart put combined FCF going negative at **2026Q3E**. Filed data puts the four
  calendar-aligned names at OCF/C 0.999 in **2026Q2** — with META's leases undisclosed, i.e. biased high.
  *(⚠️ Not a like-for-like refutation: GS's basket includes ORCL and uses its own FCF definition. The
  honest statement is that the measured Q2 number sits at the line GS expected to be crossed in Q3.)*
- *(analysis)* **MSFT'S 15→25-YEAR EXTENSION IS THE CHEAPEST EARNINGS LEVER IN THE COMPLEX AND IT IS NOW
  DATED.** Extending building lives lowers depreciation, which raises reported earnings, **with no change
  in cash whatsoever.** The instrument predicts the exact signature: **E/C up, OCF/C flat or down, DA/C
  down.** It is confined to buildings — servers and network gear, the short-lived assets that actually
  matter for the AI wave, were explicitly excluded, which limits the size of the effect.

### 📌 REGISTERED, DATED, FALSIFIABLE — the three tests this entry arms
1. **MSFT calendar-Q3 2026 earnings (late Oct):** does E/C rise while OCF/C does NOT? **Confirms the
   depreciation-lever read.** If OCF/C rises *with* E/C, the improvement is real and the read is wrong.
2. **META's finance leases** — the one disclosure that could push aggregate OCF/C decisively below 1.00.
   ⬜ NOT KNOWN. Until it lands, 0.999 is an upper bound and must be quoted as one.
3. **GOOGL 2026Q2 net income 112,193 → verify against the primary 10-Q.** A 93.6% net margin is the single
   most likely place for a digest error, and the vault has not read the filing. **⚠️ THE ARTIFACT TEST
   APPLIES: the artifact read was a digest, not the 10-Q.** *(The PATTERN survives a bad GOOGL Q2 number —
   GOOGL Q1 is independently negative at −2.59 and AMZN is negative in both quarters. The MAGNITUDE does not.)*

**Instrument:** `tools/cepi_tracker_cell.py` v2 — 5 ratios, headline-vs-true capex, calendar-alignment
gating, self-reporting coverage gaps. Adding a filing is one `dict(...)` line.
  ⟲ SUPERSEDES cepi.md:L82 — aggregate crossing decomposed: 3/5 diffusion, only GOOGL on both blades, META's fall is pure capex step-up

### Addendum 2026-08-07 ~4:55pm PDT — ⟲ THE "COMPLEX CROSSED THE LINE" HEADLINE IS TRUE OF THE AGGREGATE AND FLATTENS THE PICTURE. Three additions the aggregate hid.
The 5:00pm entry above led with **OCF/C 1.106 → 0.999** and read it as the complex crossing. That number is
right, but an aggregate is one number and it cannot say whether the move is **broad or concentrated**, or
whether it came from **falling cash or rising spending**. Instrument extended (diffusion + QoQ attribution
blocks); all three findings below are printed by the cell, not asserted.

### DATA (observed)
- **DIFFUSION — the crossing is SEQUENTIAL BY NAME, not a simultaneous event.** Individually below 1.00:
  **2026Q1 = 2 of 5** (ORCL 0.38, AMZN 0.57) → **2026Q2 = 3 of 5** (ORCL 0.81, AMZN 0.83, GOOGL 0.86).
  Above in Q2: **MSFT 1.34, META 1.06** *(META's leases undisclosed ⇒ its 1.06 is a ceiling)*.
- **ATTRIBUTION Q1→Q2 — only ONE name deteriorated on both blades.**

  | tkr | OCF/C Q1 | OCF/C Q2 | Δ | OCF Δ% | capex Δ% | driver |
  |---|---|---|---|---|---|---|
  | GOOGL | 1.28 | 0.86 | **−0.42** | **−14.7%** | **+27.1%** | ★ **BOTH blades** |
  | META | 1.70 | 1.06 | **−0.64** | −1.1% | **+58.5%** | capex step-up |
  | MSFT | 1.31 | 1.34 | +0.03 | +18.8% | +16.4% | OCF recovery |
  | AMZN | 0.57 | 0.83 | **+0.26** | **+74.4%** | +19.7% | OCF recovery |
  | ORCL ⚠️ | 0.38 | 0.81 | **+0.43** | +104.4% | −3.3% | OCF recovery |
- **THE LARGEST SINGLE MOVE WAS META's −0.64, AND ITS OPERATING CASH FLOW BARELY CHANGED** (32,226 → 31,862,
  −1.1%). Its capex went **18,997 → 30,116, +58.5%.** The entire fall is the denominator.
- **CASH QUALITY WENT NEGATIVE A QUARTER BEFORE THE FUNDING LINE BROKE.** Aggregate CQ **−0.02 in 2026Q1**,
  when aggregate OCF/C was a comfortable **1.106**. Q2: CQ **−1.23**, OCF/C 0.999.
- Two of the five (AMZN, ORCL) **improved** Q1→Q2; a third (MSFT) improved slightly.

### THESIS (interpretation — NOT fact)
- *(analysis)* **⟲ THE CORRECTION TO MY OWN HEADLINE: "the complex is not self-funding" invites a
  cash-collapse reading, and the decomposition does not support that reading yet.** Four of five names show
  flat-to-strongly-rising operating cash flow. **The aggregate crossed mostly because spending accelerated,
  not because cash generation failed.** The direction is real and the threshold is real; the MECHANISM is
  mostly deliberate.
- *(analysis)* **AND THAT DISTINCTION DECIDES HOW IT RESOLVES, WHICH IS THE WHOLE POINT OF SEPARATING THE
  BLADES.** A capex step-up is a **decision** — reversible in one quarter by guidance, which is precisely
  what [[ai-capex-cycle]]'s capex-cut trigger is watching for. An OCF decline is **not** reversible by
  decision. **META at 1.06 is a company choosing to outspend its cash flow. GOOGL at 0.86 is a company whose
  cash flow fell 14.7% while it spent 27.1% more.** Those are different objects and the aggregate merges them.
- *(analysis)* **GOOGL IS THE ONLY NAME THAT LOOKS LIKE THE BEAR CASE, AND IT IS ALSO THE NAME WITH THE
  WORST CASH QUALITY (CQ −10.29).** Both blades moving *and* $73.1B of earnings that generated no cash is a
  single coherent picture in one name — not a sector state. → [[ai-financing-fragility]].
- *(analysis)* **CQ MAY BE THE LEADING INDICATOR AND OCF/C THE CONFIRMING ONE.** Cash quality was already
  negative in Q1 while the funding ratio still read comfortably above 1.00. **One observation of a lead is
  not a lead** — this is a hypothesis with n=1, registered so the next two quarters can kill it.
- *(⚠️ the honest limit on the diffusion count)* **n=5, and one of them (ORCL) is fiscal-misaligned with
  fully derived numbers.** "3 of 5" is a count, not a rate; do not annualise it or read a trend into two
  quarters of a five-name basket.

### 📌 REGISTERED — two more tests, both falsifiable
4. **Does CQ lead OCF/C again?** If 2026Q3 shows a name's CQ turning negative while its OCF/C is still >1.00,
   the lead survives. If CQ and OCF/C break together, **the lead was an artifact of Q2's mark-ups** and this
   hypothesis dies. ⬜ NOT KNOWN.
5. **Does META's capex step-up reverse on guidance?** +58.5% QoQ with flat OCF is the most reversible
   configuration in the table. A guided-down Q3/Q4 capex number puts META back above 1.00 without any change
   in cash — and would be the first hard datapoint for [[ai-capex-cycle]]'s capex-cut trigger. ⬜ NOT KNOWN.
