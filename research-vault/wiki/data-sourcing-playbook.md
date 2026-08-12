# Data-Sourcing Playbook — offload heavy fetching, keep the chat lean

The standard drill for pulling data without burning tokens in-session. Related: [[CLAUDE|../CLAUDE.md]].

> Not market research — this is workflow. No firewall needed.

## Why (the mechanic)
Tokens get burned mostly by things that **land in context and get re-read every turn after**.
So the rule: if the *retrieval* is big but the *answer* is small, do the retrieval **elsewhere**
and bring back only the small answer. The vault is the pressure valve — anything pasted gets
ingested, then it's on disk instead of on the context clock.

## Token cost, most → least expensive (in-session)
1. 🔴 Reading PDFs in-session (esp. scanned/image) → **offload**, paste text
2. 🔴 Fetching long web pages (full article/report) → **offload** if heavy; keep one short page
3. 🔴 Bulk data dumps to chat (500-ticker tables, long CSV/JSON) → **offload** (Colab/ChatGPT), paste summary
4. 🟠 Multiple WebSearches in one turn → offload multi-angle research; keep single lookups
5. 🟠 Long pasted source text (essays/memos) → paste ONCE → ingest → it's on disk
6. 🟡 Me writing long code/notes → write to files instead of printing when big
7. 🟡 Long multi-step tool loops → fine; batch where possible
8. 🟢 Normal Q&A / reasoning → keep here
9. 🟢 Small edits / status checks → cheapest

## Which external tool for which job
- **Perplexity** → sourced web data with citations. Default for "latest X + numbers + links."
- **Grok** → X/Twitter (only one with native access). "@handle last N posts verbatim."
- **Gemini** → big documents / long PDFs (huge context window).
- **ChatGPT** (code interpreter / agent) → actual data pulls (runs Python/yfinance → table).

## The ingest-ready prompt (paste to the external tool, fill the bracket)
> **Retrieval task.** Fetch: **[what you want]**.
> Return ONLY a compact digest, no intro/prose/disclaimers:
> - One bullet per fact: `<number or fact> — <source>, <date>`
> - Max ~12 bullets, most important first.
> - Flag anything estimated vs reported.
> - End with `Sources:` and the URLs.

Tool tweaks:
- **Grok:** "Give me @zerohedge's last 15 posts verbatim with URLs, newest first."
- **Perplexity:** add "with inline citations."
- **Gemini:** paste the PDF/report + "Digest into the format above; ignore boilerplate."
- **ChatGPT:** "Use code interpreter to pull [tickers] daily closes for [dates] → compact table + net % per name."

## The loop
1. Heavy pull needed → paste the ingest-ready prompt to the right tool.
2. Paste the compact digest back here → say **"ingest"**.
3. It's small + sourced → files into the vault for ~nothing.

## In-house fallback (what I CAN do from here)
- WebSearch / WebFetch (server-side) → single public pages, quotes, news. ✅
- Bulk ticker/quant pulls, PDFs, walled sites (X, Cloudflare) → ❌ in-container; offload.

## Weekly structural pull (added 2026-07-11 — `tools/structural_pulls.py`)
Jake's directive: "reports, filings etc probably matter more in the long run than news and shock
events." The standing weekly manual Colab run (NO cron per spending rule):
- **Cell A — CFTC COT** (weekly, free): leveraged-fund net positioning ES/NQ/CL/GC = the free proxy for
  prime-book flow. Limitation: futures/macro level, not single-stock sectors — GS Prime sector data
  remains leak-only.
- **Cell B — Form 4 tripwire** over all vault watchlists (semi grid, quiet-health, mold-12, bottleneck),
  14d lookback. 3+ filings on a name → run the detailed buy/sell parser on it.
- **Cell C — short interest** snapshot (bi-monthly data; MoM change direction).
- **Cell D — 13F freshness** for Scion/Berkshire/Appaloosa (quarterly, 45d lag; link to filing when new).
Cadence philosophy: the structural layer confirms/kills theses; news only tests them. Feeds still
supply shocks — they land ON a maintained positioning picture now.

## Monday flows routine (added 2026-07-11 — `tools/monday_flows.py`)
Pre-open Monday: monday_flows (sector 1w return x abnormal $vol + S&P top movers in/out) → COT cell
(Friday release) → Form 4 tripwire. "Where money went" = tape + positioning + operators; no single API
sells the combination. **Paid-key verdict (2026-07-11): buy nothing yet.** Free stack covers all layers
except intraday options ORDER FLOW (Unusual Whales ~$50/mo = the only genuinely additive purchase;
FMP ~$25/mo only if scraping reliability becomes the pain). Rule: buy the pain actually felt after
3-4 weeks of the routine, not the data that sounds powerful. Any purchase = Jake's explicit call.

