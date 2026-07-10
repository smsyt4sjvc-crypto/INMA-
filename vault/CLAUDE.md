# INMA Second-Brain Vault — Operating Rules

> This file is the brain's operating system. It auto-loads whenever work happens
> inside `vault/`. Every new session: **read this file, then read `wiki/state.md`,
> then work.** The chat is ephemeral. This repo is the memory. If it isn't
> committed and pushed, it didn't happen.

This vault is Jake Bishop's persistent memory for running **INMA** (Inland
Northwest Marketing Affiliates) — clients, offers posted, contractor pipeline,
business decisions, marketing experiments, and the honest record of what worked
and what didn't. The business facts live in the repo-root `CLAUDE.md`; this vault
tracks *what is happening and what we're learning*, over time.

---

## The Firewall (non-negotiable)

Every note in `wiki/` splits its content into two labeled sections:

```
## DATA (observed)
- [YYYY-MM-DD] A measured, verifiable fact. Traced to a raw/ file or a named
  source. Numbers, quotes, dates, outcomes — things that are actually true.

## THESIS (interpretation — NOT fact)
- [YYYY-MM-DD] The read. The hypothesis. Whose read it is. Why we think it.
  Never stated as settled. This is where opinion, prediction, and strategy live.
```

- A **number never appears in THESIS as settled**. An **opinion never appears in
  DATA.** When in doubt, it's THESIS.
- Every DATA line is **dated** and **sourced** (a `raw/` filename, a person, a
  URL, a commit). No orphan facts.
- If a note is pure reference (a definition, a process), it can be all DATA — but
  the moment you interpret, that goes under THESIS.

## Corrections stay visible

When a claim turns out wrong, **never silently delete it.** Either:
- strike it through (`~~old claim~~`) in place, or
- move it to a `## Falsified` list in the note,

and add a dated correction:

```
> ⚠️ CORRECTION [YYYY-MM-DD]: <what was wrong> → <what's actually true>. Source: <...>
```

The corrected record is the most valuable content in the vault. The brain must
remember what it got wrong so it stops repeating it.

## One idea per file

A note is **one** concept, thesis, or state — not a dump. If a note is becoming a
40-bullet catch-all, split it. Write-only notes nobody retrieves from are a
failure. Small, linked, retrievable.

## Always link

Every note names its related notes with `[[wiki-links]]` (Obsidian-style, plain
text everywhere else). We are building a graph, not a pile. A note with zero
links is probably in the wrong shape.

## Date + source everything

`[YYYY-MM-DD]` prefix on every DATA line and every correction. Sources named.

## Commit + push every turn

**Any file change in `vault/` is committed with a descriptive message and pushed
before the turn ends. No exceptions.** This is the survival mechanism — a dead
container or a new session loses nothing only because the last turn pushed.
If a turn touched a file and didn't push, that's a bug in the process.

## Load persona + calibration before responding

Before answering anything in a vault working session, load
[[_persona]] (how to talk to Jake) and [[_calibration]] (Jake's bias map — what
to push back on). Pushback is tuned to `_calibration`; it only works if that file
is honest and current.

---

## Commands

- **"ingest this"** — take the pasted/attached source, save it verbatim to
  `raw/YYYY-MM-DD-short-description.md` (never edited after), then create or
  update the relevant `wiki/` note(s): split through the firewall (DATA vs
  THESIS), date every line, link related notes, and if it changes reality, update
  [[state]]. Commit + push.
- **"what do we know about X"** — answer *only* from the vault. Cite the files
  (`wiki/foo.md`, `raw/2026-…md`). If the vault is silent, say so — don't
  improvise from general knowledge and pass it off as ours.
- **"update state"** — edit `wiki/state.md` to match current reality. If it
  contradicts an existing note, correct `state.md` first, then annotate the note
  with a dated correction.
- **"what's stale"** — list DATA lines old enough to re-verify (default: flag
  anything unverified for 30+ days, plus anything in a fast-moving area), so we
  can recheck them.

---

## Domain map (INMA-specific)

Notes tend to fall into these buckets — link across them freely:
- **clients/** — homeowners in the pipeline (retained, scoping, decided).
- **offers/** — jobs posted to the board, their status, who applied.
- **contractors/** — the vetted network; credentials, standing, history.
- **decisions/** — business/positioning calls and *why* (so we don't relitigate).
- **experiments/** — marketing tests (mailers, banners, copy) and their results.
- **tools/** — the site tools (builders, board) — what's live, known issues.

`state.md` is the single canonical snapshot across all of them. Individual notes
hold the detail and the history.
