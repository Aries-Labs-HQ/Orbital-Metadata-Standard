# Orbital Metadata — a proposal for Alkanes collections (draft v0.1, Sep 21 2026)

**Author: Aries Labs. Worked example: Aries Orbitals. Status: PROPOSAL — never a decree.** Publication gate: this document publishes when Aries Orbitals itself conforms, as measured by OZ-SCHEMA-1's re-proof. Until then it is an internal draft. It states plainly what our own implementation does not yet do.

## 0 · Why this exists

Three live Alkanes collections answer the same attributes opcode with three incompatible shapes. *(Section 1, the measured survey with its controls, is owed from the OZ-META-1 report and is not yet inlined here — the numbers must come from that report, never from memory.)* An indexer or marketplace cannot consume "an Alkanes collection" today; it consumes each one by hand. This proposal defines one document, one attributes array, and one membership oracle that any Orbital can implement and any reader can rely on.

## 2 · Principles

1. **The chain is the authority.** Image, attributes, and provenance are read from the contract. Nothing in this standard points at a server.
2. **A piece is a complete document.** The alkane a holder actually holds answers for itself — name, description, image, attributes, origin — without the reader knowing the parent.
3. **Membership is proven by the parent, never claimed by the child.** A child's collection pointer is a claim; the parent's `index-of` is the proof, because any contract can instantiate the same template.
4. **Stable trait keys.** Every attribute carries a machine `id` that never changes, beside the display `trait_type`. Renaming a display label never breaks an indexer.
5. **Traits do not exist before the mint.** A piece's traits are seeded by the transaction that mints it; the contract refuses to describe an unminted index. Rarity cannot be enumerated in advance.
6. **No dead weight.** A view that is derivable from another view, or a field that is single-valued forever, is not part of the surface.

## 3 · The parent views (Aries Orbitals as shipped after OZ-SCHEMA-1)

| opcode | name | returns | role |
|---|---|---|---|
| 99 | get-name | string | collection name — `Aries Orbitals` |
| 100 | get-symbol | string | `ARIESORB` (ruled Sep 21; `ARIES` deliberately left free) |
| 101 | get-total-supply | u128 | pieces issued |
| 102 | get-cap | u128 | hard cap, immutable |
| 1000 | get-data(index) | svg | the image, rendered in-contract |
| 1001 | get-content-type | string | `image/svg+xml` |
| 1002 | get-attributes(index) | json | the attributes array (§5) |
| 1005 | minter-record(spk) | json | per-address count and cap — **the pre-flight** |
| 1006 | paid-of(index) | u128 | sats paid to the treasury for this piece |
| 1007 | supply | json | the supply surface (§6) |
| 1008 | orbital(index) | json | **the metadata document** (§4) |
| 1010 | instance-of(index) | json | index → child alkane id |
| 1011 | index-of(block, tx) | json | child alkane id → index; **the membership oracle** |
| 1012 | piece-of-txid(txid) | json | mint transaction → piece |
| 1013 | standards | json | the machine-readable token model (§7) |

**Removed by ruling, Sep 21:** 103, 104 (derived from 101/102), 1003 (a subset of 1008 with an empty `traits` field), 1004 (single-class histogram). An Orbital implementing this proposal should not carry views whose answers are derivable from others.

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

## 7 · The child views

99 name (`Aries Orbital #0001`) · 100 symbol (`ARIESORB-0001`) · 101 total-supply (always 1) · 998 collection-identifier (a claim) · 999 index · 1000 data · 1001 content-type · 1002 attributes · 1006 number · **1008 orbital (delegates to the parent at its own index).** With 1008 the child is a complete document on its own.

## 8 · `standards` — the machine-readable model

The contract describes its own token model: `piece_supply: 1`, `piece_divisible: false`, `transfer_hooks: false`, the child view numbers, the instance template, the holder-query direction, and — in its own words — that holder indexing is off-chain and non-authoritative. A reader can trust what this view says about the contract because the contract says it.

## 9 · What Aries Orbitals does not yet do (honesty section)

- The minimum donation is an initialize parameter with no view that reads it back; readers infer it from refusals.
- The per-address cap is per scriptPubKey; a wallet rotating addresses is uncapped. Public copy says "3 per wallet address."
- `permanent_id` is defined here and emitted by no contract yet.
- Section 1's survey is not yet inlined.

## 10 · Aries Honorary (sibling collection, separate contract, no deadline) — ruled naming

- `name`: `Aries Honorary: <headpiece text>` — e.g. `Aries Honorary: ᛒᚱᚨᚷᛁ`.
- `description` (operator text, verbatim and ruled final Sep 21): *Aries Honorary: ᛒᚱᚨᚷᛁ is one of 333 custom pieces designed by the top donors who believed in Alkanes builders plus all the OG's who made programmable assets on Bitcoin a reality. These Legendary 1/1's are the first of their kind, rendered in-contract on Bitcoin via Alkanes.* — per-piece, with the name substituted.
- `symbol`: **`ARIESHON`** (operator-ruled Sep 21; "OG" stays reserved for the builder registry). Per-piece suffix format is the Honorary lane's to define.
- Tickers overall: **`ARIESORB`** (public round) · **`ARIESHON`** (Honorary) · **`ARIES` is reserved, unassigned, for a possible future token.**
