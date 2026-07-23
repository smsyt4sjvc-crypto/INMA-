# Metered compute & agentic token demand — Jake's structural-demand thesis (April–May 2026)

Jake's original framework (predates + out-disciplines the 2026-07-21 Franklin Templeton crypto piece by 3 months).
Sources: `raw/2026-04-jake-x402-metered-compute-report.md`, `raw/2026-05-07-jake-stripe-sessions-x402-confirmation.md`.
The DEMAND side of the AI-capex cycle + the settlement layer + the value-capture discipline.
Related: [[ai-capex-cycle]], [[compression-thesis]] (the shortage-vs-glut razor), [[agentic-payments]] (settlement/FT piece),
[[ai-financing-fragility]], [[portfolio-state]].

> Firewall: DATA = Jake's sourced metrics + dated confirmations. THESIS = the structural-demand read + value-capture (Jake's).

## THE CORE THESIS (Jake, April 2026) — token demand is STRUCTURAL/GEOMETRIC, not cyclical
- The mainstream frames the compute crunch as a supply-demand LAG capex will resolve. **Jake's counter:** the demand
  explosion is the **agentic PRODUCTION layer**, not retail chat. Retail chat = token-efficient (ask→answer→close).
  **Agentic workflows spawn sub-agents; each tool call feeds the next prompt → token consumption is GEOMETRIC, runs
  24/7, and is load-bearing production infra that "does not turn off when hype cools."**
- Railroad analogy applied correctly: the speculative build creates the infra; the **freight (daily agentic token
  consumption) is the durable demand.** $700B+ capex is being built for a production layer already consuming ~15B
  tokens/min and doubling every few months.

## DATA (observed — Jake's sourced metrics, Apr 2026)
- OpenAI API: **6B tokens/min (Oct 2025) → 15B (late Mar 2026), +150% in 5mo.**
- **Anthropic API uptime DEGRADING**: 99.82% (Oct) → 98.32% (Mar) = demand exceeding physical capacity.
- Anthropic ARR: **$9B (2025) → $14B (Feb) → $30B (Apr), 3.3x in 4 months.**
- Nvidia Blackwell hourly rental **$2.75 → $4.08, +48% in 2 months**; CoreWeave +20% prices + 2029 contracts.
- Adoption: 79% orgs use AI agents; 72% of Global 2000 in OPERATIONAL (not pilot) deployment by Mar 2026.
- FinOps: 98% of practitioners manage AI spend (up from 31% in 2024) — metered token consumption = the unit of account.

## ⭐ CONFIRMED 2026-07-22 (tonight) — the shortage-not-glut read validated on GOOGL
- GOOGL CFO: plans to **EXPAND third-party capacity use in 3Q**, "modest margin pressure" — i.e. even $205B of self-build
  can't meet demand → renting is EXPENSIVE (tight). **Jake's April "structural/geometric demand" thesis is exactly why
  it's SHORTAGE, not glut.** This is the disciplined BULL counter to the compression-bear ([[compression-thesis]] razor):
  demand is real, geometric, load-bearing → supports capex being justified by revenue catching up, NOT a demand-void.
  ⚠️ Calibration: still the razor's benign branch (shortage today); the GLUT risk is future (when all capex lands at once).

## THE SETTLEMENT LAYER (x402 vs MPP; the toll)
- **x402** (Coinbase/Cloudflare/Google/Visa/AWS; IP → Linux Foundation): revives HTTP 402; agent gets a 402 w/ machine-
  readable terms → pays via **signed STABLECOIN (USDC) tx** through a facilitator → server verifies. Since May-2025:
  ~35M tx on Solana, ~$600M annualized; ~93% of activity on Base (⚠️ concentration risk). V2 = sessions, multi-chain.
- **MPP** (Stripe/Tempo, launched Stripe Sessions 2026-04-29, 288 products): merchant-facing agent settlement at scale —
  Privy (agent wallets w/ spending policy, hierarchical approval), Bridge (9+ chains, multi-stablecoin), Metronome+Tempo
  (streaming/real-time metered billing = the token-credit architecture native), Meta+Google distribution. Jake PREDICTED
  Armstrong's agentic-wallet architecture (May 2) before he stated it publicly. Standards war: x402 vs MPP, both may survive
  as different layers.

