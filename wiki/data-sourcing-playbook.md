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
