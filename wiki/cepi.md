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

### Addendum 2026-08-07 ~4:58pm PDT — ★★★★ "DO EARNINGS EXCEED CAPEX?" HAS TWO ANSWERS, THEY DISAGREE, AND THE ONE THAT SAYS YES IS ONE COMPANY (Jake's Q)
Jake asked the question the whole instrument was built for, plainly: *"So are the earnings exceeding the
capex or not."* Both answers are computed by the cell (new **reported-vs-cash + concentration** block).

### DATA (observed — calendar-aligned hyperscalers MSFT+GOOGL+AMZN+META, $M, on TRUE capex)
| basket | reported E/C | cash E/C | OCF/C | non-cash gap | as % of NI |
|---|---|---|---|---|---|
| **2026Q1 all** | 1.11 | 0.80 | 1.11 | 42,250 | 28% |
| **2026Q1 ex-GOOGL** | **0.89** | 0.70 | 1.05 | 18,980 | 21% |
| **2026Q2 all** | **1.32** | **0.74** | 1.00 | **99,165** | **44%** |
| **2026Q2 ex-GOOGL** | **0.90** | 0.75 | 1.05 | 18,937 | 17% |

- **REPORTED: YES.** 2026Q2 net income **226,454** vs true capex **171,904** ⇒ **E/C 1.32** (Q1: 1.11).
- **CASH: NO.** Cash earnings (OCF − D&A) **127,289** vs the same capex ⇒ **cash E/C 0.74** (Q1: 0.80).
  **The two answers move in OPPOSITE directions Q1→Q2** — reported up 1.11→1.32, cash down 0.80→0.74.
- **THE WEDGE: 99,165 — 44% of reported net income did not become cash**, up from 42,250 (28%) in Q1.
  *(Wedge = (NI + D&A) − OCF: what operating cash flow WOULD have been if nothing in earnings were non-cash.)*
- **★ THE CONCENTRATION TEST — REMOVE ONE NAME AND THE "YES" DISAPPEARS. Ex-GOOGL reported E/C is 0.90 in
  Q2 and 0.89 in Q1** — below 1.00 in both quarters, and **flat**. The rise from 1.11 to 1.32 is Alphabet.
- **THE SAME NAME MOVES THE FUNDING RATIO. Ex-GOOGL OCF/C = 1.05 in BOTH quarters** — steady and above the
  line. The aggregate's 1.106 → 0.999 crossing is Alphabet too.
- **THE CASH ANSWER IS UNIFORM, THE REPORTED ANSWER IS NOT.** Cash E/C: **0.74 with GOOGL, 0.75 without.**
  Removing the outlier barely moves it. Reported E/C: **1.32 with, 0.90 without.**
- ⚠️ **`cash earnings = OCF − D&A` is a PROXY, and it is a GENEROUS one.** D&A lags the asset base during a
  buildout (**DA/C is only 0.26**), so the eventual depreciation charge is larger than what currently runs
  through the P&L. The true cash coverage is at or below 0.74.

### THESIS (interpretation — NOT fact)
- *(analysis)* **THE ANSWER TO JAKE'S QUESTION IS: ON CASH, NO — AND THAT ANSWER IS THE GROUP'S. ON REPORTED
  EARNINGS, YES — AND THAT ANSWER IS ALPHABET'S.** Two rows of the same table, and which one gets quoted
  decides whether the complex looks like it is comfortably out-earning its buildout or quietly under-funding it.
- *(analysis)* **THE CONCENTRATION TEST IS THE GENERALISABLE FINDING, NOT THE ALPHABET FACT.** An aggregate
  that crosses a threshold because of ONE constituent is a statement about that constituent. This is the same
  defect as the ⟲ 4:55pm addendum (aggregate hid diffusion) showing up a second time in one hour, on a
  different ratio. **Both are now blocks in the cell rather than things I have to remember to check** —
  consistent with STEP ZERO's founding logic: *a rule that only fires when remembered is an intention.*
