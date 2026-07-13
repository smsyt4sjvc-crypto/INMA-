# Jake's DigiKey memory BOM check (PDF upload, list saved 2026-07-13 10:48am)
15-line basket of server DDR5 RDIMMs across all three makers. Result: EXTENDED PRICE $0.00 —
nothing purchasable.
- **Micron modules (5 SKUs: 64GB/32GB/16GB DDR5 RDIMMs, MTC40F/MTC36F/MTC20F/MTC10F...):
  listed but marked OBSOLETE, "No Backorders Allowed," quantities force-altered to availability
  (= zero).** These ARE DigiKey catalog items — the allocation has been pulled from distribution.
- Kingston KSM48R40: one match found (no price captured in export).
- **Samsung (M321R...) and SK Hynix (HMCG...) part numbers: "Exact match not found"** — not in
  the catalog at all.
- ⚠️ Caveats: DigiKey is not the primary server-RDIMM channel (hyperscalers buy direct); OEM part
  numbers (Samsung/Hynix) often never sit in distribution; "obsolete" can be part-revision churn.
  The strong reading is about DISTRIBUTION STARVATION, not absolute market supply.

## Full-table update (Jake paste, ~12:15pm PT)
- **Kingston KSM48R40 also OBSOLETE → basket is 15/15 dead** (6 obsoleted listings + 9 delisted).
- Micron rows = catalog husks: no price, no stock, ROHS "Unknown," no tariff/HTSUS data.
- Kingston row: Taiwan origin, "US import tariff: may apply" — the memory-tariff watch item
  visible in catalog metadata.
- ⚠️ SENSOR FLAW FIXED: obsolete SKUs never restock — a fixed basket of EOL'd parts reads dark
  forever. The LIVING gauge = DigiKey parametric search ("DDR5 RDIMM, in stock"): record the
  IN-STOCK SKU COUNT + median unit price monthly (today ≈ 0). Shelf relights = shortage breaking.
  Consumer leg: Newegg 32GB DDR5 UDIMM kit, in-stock count + price, same cadence.

## The LIVE datapoint (Jake, ~12:30pm PT): Advantech SQR-RD5N96G5K6SRUB
- 96GB DDR5-5600 RDIMM, part status ACTIVE, available-to-order (NOT stocked; 8-wk mfr lead),
  **$9,829.74/unit = $102.39/GB.**
- Context math: pre-shortage server DDR5 ≈ $3-5/GB (a 96GB RDIMM ~$300-450). Consumer shortage
  pricing (vault, 7/01): 32GB DDR5 $80→$375 ≈ $11.7/GB (~3-4x). **This listing = ~20-30x
  pre-shortage, ~9x above even consumer-shortage pricing.**
- ⚠️ Channel caveat: Advantech = industrial/embedded reseller — low-volume desperate-buyer pricing
  with fat markup, NOT maker contract pricing. That's the point: this is the MARGINAL,
  UNCONTRACTED buyer's price — the spot end of the two-tier market.
- **SENSOR BASELINE SET: server-DRAM spot-distribution = $102/GB, 8-wk lead, zero stock
  (2026-07-13).** The turn = this class compressing toward ~$5-15/GB and/or stock reappearing.
- *(vault connection — the receipt for GEHC's guidance cut)* WHO buys through this channel:
  industrial/medical equipment makers — imaging systems, test gear — the uncontracted buyers.
  Hammack's "will pay almost any price" has a shelf tag now, and the GEHC "$250M inflation-driven
  costs / DRAM casualty" mechanism has its receipt: the hyperscalers pay LTA contract prices;
  the GEHCs of the world pay $102/GB spot.
