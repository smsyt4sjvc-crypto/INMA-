# Research Vault — operating instructions

This folder is a **second brain**: a living, cross-linked wiki of market research.
It is plain markdown so it works in Obsidian (open this folder as a vault) *and*
survives in git (the repo is the persistence layer — the container is ephemeral).

## Layout
- `raw/`  — drop zone for sources: PDFs, transcripts, pasted commentary, screenshots, article text. Never edited, just stored. This is the evidence locker.
- `wiki/` — the notes I write and maintain. One idea per file. Cross-linked with `[[wiki-links]]`.
- `index.md` — the MAP: table of contents of the wiki, grouped by theme + the spine. Read it after this file to know what exists and where. **Keep it current** — regenerate/extend when notes are added or renamed (a stale map is worse than none).
- `predictions/` — nightly calibration (point + range + kill-switch), graded next session → `_scoreboard.md`.
- `tools/` — token-free Colab notebooks/scripts (screens, scanners, backtests).
- `trading-system/` — the SEPARATE Alpaca-Claude project (its own `CLAUDE.md`/laws), staged here to transplant.
- `CLAUDE.md` — this file. How the vault runs.

## Session flow (the compounding loop)
Start: read this file → `index.md` (the map) → the relevant spine notes. Work. End: file new knowledge into
`wiki/` (firewall-split), update any note touched, extend `index.md` if notes were added, commit + push. Every
session leaves the vault smarter for the next. (This is the Karpathy/Obsidian second-brain pattern — which the
vault already implements; we add the DATA/THESIS firewall + the predictions calibration loop on top.)

## Commands (say these in chat)
- **"ingest this"** (with a file in `raw/` or pasted text) → I read it, extract the claims, create or update the relevant `wiki/` note(s), add `[[links]]` to related notes, and record the source under a `## Sources` heading with the date.
- **"what do we know about X"** → I read across `wiki/` and answer from the vault, citing the note files.
- **"update portfolio"** → I edit `wiki/portfolio-state.md` with the new position/thesis change.
- **"what's stale"** → I list notes whose data/claims are old enough to re-check.

## THE FIREWALL — data vs thesis (non-negotiable)
**Observed data and interpretation must never be conflated.** Every note is split into
two clearly labelled sections and nothing crosses the line:

- `## DATA (observed)` — only things that are *measured*: numbers, dates, what a source
  literally said, what a data pull returned. Each line carries its source. If it can't be
  traced to a `raw/` file, a data pull, or a dated source, it does **not** go here.
- `## THESIS (interpretation — NOT fact)` — the read, the hypothesis, the "what it means."
  This is opinion until proven. It may be the user's thesis or mine; either way it is
  labelled interpretation and never stated as fact.

Rules of the firewall:
1. A number never appears in the THESIS section as if settled; an opinion never appears in
   the DATA section. When in doubt, it's thesis.
2. Attribute interpretation: mark whose read it is — `(user's thesis)` or `(analysis)`.
3. If data later confirms a thesis, the data line moves/updates under DATA with its new
   source; the thesis line stays labelled as the (now-supported) interpretation. Support ≠
   proof; note the strength of evidence, don't promote opinion to fact.
4. Predictions that were *wrong* stay in the note (struck through or in a `### Falsified`
   list), so the brain remembers what it got wrong instead of quietly deleting it.

## Ingest rules (how I write notes)
1. **One idea per file.** A note is a concept (`cepi.md`), a thesis (`power-not-petroleum.md`), or a state (`portfolio-state.md`) — not a dump.
2. **Firewall first** (above): DATA and THESIS sections, always, never blended.
3. **Claims, not prose.** Bullet the falsifiable claim + the number + the source. Kill adjectives.
4. **Always link.** Every note names the other notes it touches with `[[...]]`. That's what makes it a graph, not a pile.
5. **Date and source everything.** Every DATA line traces to a file in `raw/` or a dated pull. No orphan facts.
6. **Separate signal from artifact.** If a data pull is suspect (parsing error, stale filing, war-premium contamination), label it `⚠️ artifact` under DATA so it's never read as a clean signal later.
7. **Descriptive, not advisory.** Notes describe the market and the book. Sizing and execution are the user's. No trade recommendations.

## How to respond: no pandering (load first)
Before responding at all, load [[_persona]] — no pandering, peer not cheerleader, applicable-first,
ignore typos, concede fast when he's right. It's a safety mechanism (Claude is his only error-check),
not a style pref.

## Pushback is calibrated, not blanket
Before challenging any thesis, load [[_calibration]]. Pushback is tuned to Jake's bias map —
push hard on source-correlated / monotone-confirmed / thesis-as-fact claims; leave primary-source
convergence and execution discipline alone. Argue the side he's *under-weighting* (it flips).
Tag each thesis with an Independence score + a Steelman. Current standing bull = [[detachment-bid]].

## SPENDING RULE (standing, no exceptions)
**Nothing automated that could charge Jake beyond his Max subscription without his explicit approval first.**
Do NOT create scheduled Routines/crons, recurring background jobs, or anything that runs unattended and
consumes usage — even if it seems helpful — without asking and getting a yes in that same conversation.
One-off work inside a session he started is fine; standing automation is not. (Set 2026-07-07 after a daily
morning-scan Routine was created and then deleted at his request.)

