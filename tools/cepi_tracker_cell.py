# ═══════════════════════════════════════════════════════════════════════════
#  CEPI TRACKER v1 — the running E/C ratio
#  Capex → Earnings → Price Intensity, instrumented.   Built 2026-08-07 (Jake's spec)
#
#  Paste into Colab and run. Zero dependencies. Add ONE BLOCK per company-quarter
#  as earnings land — the series builds itself.
#
#  WHY FOUR RATIOS AND NOT ONE:
#   E/C   = net income / capex .......... Jake's ask. GAAP profit per $ of capex.
#   OCF/C = operating cash flow / capex . THE LINE THAT MATTERS. <1.00 = the company
#                                         is NOT self-funding its buildout. (FCF<0 ⟺ OCF/C<1)
#   C/R   = capex / revenue ............. intensity (SpaceX 2.35x vs MSFT ~0.7x)
#   DA/C  = D&A / capex ................. the CATCH-UP ratio. Near 0 = the capex wave
#                                         has not hit the P&L yet. Toward 1.0 = it has.
#
#  ⚠️ THE TRAP E/C ALONE WALKS INTO: earnings are AFTER depreciation, so as the
#  2024-26 wave starts depreciating, E/C falls for TWO reasons at once (capex up AND
#  earnings down). DA/C is what separates them. Never read E/C without it.
#
#  ⚠️ THE OTHER TRAP — FINANCE LEASES. Headline "capex" from a press release often
#  EXCLUDES finance-lease additions, which is where a lot of AI infrastructure sits.
#  Use the CASH FLOW STATEMENT line + the lease footnote. (The vault already caught
#  one stale-by-$132B figure this way: MSFT $196.6B vs $329.1B.)
# ═══════════════════════════════════════════════════════════════════════════

# ── DATA ───────────────────────────────────────────────────────────────────
# $ MILLIONS, per QUARTER. None = not yet in hand (the cell reports coverage).
# ADD A LINE PER FILING. That is the whole maintenance burden.
FILINGS = [
    # ticker  quarter    revenue  capex    net_inc  op_cash_flow  ebitda   D&A    source
    dict(tkr="SPCX", q="2026Q2", rev=7814,  capex=18369, ni=None, ocf=None, ebitda=3538, da=None,
         src="segment table 8/4 (ZH-confirmed to the dollar); NI + OCF NOT disclosed"),

    # ── SEEDS THE VAULT HOLDS ONLY AS FRAGMENTS — fill from the 10-Q and delete the note ──
    # dict(tkr="GOOGL", q="2026Q2", rev=None, capex=None, ni=None, ocf=None, ebitda=None, da=None,
    #      src="KNOWN: first NEGATIVE-FCF quarter since the 2004 IPO ⇒ OCF/C < 1.00; capex guide 'up to $205B' FY26"),
    # dict(tkr="MSFT",  q="2026Q2", ...),   # vault comparator: capex/revenue ~0.7x
    # dict(tkr="ORCL",  q="2026Q2", ...),   # vault comparator: capex/revenue ~1.0x; FY FCF −$23.69B
    # dict(tkr="AMZN",  q="2026Q2", ...),
    # dict(tkr="META",  q="2026Q2", ...),
]

# Independent AGGREGATE cross-check: GS/FactSet combined FCF for META+MSFT+GOOGL+AMZN+ORCL
# ($bn/qtr, chart-read 8/6 — approximate). Combined FCF < 0  ⟺  combined OCF/C < 1.00.
GS_COMBINED_FCF_BN = {"2024Q2": 104, "2026Q1": 57, "2026Q3E": -20, "2027E": -25, "2029Q3E": 122}

ORDER = ["C/R", "E/C", "OCF/C", "DA/C"]

# ── ENGINE ─────────────────────────────────────────────────────────────────
def r(a, b):
    """Ratio with None-safety. Returns None if either side is missing or denom is 0."""
    if a is None or b is None or b == 0:
        return None
    return a / b

def fmt(x, w=7, dp=2):
    return ("—".rjust(w) if x is None else f"{x:,.{dp}f}".rjust(w))

def ratios(f):
    return {
        "C/R":   r(f["capex"], f["rev"]),
        "E/C":   r(f["ni"],    f["capex"]),
        "OCF/C": r(f["ocf"],   f["capex"]),
        "DA/C":  r(f["da"],    f["capex"]),
    }

