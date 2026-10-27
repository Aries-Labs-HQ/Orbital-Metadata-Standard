# Orbital Standard — a proposal for Alkanes collections

**Draft v0.3.0 · public · MIT · a proposal, not a decree.**

> **Aries Labs did not create Alkanes, and this document does not speak for the Alkanes project.** It is one team's proposal, published so that others can improve it, adopt it, or argue with it.

This proposal aims at the highest standard for NFTs on Bitcoin. The chain is the authority: image, attributes and provenance are read from the contract, never from a server. A piece is a complete document: the alkane a holder holds answers for itself. Membership is proven by the parent, never claimed by the child. Trait keys are stable: a machine `id` sits beside every display label. Aries Orbitals is the measured reference implementation; every claim made about it here was read from Bitcoin mainnet, and its gaps are listed (STANDARD §9, §11). Aries Honorary will be the second implementation.

Orbitals can be made in more than one way. The **core** ([`STANDARD.md`](STANDARD.md)) is what every kind shares: one metadata document, one attributes array, one supply surface and one membership oracle. A **profile** ([`profiles/`](profiles/)) is what one kind guarantees about its image. **Profile 1, [Data-Rendered SVG Orbitals](profiles/data-rendered-svg.md),** is the kind Aries Orbitals are: the image is an SVG the collection's own contract draws from onchain data. It was written from a live collection and measured on it. Two other kinds, [Ordinals-backed](profiles/ordinals-backed.md) and [Static onchain bytes](profiles/static-onchain-bytes.md), are named as placeholders, and a profile for them, or for a kind not listed, is welcome by PR.

*Formerly `Orbital-Metadata-Standard`; GitHub redirects the old address here.*

## The problem

Three live Alkanes collections answer the same attributes opcode with three different shapes: one flat object, and two arrays whose members disagree on keys and value types (measured, STANDARD §1). An indexer, wallet or marketplace cannot consume "an Alkanes collection" today — it has to be taught each one by hand. This proposal defines **one metadata document, one attributes array and one membership oracle** that any Orbital can implement, so that a reader who has integrated one conforming collection has integrated all of them.

## What is here

| file | What it covers |
|---|---|
| [`STANDARD.md`](STANDARD.md) | **The core.** §0 why · §1 the survey, measured · §2 principles · §3 parent views · §4 the metadata document · §5 attributes · §6 supply · §7 child views · §8 `standards` · §9 honesty section · §10 the second implementation · §11 core conformance |
| [`profiles/`](profiles/) | What a profile is and how one is proposed |
| [`profiles/data-rendered-svg.md`](profiles/data-rendered-svg.md) | **Profile 1 — Data-Rendered SVG Orbitals:** two MUSTs, two OPEN questions, its conformance table |
| [`profiles/ordinals-backed.md`](profiles/ordinals-backed.md), [`profiles/static-onchain-bytes.md`](profiles/static-onchain-bytes.md) | Placeholders |
| [`proposals/`](proposals/) | Larger changes under discussion |
| [`examples/`](examples/) | Chain answers from the reference implementation, verbatim, with how they were read |

**Reference implementation: Aries Orbitals**, Aries Labs' own collection: parent `2:98433` on Bitcoin mainnet, deployed at block 968,677, symbol `ARIESORB`. 3,000 pieces. 3,000 offered in the public round — minted out. Each piece is its own supply-1 alkane, created from the template `4:333333` in the transaction that minted it. The document was written from that contract's shipped views and is re-measured against it; where the two disagree, the document moves to the chain.

## Status, honestly

- **Draft v0.3.0.** STANDARD §1, §3, §7, Profile 1 and [`examples/`](examples/) are measured from Bitcoin mainnet. How, at which heights and through which reader is written beside each table and in [`examples/MEASURED.md`](examples/MEASURED.md).
- **The DRAFT label comes off (v1.0) when a collection conforms to the whole core and one profile, and an independent reader consumes it.** Aries Orbitals meets both MUSTs of Profile 1 but not yet the whole core; STANDARD §9 and §11 say where it falls short. An independent reader is an indexer, wallet or marketplace that Aries Labs does not run.
- **Profile 1 has two open questions**, each with its own issue. They stay open until a second implementation conforms.

## How input works

- **Weigh in on the two open questions:** [#ISSUE_A — freeze the renderer at deploy?](https://github.com/Aries-Labs-HQ/Orbital-Standard/issues/ISSUE_A) and [#ISSUE_B — declare SVG size and image-view fuel bounds?](https://github.com/Aries-Labs-HQ/Orbital-Standard/issues/ISSUE_B)
- **Open an issue** for any other question, disagreement, or hole. Every issue gets an answer.
- **Send a pull request** for a change to the text. Small, one idea per PR. A new profile arrives as a PR with a measured implementation ([`profiles/`](profiles/)).
- **Propose something larger** as a file in [`proposals/`](proposals/) — a short document with the problem, the change, and what it breaks. Discussion happens on the PR.
- **Decisions are logged.** Every accepted or declined change goes in [`CHANGELOG.md`](CHANGELOG.md) with its reason, so the record is the rationale, not just the diff.
- Aries Labs edits the document. That is the current arrangement, not a claim of authority — if other teams want to co-edit, open an issue and say so.
- **Talk to us.** Reply on X ([x.com/AriesAlkanes](https://x.com/AriesAlkanes)), or join the builders group on Telegram: https://t.me/+Ld4JmrPXPNI5ZDEx

## For readers (indexers, wallets, marketplaces)

Read STANDARD §4 and §7, then the profile the collection names. A conforming piece answers `orbital()` on its own; a conforming parent answers `orbital(index)`, `supply` and `index-of`. Membership is proven by the parent's `index-of`, never by the child's claim. Under Profile 1, a piece's image is a complete SVG that fetches nothing, and it is the same bytes at every height after the mint.

## For collection authors

Read STANDARD §2 first, then pick the profile that matches how your art is made. Ship the §4 document, the stable-keyed attributes array and the membership oracle; meet your profile's MUSTs; then fill in STANDARD §11's table and your profile's table for your collection, and every reader that consumes this proposal consumes your collection. If no profile fits, propose one.

## Contributing

Enable the secret-scan gate once per clone, before your first commit:

```
git config core.hooksPath .githooks
```

`.githooks/pre-commit` runs [`scripts/secret-scan.py`](scripts/secret-scan.py) over the staged content of every commit and refuses anything carrying a credential, a private network address or a real filesystem path. Run it by hand with `scripts/secret-scan.py --all`.

## Author and licence

Author: Aries Labs. Licensed under the [MIT License](LICENSE) — use it, fork it, implement it, no permission needed. Attribution is appreciated, not required.
