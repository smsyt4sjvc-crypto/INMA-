#!/usr/bin/env python3
"""
fragility_html.py -- renders data/fragility/latest.json into docs/index.html
for GitHub Pages.

THE NUMBERS ARE BAKED IN AT BUILD TIME. There is no client-side fetch and that
is the whole design. A page that pulls its data with JavaScript renders EMPTY
to an agent (WebFetch converts HTML to markdown; it does not execute scripts),
so a "live" dashboard would be unreadable by the one reader who checks it daily.
Static values in the HTML are readable by a person AND by Claude, diff cleanly
in git, and need no CORS, no API key, and no server.
"""
import json, os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D    = json.load(open(os.path.join(ROOT, "data", "fragility", "latest.json")))

# dataviz skill: reserved status palette, never reused for a series hue.
SC   = {"calm": "#0ca30c", "warning": "#fab219", "serious": "#ec835a", "critical": "#d03b3b"}
GLYPH= {"calm": "●", "warning": "▲", "serious": "▲", "critical": "■"}
LBL  = {"calm": "calm", "warning": "warning", "serious": "serious", "critical": "critical"}

def spark(vals, status, w=118, h=28, pad=3):
    """One series, no legend, no axis -- the row label names it.

    A CALM row draws in neutral ink, not in the 'good' green. Painting sixteen
    quiet series green makes the page read as a reassurance; the eye should go
    to the two rows that are actually lit."""
    if not vals or len(vals) < 2:
        return '<span class="nodata">no history</span>'
    lo, hi = min(vals), max(vals)
    rng = (hi - lo) or 1.0
    n = len(vals)
    pts = [(pad + i * (w - 2 * pad) / (n - 1),
            h - pad - (v - lo) * (h - 2 * pad) / rng) for i, v in enumerate(vals)]
    col = "var(--text-muted)" if status == "calm" else SC[status]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    ex, ey = pts[-1]
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="last {n} observations, low {lo:.4g} high {hi:.4g}">'
            f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2" '
            f'stroke-linejoin="round" stroke-linecap="round"/>'
            f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="2.6" fill="{col}" '
            f'stroke="var(--surface-1)" stroke-width="1.5"/></svg>')

def chip(status, extra=""):
    return (f'<span class="chip" style="--c:{SC[status]}">'
            f'<span class="g" aria-hidden="true">{GLYPH[status]}</span>'
            f'{LBL[status]}{extra}</span>')

def num(v, unit):
    if v is None: return "—"
    if abs(v) >= 1000: return f"{v:,.0f}"
    if abs(v) >= 100:  return f"{v:,.1f}"
    return f"{v:,.2f}"

def dl(v, stress_up=True):
    """Colour by whether the move is TOWARD stress, not by its sign. Rising
    deposits are not a red number just because dealer fails rising is."""
    if v is None: return '<span class="mut">—</span>'
    toward = (v > 0) if stress_up else (v < 0)
    cls = "mut" if v == 0 else ("up" if toward else "dn")
    s = f"{v:+,.0f}" if abs(v) >= 1000 else f"{v:+,.2f}"
    return f'<span class="{cls}">{s}</span>'

lit = [l for l in D["ladder"] if l["lit"]]
worst = max((l["status"] for l in D["ladder"]), key=lambda s: list(SC).index(s))

rows_html = []
cur = None
for r in sorted(D["rows"], key=lambda x: (x["stage"] or 99, -list(SC).index(x["status"]))):
    if r["stage"] != cur:
        cur = r["stage"]
        nm = D["stages"].get(str(cur), D["stages"].get(cur, "Context — not a chain stage"))
        rows_html.append(f'<tr class="grp"><th colspan="8">'
                         f'<span class="sn">{cur if cur else "—"}</span> {escape(str(nm))}</th></tr>')
    lvl = "—" if r["level_pct"] is None else f"{r['level_pct']:.0f}"
    lvl_t = ("level percentile suppressed: this series trends, so its level is an "
             "artifact of the trend. Scored on rate of change only."
             if r["level_pct"] is None else f"{r['level_pct']:.0f}th percentile of its own 3 years")
    stale = f' <span class="stale" title="last observation {r["age_days"]}d old">STALE {r["age_days"]}d</span>' if r["stale"] else ""
    rows_html.append(f'''<tr>
<td class="nm"><b>{escape(r['label'])}</b><span class="sub">{f"chart {r['chart']} · " if r['chart'] else ""}{escape(r['note'])}</span></td>
<td class="sp">{spark(r['spark'], r['status'])}</td>
<td class="v">{num(r['value'], r['unit'])}<span class="u">{escape(r['unit'])}</span></td>
<td class="d">{dl(r['d1'], not r['inverted'])}</td>
<td class="d">{dl(r['d20'], not r['inverted'])}</td>
<td class="p" title="{escape(lvl_t)}">{lvl}</td>
<td class="p" title="percentile of the trailing 20-observation change">{'—' if r['rate_pct'] is None else f"{r['rate_pct']:.0f}"}</td>
<td class="st">{chip(r['status'])}{stale}</td></tr>''')

