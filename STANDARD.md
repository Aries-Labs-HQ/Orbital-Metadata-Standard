# Orbital Metadata — a proposal for Alkanes collections (draft v0.1, Sep 21 2026)

**Author: Aries Labs. Worked example: Aries Orbitals. Status: DRAFT v0.1, PUBLIC PROPOSAL — never a decree.** The document was written from the Aries Orbitals contract as shipped, which is therefore its reference implementation. The DRAFT label comes off when §1, §3 and `examples/` are measured from that collection's mainnet parent rather than typed. It states plainly what our own implementation does not yet do (§9).

## 0 · Why this exists

Three live Alkanes collections answer the same attributes opcode with three incompatible shapes. *(Section 1, the measured survey with its controls, is owed from the OZ-META-1 report and is not yet inlined here — the numbers must come from that report, never from memory.)* An indexer or marketplace cannot consume "an Alkanes collection" today; it consumes each one by hand. This proposal defines one document, one attributes array, and one membership oracle that any Orbital can implement and any reader can rely on.

## 2 · Principles

1. **The chain is the authority.** Image, attributes, and provenance are read from the contract. Nothing in this standard points at a server.
2. **A piece is a complete document.** The alkane a holder actually holds answers for itself — name, description, image, attributes, origin — without the reader knowing the parent.
3. **Membership is proven by the parent, never claimed by the child.** A child's collection pointer is a claim; the parent's `index-of` is the proof, because any contract can instantiate the same template.
4. **Stable trait keys.** Every attribute carries a machine `id` that never changes, beside the display `trait_type`. Renaming a display label never breaks an indexer.
5. **Traits do not exist before the mint.** A piece's traits are seeded by the transaction that mints it; the contract refuses to describe an unminted index. Rarity cannot be enumerated in advance.
6. **No dead weight.** A view that is derivable from another view, or a field that is single-valued forever, is not part of the surface.

## 3 · The parent views (Aries Orbitals, measured)

The certified source dispatches **16** opcodes on the parent: two writes (`0`, `8`) and fourteen views. All sixteen were called on mainnet. Every view answered, and both writes refused in the contract's own words, so the dispatch table on chain is the source's.

| opcode | name | args | measured answer at `2:98433` | gas |
|---|---|---|---|---|
| 0 | initialize | floor-sats, treasury-spk, auth-factory, orbital-factory | write, one-time. Refuses: `Aries Orbitals: already initialized` | — |
| 8 | public-mint | — | write. A simulate carries no transaction, so it refuses: `Aries Orbitals: no minter output found in mint tx` | — |
| 99 | get-name | — | `Aries Orbitals` | 39,743 |
| 100 | get-symbol | — | `ARIESORB` | 38,555 |
| 101 | get-total-supply | — | u128 LE: `3000` (pieces issued) | 48,960 |
| 102 | get-cap | — | u128 LE: `3000` | 39,693 |
| 1000 | get-data | index | the SVG, rendered in-contract (index 7: 5,078 B) | 3,568,461 |
| 1002 | get-attributes | index | JSON array of seven `{id, trait_type, value}`, every value a string (§5) | 100,441 |
| 1005 | minter-record | spk (length-prefixed bytes) | `{"minter", "minted", "cap", "remaining"}`, the pre-flight | 242,136 |
| 1006 | paid-of | index | u128 LE: sats paid for that piece (index 6: `3000`) | 54,492 |
| 1007 | supply | — | the supply surface (§6). The minimum donation is `mint.floor_sats` = `3000` | 125,928 |
| 1008 | orbital | index | **the metadata document** (§4), 3,135 B at index 6 | 984,391 |
| 1010 | instance-of | index | `{"index", "number", "instance": {"id", "block", "tx"}}` | 60,176 |
| 1011 | index-of | block, tx | `{"instance", "member", "index", "number"}`, **the membership oracle** | 67,571 |
| 1012 | piece-of-txid | txid (32 bytes, internal order) | `{"txid", "order": "internal", "index", "number", "instance"}` | 258,285 |
| 1013 | standards | — | the machine-readable token model (§8) | 66,490 |

**Measured absent.** `1001` (content type is a child view, §7), `103`, `104`, `1003`, `1004`, `1009`, `7`, `9`, `10` and `12` all refuse with `Unrecognized opcode`, even when four argument cells are supplied. A never-defined opcode (`4242`) refuses identically. Padding is a valid probe: `1007` with the same four extra cells answers byte-identically to `1007` with none.

**How to read a refusal on this contract.** A view called with too few arguments refuses with the **same** text as an absent opcode. `1000` with no index, `1002` with no index and `0` with no arguments all answer `Unrecognized opcode` at zero gas. The pinned codegen routes a failed argument parse to the runtime's `fallback()`, so source and chain agree. A reader cannot tell "wrong arity" from "not implemented" by the text alone. Supply the arguments, or pad, before concluding that a view is absent.

*Measured against `2:98433` at height 969,800–969,801 on 2026-10-04. Reader: SUBFROST gateway (anonymous tier), the only Alkanes reader on mainnet. Expected to transfer to any reader of the same protocol version. Every call and its control: [`examples/parent-2-98433.json`](examples/parent-2-98433.json); conditions: [`examples/MEASURED.md`](examples/MEASURED.md).*

**Removed by ruling, Sep 21 (measured absent above):** 103 and 104 (derivable from 101/102), 1003 (a subset of 1008 with an empty `traits` field) and 1004 (a single-class histogram). An Orbital implementing this proposal should not carry views whose answers can be derived from other views.

## 4 · The metadata document — `orbital(index)` / child `orbital()`

