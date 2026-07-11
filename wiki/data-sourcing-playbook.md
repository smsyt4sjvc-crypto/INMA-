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
