# Orbital Metadata — a proposal for Alkanes collections

**Draft v0.1 · public · MIT · a proposal, not a decree.**

> **Aries Labs did not create Alkanes. This is not an official Alkanes document.** It is one team's proposal, published so that others can improve it, adopt it, or argue with it.

## The problem

Three live Alkanes collections answer the same attributes opcode with three incompatible shapes. An indexer, wallet or marketplace cannot consume "an Alkanes collection" today — it has to be taught each one by hand. This proposal defines **one metadata document, one attributes array and one membership oracle** that any Orbital can implement, so that a reader who has integrated one conforming collection has integrated all of them.

## What is here

Everything normative lives in [`STANDARD.md`](STANDARD.md):

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
| 10 | Aries Honorary — the sibling collection's naming |

**Worked example: Aries Orbitals**, Aries Labs' own collection. The document was written from that contract's shipped views, so it is the reference implementation.

## Status, honestly

- **Draft v0.1.** The shape is settled; the measurements are not all in the repository yet.
- **§1 is deliberately absent rather than sketched.** Its numbers are measurements and belong here only when they are carried over from the report that took them.
- **§3's opcode table is being re-derived byte-exact from the certified contract.** Until that lands, read it as descriptive. One row is already known to be wrong: `1001` (content type) is answered by each child, not by the parent.
- **[`examples/`](examples/) is empty on purpose.** It will hold decoded view payloads read from a live contract; nothing in it is written by hand.
- **The DRAFT label comes off (v1.0) when §1, §3 and `examples/` are measured from the collection's mainnet parent.** An independent reader — an indexer, wallet or marketplace Aries Labs does not run — consuming a conforming collection is the milestone after that.

## How input works

- **Open an issue** for a question, a disagreement, or a hole. Every issue gets an answer.
- **Send a pull request** for a change to the text. Small, one idea per PR.
- **Propose something larger** as a file in [`proposals/`](proposals/) — a short document with the problem, the change, and what it breaks. Discussion happens on the PR.
- **Decisions are logged.** Every accepted or declined change goes in [`CHANGELOG.md`](CHANGELOG.md) with its reason, so the record is the rationale, not just the diff.
- Aries Labs edits the document. That is the current arrangement, not a claim of authority — if other teams want to co-edit, open an issue and say so.

## For readers (indexers, wallets, marketplaces)

Read §4 and §7. A conforming piece answers `orbital()` on its own; a conforming parent answers `orbital(index)`, `supply` and `index-of`. Membership is proven by the parent's `index-of`, never by the child's claim.

## For collection authors

Read §2 first. If your contract renders in-chain, §4's `image_data` is the field; if it composes from inscriptions, `permanent_id` is reserved for you (§4). Ship the seven-field document, the stable-keyed attributes array, and the membership oracle, and every reader that consumes this proposal consumes your collection.

## Contributing

Enable the secret-scan gate once per clone, before your first commit:

```
git config core.hooksPath .githooks
```

`.githooks/pre-commit` runs [`scripts/secret-scan.py`](scripts/secret-scan.py) over the staged content of every commit and refuses anything carrying a credential, a private network address or a real filesystem path. Run it by hand with `scripts/secret-scan.py --all`.

## Author and licence

Author: Aries Labs. Licensed under the [MIT License](LICENSE) — use it, fork it, implement it, no permission needed. Attribution is appreciated, not required.