```json
{
  "name": "Aries Orbital #0014",
  "description": "One of 3,000 Aries Orbitals — generative art rendered in-contract on Bitcoin via Alkanes, seeded by its own mint transaction, with image, traits and provenance read from the chain itself. The first exhibition collection on Open Orbit.",
  "image_data": "<svg …>…</svg>",
  "content_type": "image/svg+xml",
  "attributes": [ { "id": "palette", "trait_type": "Palette", "value": "Ultraviolet" }, … ],
  "number": 14,
  "index": 13,
  "instance": { "id": "2:6762", "block": 2, "tx": 6762 },
  "origin": { "height": 4901, "txid": "669807a8…", "seed": "0xac2b…" },
  "provenance": { "identity": "<minter scriptPubKey hex>", "paid_sats": 3500 },
  "renderer": "in_contract",
  "art_version": "v9h-3000"
}
```

*The block above shows the shape. The document as the chain returns it, for piece #0007, is [`examples/metadata-document-0007.json`](examples/metadata-document-0007.json).*

- **`name`** — the title. Singular noun, `#` + zero-padded number; padding sorts correctly on every marketplace.
- **`description`** — collection-level text, a compiled constant.
- **`image_data`** — the raw SVG, byte-identical to `get-data` at the same index. This is the field the ERC-721 metadata convention already reserves for on-chain SVG; conformance and permanence in one field. There is no `image` URL, by design.
- **`origin`** — replaces `external_url`. Instead of pointing out to a server, the document points in to the chain: the block height and transaction that seeded the piece, and the seed itself.
- **`permanent_id`** — *reserved, absent here.* For Orbitals whose content builds from Ordinals inscriptions, the inscription id(s) that compose the piece.
- **`provenance`** — who minted it (as a script, never a name) and what was paid.
- **What is deliberately not here:** `external_url`, any URL at all, any field with one possible value across the collection.

## 5 · The attributes array — `get-attributes`

An array of `{ id, trait_type, value }`. `id` is the stable machine key; `trait_type` is the display label; `value` is a string. Aries Orbitals ships exactly seven, in fixed order: Palette, Ram Render, Eyes, Headwear, Accessory, Frame, Signal. The child's array is byte-identical to the parent's at its index. Number, entry class and seed are **not** attributes — they are document fields.

## 6 · The supply surface — `supply`

```json
{ "collection": "Aries Orbitals", "symbol": "ARIESORB", "art_version": "v9h-3000",
  "cap": 3000, "minted": 15, "remaining": 2985,
  "numbering": { "first": 1, "last": 3000 },
  "mint": { "floor_sats": 3000, "per_tx": 1, "per_address": 3, "initialized": true },
  "instances": { "template": "4:910921", "created": 15 } }
```

*The block above shows the shape. The live answer, with the mainnet template `4:333333`, is the `1007` row of [`examples/parent-2-98433.json`](examples/parent-2-98433.json).*

## 7 · The child views

99 name (`Aries Orbital #0001`) · 100 symbol (`ARIESORB-0001`) · 101 total-supply (always 1) · 998 collection-identifier (a claim) · 999 index · 1000 data · 1001 content-type · 1002 attributes · 1006 number · **1008 orbital (delegates to the parent at its own index).** With 1008 the child is a complete document on its own.

*Measured on #0007 (`2:98825`) and #3000 (`2:102171`): every view above answered as listed, `0 initialize` refused (`already initialized`), and an undefined opcode refused. The child's `1000`, `1002` and `1008` are byte-identical to the parent's `1008 image_data`, `1002` and `1008` at the same index. See [`examples/piece-0007.json`](examples/piece-0007.json) and [`examples/piece-3000.json`](examples/piece-3000.json).*

## 8 · `standards` — the machine-readable model

The contract describes its own token model: `piece_supply: 1`, `piece_divisible: false`, `transfer_hooks: false`, the child view numbers, the instance template, the holder-query direction, and — in its own words — that holder indexing is off-chain and non-authoritative. A reader can trust what this view says about the contract because the contract says it.

## 9 · What Aries Orbitals does not yet do (honesty section)

Each bullet stands on a row measured in §3, §7 or [`examples/`](examples/).

- **No zero-argument collection image view.** The minimum donation is readable (`1007`, `mint.floor_sats` = 3000). But the parent's `1000` requires an index, so an explorer that asks the parent for a collection image with no argument gets a revert. Children answer `1000` and `1001` normally. This is still open (proposal 0001).
- **A missing argument reads as a missing opcode.** The parent answers `1000` and `1002` without an index with `Unrecognized opcode`, the same text an absent opcode returns (§3). The contract does not override the runtime's `fallback()`, so it never says "this view needs an index".
- **Our own parent and child disagree on `1006`.** On the parent, `1006` is `paid-of(index)`: sats paid, `3000` for index 6. On the child, `1006` is `get-number`: `7` for #0007. One number means two things inside one collection. Never carry an opcode number from a parent to its children.
- **The per-address cap is per scriptPubKey.** `1005` keys its record by scriptPubKey, so a wallet that rotates addresses is uncapped. Public copy says "3 per wallet address."
- **`permanent_id` is defined here and not emitted.** The `1008` document carries twelve fields; `permanent_id` is not among them, and it is `null` in [`examples/metadata-document-0007.json`](examples/metadata-document-0007.json).
- **Section 1's survey is not yet inlined.**

## 10 · The sibling collection

A separate 333-piece Aries Honorary collection follows. It is not described here.

Tickers: **`ARIESORB`** is Aries Orbitals. **`ARIES` is reserved, unassigned.**
