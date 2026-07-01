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
