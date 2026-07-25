# convoy-pricing — supplier unit prices (Hardie B&B line)

> Working price memory for takeoffs. Confirm at the counter — prices drift.

Related: [[measure-tool-product]] · [[architecture]] · [[state]]

## DATA (quoted, via Jake 2026-07-22 — Convoy, cedarmill B&B)
- [2026-07-22] Sheet 4×10 cedarmill B&B: **ColorPlus (Arctic) White $90.05** ·
  **Primed $82.95** (40 SF/sheet → 2.5 sheets per square).
- [2026-07-22] Batts 10': **ColorPlus $23.80** · **Primed $13.95**.
- ~~[2026-07-22] 5/4 trim ≈ $21.30 per 12' pc~~
  > 🔄 UPDATED [2026-07-22]: real Convoy quote came in — Hardie Trim RUSTIC
  > GRAIN, 12' pcs, 5/4 (actual widths):
  > | Size (actual) | ColorPlus Arctic White | Primed |
  > |---|---|---|
  > | 5/4×3.5 (nom ×4) | **$20.70** stock | **$18.70** stock |
  > | 5/4×5.5 (nom ×6) | **$32.50** stock | **$29.40** stock |
  > | 5/4×9.25 (nom ×10) | **$82.80 — SPECIAL ORDER, 8-wk lead** | **$49.40** stock |
  > ⚠ Wide ColorPlus (×10) = 8-week lead + ~1.7× primed price — never spec a
  > white wide band without checking lead time. **No 4/4 quoted yet.**
- [2026-07-22] ⚠ TRIM/PANEL COLOR — the accurate rule (Jake, refined). It's a
  **James Hardie factory** rule, NOT a supplier/Convoy choice:
  - HardieTrim & panels come **primed** (paintable, any color, field-finished) or
    **ColorPlus** (factory prefinished).
  - **ColorPlus is available in ANY color Hardie offers.** But **Arctic White is
    the only color Hardie paints made-to-stock (no special order)** — every other
    ColorPlus color is a factory **special-order** (added cost + lead time).
  - Suppliers stock only White for that reason; any other prefinished color on a
    shelf is an extra, a return, or someone's own special order.
  - ~~"Arctic White is the only ColorPlus trim color Convoy stocks"~~
    🔄 CORRECTED [2026-07-22]: framing it as a Convoy inventory limit was wrong —
    it's Hardie's make-to-stock rule. White = the only no-special-order color.
  - Estimate phrasing: "ColorPlus comes in any Hardie color; Arctic White is the
    only no-special-order (stock) color — others are factory special-order.
    Primed trim is field-painted to any color."
  - **Hardie "Statement Collection"** = the curated standard ColorPlus palette
    (samples in Select Cedarmill): Arctic White · Cobble Stone · Navajo Beige ·
    Khaki Brown · Timber Bark · Rich Espresso · Light Mist · Pearl Gray · Gray
    Slate · Aged Pewter · Iron Gray · Night Gray · Midnight Black · Boothbay Blue ·
    Evening Blue · Deep Ocean. (Hardie also has a broader "Dream Collection.")
    Source: [[2026-07-22-hardie-statement-collection]]. Still, all but White are
    special-order from the factory.
- [2026-07-22] Jake's stock rules: anything installed BEFORE panels = **5/4**
  (window trim, frieze, belly band, skirt); anything AFTER = **4/4** (corners).
  Belly band standard **5/4×8**; frieze = 5/4×4 ripped (buy run÷2).
  Caulk: **1 tube per square**.
- [2026-07-22] ⚠ Batt math: at 16" O.C. it's **3 batts per SHEET = 7.5 per
  square** (0.75 LF batt per SF). "3 per square" is a shorthand trap — on the
  Bauer job it hid ~$4.7k (white). Corrected per-square panels+batts:
  **$403.63 white · $312.00 primed** (vs shorthand $296.53 / $249.22).

- [2026-07-22] **ALT SIDING / lap options** (Convoy note dated 01/05/2026 —
  "call for current quote", so ~6 mo old; reconfirm before firming):
  | Material | $/pc | pcs/sq | $/sq |
  |---|---|---|---|
  | Simplank (fiber-cement lap, budget) | $8.50 | 14 | **$119.00** |
  | LP lap (SmartSide — ENGINEERED WOOD) | $13.25 | 10 | $132.50 |
  | Hardie lap, primed | $12.35 | 14 | $172.90 |
  | Hardie ColorPlus lap (Statement) | $16.75 | 14 | $234.50 |
  Simplank vs Hardie lap = **31% cheaper**. vs Hardie primed **B&B** (~$312/sq
  incl. battens) = ~62% cheaper, but it's LAP not B&B (different look; plans
  show B&B) and LP is engineered wood, not fiber cement.
  - **LP trim 5/4×4 $18.95/pc** ≈ Hardie primed 5/4×3.5 $18.70 — trim swap is a
    WASH; savings live in the siding, not the trim.
  - Accessories (same note): Tyvek 9×150' $148.75/roll · Nails $52/box · OSI
    caulk ~$8.75 · (Alderson quote 04/09 has real per-item accessory pricing:
    receptacle/light/hosebib/dryer blocks $12.50–$14, Z-flash $5.65, drip cap
    $6.05/10', OSI H2U $7.20, J-channel $6.06, soffit $26.27, fascia $21.09.)
  - **Bauer "value alternative" (Simplank + LP primed lap):** ~$25–26k, a
    ~25–28% cut from the $34,670 Hardie primed B&B — material-driven (~$8.5k
    siding), still needs field paint, shorter warranties, different style.

- [2026-07-22] **VALUE-TIER PRICING RULE (general, reusable).** A single
  cheaper-plank swap does NOT cut ~20% — the siding plank is only ~1/5 of the
  installed price (material ≈ 40–45% of job; plank ≈ half of material). So:
  - Hardie lap → Simplank, same style/finish = only **~5–7% off total**.
  - To hit ~20% you STACK downgrade steps, each ≈ **5–10% of installed**:
    ColorPlus→Primed ~5–8% (but buyer then pays a painter — not a real save,
    just moved) · Hardie→Simplank ~5% · **B&B→lap ~10–15%** (battens gone,
    material AND labor — the biggest single lever, changes the look).
  - Bauer's ~25% = primed B&B → primed Simplank LAP (batten drop did most of it),
    which is why it doesn't generalize to lap-only jobs.
  - Big levers = finish tier (ColorPlus vs primed), style (B&B vs lap), and
    labor/margin. Plank price is the SMALL lever. On an already-lap job, a real
    20% cut has to come mostly from labor/margin, not Simplank.

## IDEAS & DIRECTION
- [2026-07-22] Teach these as measure-tool presets/library entries (batt count
  from SF, per-sq caulk) so the app does this math on future B&B jobs.

## Superseded
- (none yet)
