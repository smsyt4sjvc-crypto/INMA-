# INMA — Business Context & Brand Brief

> Drop this file into a Claude Project (as a knowledge file or in custom instructions) to give any chat the full context of the business. For a specific customer, add a short customer note on top of this. If placed in a code repo as `CLAUDE.md`, Claude Code reads it automatically.

---

## 1. The Business in One Line

**INMA (Inland Northwest Marketing Affiliates)** is a *homeowner advocacy* service run by **Jake Bishop** in **Spokane, WA**. Jake is **not a contractor** — he's a **buyer's agent for exterior remodeling projects**. He represents the homeowner, prices the job to fair market, and presents *their offer* to a network of vetted local contractors. His fee comes out of the contract price, not added on top.

- **Owner:** Jake Bishop
- **Title (short):** Homeowner Advocate
- **Title (descriptive):** Your Personal Homeowner Advocate
- **Location:** Spokane, WA · serves the Inland Northwest
- **Phone/text:** (509) 251-7792
- **Email:** jake@inmagent.com
- **Web:** inmagent.com
- **License:** WA UBI #606 027 063
- **Background:** 25+ years residential construction; ran his own siding company in Spokane 2018–2023; 14 years installing windows (last 5 as lead installer for a local manufacturer).

---

## 2. The Positioning (the core idea)

Jake is the **buyer's agent / insurance agent** for a remodel. The analogy that lands best:

> "Think of it like an insurance agent. You hire them, they shop the market, and the insurance company pays them a commission out of the deal. Same model here — except my fee comes out of the project budget, not tacked on top. Your total cost stays the same. You just get someone in your corner."

**The value flip / "leverage, hindsight ahead of time":** a homeowner only remodels a few times in their life; contractors sell every day. That asymmetry is why homeowners get burned. INMA gives the homeowner a repeat-player on their side — the experience and leverage of someone who does this daily, applied *before* the mistake instead of as hindsight after.

**Who he protects them from (two distinct pains):**
1. The **national-brand salesman** who flew in this week and can't tell you why one product beats another.
2. The **new local "installer"** hiding behind a $200 state license — good intentions, no business experience, often runs out of cash mid-job.

---

## 3. The Money Model

- **Fee: 10–15% of the total project cost, depending on scope complexity.**
- **Deducted from the contract price — comes out of the contractor's number, not added on top.** The homeowner's total cost does not increase.
- Paid to INMA at signing; covers advocacy + coordination only, **never construction**.
- INMA **never collects, holds, or disburses construction funds.** All construction payments go directly from homeowner to contractor under a separate agreement.
- **Fair-market pricing is verifiable** — the estimate is anchored to real fair-market data the homeowner can check themselves. Framing: *"Cheapest isn't best. Most expensive isn't best. You get what you pay for — and an advocate makes sure you actually get it."*

---

## 4. Ways to Work With INMA

1. **DIY Assistance** — coaching for the hands-on homeowner. From $250 initial visit · $250/week unlimited support · $75/visit additional house calls.
2. **Standalone Proposal** — Jake scopes + prices it; homeowner shops it themselves. Flat fee.
3. **Full Scope** — the complete buyer's-agent service: scope, fair-market pricing, vetted contractor match, coordination through the job.
4. **Home Tune-Up** — *Inspect · Seal · Clean · Report.* A checkup of exterior systems (roofing, siding, windows, doors, paint) with complete remaining-lifespan reporting + full thermal scan to find energy loss. Year-round (not seasonal). ~$750.

---

## 5. Verbiage Rules — SAY THIS

- "I'm not a contractor. I'm your personal homeowner advocate."
- "Like a buyer's agent for your project. I work for you, not the crew doing the work."
- "You make the offer. **INMA presents it as your offer** to our network of vetted local crews. They accept your terms or they pass."
- "My fee comes out of the contract price — deducted dollar-for-dollar, in front of you. Not added on top."
- "Fair-market pricing you can verify yourself."
- "Vetted local crews, no kickbacks, no ad budget buried in your quote."
- "Hire the right guy, the first time." / "No phone tag. No surprise costs. No hiring twice."
- Home Tune-Up strapline: **"Inspect · Seal · Clean · Report."**

