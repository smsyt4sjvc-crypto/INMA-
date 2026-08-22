# wiki-brain

Markets and trading research vault. Moved out of the `INMA-` repo on 2026-08-22 so
it has its own default branch, its own Actions schedule, and no contact with the
INMA business site at inmagent.com.

Full history preserved — 1,315 commits back to the 2026-07-01 seed.

## The rulebook

`CLAUDE.md` is the operating manual. Read it before touching anything: the ingest
protocol, the evidence ladder, the DATA/THESIS firewall, amend-vs-extend, and the
recurring error classes that produced most of this vault's corrections.

## Layout

| path | what |
|---|---|
| `wiki/` | the notes — one file per thread, append-only with supersession markers |
| `wiki/_timelines/` | generated; do not hand-edit (`tools/timeline_header.py`) |
| `tools/` | the ingest gate, the fragility feed, the PDF extractor, timeline builders |
| `backtest/` | oracle backtest harness, feature tables, base-rate panels |
| `data/fragility/` | the dashboard's committed series — CSV per indicator + `latest.json` |
| `docs/` | generated dashboard page |
| `raw/` | archived source artifacts, referenced by note entries |
| `chat-log/` | dated session logs with open/closed item tracking |

## Daily

```
python3 tools/fragility_feed.py    # ~90s, refreshes 24 series
python3 tools/fragility.py         # scores them, prints the transmission ladder
```

Every inbound goes through the gate first:

```
python3 tools/librarian.py < some-file    # reads STDIN, not a path argument
```

## The fragility ladder

24 public credit/funding series scored against **their own trailing 3 years** — no
absolute thresholds anywhere. Series that trend structurally are scored on rate of
change only, because a level percentile on a trending series measures the trend, not
stress.

**A gap is not a calm row.** CDX IG/HY, swap spreads, and single-name CDS have no
free source and are listed as gaps. Two of those three are where AI-complex stress
would appear first, so the ladder reading is always a statement about the *public*
data, never about the whole market.
