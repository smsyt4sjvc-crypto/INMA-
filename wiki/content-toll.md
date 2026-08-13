# Content Toll — the crawler unbundling, and content becoming a priced AI input

Opened 2026-08-12 ~7:50pm PDT off a Goldman TMT note Jake pasted on "Google Zero."
Related: [[metered-compute]] · [[compression-thesis]] · [[cepi]] · [[ai-capex-cycle]] · [[agentic-payments]] · [[concentration]]

> **⛔ ARTIFACT TEST — name what was actually read.** Jake pasted **a Goldman TMT note characterising
> WSJ reporting.** That is THREE layers (WSJ → Goldman → paste) and **I have read neither the WSJ piece
> nor the Goldman note.** What I DID read: **Cloudflare's own July-2026 announcement + developer
> changelog**, and secondary coverage of the WSJ report (Nieman Lab, Digiday, TechCrunch, Editor &
> Publisher). **So the Cloudflare mechanics below are near-primary; the publisher claims are not.**
> Per rule 9's "N outlets, one origin": **every publisher item traces to ONE origin, the WSJ report.**

## DATA (observed — verified 2026-08-12 unless marked)
### The traffic collapse
- **"Google Zero"** = the point at which Google Search stops sending traffic to third-party sites.
  **Term coined by Nilay Patel (The Verge), 2024** — it is a 2-year-old coinage, not a new concept.
