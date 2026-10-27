# Orbital Metadata — a proposal for Alkanes collections

**Draft v0.2.1 · public · MIT · a proposal, not a decree.**

> **Aries Labs did not create Alkanes, and this document does not speak for the Alkanes project.** It is one team's proposal, published so that others can improve it, adopt it, or argue with it.

This proposal aims at the highest standard for NFTs on Bitcoin. The chain is the authority: image, attributes and provenance are read from the contract, never from a server. A piece is a complete document: the alkane a holder holds answers for itself. Membership is proven by the parent, never claimed by the child. Trait keys are stable: a machine `id` sits beside every display label. Aries Orbitals is the measured reference implementation; every claim made about it here was read from Bitcoin mainnet, and its gaps are listed (§9, §11). Aries Honorary will be the second implementation.

## The problem

Three live Alkanes collections answer the same attributes opcode with three different shapes: one flat object, and two arrays whose members disagree on keys and value types (measured, §1). An indexer, wallet or marketplace cannot consume "an Alkanes collection" today — it has to be taught each one by hand. This proposal defines **one metadata document, one attributes array and one membership oracle** that any Orbital can implement, so that a reader who has integrated one conforming collection has integrated all of them.

## What is here

Everything normative lives in [`STANDARD.md`](STANDARD.md):

| § | What it covers |
|---|---|
| 0 | Why this exists — the incompatibility the proposal answers |
| 1 | The survey — three live collections, measured on mainnet with their controls |
| 2 | Principles — six rules the rest of the document follows from |
| 3 | The parent views — the opcode surface, measured on mainnet |
| 4 | The metadata document — the single object a reader consumes |
| 5 | The attributes array — stable machine keys beside display labels |
| 6 | The supply surface — one view describing the collection's shape |
| 7 | The child views — how a piece answers for itself without its parent |
| 8 | `standards` — the contract's machine-readable account of its own token model |
| 9 | Honesty section — what the worked example does *not* yet do |
| 10 | Aries Honorary — the second implementation |
| 11 | Conformance — Aries Orbitals against every principle and required view; the table the next collection fills in |

**Reference implementation: Aries Orbitals**, Aries Labs' own collection: parent `2:98433` on Bitcoin mainnet, deployed at block 968,677, symbol `ARIESORB`. 3,000 pieces. 3,000 offered in the public round — minted out. Each piece is its own supply-1 alkane, created from the template `4:333333` in the transaction that minted it. The document was written from that contract's shipped views and is re-measured against it; where the two disagree, the document moves to the chain.

## Status, honestly

- **Draft v0.2.1.** §1, §3, §7 and [`examples/`](examples/) are measured from Bitcoin mainnet. v0.2.1 re-measured every row at block 973,316, and every row matched. How, when and through which reader is written down in [`examples/MEASURED.md`](examples/MEASURED.md).
- **The DRAFT label comes off (v1.0) when a collection conforms to the whole surface and an independent reader consumes it.** Aries Orbitals does not yet; §9 and §11 say where it falls short. An independent reader is an indexer, wallet or marketplace that Aries Labs does not run.

## How input works

- **Open an issue** for a question, a disagreement, or a hole. Every issue gets an answer.
- **Send a pull request** for a change to the text. Small, one idea per PR.
- **Propose something larger** as a file in [`proposals/`](proposals/) — a short document with the problem, the change, and what it breaks. Discussion happens on the PR.
- **Decisions are logged.** Every accepted or declined change goes in [`CHANGELOG.md`](CHANGELOG.md) with its reason, so the record is the rationale, not just the diff.
- Aries Labs edits the document. That is the current arrangement, not a claim of authority — if other teams want to co-edit, open an issue and say so.
- **Talk to us.** Reply on X ([x.com/AriesAlkanes](https://x.com/AriesAlkanes)), or join the builders group on Telegram: https://t.me/+Ld4JmrPXPNI5ZDEx

## For readers (indexers, wallets, marketplaces)

Read §4 and §7. A conforming piece answers `orbital()` on its own; a conforming parent answers `orbital(index)`, `supply` and `index-of`. Membership is proven by the parent's `index-of`, never by the child's claim.

## For collection authors

Read §2 first. If your contract renders onchain, §4's `image_data` is the field; if it composes from inscriptions, `permanent_id` is reserved for you (§4). Ship the §4 document, the stable-keyed attributes array and the membership oracle, then fill in §11's table for your collection, and every reader that consumes this proposal consumes your collection.

## Contributing

Enable the secret-scan gate once per clone, before your first commit:

```
git config core.hooksPath .githooks
```

`.githooks/pre-commit` runs [`scripts/secret-scan.py`](scripts/secret-scan.py) over the staged content of every commit and refuses anything carrying a credential, a private network address or a real filesystem path. Run it by hand with `scripts/secret-scan.py --all`.

## Author and licence

Author: Aries Labs. Licensed under the [MIT License](LICENSE) — use it, fork it, implement it, no permission needed. Attribution is appreciated, not required.