ladder_html = "".join(
    f'''<li class="{'lit' if l['lit'] else 'dark'}" style="--c:{SC[l['status']]}">
<span class="sn">{l['stage']}</span>
<span class="ln">{escape(l['name'])}</span>
{chip(l['status'])}<span class="cnt">{l['n_lit']}/{l['n_indep']} lit{'&nbsp;✦' if l['corroborated'] else ''}</span></li>''' for l in D["ladder"])

gaps_html = "".join(
    f'<li><b>Chart {g["chart"]} — {escape(g["name"])}</b><span class="gs">{escape(g["status"])}</span>'
    f'<span class="sub">{escape(g["why"])}</span></li>' for g in D["gaps"])

errs = D.get("feed_errors") or []
err_html = ('<p class="err">Feed errors this run: <b>' +
            escape(", ".join(e["key"] for e in errs)) +
            '</b> — those rows show the last good value and will read STALE.</p>') if errs else ""

HTML = f'''<title>Fragility Ladder</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{{--surface-0:#f6f6f4;--surface-1:#fcfcfb;--line:#e2e1dc;
--text-primary:#0b0b0b;--text-secondary:#52514e;--text-muted:#84837d;--up:#b3261e;--dn:#0f7a3d;}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{color-scheme:dark;
--surface-0:#121211;--surface-1:#1a1a19;--line:#2f2f2c;
--text-primary:#fff;--text-secondary:#c3c2b7;--text-muted:#8d8c83;--up:#f2857c;--dn:#5cc98a;}}}}
:root[data-theme="dark"]{{color-scheme:dark;--surface-0:#121211;--surface-1:#1a1a19;--line:#2f2f2c;
--text-primary:#fff;--text-secondary:#c3c2b7;--text-muted:#8d8c83;--up:#f2857c;--dn:#5cc98a;}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--surface-0);color:var(--text-primary);
font:14px/1.5 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif;
-webkit-text-size-adjust:100%}}
.wrap{{max-width:1080px;margin:0 auto;padding:28px 18px 64px}}
h1{{font-size:19px;margin:0 0 2px;letter-spacing:-.01em}}
.meta{{color:var(--text-muted);font-size:12px;margin-bottom:20px}}
.card{{background:var(--surface-1);border:1px solid var(--line);border-radius:10px;
padding:16px 18px;margin-bottom:18px}}
.verdict{{border-left:4px solid {SC[worst]};font-size:15px;font-weight:600}}
.verdict .sub{{font-weight:400;color:var(--text-secondary);font-size:13px;
display:block;margin-top:6px}}
h2{{font-size:12px;text-transform:uppercase;letter-spacing:.07em;
color:var(--text-muted);margin:0 0 12px;font-weight:600}}
ol.ladder{{list-style:none;margin:0;padding:0}}
ol.ladder li{{display:flex;align-items:center;gap:10px;padding:8px 0;
border-bottom:1px solid var(--line)}}
ol.ladder li:last-child{{border-bottom:0}}
ol.ladder li.dark{{opacity:.55}}
.sn{{flex:none;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;
font-size:11px;font-weight:700;background:var(--surface-0);border:1px solid var(--line);
color:var(--text-secondary)}}
li.lit .sn{{background:var(--c);border-color:var(--c);color:#fff}}
.ln{{flex:1;min-width:0}}
.cnt{{flex:none;color:var(--text-muted);font-size:12px;width:78px;text-align:right;
font-variant-numeric:tabular-nums}}
.chip{{display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;
color:var(--c);white-space:nowrap}}
.chip .g{{font-size:9px;line-height:1}}
.scroll{{overflow-x:auto}}
table{{border-collapse:collapse;width:100%;min-width:760px}}
th,td{{text-align:right;padding:9px 8px;border-bottom:1px solid var(--line);
font-variant-numeric:tabular-nums}}
thead th{{font-size:11px;text-transform:uppercase;letter-spacing:.05em;
color:var(--text-muted);font-weight:600;border-bottom:1px solid var(--line)}}
td.nm,th.nm,tr.grp th{{text-align:left}}
tr.grp th{{padding-top:18px;font-size:12px;color:var(--text-secondary);
font-weight:600;border-bottom:0}}
tr.grp .sn{{display:inline-grid;margin-right:6px;vertical-align:middle}}
.nm b{{font-weight:600}}
.sub{{display:block;color:var(--text-muted);font-size:11.5px;margin-top:1px}}
.v{{font-weight:600}}
.u{{color:var(--text-muted);font-weight:400;font-size:11px;margin-left:4px}}
.up{{color:var(--up)}}.dn{{color:var(--dn)}}.mut{{color:var(--text-muted)}}
.p{{color:var(--text-secondary);font-size:12.5px}}
td.st{{white-space:nowrap}}
.stale{{font-size:10px;font-weight:700;color:var(--surface-1);background:var(--text-muted);
border-radius:3px;padding:1px 4px;margin-left:5px}}
.spark{{display:block}}
td.sp{{width:126px;padding:4px 8px}}
.nodata{{color:var(--text-muted);font-size:11px}}
ul.gaps{{list-style:none;margin:0;padding:0}}
ul.gaps li{{padding:9px 0;border-bottom:1px solid var(--line)}}
ul.gaps li:last-child{{border-bottom:0}}
.gs{{font-size:10.5px;font-weight:700;color:var(--text-muted);margin-left:8px;
text-transform:uppercase;letter-spacing:.04em}}
.err{{color:{SC['serious']};font-size:12.5px;margin:0}}
p.note{{color:var(--text-secondary);font-size:12.5px;margin:0 0 8px}}
code{{background:var(--surface-0);border:1px solid var(--line);border-radius:4px;
padding:1px 5px;font-size:12px}}
</style>
<div class="wrap">
<h1>Credit &amp; debt fragility ladder</h1>
<p class="meta">Generated {escape(D["generated"][:16].replace("T", " "))} · every number
baked in at build time, no client-side fetch · scored against each series&rsquo; own 3-year history</p>

<div class="card verdict">{escape(D["verdict"])}
<span class="sub">Stress is supposed to migrate <b>downward</b> through these stages.
A single lit stage is a repricing. Stages lighting <b>in order</b> is the chain.
<b>n/N lit</b> counts the independent series in a stage at warning or worse — a stage with
eight series has eight chances to light and one with a single series has one, so the count
is shown rather than hidden. <b>✦ = corroborated</b> (two or more independent series agree).</span></div>

<div class="card"><h2>Transmission ladder</h2><ol class="ladder">{ladder_html}</ol></div>

<div class="card"><h2>Indicators</h2>
<p class="note">Change columns are in <b>observations, not days</b> — a weekly series&rsquo;
&ldquo;1p&rdquo; is one week. <b>lvl%</b> is the percentile of today&rsquo;s value within its own
3 years; it is shown as &ldquo;—&rdquo; for series that trend structurally, where a level
percentile measures the trend rather than stress. <b>rate%</b> is the percentile of the
trailing 20-observation change.</p>
<div class="scroll"><table>
<thead><tr><th class="nm">Indicator</th><th>120 obs</th><th>Value</th>
<th>chg 1p</th><th>chg 20p</th><th>lvl%</th><th>rate%</th><th>Status</th></tr></thead>
<tbody>{"".join(rows_html)}</tbody></table></div>{err_html}</div>

<div class="card"><h2>Known gaps — not in the data above</h2>
<p class="note">These are named so an empty row is never mistaken for a calm one.</p>
<ul class="gaps">{gaps_html}</ul></div>

<div class="card"><h2>Method</h2>
<p class="note"><b>No absolute thresholds anywhere.</b> Every indicator is ranked against its
own trailing three years, on level and on 20-observation rate of change. Status is
<code>critical</code> at level ≥95th <i>and</i> rate ≥80th; <code>serious</code> at level ≥90th
<i>or</i> rate ≥95th; <code>warning</code> at level ≥75th <i>or</i> rate ≥85th. Trending and
inverted series are scored on rate alone. Bank C&amp;I loans and deposits are inverted —
for those, <b>contraction</b> is the stress.</p>
<p class="note">A series that merely restates another (the CCC-minus-HY gap is arithmetic on
CCC and HY) is shown and scored but <b>excluded from the corroboration count</b>, so CCC is not
counted twice. Derived and cross-bank series are held to like-for-like seasonal adjustment:
large-bank C&amp;I is computed as domestically-chartered minus small, both <b>not</b> seasonally
adjusted, because the seasonally-adjusted small-bank series was discontinued in 2018.</p>
<p class="note">Sources, all keyless: FRED public graph CSV · NY Fed markets API ·
TreasuryDirect auction API · Yahoo (^MOVE). Rebuilt daily by GitHub Actions; the raw
series live in <code>data/fragility/series/*.csv</code>.</p></div>
</div>'''

os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
p = os.path.join(ROOT, "docs", "index.html")
open(p, "w").write(HTML)
print(f"wrote {p}  ({len(HTML):,} bytes, {len(D['rows'])} indicators, "
      f"{len(lit)} stage(s) lit, worst={worst})")
