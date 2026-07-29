# financing-tool — home-screen loan-application front door

> Idea (2026-07-22): an HTML/home-screen app — same style as [[measure-tool-product|Wall Measure]] —
> that lets a contractor's customer apply for home-improvement financing through
> a LOCAL lender directly, cutting the third-party middleman (Hearth/GreenSky).
> Sparked by Tricia (loan officer, new, in Jake's network) asking about it.

Related: [[architecture]] · [[measure-tool-product]] · [[state]]

## DATA (what's true now)
- [2026-07-22] Contractors today pay third-party apps (Hearth, GreenSky) a
  monthly/per-deal fee to offer on-the-spot financing → the customer goes to a
  national call center, contractor pays for the privilege.
- [2026-07-22] Tricia = a loan officer in Jake's network, willing to help; the
  natural compliance/lender partner for a pilot.

## IDEAS & DIRECTION (thinking — not yet fact)
- [2026-07-22] Concept: branded "apply for financing" front-door tool + a
  payment/what-if calculator (down payment, term, collateral) → routes the
  customer into the LOCAL lender's real application. Contractor looks pro,
  customer gets a local human, nobody pays a third party.
- [2026-07-22] **Compliance realities (flag before building):**
  1. App is NOT the lender — it hands off to the licensed lender's compliant
     application. Payment slider must be labeled ESTIMATES, not a binding quote.
  2. Paid loan-referral = anti-kickback exposure (RESPA §8 mortgages; CFPB/state
     otherwise). Cleanest = FREE tool, nobody pays for leads (also a better pitch).
  3. Financial PII (SSN/income/DOB) canNOT live in browser localStorage like the
     measure app — must go through the lender's secure/encrypted system. App
     collects minimal sensitive data; pushes to lender for the rest.
  4. Loan type drives the rules: unsecured home-improvement loans vs mortgage/
     HELOC are different regimes. Confirm which Tricia does.
- [2026-07-22] Right architecture = sharp, free front door into a licensed
  lender + estimate calculator. NOT a DIY origination system. Tricia = compliance
  brain; Jake = tech + contractor network.

## Superseded
- (none yet)