## 6. Verbiage Rules — NEVER SAY THIS (liability + brand)

- ❌ **"We handle the match, scope, and accountability"** / "we control the work" / anything implying INMA is responsible for construction outcomes. This creates **general-contractor liability**. INMA coordinates and advocates; the licensed contractor is responsible for the work.
- ❌ "I shred my estimate" / "uniform contract" — sounds shady and implies GC control.
- ❌ "We'll beat any quote by 20% guaranteed" — softened to "I can very often reduce these by around 20%."
- ❌ Seasonal-only language for tune-ups ("Spring tune-up") — it's **year-round**.
- ❌ Presenting the estimate as a binding contractor bid. It's an **estimate of fair-market cost** and the homeowner's **offer**.

**Standard disclosure line (use verbatim where a disclaimer is needed):**
> "INMA is not a contractor. INMA presents this as your offer to our network of vetted local crews as an advocate for our clients. This is an estimate of fair-market cost for the scope described above."

---

## 7. Voice & Tone

- Punchy, plainspoken, blue-collar-premium. Pacific Northwest craftsman.
- Confident but not salesy or hype-y. Honest about tradeoffs.
- "Trusted local expert," not "tech startup." Avoid corporate-speak, neon, and exclamation-point hype.

---

## 8. Brand / Visual System

**Palette:**
- Warm Black (bg): `#1C1A17`
- Brand Gold (primary): `#B8941F`
- Deep Bronze (accent): `#8B6914`
- Warm Cream (text/light): `#F5F2ED`
- Sage Green (secondary): `#6B7F5E`
- Warm Card Brown: `#2C2A27`

**Type:** Outfit (sans) + DM Serif Display (display serif). Google Fonts.
**Logo:** hand-painted white bear on red (`bear-logo.jpg`). Warm, grounded, premium-but-approachable.
**Vibe note for image generation:** dark warm-brown backgrounds, hand-painted gold accents, cream text. Avoid corporate blue, neon, pure black.

---

## 9. The Website & Tools (inmagent.com)

Static site on GitHub Pages (main branch), Vercel for the AI quote-analysis functions, GA4 analytics.

**Public pages:** `index.html` (home), `work.html` (portfolio), `market-report.html` (Spokane fair-market pricing), `diy.html`, `consult.html`, `game.html`, `welcome` (mailer QR landing), `upload.html` (quote upload/contract audit).

**Internal tools (savable to home screen as PWAs):**
- `estimate.html` — **Estimate Builder** (icon E) — the current 2-page builder. Generates an estimate + a branded lined notes page (page 2).
- `field-estimate.html` — older Field Estimator (icon I) with photos + contractor pack.
- `service-agreement.html` — **Service Agreement builder** with updated advocate language, **on-screen signature pads** (sign with finger → Print/Save PDF → text it), Import from Contacts.
- `estimate-blank.html` — blank **Fair Market Estimate** form to print and fill by hand on-site.
- `/agreement.html` redirects to `service-agreement.html` (old duplicate retired).

**Side projects (unlisted, noindex):**
- `ioss.html` — Jake's policy proposal (Increased Output Share Structure).
- `sim.html` — "Reality Check" economic policy simulator.
- `/showcase/` — client-site demos Jake builds to sell (e.g. Right Now Exteriors, Elliott Elite Detailing).

**Client-site business:** Jake also builds simple sites for other local businesses. Model: he builds it (often first as a live demo under `/showcase/`), the client owns it once they pay (own GitHub repo + domain), Jake holds credentials for easy management unless they ask for them.

---

## 10. Contact Block (for documents/footers)

**INMA** · Inland Northwest Marketing Affiliates · Spokane, WA · WA UBI #606 027 063
(509) 251-7792 · jake@inmagent.com · inmagent.com