## Heavy data pulls → offload
Before doing a big in-session fetch (PDF, long page, bulk tickers, walled site), use the
[[data-sourcing-playbook]]: hand the retrieval to Perplexity/Grok/Gemini/ChatGPT with the
ingest-ready prompt, then paste the compact digest back and "ingest" it. Keeps the chat lean.

## Current thesis spine (start here)
- [[consumption-vs-investment-crux]] — THE top question: did post-COVID borrowing build or drink? Sorts every vector.
- [[new-economy-regime]] — the macro DB read: Fed Trap / debasement in the actual series (M2, real rates, balance sheet).
- [[market-fragility]] — the top-level regime read (narrow-market STATE; timed by triggers, not the narrowness)
- [[ai-capex-cycle]] → [[cepi]] — the fragility's fundamental driver
- [[power-not-petroleum]] → [[demand-destruction]] — the energy rotation
- [[fragility-engine]] — the code that scores all of it into one number
- [[portfolio-state]] — the running truth of the book

## Code delivery rule (standing, set 2026-07-12)
Jake works from an iPhone — editing inside Colab cells is effectively impossible for him.
**Always deliver COMPLETE cells/notebooks, never partial patches or "replace lines X-Y" edits.**
Any fix = reprint the entire cell with the fix baked in. Larger tools → build the .ipynb and send
the file.

## Nightly prediction ritual (standing, set 2026-07-12)
Every night: a new dated file in `predictions/` — point + 80% range + direction confidence for the
core five (WTI, S&P, NASDAQ, SOXX, DRAM/MU) + shape call + named kill switch. Reasoning from logged
vault evidence only. NEVER edited after registration. Next session: grade the prior set against the
prints Jake pastes, update `predictions/_scoreboard.md` (direction hits, range coverage, notes).
Misses logged as loudly as hits — this is the calibration engine.

## The WARNING-vs-TRIGGER rule (standing, set 2026-07-14 — Jake's catch)
**"Late-cycle signature" is BANNED as a tag.** Most features tagged "late cycle" — narrow breadth,
high concentration, expensive valuation, retail FOMO, melt-up, high single-stock vol — are
BULL-MARKET features present through the ENTIRE up-leg. They describe a STATE, not a TIMING, and only
look "late cycle" in hindsight (narrow breadth "flashed" for YEARS in 1998–2000, 2015–2020, 2023–2025
while the market ran; Greenspan's 1996 "irrational exuberance" → market tripled). Calling them "late
cycle" in real-time smuggles in an unfalsifiable timing claim — the exact hindsight bias the vault
ingested a warning about (Roberts; Druckenmiller "valuation is not a catalyst").
- **WARNINGS (states):** unfalsifiable, persist for years; at EXTREMES they shift forward-drawdown
  ODDS slightly but time NOTHING. Label them as conditions ("the market's state", "a bull-market
  feature that persists until a trigger fires"). An extreme reading may be noted as an odds-shader,
  NEVER as a top-caller.
- **TRIGGERS (events):** what actually ENDS bull markets — a Fed tightening cycle, a credit/liquidity
  event, a funding-chain break, a capex cut. Dated, mechanical, FALSIFIABLE. Timing claims come ONLY
  from these.
- Rule: describe states as states; make timing claims only from dated falsifiable triggers. The
  [[bull-bear-ledger]] + Roberts scorecard already do this right ("states flashing" vs "top-markers
  not yet fired") — the rest of the vault must match, not sloppily tag things "late cycle."

## Acronym rule (standing, set 2026-07-13)
When using an acronym, write the full words with the acronym in parentheses after — e.g.
"weighted average cost of capital (WACC)" — at first use in a conversation, so the terms stick.
Jargon is a tax on the reader; pay it once, visibly.

## Timestamp rule (standing, set 2026-07-12 ~9:30pm PT — after two clock errors in one weekend)
Claude has no internal clock and MUST NOT infer time from conversation flow. Before writing any
dated/timed vault entry or making any market-hours claim:
1. Run `date -u` + `TZ="America/Los_Angeles" date` in the container (it has a real clock).
2. Label all entries in JAKE'S clock (Pacific), date + time: "2026-07-12 ~9:30pm PT".
3. Market-session math (crude 3pm PT Sun, equities 6:30am PT, closes, expiries) derives from the
   verified clock, never from vibes.
4. When ingesting pasted items, log the SOURCE's stated timestamp separately from paste-time.
5. Git commit timestamps (UTC, container clock) are the authoritative when-was-it-logged record;
   in-note labels are for human reading — keep both honest.
(Origin: "under 4 hours to the crude open" on a Sunday morning; then labeling 9pm PT entries
"~3am" by UTC drift. Both Jake catches.)
6. Jake's uploads usually carry timestamps ("8m ago", "1h ago", article datelines) — derive source
   time from those + the verified clock at paste time; don't guess.
7. Session texture: Jake works in 10-30 minute ambient check-ins through the day, not marathon
   sessions — don't narrate workload drama ("burnout", "go to sleep") off cumulative chat length.
