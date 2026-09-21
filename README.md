# Orbital Metadata — a proposal for Alkanes collections

**Draft v0.1 · private preview · a proposal, not a decree.**

> **Aries Labs did not create Alkanes. This is not an official Alkanes document.**

Three live Alkanes collections answer the same attributes opcode with three incompatible
shapes, so an indexer cannot consume "an Alkanes collection" today — it has to be taught each
one by hand. This document proposes one metadata document, one attributes array and one
membership oracle any Orbital can implement, so that a reader who has integrated one
conforming collection has integrated all of them.

**Worked example: Aries Orbitals. Conformance gate: this proposal publishes when Aries
Orbitals itself conforms — it is not published yet.**

---

## How to read this

Everything normative lives in [`STANDARD.md`](STANDARD.md). Its sections:

| § | What it covers |
|---|---|
| 0 | Why this exists — the incompatibility the proposal answers |
| 1 | *(owed)* the measured survey of live collections, with its controls |
| 2 | Principles — six rules the rest of the document follows from |
| 3 | The parent views — the opcode surface, what each returns and why |
| 4 | The metadata document — the single object a reader consumes |
| 5 | The attributes array — stable machine keys beside display labels |
| 6 | The supply surface — one view describing the collection's shape |
| 7 | The child views — how a piece answers for itself without its parent |
| 8 | `standards` — the contract's machine-readable account of its own token model |
| 9 | Honesty section — what the worked example does *not* yet do |
| 10 | Aries Honorary — the sibling collection's ruled naming |

Section 1 is deliberately absent rather than sketched: its numbers are measurements and
belong in the document only when they are carried over from the report that took them.

[`examples/`](examples/) will hold decoded view payloads read from a live contract. It is
empty on purpose — nothing in it is written by hand.

## Feedback

Open an issue on this repository. During the private preview that means organisation
members; the proposal is not public, and neither is this repository.

## Contributing

Enable the secret-scan gate once per clone, before your first commit:

```
git config core.hooksPath .githooks
```

`.githooks/pre-commit` then runs [`scripts/secret-scan.py`](scripts/secret-scan.py) over the
staged content of every commit and refuses anything carrying a credential, a private network
address or a real filesystem path. Run it by hand with `scripts/secret-scan.py --all`.

## Author and licence

Author: Aries Labs · Licence: see [`LICENSE`](LICENSE).