## Lag-vs-lead doctrine (2026-07-11, Jake's Q: "does this lag or indicate where money could go?")
Per layer: **tape** = coincident; forward value = persistence (volume-backed moves continue;
volume-less drift is hollow both ways). **COT** = leading only at EXTREMES and inverted (crowding =
stored reversal energy, not direction). **Insiders** = genuinely leading, months-to-quarters horizon
(runner-study confirmed). **Short interest** = fuel, not signal. **13F** = lagging, slow theses only.
**Mechanical flows** = the truly predictive class: rule-forced money (fallen-angel exits, index
rebalances, 10b5-1 calendars, buyback blackouts, LTA prepayment schedules) — public rules, readable in
advance. **The distribution chain is the master structure:** insiders → HFs → retail; each layer's
record is the leading indicator for the next layer's behavior. Edge = read the earliest layer while
later layers are in transit. Calibration: all tilts, not prophecies — insider clusters matter most
inside panic windows; the stack locates commitment/crowding/forced flow, thesis work does the rest.

## Form 4 reading hierarchy (2026-07-11 — the key for insider_pull output)
1. **P discretionary buy** — highest signal/$ (buys are never scheduled; one reason to buy). Weight vs
   the person's income; uniform small synchronized buys = theater (EPAM $7.5K x6).
2. **P cluster (3+ distinct buyers)** — the MTDR/GPK signature; tool auto-flags.
3. **S without 10b5-1** — real negative; strongest = first sale after long hold or large % of stake
   (AXTI Young ~$22M discretionary).
4. **S with 10b5-1** — weak per-transaction, BUT: adoption date = the real decision date (cluster of
   NEW adoptions = queued exits, leading signal); plan modifications/accelerations = discretionary acts;
   aggregate size still counts (GPK complaint weaponized $8.8M of "routine" sales).
5. **M+S exercise-and-sell** — comp monetization (expiries force it); signal only if retained fraction
   is persistently zero.
6. **A/F/G (grants/withholding/gifts)** — noise; explains grant-cycle tripwires (CME's 18 likely this).
Extension if ever needed: **Form 144** (notice of INTENT to sell) = the only forward-looking insider
filing; small add to the tool.

## Options asymmetry doctrine (2026-07-12, Jake's insight confirmed: "it's not equal opposites")
The opposite of a losing long call = a SHORT call, not a long put. Buyer-vs-buyer of the same question
both lose whenever the move stays inside the priced range (live example: 7/13 SPY straddle ±0.43% —
a +0.2% open loses for BOTH buyers). You are paid for the move EXCEEDING the priced expectation, never
for direction alone. Three ways to lose (direction / magnitude / time) vs one to win; the rake = theta
+ spread + IV crush. BNO calls tuition: the matching puts would likely have died in the same chop.
Justified option BUYING = a specific evidenced view that realized will exceed implied (the Dec-745
puts: long correlation at a record discount). The house seat = selling premium (wrong fit for a
fat-tail regime) or owning the toll booth (CME/CBOE — the rake's landlord, no tail).

## Premium-selling doctrine (2026-07-12, Jake's Q: "how do I find the absurdly expensive ones to sell?")
Finder: IV/RV ratio (IV30 vs 20d realized) > ~1.5 + high IV percentile = statistically rich. Recurring
sources: pre-earnings inflation, post-panic hangover (fear-episode END = an IV-sell signal), paranoid
put skew on crowd-hated names. Screen cell in chat 2026-07-12.
The three rules: (1) high premium = CONCENTRATED risk, not low risk — seller's distribution is many
small wins + one catastrophe; the screen can't separate overpriced fear from correctly-priced fear,
only thesis work can. (2) REGIME CHECK: selling vol now = shorting the book's own thesis (tails
underpriced, correlation at record discount); "single names rich while index calm" = the crowded
dispersion trade that detonates on correlation snap. (3) If selling at all: cash-secured puts ONLY at
ladder prices on intact businesses (paid to place the limit order; assignment = a buy the work already
chose). Never naked calls. Covered calls need 100-share lots (unavailable at current sizing).
Inverse use: IV/RV < 1.0 on wanted exposure = the BUYER'S edge — how the next Dec-745-style entry
gets identified.

## Sell-the-fear confluence (2026-07-12 — Jake's synthesis: rich IV puts x insider cluster buying)
Resolves the premium-selling doctrine's rule-1 gap: insider discretionary buying = the non-technical
discriminator between overpriced fear and correctly-priced fear. Structure: CASH-SECURED PUTS on names
where IV/RV >= ~1.3 AND >=2 distinct discretionary buyers (>$100K) — selling insurance to the crowd at
prices the operators just paid with personal money. Screen cell in chat 2026-07-12.
Rules: (1) strike <= insiders' own price; (2) only on intact-business-verified names (confluence
supplements the E-path work, never replaces it); (3) size for assignment-and-hold — insiders lead by
MONTHS, puts expire (CEO right at $10.95, stock prints $7 first = the risk); (4) earnings inside the
window = a different bet, decide explicitly; (5) thin chains: limit orders, verify quotes off-yfinance;
(6) exit falsifier = insiders flip to selling. Expect the table EMPTY most weeks — the overlap is rare
because it IS the mispricing. Live specimen at inception: GPK (post-kitchen-sink IV hangover + class-
action headline vs CEO+3 directors $1.05M, shorts −32%, price based at insider level).