- **Traffic fell >40% for some publications, June 2025 → June 2026 — per SEMRUSH data** *(the number
  Goldman quotes; its origin is Semrush, not WSJ's own measurement).*
- **USA Today: Google search traffic down ~half over the 12 months ending June 2026.**
- **58% of Google searches now end with ZERO CLICK** (attributed to AI Overviews).
- **Outlets reported reconsidering ties to Google: USA Today, Politico, Reuters, The Economist**
  (Goldman's paste also names Reddit).

### The mechanism
- **Googlebot is ONE crawler serving TWO purposes** — search indexing *and* AI training. Publishers
  cannot separate "index me" from "train on me."
- **Cloudflare's own data: 36% of all crawler activity is now mixed-use** (blending Search + Training
  in a single bot).

### Cloudflare's policy — announced ~2026-07-01, effective **2026-09-15**
- From **Sept 15, 2026**: **Training and Agent bots blocked BY DEFAULT** — but only on:
  1. **NEW domains** joining Cloudflare, or new sites added to existing accounts, **and free-tier sites**
  2. **pages that CARRY ADVERTISING**
- **SEARCH BOTS REMAIN ALLOWED BY DEFAULT.**
- **Existing customers keep their settings**, get advance notice, and can opt out any time before the date.
- The Googlebot collision bites **only customers who have themselves enabled Training-bot blocking** —
  for them, Googlebot is also blocked on ad-monetised pages because it is combined.

### ⛔ THE EVIDENCE-LADDER STATE OF THE PUBLISHER CLAIM
- **AS OF 2026-07-25: NO NAMED PUBLISHER HAD ACTUALLY BLOCKED GOOGLE'S CRAWLERS. Reddit had not cut
  Google off.** ⬜ Not re-checked between 7/25 and today.

## THESIS (interpretation — NOT fact)
- **⛔ THE SELL-SIDE NOTE IS MATERIALLY WIDER THAN THE UNDERLYING FACTS, IN TWO PLACES, AND BOTH
  OVERSTATE IMMINENCE.** *(Analysis.)*
  1. *"Cloudflare plans to start blocking multi-purpose crawlers by default from mid-September unless
     site owners opt out"* reads as a **web-wide default flip.** The actual policy is **new domains +
     new sites + free tier, on AD-CARRYING PAGES ONLY, with SEARCH still allowed by default.**
     **Existing paying customers' existing sites are untouched unless they act.** The immediate
     footprint is a small fraction of what the sentence implies.
  2. *"openly considering **or preparing to restrict**"* — the verified state is **considering, ZERO
     executed.** **Announced vs FID.** A publisher "considering" blocking Google is a negotiating
     posture with a free option attached; blocking is an act with a revenue consequence. **They are
     not the same rung.**
- **★★★★ THE STRUCTURAL POINT, AND IT IS NOT THE TRAFFIC NUMBER: THE ENTIRE SOURCE OF GOOGLE'S
  LEVERAGE IS THAT ONE CRAWLER SERVES TWO PURPOSES.** Search indexing historically *paid* publishers
  in traffic; training pays them nothing. **Bundling them into a single bot makes the price of training
  data equal to the price of search visibility — i.e. it makes it unpriceable separately.** Cloudflare's
  move matters **not for its immediate footprint but because it UNBUNDLES the crawler BY PURPOSE at the
  edge.** Once purpose is separable and enforceable, content becomes priceable per-use. **That is the
  precondition for a market in training data, and it is the first time the precondition exists.**
- **★★★ AND IT IS THE SAME ARCHITECTURE AS [[metered-compute]], APPLIED TO A DIFFERENT INPUT.** That
  note's spine is metering + a settlement toll (x402/MPP). **This is metering + a toll on CONTENT.**
  ⚠️ **And the same company sits on both rails: `metered-compute:36` already logs Cloudflare inside
  the x402 consortium** (Coinbase/Cloudflare/Google/Visa/AWS). **Cloudflare is simultaneously building
  the gate (crawler purpose-detection) and the turnstile (machine payment).** *(Analysis.)*
- **⚠️ BUT THE VAULT HAS ALREADY GRADED THE NET-AS-TOLLBOOTH THESIS ONCE AND CUT IT, AND THAT PRIOR
  SURVIVES — WITH ONE REAL UPDATE.** `metered-compute:540`: *"Digest ranks NET #1 as 'neutral
  tollbooth' — but our read-2 cuts the tollbooth thesis: NET's actual model = give the gateway away to
  sell security/edge around it (adjacency, not toll)."* **That read still holds: there is no disclosed
  crawler revenue and the default applies to the FREE tier, which is customer acquisition, not a toll.**
  **THE UPDATE: the AI Gateway was a giveaway SIDE product; crawler control is a default setting on the
  CORE CDN/security product NET actually sells.** ⇒ **This is the first move that puts the gate on the
  thing being paid for rather than beside it. An update to the prior, not a reversal of it.** 🚩
- **★★ THE COUNTERINTUITIVE READ ON GOOGL, WHICH IS THE SIDE JAKE'S SOURCE IS UNDER-WEIGHTING: "GOOGLE
  ZERO" IS NOT OBVIOUSLY BAD FOR GOOGLE'S NEAR-TERM ECONOMICS.** A zero-click answer keeps the user ON
  Google's page: **the session, the ad inventory and the next query all stay in-house, and the traffic
  that used to leak to a publisher no longer leaks.** **58% zero-click is a monetisation-surface
  statistic as much as a publisher-harm statistic.** The genuine risks are *(a)* **regulatory — tying
  search-index access to training-corpus access is a textbook bundling theory**, *(b)* index
  degradation if blocking ever moves from considered to executed, *(c)* whether an AI Overview
  monetises as well per query as the ten blue links did. **⬜ None of the three is measured here, and
  (c) is the one that would actually move the P&L.** *(Analysis. Descriptive — rule 7.)*
- **★★ FOR [[compression-thesis]]: THIS IS AN INPUT LEAVING THE FREE COLUMN.** The thesis is that AI
  costs collapse as inputs deflate. **Training data has been priced at zero for the entire era.** If
  purpose-separated crawling makes corpus access a paid line item, **one major input starts inflating
  while compute deflates** — which is the first identified counter-current to the compression spine
  that is not about capital or power. ⬜ **Unquantified: nobody has disclosed what a corpus licence
  costs as a share of training spend.** 🚩 **That number is the whole question.** *(Analysis.)*

## 🚩 THE DATED, FALSIFIABLE TRIGGERS (per the WARNING-vs-TRIGGER rule)
*"Publishers are considering blocking Google" is a STATE — unfalsifiable, persists indefinitely, times
nothing. These are the events:*
- **T1 — 2026-09-15: Cloudflare's default flips.** Dated, mechanical, certain to occur. **What to
  watch is not the date but whether the scope stays as announced** (new + free + ad-pages) **or is
  widened to existing customers.** Widening is the real signal.
- **T2 — the first NAMED publisher actually blocking Googlebot.** As of 7/25 the count was **ZERO**.
  **This is the trigger that converts the story from posture to fact.** Reddit is the highest-signal
  candidate *and the most confounded* — ⚠️ it is already a Google *licensor* (paid content deal,
  ~$60M/yr per 2024 reporting — **⬜ recalled, NOT verified**), so a Reddit block is a **contract
  renegotiation**, not a publisher revolt. **Do not read it as the same event.**
- **T3 — the first disclosed crawler/licensing revenue line** at NET or a publisher. Turns the toll
  thesis measurable, exactly as `metered-compute` registered for the routing layer.
- **T4 — an antitrust filing or inquiry naming the search/training crawler bundle.** The tying theory
  is the cleanest legal handle in the whole story.

## ⬜ NOT-KNOWN
- ⬜ The WSJ article itself — unread. Every publisher claim here is second-hand.
- ⬜ The Goldman note itself — unread; Jake's paste is the only text.
- ⬜ Whether any publisher has blocked between 2026-07-25 and today.
- ⬜ What share of Google's index/training corpus is Cloudflare-fronted — **this sizes the entire
  story and I have no figure for it.**
- ⬜ Whether AI Overviews monetise per query above or below the displaced link. **The load-bearing
  unknown for GOOGL.**
- ⬜ Cost of a corpus licence as a share of training spend.

## Sources
- Cloudflare blog + developer changelog, 2026-07-01 ("Your site, your rules: new AI traffic options");
  effective date 2026-09-15 — read via search summary, not the raw page.
- Secondary on the WSJ report: Nieman Lab (2026-07), Digiday, TechCrunch (2026-07-01),
  Editor & Publisher, Help Net Security, The AI Insider.
- Goldman TMT note — **via Jake's paste only, 2026-08-12 ~7:45pm PDT. Not read.**

---

## 2026-08-12 ~8:30pm PDT — ★★★★★ JAKE'S TWO QUESTIONS INVERT THE NOTE'S CONCLUSION
Jake: *(1) "This is the first I've ever heard of it as well. 2 days after they announce one billion
Gemini users. Hmmmm…"* *(2) "Is it a revenue [play] as much as **not** paying for that training data?"*

### DATA (observed — verified 2026-08-12)
- **2026-08-11: Pichai announced the Gemini app crossed 1 BILLION monthly active users** — the
  fastest-growing product in Google's 28-year history, its 14th service at that scale.
  *(Jake's paste of the Goldman note reached me **2026-08-12 ~7:45pm PDT** — **next-day, not two days.**)*
- **The ramp: 400M (May-2025 I/O) → 650M (Oct-25) → 750M (Feb-26) → 900M (May-26) → 950M (Jul-26) →
  1B (Aug-26).** The last 50M took ~3 weeks.
- **63% of active users interact by VOICE · >150M images generated per day · >100M active on iOS.**
- **⛔ GOOGLE DID NOT DISCLOSE HOW MANY OF THE 1B PAY.** Flagged as a notable omission in the coverage.
- Vault-held for scale: **GOOGL capex/OCF ran 27% (2023-03) → 42% → 48% → 78% (2026-03)**
  ([[cepi]]:442).
- ⬜ **Content-licensing comparables are RECALLED, NOT VERIFIED this session** — News Corp–OpenAI
  (~$250M/5yr), Reddit–Google (~$60M/yr), Axel Springer–OpenAI. **Do not cite as vault data.**

### THESIS (interpretation — NOT fact)
- **★★★ (1) THE JUXTAPOSITION IS REAL, AND IT IS TIGHTER THAN "SUSPICIOUS TIMING": THE 1B GEMINI MAU
  AND THE 58% ZERO-CLICK RATE ARE THE SAME MIGRATION MEASURED FROM OPPOSITE ENDS.** Query volume moving
  from *search → link → publisher* to *answer on Google's own surface* **produces both numbers at
  once.** Google announces one as the fastest ramp in its history; the other is reported as an industry
  crisis. **Same flow, two press releases.** *(Analysis.)*
  ⚠️ **But do NOT read intent into the sequencing.** The Cloudflare policy is dated **2026-07-01** and
  the WSJ report ~late July — **both predate the Gemini milestone by weeks.** What is same-week is
  **GOLDMAN'S NOTE**, not the underlying events. ⇒ **The sell-side re-packaged a five-week-old story as
  news the day after a Google triumph.** That is a fact about the note's framing, not about Google's.
- **⛔ AND THE MISSING SUBSCRIBER NUMBER IS THE VAULT'S OWN PATTERN, UNPROMPTED: A USAGE NUMBER WITHOUT
  A REVENUE NUMBER.** 1B MAU, 150M images/day, 63% voice — **and no paid conversion disclosed.** That is
  the same shape [[cepi]] tracks on the capex side and [[metered-compute]] tracks on tokens: **the
  engagement metric is volunteered and the monetisation metric is not.** *(Analysis.)*
- **★★★★★ (2) JAKE'S SECOND QUESTION IS THE BETTER FRAME, AND THE ANSWER IS "YES, BUT NOT FOR THE COST
  REASON."** Three layers, and only the third is load-bearing:
  1. **DIRECT DOLLARS AVOIDED — REAL BUT SMALL, AND THIS KILLS THE NAIVE VERSION.** Disclosed licensing
     deals run in the **hundreds of millions per year** for a major buyer. Against a hyperscaler capex
     line where GOOGL alone spends **78% of operating cash flow**, a few hundred million is a rounding
     error. **"Google saves money by not paying" is true and unimportant.**
  2. **THE ASYMMETRY — better, still not the point.** Google pays ~zero for what OpenAI/Anthropic
     increasingly pay for, *and* gets wider coverage. In a market [[compression-thesis]] says is
     commoditising, **relative input cost is what survives**. But it is a margin story, not a moat.
  3. **★★★★★ THE ACTUAL ASSET IS NOT CONTENT, IT IS COMPREHENSIVENESS AND RECENCY, CONTINUOUSLY,
     WITHOUT NEGOTIATION — AND NO AMOUNT OF MONEY BUYS IT.** A licence buys one publisher's archive from
     a willing seller. **The crawl buys the whole web, fresh, daily, including the entire long tail that
     will never sign a deal and has no one to negotiate with.** **There is no counterparty for "the
     web."** ⇒ **This is not a revenue question or a cost question. It is an ACCESS question, and access
     is the only genuinely non-substitutable input in the stack.** *(Analysis. This is the answer to
     Jake's question and it is stronger than the framing he offered.)*
- **★★★★★ AND THAT INVERTS GOLDMAN'S CONCLUSION. "The old model is cracking" reads as bearish Google.
  A world where crawling becomes blocked or priced is a world where THE FREE, OPEN, WEB-SCALE CORPUS
  STOPS EXISTING FOR EVERYONE — and the party that already has one is Google.** *(Analysis.)*
  - **A new entrant cannot reconstruct a 20-year index at any price.** Fencing the commons **raises the
    wall around whoever is already inside it.**
  - **And Google's FIRST-PARTY reserve is the part nobody can licence at all: YouTube** (the largest
    video corpus on earth, wholly owned) **plus Search query logs, Maps, Android.** **The open web is
    the input everyone SHARES; YouTube and the query log are the inputs only Google has.** ⇒ **If the
    shared input gets fenced, the competitor with the largest PRIVATE reserve is advantaged, and that
    is Google by a distance.**
  - **⚠️ THE HONEST LIMIT ON MY OWN ARGUMENT: a frozen index degrades.** Grounded, current answers
    (news, prices, events) need continuous fresh crawl, so "already has the corpus" is a decaying
    advantage, not a permanent one. **It is a bigger moat than a new entrant has; it is not a moat
    forever.**
- **🚩 THE TEST THAT SEPARATES THE TWO READS, and it is checkable:** if the unbundling genuinely
  threatens Google, **Google pays to keep access** — expect *more* licensing deals, faster, and Google
  arguing for crawler exemptions. If it entrenches Google, **Google lets the fence go up** and competes
  on its private reserve. **Watch which one it does between now and 2026-09-15.** *(Registered as T5.)*

### ⬜ NOT-KNOWN (added)
- ⬜ **How much of Gemini's 1B MAU is paid.** Undisclosed, and the omission was noted publicly.
- ⬜ Whether Google's *training* dependence on the third-party open web is rising or falling as
  YouTube/first-party/synthetic data scale. **This decides layer 3 and nobody has published it.**
- ⬜ Actual content-licensing spend at any frontier lab as a share of training cost.
