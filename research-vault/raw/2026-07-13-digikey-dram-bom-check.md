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