### First confluence run (2026-07-12, Jake's Colab, 22 names) — ONE hit: GPK
- **GPK: IV/RV 1.37 (59 vs 43), put OI 819 (tradeable), SI 11%, $354K buys / ZERO sells.** (90d window
  undercounts the full cluster — March CEO $501K + Venturelli $199K aged out; full record = 4 buyers,
  $1.05M.) ⚠️ GPK earnings ~late Jul/early Aug sits INSIDE a 30-45 DTE window → rule 4 live.
- **The discriminator visibly worked:** CLF (1.36, equally rich) excluded on −$2.9M insider SELLING =
  correctly-priced fear; UPWK (1.32) same; EPAM's $7.5K-x6 theater excluded by the $100K floor;
  ADMA (1.65) near-miss on breadth (1 repeat buyer, not a cluster).
- ⚠️ Artifacts: FRPT/AMPH/INSP IV ~2-3% = dead yfinance quotes (OI 0 rows), not cheap options.
  HIG 2.68 and UHS 1.41 on OI 6-9 = stale-quote suspects, verify off-platform. VICR "-$220.7M sells"
  needs verification (founder distribution vs parse error). MU −$78.6M/90d sells = cumulative officer
  selling beyond the CEO's $32.8M print, consistent with the grid.
- **Check-item, not artifact: WEN — 44.2% short interest, 110% realized vol, IV/RV 0.68.** Something is
  in play at Wendy's (squeeze/activist/event?) and options are priced CHEAP vs realized — the opposite
  setup (buyer's market on a name in motion). Investigate before touching from either side.

### Short-dated selling addendum (2026-07-12, Jake's Q: 1-2 week puts?)
Premium scales ~sqrt(time): 1wk collects ~40% of a 6wk premium for 100% of that week's gap risk —
the short end harvests GAMMA, the dealer's home game (continuous hedging vs checking a phone).
Documented edge lives at 30-45 DTE closed ~50% of max profit. Practical killers: confluence-cohort
names have monthlies only + thin chains; weekly round-trip spreads eat half the edge; THIS regime
schedules binaries into weekends (BNO lesson, sign-flipped — short side now owns the gap).
ONE aligned use: duration as EVENT DODGE — expire BEFORE the known binary (GPK: July monthly ~7/17
expires ahead of early-Aug earnings = hangover IV harvested, coin never held). Rule: never sell short
because annualized yield looks big — that number is the gamma you haven't met yet.

### GPK chain verdict (2026-07-12, spot $10.28)
- July 17: DEAD (no live bids) → **the event-dodge version does not exist on GPK; only the
  deliberate-binary version exists** (every live expiry spans early-Aug earnings).
- Aug 21 $10P: bid 0.30/ask 0.90 — 100% spread, OI 50 → UNTRADEABLE.
- Sep 18 $10P: bid 0.70/ask 1.10, OI 819, spread 44% of mid → fails the harvest gate, marginally
  executable ONLY in assignment-welcome framing: sell ~$0.70-0.80 limit → breakeven ~$9.30-9.35
  (10% under the CEO's $10.95, 9.5% under spot), ~7% / 67 days, hold-to-expiry-or-assignment
  (the spread makes early exit punitive — roach-motel for harvesters, irrelevant for true CSPs).
- Lesson generalized: small-cap confluence premium is rich partly BECAUSE the spread is where MMs
  bank it — screen shows IV 59 at mid; selling at the bid nets ~IV low-50s vs RV 43. The mispricing
  persists because it is only partially accessible. Executable form = patient limit + assignment
  welcome + earnings binary accepted consciously; there is no harvest version of this trade.

### Market-wide confluence funnel (2026-07-12 — Jake: "scan the whole NASDAQ")
Architecture flipped: INSIDERS FIRST (OpenInsider latest-cluster-buys = whole market, one request),
then drawdown/IV-richness/chain-liquidity gates on survivors only. Gates: cluster value >$200K →
dd <= −25% vs 2y high → IV/RV >= 1.25 → put OI >= 100 + spread <= 25% + yield computed AT THE BID
(the GPK lesson baked in: never display premium that can't be collected). Cells in chat 2026-07-12.
Calibration corrections logged with it: (1) insider buying = months-horizon VALUE signal, NOT gap
protection (MTDR bought 46x through the COVID crash) — cluster buys reduce thesis risk, never event
risk; short puts remain fully exposed to sudden drops. (2) "Drawdown + insiders" marks the bottom
ZONE, not the tick — insiders are early by months, the put adds a deadline; assignment-welcome sizing
is the load-bearing bridge. Expect the survivor table empty most weeks; the rejection rate is the edge.

## 2026-07-12 — SEC: activists must disclose CLIENT identities in 13D/proxy filings (Reuters 7/10)
- New interpretations (Q 110.09, 155.02): SPV/"sidecar" investors in single-target activism vehicles
  must be named; LPs investing >$500 in a proxy-solicitation LP = "participants." Unexpected, quietly
  issued after a busy activist H1 (Elliott/Ancora/TOMS at WBD, DVN).
- **Toolkit upgrade (future):** 13Ds will start exposing WHO FUNDS campaigns — a new free layer for
  follow-the-money scans (sidecar LP names = which family offices/SWFs back which attacks). Add to
  the watch when first disclosures print.
- **Market-structure read:** disclosure kills the sidecar anonymity premium → chills campaign
  financing at the margin → marginally FEWER activist catalysts for the wreckage cohort (relevant to
  the [[cluster-shortlist-workup]] names where activism is the fix-it path: FISV/Jana, post-Starboard
  ADSK). A quiet management-friendly tilt in regulation, consistent with the champion-protection
  pattern — held loosely.

## 2026-07-13 ~9am PT — LangChain ships "OpenWiki Brains" = the vault's architecture, productized
- DATA: LangChain OSS release — "general-purpose wiki memory for agents": local markdown wiki,
  agent-maintained, connector-fed (Gmail/Notion/git/X/HN/web), scheduled background updates,
  filesystem-first. Their pitch = proactive memory vs the reactive built-in kind.
- *(analysis — validation + the deliberate divergence)* The vault IS this architecture, built by
  hand, plus the layers their version lacks: the DATA/THESIS firewall, corrections-stay-visible,
  pre-registration, the graded prediction scoreboard, source-independence calibration. **We do NOT
  adopt their headline feature — automatic connector ingestion — on doctrine:** (1) the standing
  no-unattended-jobs spending rule; (2) more fundamentally, auto-ingestion pipes the FEED'S noise
  straight into the brain — this weekend alone the manual gate caught helium-supply inversion,
  "Hormuz closed" inflation, a stale UAE claim, and a fake 155% FCF yield BEFORE they entered the
  wiki. **The vault's value is the curation and verification at the door, not the plumbing behind
  it.** Jake curates what enters; that's a feature, not missing automation.
- *(thesis crumb)* Agent memory commoditizing as OSS markdown (LangChain now, "Open Knowledge
  Format" namechecked) = the interop thread again: own your memory like you own your weights —
  local files + git beat platform lock-in. The vault was accidentally ahead of the category.

## 2026-07-13 ~7:45pm PT — source calibration: the ZH-repost layer question (Jake's challenge)
- Jake: "I give a fair amount of validity to ZH reposts. Haven't found a single false post yet."
- *(analysis — the layer model, with this week's receipts)* ZH is not one source; it's three
  layers with different base rates, and the brand gets credit earned by only the first:
  1. **Wire relays** (BBG/Reuters headlines, official statements verbatim): high accuracy as
     TRANSCRIPTION — this is what "never found a false post" is correctly measuring. The
     CENTCOM statements, the Waller quotes, the Araghchi quote: all clean relays.
  2. **Claim relays** (FARS, unnamed officials, partisan accounts): accurately QUOTED,
     unverified CONTENT. This week's receipt: the 5th-Fleet-casualties claim (relayed
     accurately, denied by CENTCOM within hours). The post wasn't false — the claim was. The
     repost format makes the reader grade the wrong thing.
  3. **Narrative/framing** (editorial, "what it means" threads): mixed record BOTH directions —
     the DC-cancellation narrative (debunked by SemiAnalysis) vs the token-spend claim (ZH
     ecosystem RIGHT, my 7/03 dismissal wrong, corrected in the vault). Neither trust nor
     dismiss: verify.
  - The falsifiability trap: "haven't found a false one" requires a verification channel
    INDEPENDENT of the feed. Most flash claims are never adjudicated at all — absence of
    discovered falsehood ≠ presence of truth. The vault's graded-instance ledger is the fix.
- **Source card — Seth Keshel (@RealSKeshel):** former Army intelligence captain, prominent
  since 2020 as an election-fraud trend analyst (county-level voter-registration vs vote-count
  "excess vote" methodology — widely criticized by statisticians as not identifying fraud);
  election-integrity circuit speaker; advocacy account, not a reporting or official source.
  The pasted tweet is PREDICTION-AS-CERTAINTY ("will compel... will mandate") about a speech
  he hasn't seen — tier 2/3 content in repost form. Gradeable Thursday alongside the
  Daugherty claim (both now on the calibration ledger).

## 2026-07-15 ~7:20am PT — rotation + unusual-options scanner (built)
- Two-stage tool (Jake's design): (1) SECTOR rotation via sector-ETF relative volume + direction;
  (2) unusual OPTIONS positioning in tickers that HAVEN'T moved yet (= someone building ahead of price,
  the systematic PYPL-call-surge pattern). The mechanical-flow / two-population edge in code.
- **Honest limits (stated to Jake):** yfinance options data is DELAYED (~15m) + often stale/zero →
  CANDIDATE GENERATOR, not a trade signal. "Unusual" options = volume>OI proxy (fresh positioning), NOT
  vs a true historical avg (no baseline in free data). Can't tell informed flow from hedging/spreads.
  Intraday equity RVOL is understated (partial day) → projected by fraction-of-day-elapsed. Rank-wise
  comparative reads > absolute. Generates names to VERIFY, per doctrine.
- Read: healthcare-leading = classically DEFENSIVE (risk-off) — tests Jake's "back to AI" hypothesis
  (which would need tech/semis leading). Scanner settles rotation direction.

## 2026-07-27 ~5:40am PT — NEW TOOL: the headline COLLECTOR (capture-everything → CSV → upload → Claude sorts)
- `tools/vault_headline_collector.ipynb` — flips the scanner's architecture per Jake's ask: NO keyword gate.
  Pulls ALL headlines (Google News Business/Tech/World firehoses = the paywalled majors aggregated, + direct
  feeds + topic queries + tickers), dedups, tags as metadata ONLY (nothing dropped), writes one CSV,
  auto-downloads in Colab. Workflow: run → upload CSV here → **"ingest headlines"** → Claude triages/
  summarizes into threads + flags the links worth opening. Fixes the keyword blind spot structurally (the
  scanner missed the CNBC CFO-blindsided story + CXMT items by construction — keyword-gated). The scanner
  notebook stays for the filtered quick-read + LEVEL WATCH prices. Division of labor per this playbook:
  Jake fetches free; Claude reasons on upload.

## 2026-08-09 ~12:55pm PDT — THE RESEARCH-ECOSYSTEM MAP (Jake's ranking) + the thesis-radar loop it commissioned
Source: `raw/research-ecosystem-ranking-2026-08-09.txt`. Jake's ranked map of where serious theses publish:
**VIC → SumZero → author-selected Substacks → CoBF → r/SecurityAnalysis → Seeking Alpha (as database) →
Bogleheads (implementation only) → Hacker News (engineer-grade tech dissection).** His usage stack:
ideas (VIC/SumZero/Substacks) · **anti-thesis (CoBF, r/SecAnalysis, SA bears)** · industry (specialist
Substacks, HN) · implementation (Bogleheads) — **then always primary documents.**
- **The standing loop this created (run on request, NOT scheduled — spending rule):** isolated scouts per
  ecosystem → filings confirmation via EDGAR on the best theses → reconciliation where **convergence
  only counts across ISOLATED branches**, filings verdicts outrank forum consensus, and results are
  checked against the vault's live threads. First run: `wf_7c8e88d5` (2026-08-09).
- *(analysis)* The ranking's own sharpest line is the closer: *"the more useful people arguing about one
  obscure assumption buried in a company's gross-margin model becomes."* That is this vault's firewall
  philosophy stated from the other direction — and the anti-thesis leg (his #2 use) is [[_calibration]]'s
  argue-the-underweighted-side, outsourced.

## 2026-08-10 ~6:50pm PDT — THE MAJORS' LAG, CODIFIED INTO A CONVENTION (Jake: "WSJ/Reuters… writing about things we've had mapped for weeks")
### DATA (the dated receipts, this month alone)
- Private-credit strain: vault's Dowd/gating fork + BDC gauges registered JULY (L150 fragility); Sarin
  corroboration 8/5; **WSJ's filings analysis arrived 8/9** — printing three of our five pre-registered
  gauges.
- SPV/off-B/S architecture: the fragility thread's FOUNDING frame (private credit → insurance →
  Bermuda); **ZH itself wrote 8/10 the FT "caught up with today."**
- Circularity: L517's verbatim circle filed weeks before **Huang pre-butted "circular financing" by
  name in his own launch FAQ (8/10)**.
- Disclosure fork (MSFT leases vs META SPVs): board-filed the MORNING BEFORE Wigglesworth's $1T tweet.
- Memory thrifting → SKH −15%: vault 8/6; JPM's defense note post-crash 8/10.
### THESIS (both sides, deliberately)
- *(why it is STRUCTURAL, not brilliance)* The majors' unit of production is the VERIFIED EVENT —
  publication requires a peg and two sources; their lag is the PRICE of their accuracy standard. The
  vault's unit is the REGISTERED QUESTION — a question registered in July makes August's answer-event
  coverage look "late." Different products. **And the vault FEEDS on their output** — the WSJ filings
  analysis was our explicitly-wanted "current source"; the FT's "six people briefed" is reporting we
  cannot do. Their access + our synthesis-speed are complementary, not competitive.
- *(⚠️ the trap, stated before it compounds)* "The news is behind us" is ALSO what an echo chamber
  feels like from inside. The viral layer was "ahead of" WSJ on today's OpenAI-exodus story too — and
  it was WRONG; the majors' slowness would have been accuracy. **Early and right are only
  distinguishable at GRADING time** — the scoreboard, not the feeling, arbitrates. (⛔ _calibration
  L342: "clear-eyed one; everyone else spins" = ego-bait.)
- *(★ THE CONVENTION — the applicable version of Jake's observation)* **Major-outlet arrival on a
  vault thread is a DIFFUSION DATUM, not an information datum.** It marks the thesis being socialized
  to the widest audience — the same class as "a sell-side how-to-profit list marks the idea as
  distributed," one ring further out. **RULE: when WSJ/FT/Reuters land on a mapped thread, log the
  LAG (vault-filed date → majors date) in the thread as a diffusion marker.** A thread the majors
  have reached is late in its information cycle; a thread they haven't is where the vault's edge
  still lives (current examples: the NdPr/magnet silence, the SDLLMTK squeeze pair, the duration
  mismatch — unmapped by any major as of tonight).

### 2026-08-11 ~11:10am PDT — 🔴 INFRASTRUCTURE: FRED IS DOWN FOR PROGRAMMATIC ACCESS, AND FOUR VAULT CELLS DEPEND ON IT
Discovered building F19. **Not a bad-series-ID problem — a FRED problem.**

#### DATA (observed — two independent networks, same result)
- **Container (via proxy) and Jake's Colab both TIME OUT on every FRED series tried.** Not 404s —
  **timeouts**, i.e. the request hangs rather than being rejected.
- **The IDs are not the issue and this is the proof: `NEWORDER`, `AMTMNO` and `TTLCONS` all failed.**
  Those unquestionably exist. **When a canonical series fails, stop debugging the ID.**
- Both endpoint forms fail: `fred.stlouisfed.org/graph/fredgraph.csv?id=` and `/data/{id}.txt`.
- **Adjacent sources, tested the same hour:** ✅ **SEC EDGAR XBRL — WORKING** (the FCF pull ran fine).
  ✅ **census.gov STATIC FILES — WORKING** (C30 xlsx served with no key). ❌ **Census API — "Missing
  Key"** (was keyless, now is not). ❌ **Census currentdata CSV export — 400 on every parameter
  combination tried.** ❌ **DBnomics — 404 on its series endpoints.** ❌ census.gov root — 520.

#### ⚠️ BLAST RADIUS — cells that will silently degrade or fail
| cell | FRED dependency | consequence |
|---|---|---|
| **`acute_scanner_cell.py`** | macro series via fredgraph | **⚠️ THE DAILY DRIVER. Its macro block is dead.** Jake ran it 8/11 14:26 UTC — **⬜ unknown whether the FRED legs were already failing then or degraded after.** |
| `momentum_extrapolation_backtest_cell.py` | VIXCLS, DTB3 | backtest cannot re-run (CBOE SPX leg still fine) |
| `long_yield_regime_cell.py` | yield series | dead |
| `civil_materials_cascade_cell.py` | materials series | dead (was already never-run — see chat-log 7/31) |

#### THESIS (interpretation — NOT fact)
- **★★★ THE LESSON IS A DIAGNOSTIC RULE, not a fact about FRED: WHEN A CANONICAL IDENTIFIER FAILS,
  THE TRANSPORT IS BROKEN, NOT THE IDENTIFIER.** I spent two rounds widening a candidate list from 17
  IDs to 27 — **treating a transport failure as a naming problem** — and only Jake's paste of the full
  ✗ block (showing `NEWORDER` and `TTLCONS` failing) made it unmistakable. **A probe that cannot
  distinguish "wrong ID" from "no connection" is a badly designed probe: 404 and timeout mean opposite
  things and mine collapsed both into `✗`.** 📌 **FIX FORWARD: every future probe prints the EXCEPTION
  TYPE, not just pass/fail.** *(Analysis.)*
- **★★★ GO TO THE ORIGINAL SOURCE, NOT THE AGGREGATOR. FRED does not produce a single series in this
  vault — it MIRRORS Census, BLS and Treasury.** The C30 data-centre line was available direct from
  census.gov the whole time, **at higher resolution than FRED carries** (FRED has no data-centre
  series at all; Census breaks it out as its own column). ⇒ **The aggregator was both the fragile leg
  AND the lossy one.** *(Analysis. This generalises: prefer the issuing agency.)*
- 🚩 **OPEN: whether this is an outage, a UA/bot block, or a permanent access change.** Retest before
  assuming any FRED-dependent cell works. **⬜ If it is a UA block, a browser-like header set may pass
  — untested.** *(Analysis.)*
- 🚩 **STILL UNSOLVED: a keyless M3 source** (manufacturers' new orders, NAICS 334) for F19's orders
  leg. Every route tried is walled. **A free Census API key (instant signup) is the obvious unlock and
  needs Jake's yes — it is a registration, not a charge.**
**Links:** [[ai-capex-cycle]] · [[fragility-engine]]

### 2026-08-11 ~4:20pm PDT — ★★★ JAKE'S API RULE, IMPLEMENTED AND MEASURED: "batch smaller requests" — the EDGAR win is 137x, and it fixes the Q1-only bug as a side effect
**Jake, 8/11:** *"I think with data fetch through APIs we should batch smaller requests."* **Correct,
and on EDGAR it is measurable.** Built `tools/edgar_batch_cell.py`; run end-to-end 2026-08-11.

#### DATA (observed — measured this session)
| endpoint | scope | size | note |
|---|---|---|---|
| `companyfacts` | one company, **EVERY tag** | **2.70 MB** | what every prior vault pull used |
| `companyconcept` | one company, **ONE tag** | **0.020 MB** | **137× smaller** |
| `frames` | **ONE tag, EVERY filer** | 0.03-0.69 MB | **4,548 companies in ONE call** |
- **THE OLD PATTERN SCALED WITH THE NUMBER OF COMPANIES** (8 names = 8 blobs ≈ 22 MB to read two
  lines each). **`frames` scales with the number of PERIODS instead** — adding names is free.
- **⚠️ THE FILING-LAG GRADIENT, which the old script could not see and which silently lies:**
  **CY2026Q1 = 4,548 filers · CY2025Q3 = 407 · CY2025Q4 = 340 · CY2026Q2 = 168.**
- **⛔ AND THE GRADIENT EXPOSES THAT `frames` INHERITS THE SAME YTD DEFECT — do not oversell it.**
  Q1 is fat and every other quarter is thin **for the same reason the 80-100 day filter only caught
  Q1: most filers tag cash flow YEAR-TO-DATE, so only Q1 is a discrete quarter.** ⇒ **`frames` fixes
  the BATCHING, not the DURATION problem. YTD-differencing (Q2 = H1 − Q1) is still required**, and is
  built in as an explicit fallback.
- Multi-tag merge added after the first run returned "no capex" for AMZN — **AMZN tags capex as
  `PaymentsToAcquireProductiveAssets`.** A single-tag pull returns a silent blank, not an error.

#### THESIS (interpretation — NOT fact)
- **★★★ THE GENERALISABLE RULE IS NOT "SMALLER" — IT IS "BATCH ACROSS ENTITIES, NARROW ACROSS FIELDS."**
  Both moves shrink the payload, but they solve different problems: **narrow** stops downloading a
  company's whole history to read two lines; **batch** stops paying per-company round-trips. **Most
  agency APIs offer both and the vault was using neither.** *(Analysis.)*
- **★★★★ THE SECOND-ORDER WIN IS DIAGNOSTIC, AND TODAY PROVED IT MATTERS MORE THAN THE BYTES. Short
  timeouts + fail-fast turn an unreachable host into a 12-second answer instead of a 40-minute hang**
  — the exact failure Jake hit on the F19 cell. **And separating "HTTP status" from "timeout" is the
  distinction that would have diagnosed FRED in one call: a 404 means the ID is wrong, a TIMEOUT means
  the host is gone, and my probe rendered both as `✗`.** *(Analysis.)*
- **★★★ REPORT COVERAGE, NOT JUST VALUES. A period with 168 filers and one with 4,548 are not the same
  evidence.** A table that prints only numbers cannot tell you whether a blank means *no data* or *not
  filed yet* — **and today that difference was the whole META error.** ⇒ **Any cross-sectional pull
  from now on prints its own denominator.** *(Analysis.)*
- 📌 **MIGRATION LIST — cells still on the `companyfacts` blob pattern:** `cepi_tracker_cell.py` ·
  `balance_sheet_ledger_cell.py`. ⬜ **Not yet migrated. Their numbers stand** (they read INSTANT
  balance-sheet concepts, which have no YTD problem) **but they should move for speed.**
**Links:** [[cepi]] · [[balance-sheet-board]] · [[ai-capex-cycle]]

## 2026-08-12 ~2:35pm PDT — ⛔ A 429 IS NOT A TIMEOUT AND NOT AN AUTH WALL. THREE FAILURES, THREE TRIAGES.
Source: reachability tests during the [[colab-archive-audit]] ingest.
### DATA (observed — this container, 2026-08-12)
- `query1.finance.yahoo.com` / `query2.finance.yahoo.com` v8 chart API → **HTTP 429 "Too Many Requests."**
  Persists with a browser User-Agent, on both hosts.
- `stooq.com` CSV endpoint → **connection failure (curl code 000, zero bytes).**
- `drive.google.com` public folder HTML + `uc?export=download` → **HTTP 200**, 50 files, 5.60 MB pulled clean.
### THESIS (interpretation — NOT fact)
- **The failure MODE dictates the triage, and conflating them wastes sessions.** *(Analysis.)*
  - **HTTP 4xx/5xx = the host answered.** 429 specifically = a *shared-egress rate limit on a live service*
    — it can clear by itself, and a different network (Colab) resolves it immediately. **Never mark the
    host dead.**
  - **Timeout / connection failure = the host is unreachable from here.** FRED and stooq. Retrying is pure
    cost; `edgar_batch_cell.py`'s fail-fast marks the host dead for the run, which is correct here.
  - **"Missing Key" = an auth wall.** Census API. No amount of retrying or waiting fixes it; only a key does.
- **This is the same lesson as the 8/11 FRED misdiagnosis, stated as a rule instead of a war story: a probe
  that renders all three as `✗` will send you to fix the wrong layer.** On 8/11 that cost two rounds and a
  17→27 ID expansion against a transport failure. *(Analysis.)*
- **Standing consequence: yfinance-dependent cells are JAKE-SIDE, not container-side, until 429 clears.**
  23 of the 50 archived notebooks and `tools/acute_scanner_cell.py` are in that set.