## VALUE-CAPTURE (Jake's disciplined conclusion — ahead of FT, and correct)
- *(the sequence)* **Own the physical bottlenecks NOW** (NVDA, MU, AVGO, TSM, COHR — picks-and-shovels, benefit whoever
  wins) → **position in settlement infra** as the agent economy develops (**COIN** = the primary toll, "every x402 tx
  touches Coinbase"; PYPL adjacent) → **monitor x402 tokens speculatively** (PAYAI, size for volatility). Settlement =
  STABLECOINS/USDC, NOT volatile alt coins. Same "own the toll not the barrel" as [[oil-value-chain]] / [[agentic-payments]].
- *(COIN structural edge)* USDC reserve interest income (Q1 stablecoin rev $1.35B), Circle relationship, on-chain custody
  Stripe can't duplicate. Stripe took the merchant-facing layer; COIN keeps custody/settlement. Adjacent, not overlapping.
- *(retail-exit markers — ties fragility)* SpaceX IPO, Stripe pre-IPO (288-product "narrative consolidation" = pre-S-1),
  OpenAI/Anthropic eventual IPOs, Robinhood Ventures Fund I (150k retail into private tech) = distribution to retail at the
  top. Jake tracks these as a retail-exit ledger ([[market-fragility]] distribution-to-retail pattern). Watch Tempo ownership.

## What to watch (Jake's list)
- MPP vs x402 adoption split; Stripe S-1 timing; Bridge stablecoin volume vs Coinbase USDC volume; Tempo as a separate
  vehicle; Q2-2026 = first quarter AI metered-compute revenue shows up in Stripe-customer SaaS reporting.

## 2026-07-22 ~11:57pm PT — Jake's conversion-rail thesis: the toll ON the tolls (the meta-layer)
Jake: "whoever creates the rail that can seamlessly convert coins to whatever the client uses — conversion ratios, or a
reconciliation to a system standard, transacts, converts again out the other end — will own the environment." The logical
endpoint of "own the toll," one layer up. Answers the reconciliation-constraint Jake flagged in his own May doc.
### THESIS (interpretation — Jake's, sharpened)
- *(the layer)* Not the coin/chain/protocol — the **conversion + reconciliation ABSTRACTION layer** that normalizes a
  permanently fragmented world (9+ chains, 7+ stablecoins, siloed provider credits — per Jake's May doc) into a single
  routable settlement standard, with the audit trail enterprise FinOps requires. Every M2M tx must route through it.
- *(why right — the Visa/MC pattern)* Payment value never accrues to the currency or the bank; it accrues to the RAIL
  that abstracts heterogeneity (any card↔any merchant↔any bank → interchange). Fragmentation is guaranteed, so the interop
  layer is the universal toll regardless of which coin/chain/credit-silo wins underneath.
- *(who's building it)* Stripe/**Bridge** (multi-chain multi-stablecoin conversion + Open Issuance; private/pre-IPO),
  **Circle/CRCL** (CCTP cross-chain USDC), **Coinbase/COIN** (facilitator = routing/abstraction), **Visa/MA** (co-opting
  via x402/MPP). Public expressions: CRCL, COIN, V, MA.
- *(⚠️ the seam — the MOAT, the side Jake under-weights)* The conversion SOFTWARE commoditizes — x402 → Linux Foundation
  (open standard captures nothing); open protocols are copyable. The rail "owns the environment" only if DEFENSIBLE, and
  the moat is **liquidity DEPTH + regulatory license + two-sided network effects, NOT the routing logic.** Seamless
  conversion is a balance-sheet/market-maker game (deep liquidity in every pair at tight spreads) → favors capitalized
  incumbents (Circle float, Coinbase liquidity, Visa network) over pure-tech startups. Likely an OLIGOPOLY (Visa+MC pattern),
  so "own a LANE," not "own the environment" winner-take-all.
- *(net — own the toll not the barrel, again)* The tradeable read = the capitalized incumbents building the rail (CRCL,
  COIN, V, MA, private Stripe); the barrel = the clever routing protocol anyone can copy. Value → liquidity + license +
  network, not the conversion tech. Consistent with [[oil-value-chain]] / [[where-the-edge-is]] / [[agentic-payments]].

### 2026-07-23 ~12:05am PT — the architecture: hub-and-spoke via a "system coin" (Jake solves the N² liquidity problem)
Jake: "Xx USDC = xxx system coin = x bitcoin. Operations transacted in system-coin standard, reconciled out to whatever
coin the user prefers, with a wallet acting as the hub for the conversion."
- *(what it solves)* Routing every tx through ONE system coin collapses the moat problem from **N² pairs** (every coin↔every
  coin) to **N spokes** (each coin↔system coin). This IS the FX vehicle-currency architecture (route EUR→USD→THB, not
  direct) + central-clearing (CLS/CCP net to a standard). Jake independently re-derived the proven design — and it directly
  answers the "need liquidity in every pair" objection from the 11:57pm entry.
- *(the load-bearing question — what IS the system coin)* Must be PRICE-STABLE (it's the internal accounting standard) →
  a STABLECOIN, **NOT bitcoin** (bitcoin is a SPOKE — a coin users hold/prefer — never the hub). Front-runner system coin =
  **USDC** (deepest, most-regulated, most-trusted — same reasons USD won as the FX vehicle currency). May not need inventing.
- *(who owns the system coin owns the environment — value AND risk)* Route everything through one hub coin → the ISSUER
  earns the FLOAT on all in-transit value (Circle model, CRCL ~$1.35B/qtr) AND becomes a too-big-to-fail systemic chokepoint
  (regulatory + concentration risk). Prize and danger in the same place.
- *(⚠️ remaining seams)* (1) DOUBLE conversion (in + out = two spreads) can dominate a $0.001 micropayment → each spoke
  still needs near-zero-cost deep liquidity; hub-and-spoke reduces HOW MANY spokes need it, not the per-spoke requirement.
  (2) Wallet-as-hub = the right UX layer (conversion at the edge, invisible to user) = the Privy/Stripe agent-wallet model.
- *(it's being built NOW)* Circle CCTP = "USDC as system coin across chains"; Stripe Bridge = "any coin in → normalize →
  any out." Thesis reduces to WHO WINS THE HUB = deepest/most-regulated system coin + tightest spoke liquidity → Circle
  (USDC) + Coinbase (settlement) today, Stripe (merchant side) coming hard. Same value-capture as the 11:57pm entry.

### 2026-07-23 ~10:15am PT — ⚠️ CORRECTION (Jake): CRCL/COIN are priced on CRYPTO-CYCLE + CLARITY Act, NOT agentic settlement
Jake: "CRCL and COIN are not priced for x402 or agentic transactions. They're priced for public-facing crypto / the Clarity Act."
Correct — Claude conflated THE THESIS with WHAT PRICES THE STOCK. Fixing the earlier "CRCL/COIN = the settlement toll" framing.
- *(what actually prices them)* COIN = retail crypto volume + BTC price + USDC float + the CLARITY Act (market-structure bill).
  CRCL = USDC-in-circulation × rates (~$1.35B/qtr float) + stablecoin adoption + regulation. **Down = crypto risk-off (MSTR
  −78% confirms) + CLARITY whipsaw** (digest: odds jumped >50% → "tumble right back down after new GOP draft"). Public-facing
  crypto + regulation, full stop.
- *(agentic = UNPRICED, not mispriced-down)* x402 ≈ $600M annualized TX VALUE → fee = single-digit $M vs COIN billions/qtr,
  CRCL $1.35B/qtr float = a ROUNDING ERROR. The agentic thesis has ~zero weight in the price — it's unpriced call-option
  optionality riding on a crypto-beta stock, NOT "the settlement toll on sale." Earlier "price-vs-thesis gap" framing = WRONG.
- *(the real implication — no clean vehicle)* Buying CRCL/COIN to play agentic = PRIMARY exposure is BTC + a regulatory vote;
  crypto beta + CLARITY swamp the slow-building agentic revenue for YEARS (per Jake's April data). Right thesis, dominated
  vehicle. Same "pure-play doesn't exist" problem as [[compression-thesis]] (no clean short). Agentic settlement is genuinely
  UNTRADEABLE cleanly today.
- *(practical)* Track the agentic thesis on ITS OWN metrics (x402 vs MPP adoption, Bridge vs Coinbase USDC volume, Stripe
  agentic-commerce ramp — the May watch-list), NOT the stock charts (which scream BTC/CLARITY). The volume data flags the
  conversion YEARS before the stock does. [[agentic-payments]].
