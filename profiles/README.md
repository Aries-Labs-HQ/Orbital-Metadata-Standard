# Profiles

The core ([`STANDARD.md`](../STANDARD.md)) is what every Orbital shares: the metadata document, the attributes array, the supply surface and the membership oracle. It says nothing about how a piece's image is made, because Orbitals are made in more than one way. A **profile** is what one kind of Orbital guarantees about its image, written as a short list of requirements a reader can check against the chain.

A collection conforms to the core and to exactly one profile. Its conformance table is the core table (STANDARD §11) plus the table of its profile.

| profile | kind | status |
|---|---|---|
| [1 · Data-Rendered SVG Orbitals](data-rendered-svg.md) | the image is an SVG the collection's own contract draws from onchain data at view time | written from Aries Orbitals and measured on mainnet |
| [Ordinals-backed Orbitals](ordinals-backed.md) | the image is composed from Ordinals inscriptions the contract names | placeholder |
| [Static onchain bytes](static-onchain-bytes.md) | the image is fixed bytes written at deploy or mint and returned unchanged | placeholder |

## Proposing a profile

A profile arrives as a pull request that adds one file to this directory, and it arrives with a collection that implements it. The file states the kind in one paragraph, lists each requirement so that a conformance check is a read of the chain and not a judgment, fills in its own conformance table for that collection with the heights it was measured at, and names the collection as the reference implementation. A profile without a measured implementation stays a placeholder.

A requirement is written as **MUST** only when a live collection meets it and it can be checked from the chain. A question the authors cannot yet settle is written as **OPEN**: what the reference implementation does, the case for requiring it, the case against, and the issue where it is being discussed. An OPEN question is resolved into a MUST, or dropped, after input and the second implementation.