print("=" * 78)
print("  CEPI TRACKER — E/C and the self-funding line".center(78))
print("=" * 78)

if not FILINGS:
    print("\n  No filings loaded.\n")
else:
    # ── PER-FILING ──
    print(f"\n{'TKR':<7}{'QUARTER':<10}" + "".join(k.rjust(8) for k in ORDER) + "   COVERAGE")
    print("-" * 78)
    for f in sorted(FILINGS, key=lambda x: (x["q"], x["tkr"])):
        R = ratios(f)
        have = sum(1 for k in ORDER if R[k] is not None)
        print(f"{f['tkr']:<7}{f['q']:<10}" + "".join(fmt(R[k], 8) for k in ORDER) + f"   {have}/4")
    print("-" * 78)

    # ── DOLLAR-WEIGHTED AGGREGATE, BY QUARTER ──
    print("\n  DOLLAR-WEIGHTED AGGREGATE (sum the dollars, then divide — not an average of ratios)")
    print(f"\n{'QUARTER':<10}" + "".join(k.rjust(8) for k in ORDER) + "   n covered (of filings that qtr)")
    print("-" * 78)
    for q in sorted({f["q"] for f in FILINGS}):
        rows = [f for f in FILINGS if f["q"] == q]
        def tot(key):
            vals = [f[key] for f in rows if f[key] is not None]
            return sum(vals) if vals else None
        def pair(num_key):
            """Sum numerator and capex ONLY over filings that have both — no mixed baskets."""
            ok = [f for f in rows if f[num_key] is not None and f["capex"] is not None]
            if not ok:
                return None, 0
            return sum(f[num_key] for f in ok) / sum(f["capex"] for f in ok), len(ok)
        cr, n_cr = pair("rev")
        cr = r(sum(f["capex"] for f in rows if f["capex"] is not None and f["rev"] is not None),
               sum(f["rev"] for f in rows if f["capex"] is not None and f["rev"] is not None)) \
             if n_cr else None
        ec,  n_ec  = pair("ni")
        ocf, n_ocf = pair("ocf")
        da,  n_da  = pair("da")
        print(f"{q:<10}" + fmt(cr, 8) + fmt(ec, 8) + fmt(ocf, 8) + fmt(da, 8)
              + f"   {n_cr}/{n_ec}/{n_ocf}/{n_da} of {len(rows)}")
    print("-" * 78)

    # ── WHAT IS MISSING — the cell tells you what to fetch ──
    print("\n  🚩 MISSING LINE ITEMS (fetch these; each closes one cell above)")
    gaps = {}
    for f in FILINGS:
        for k, label in [("rev", "revenue"), ("capex", "capex (CF stmt + finance leases)"),
                         ("ni", "net income"), ("ocf", "operating cash flow"), ("da", "D&A")]:
            if f[k] is None:
                gaps.setdefault(f"{f['tkr']} {f['q']}", []).append(label)
    if gaps:
        for who, items in gaps.items():
            print(f"    {who:<16} → " + ", ".join(items))
    else:
        print("    none — full coverage.")

print("\n" + "=" * 78)
print("  READING IT")
print("=" * 78)
print("""
  OCF/C = 1.00  is THE THRESHOLD. Above it the buildout is self-funded out of the
                business. Below it, every marginal dollar comes from a bond desk or
                a share sale — which is the state the vault documented on 8/6
                (Google's first negative-FCF quarter since its 2004 IPO, and the
                GS chart showing all five hyperscalers COMBINED going negative).

  E/C  falling  is ambiguous ALONE. Decompose it:
                  DA/C rising  → the old capex is hitting the P&L (mechanical, expected)
                  DA/C flat    → earnings are deteriorating for a REAL reason
                That distinction is the difference between a depreciation wave and
                a demand problem, and E/C alone cannot see it.

  C/R           intensity. Vault comparators: SPCX 2.35x · ORCL ~1.0x · MSFT ~0.7x.
                Nothing else in the vault's table has been above ~1x.
""")
print("  GS/FactSet combined-FCF cross-check ($bn/qtr, chart-read — sign is what matters):")
for k, v in GS_COMBINED_FCF_BN.items():
    print(f"    {k:<9} {v:>6}   {'← COMBINED NEGATIVE (OCF/C < 1.00 across the complex)' if v < 0 else ''}")
print("=" * 78)
