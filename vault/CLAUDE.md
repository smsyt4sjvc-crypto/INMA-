# INMA Second-Brain Vault — Operating Rules

> This file is the brain's operating system. It auto-loads whenever work happens
> inside `vault/`. Every new session: **read this file, then read `wiki/state.md`,
> then work.** The chat is ephemeral. This repo is the memory. If it isn't
> committed and pushed, it didn't happen.

This vault is the persistent memory for **INMA** (Inland Northwest Marketing
Affiliates) — the **evolution of the business, the brand, the ideas, and the
running architecture** of the site and tools. It's not a debate engine and not a
task tracker; it's a place where INMA's thinking and build accrete over time so
no session starts from zero. The fixed business facts live in the repo-root
`CLAUDE.md`; this vault tracks *how INMA is growing and what we've figured out.*

---

## The Firewall (keep memory honest)

Every note in `wiki/` separates **what is true now** from **what we're thinking**,
so a future session never reads last month's idea as an established fact:

```
## DATA (what's true now)
- [YYYY-MM-DD] A real, verifiable thing — live tool, shipped decision, actual
  number, something that happened. Dated, and traced to a raw/ file or named
  source.

## IDEAS & DIRECTION (thinking — not yet fact)
- [YYYY-MM-DD] A direction we're considering, a concept, an evolution of the
  brand or model, a "maybe next." Clearly a thought, not a settled fact.
```

- A **shipped fact never sits under IDEAS as if pending**; an **idea never sits
  under DATA as if done.** When in doubt, it's an idea.
- Every DATA line is **dated** and **sourced** (a `raw/` file, a person, a URL, a
  commit). No orphan facts.
- Pure-reference notes (the brand system, a definition) can be all DATA. The
  moment it's a direction or a maybe, it goes under IDEAS & DIRECTION.

## Corrections stay visible

When something we recorded stops being true — a tool changes, an idea is dropped,
a decision reverses — **don't silently delete it.** Strike it through
(`~~old~~`) or move it to a `## Superseded` list, and add a dated note:

```
> 🔄 UPDATED [YYYY-MM-DD]: <what changed> → <what's true now>. Source: <...>
```

The history of how INMA evolved *is* the value. We keep the trail.

## One idea per file

A note is **one** thing — a concept, a decision, a system, a state. Not a dump.
If a note is turning into a 40-bullet catch-all, split it. Small, linked,
retrievable beats one write-only megafile.

## Always link

Every note names its related notes with `[[wiki-links]]`. We're building a graph
of how INMA's pieces connect, not a pile of pages.

## Date + source everything

`[YYYY-MM-DD]` on every DATA line and every update. Sources named.

## Commit + push every turn

**Any change in `vault/` is committed with a descriptive message and pushed before
the turn ends.** This is the survival mechanism — a dead container or a fresh
session loses nothing only because the last turn pushed.

## Load persona + guardrails before responding

Before working a vault session, load [[_persona]] (how I work with Jake) and
[[_guardrails]] (INMA's voice + the liability lines that must never be crossed),
so everything we write and generate stays on-brand and on-message.

---

## Commands

- **"ingest this"** — save the pasted/attached source verbatim to
  `raw/YYYY-MM-DD-short-description.md` (never edited after), then create/update
  the relevant `wiki/` note(s): split into DATA vs IDEAS & DIRECTION, date every
  line, link related notes, and if it changes the picture, update [[state]].
  Commit + push.
- **"what do we know about X"** — answer *only* from the vault, cite the files.
  If the vault is silent on it, say so rather than improvising.
- **"update state"** — edit `wiki/state.md` to match reality now. If it
  contradicts a note, fix `state.md` first, then annotate the note with a dated
  update.
- **"what's stale"** — list DATA old enough to re-check (default 30+ days, plus
  anything in a fast-moving area).

---

## Domain map (INMA)

Notes tend to fall into these buckets — link across them freely:
- **architecture** — the running technical system: repo, hosting, tools, data
  flows, integrations. See [[architecture]].
- **brand** — voice, visual system, positioning, the say-this / never-say lines.
  See [[brand]] · [[_guardrails]].
- **model** — how INMA actually operates and makes money. See [[positioning]].
- **offers / clients / contractors** — the live pipeline as it fills in.
- **decisions** — calls made and *why*, so we don't relitigate them.
- **experiments** — marketing tests (mailers, banners, copy) and what they did.
- **evolution** — the running log of how INMA and its tools have changed. See
  [[evolution]].

`state.md` is the single canonical snapshot; individual notes hold the detail and
the history.