- *(analysis)* **WHY THE CASH ANSWER IS THE ONE THAT BINDS.** Reported earnings can be raised by a mark-up
  (CQ) or by a depreciation-schedule change (MSFT's 15→25y, landing calendar Q3) without a dollar of cash
  moving. Capex must be paid in cash. **A coverage question settled in reported earnings can be answered
  "yes" by an accounting entry; settled in cash it cannot.** → [[ai-financing-fragility]].
- *(⚠️ standing caveat, restated because the question invites forgetting it)* **contemporaneous E/C is NOT a
  return measure** — 2026 capex earns in 2028-30. Both numbers answer *"how much current profit is consumed
  by forward bets,"* which is the CEPI question. Neither answers *"is this capex paying off."*
- *(⚠️ and the GOOGL magnitude is still unverified)* Test #3 above is unclosed: **GOOGL Q2 NI 112,193 has not
  been checked against the primary 10-Q.** Every "ex-GOOGL" row here is robust to that — it removes the name.
  Every "all" row is not. **If the digest is wrong on GOOGL, the 1.32 and the 44% both fall; 0.90 and 0.75 stand.**

### Addendum 2026-08-07 ~5:02pm PDT — IS THE GAP CLOSING OR WIDENING? WIDENING ON THE AGGREGATE, NARROWING EVERYWHERE EXCEPT ALPHABET — AND THE ANSWER INVERTS ON ONE UNVERIFIED NUMBER (Jake's Q)
### DATA (observed — reported E/C minus cash E/C, calendar-aligned hyperscalers, on TRUE capex)
| basket | gap Q1 | gap Q2 | Δ | direction |
|---|---|---|---|---|
| **all four** | 0.31 | **0.58** | +0.27 | **WIDENING (+86%)** |
| **ex-GOOGL** | 0.19 | **0.15** | −0.04 | **NARROWING (−21%)** |

- **Non-cash wedge, all four: 42,250 → 99,165** (+56,915); **28% → 44% of net income** (+16pp).
- **Non-cash wedge, ex-GOOGL: 18,980 → 18,937** — **FLAT in dollars** (−43) while net income grew,
  so it **FELL as a share: 21% → 17%** (−5pp).
- **PER NAME the split is two and two.** Widening: **GOOGL 0.65 → 1.76** (+1.11), **AMZN 0.51 → 0.68**
  (+0.17). Narrowing: **MSFT −0.13 → −0.21**, **META 0.03 → −0.32** (−0.35). *(A NEGATIVE gap means cash
  earnings EXCEED reported earnings — the normal state for a capital-intensive filer.)*
- **⭐ SENSITIVITY — the whole answer turns on GOOGL Q2 net income.** Re-run with that one figure replaced
  by a sector-normal ~30% margin (35,939 vs the digested 112,193):
  **reported E/C 1.32 → 0.87 · gap 0.58 → 0.13 · wedge 44% → 15% of net income.**
  **The verdict flips from "widening sharply" to "small and stable."**
- **THE ONE THING THAT WIDENS IN EVERY CUT: DA/C. All four 0.31 → 0.26; ex-GOOGL 0.35 → 0.30.** Depreciation
  is falling further behind capex in both baskets, independent of Alphabet.
- ⚠️ **n = 2 quarters.** Two points give a DIRECTION, not a trend; a step-change and a slope are
  indistinguishable here.

### THESIS (interpretation — NOT fact)
- *(analysis)* **THE HONEST ANSWER IS "WIDENING, UNCONFIRMED," AND THE UNCONFIRMED HALF IS LOAD-BEARING.**
  Test #3 (GOOGL Q2 NI vs the primary 10-Q) was registered an hour ago as a data-hygiene item. It is now
  the **pivot of an analytical conclusion**: the same unread filing decides whether the complex's earnings
  quality is deteriorating fast or barely moving. **A registered test that starts as hygiene and becomes
  load-bearing should be re-priced as urgent — this one has been.**
- *(analysis)* **THE DA/C WIDENING IS THE ROBUST FINDING AND IT POINTS THE OTHER WAY IN TIME.** The
  reported-vs-cash gap is about earnings quality *now*; DA/C is about the earnings drag *ahead*. It fell in
  both baskets, so **the 2024-26 capex wave is still outrunning its own depreciation schedule** — the P&L
  hit is being deferred, not absorbed. **That is the one direction this data establishes without depending
  on Alphabet.** → [[ai-capex-cycle]].
- *(analysis)* **AND IT COMPOUNDS WITH MSFT'S 15→25y EXTENSION.** DA/C falling is the *mechanical* deferral
  (assets not yet depreciating); the life extension is a *discretionary* deferral landing calendar Q3. Both
  push the same charge further out. **Two deferrals stacking is a different object from one, and neither
  changes a dollar of cash.**
- *(⚠️ against my own read)* **THE EX-GOOGL NARROWING IS A REAL RESULT AND DESERVES EQUAL BILLING.** Three of
  four names are flat-to-improving on earnings quality, and two have cash earnings *exceeding* reported. **A
  bear framing that quotes 44% while the ex-outlier number is 17% and falling would be the "N outlets, one
  origin" error in ratio form** — one name restated four ways. → [[_calibration]].

### 📌 TEST #3 RE-PRICED — from hygiene to load-bearing
  ⟲ SUPERSEDED 2026-08-08 → cepi.md:L329 — test #3 RESOLVED 8/8: GOOGL Q2 NI was not a digest error — $98B unrealized equity gain, pre-tax; CQ fully reconciles
**GOOGL 2026Q2 net income 112,193, against the primary 10-Q.** ⬜ NOT KNOWN. It now decides: (a) whether the
reported-vs-cash gap is widening or stable, (b) whether the 44%-of-net-income wedge is real, (c) whether
aggregate reported E/C is above or below 1.00 (1.32 vs 0.87). **Every ex-GOOGL row in this vault is robust to
it; no "all four" row is.**

---

## 2026-08-08 ~7:05am PDT — ★★★★ TEST #3 RESOLVES, AND THE MECHANISM IS NAMED: ALPHABET $98B UNREALIZED, AMAZON $53B ON ANTHROPIC
  ⟲ SUPERSEDES cepi.md:L321 — test #3 RESOLVED 8/8: GOOGL Q2 NI was not a digest error — $98B unrealized equity gain, pre-tax; CQ fully reconciles
Jake pasted an S&P-500 earnings-season summary (`raw/sp500-earnings-beat-margin-paste-2026-08-08.txt`)
that **names the two gains the CQ screen inferred from the cash flow statements the day before.**
⚠️ **ARTIFACT TEST: the artifact read is a PASTE with no named provider** — not FactSet, not a 10-Q.
The gain FIGURES are third-hand. What is first-hand is the reconciliation below, run against filed cash flows.

### DATA (observed)
- **The paste's claims, verbatim:** S&P 500 beating EPS estimates by **+29.2% aggregate** ("biggest ever");
  **5-year average +7.0%** ⇒ ~4.2x; **blended net margin 16.9%**, all-time high; and — *"even if you removed
  **Alphabet's $98 billion gain from unrealized equity investments** and **Amazon's $53 billion gain from
  Anthropic**, S&P 500 earnings growth would STILL be **+32.0% year-over-year**."*
- **⭐ THE GAINS RECONCILE THE CQ FLAG, AND THE TAX TREATMENT IS DETERMINABLE FROM THE MARGINS.** Treating
  the stated gains as **PRE-TAX** (×0.79 at a 21% rate) returns sector-normal margins for both names;
  treating them as after-tax does not:

  | | ex-gain NI | net margin | CQ | vs vault comparator |
  |---|---|---|---|---|
  | GOOGL, gain PRE-tax | 34,773 | **29.0%** | 0.60 | ~30% normal ✓ |
  | GOOGL, gain after-tax | 14,193 | 11.8% | 3.50 | implausible ✗ |
  | AMZN, gain PRE-tax | 20,777 | **10.4%** | 1.23 | ~8-11% normal ✓ |
  | AMZN, gain after-tax | 9,647 | 4.8% | 1.79 | implausible ✗ |
- **⭐ AGGREGATE, CALENDAR-ALIGNED FOUR, 2026Q2 — the whole finding in three lines:**
  - **reported E/C 1.32 → ex-gains E/C 0.62**
  - **OCF/C UNCHANGED at 0.999** — the cash never moved, which is the entire point
  - **aggregate CQ −1.23 → +1.45** (normal). **Strip these two gains and cash quality fully normalises**,
    i.e. CQ was detecting these two items and essentially nothing else.
- **THE 8/7 ROBUSTNESS TEST LANDED WITHIN 3.4%.** It assumed a sector-normal 30% GOOGL margin ⇒ NI 35,939.
  The disclosed pre-tax gain implies **34,773**. *(The stress-test methodology is validated, not just the
  conclusion.)*
- **⛔ TEST #3 IS RESOLVED, AND NOT THE WAY I WEIGHTED IT.** I flagged GOOGL Q2 NI 112,193 (93.7% net margin)
  as *"the single most likely place for a digest error."* **It was not an error. The digest was right and the
  number is real** — a 93.7% net margin is what a $98B unrealized mark does to a $119.8B revenue quarter.

### THESIS (interpretation — NOT fact)
- *(analysis)* **THE 8/6 GOLDMAN CLAIM IS NOW MEASURED, NAMED AND SIZED — a full climb of the evidence
  ladder in 48 hours.** 8/6: REPORTED ("half the S&P's record earnings growth is Big Tech marking up its own
  stock portfolio"). 8/7: MEASURED but unattributed (CQ negative for exactly two names, mechanism labelled
  THESIS). 8/8: **the two names are confirmed and the two amounts are stated.** The ratio found the right
  companies before the vault had any disclosure naming them.
- *(analysis)* **⚠️ THE PASTE CORRECTS ONE OF ITS THREE SUPERLATIVES, AND IT IS NOT THE MOST CONTAMINATED
  ONE.** The ex-gains adjustment is applied to the **growth** figure (+32.0%). It is NOT applied to the
  **+29.2% "biggest beat ever"** or the **16.9% "all-time-high net margin"** — and those two are the ones
  most mechanically distorted by an unrealized mark:
  - **The BEAT.** A beat is actual-vs-ESTIMATE. Analysts do not forecast unrealized marks on private
    stakes — they are unforecastable by construction. **A beat driven by them is not an earnings surprise
    in the informative sense; it is a category of income sitting outside the estimate.** "Biggest beat ever"
    is partly measuring the biggest thing analysts don't model.
  - **The MARGIN, which is worse.** A mark-up adds to net income with **ZERO revenue** — numerator up,
    denominator untouched. It inflates a net-margin ratio *mechanically*. **A record net margin computed
    with unrealized equity gains in the numerator is not a record in operating profitability.**
- *(concession — this is the strong part of the paste)* **THE +32.0% EX-GAINS FIGURE IS THE HONEST MOVE AND
  IT SURVIVES.** Whoever wrote it ran the adjustment unprompted and in the conservative direction (stripping
  current-period gains lowers the growth rate). **Earnings growth ex-gains being genuinely strong does not
  conflict with anything in this vault** — our finding is about CASH against CAPEX, not about earnings
  growth. Both can be true, and per the arithmetic above **OCF/C is unchanged at 0.999 by construction.**
- *(analysis — the join the paste does not make)* **THE MARKS ARE ON THE AI COMPANIES THESE FIRMS ARE ALSO
  FUNDING AND SELLING COMPUTE TO.** Amazon's gain is explicitly **on Anthropic**. Alphabet's is
  "unrealized equity investments," composition ⬜ NOT STATED. **A material slice of record Big Tech earnings
  is the mark-to-market of private stakes whose valuations are set by funding rounds the same firms
  participate in** — which is the vendor-financing/circular-revenue thread in [[ai-capex-cycle]] arriving in
  the earnings line rather than the revenue line. *(⚠️ Composition unknown; this is a structural read, not a
  claim about any specific round.)*
- *(⚠️ what I am NOT claiming)* Not that the beat is fake, not that the boom is fake, not that the +32%
  is wrong. **The claim is narrower: two of the three superlatives are computed on a base that includes
  unrealized marks, and only the third was corrected for them.**

### 📌 REGISTERED — replaces test #3, which is now closed
6. **The primary 10-Q line item.** ⬜ NOT KNOWN: is Alphabet's $98B stated **pre-tax**, and what is its
   COMPOSITION by holding? The margin reconciliation above says pre-tax; the filing would settle it and
   name the stakes. **Every ex-gains number in this entry moves if the tax treatment is other than assumed.**
7. **Q3 reversal risk.** Unrealized marks run **both ways**. If private-AI marks flatten or reverse in
   calendar Q3, the same mechanism that produced a record beat produces a miss **with no operational
   change whatsoever** — and the DA/C deferral and MSFT's 15→25y life extension land in the same quarter.
   ⬜ NOT KNOWN. **This is the single most asymmetric registered item in the CEPI thread.**

### 2026-08-11 ~7:50am PDT — DA/C GETS TESTIMONY FROM THE DEMAND SIDE: a large enterprise buyer models a FIVE-YEAR SCRAP CYCLE, on the record, eight months before the $2T program that needs "long life"
- DATA: **IBM CEO Arvind Krishna** (The Verge *Decoder*, ~1-2 Dec 2025, convergent-secondary — primary
  paywalled): on AI hardware, **"you've got to use it all in FIVE YEARS, because at that point you've got
  to THROW IT AWAY and refill it."** Restated with returns math (NBIM/Tangen, ~6 May 2026): a **seven-year
  payback** on $6-8T needs **"an extra 1 to 2 trillion a year of revenue… even if it is high margin, would
  be 20 to 30%. So that much incremental revenue, I don't believe is there."**
- **WHY IT LANDS HERE AND NOT ONLY IN THE FINANCING NOTE:** L56 of this note is the standing conclusion
  that **DA/C is mandatory because earnings are AFTER depreciation** — the ratio exists precisely to catch
  a complex whose reported earnings depend on the useful life it assigns itself. **L309: the 2024-26 capex
  wave is still outrunning its own depreciation schedule.** Krishna supplies the counterparty's own
  assumed life (5yr) against the accounting lives the buyers book — **a buyer's scrap estimate is evidence
  about the DENOMINATOR the sellers control.**
- ⚠️ NOT a measurement. It is one executive's stated assumption, from a company with a disclosed conflict
  (Q2 2026 Z-mainframe revenue −42% YoY as client capex diverted to GPU-adjacent kit). **Filed as
  TESTIMONY on the depreciation question, weighted accordingly.** Full ledger, the conflict, and the
  colliding $/GW figures: [[ai-financing-fragility]] L4271. [[ai-capex-cycle]]
