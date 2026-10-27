# Profile 1 — Data-Rendered SVG Orbitals

**Status: part of draft v0.3.0. Written from Aries Orbitals and measured on Bitcoin mainnet at block 973,327.** A collection that conforms to this profile also conforms to the core ([`STANDARD.md`](../STANDARD.md)).

## Purpose

In a Data-Rendered SVG Orbital the image is a computation, not a file. The collection's own contract draws each piece as an SVG at view time, from data the chain already holds: the piece's seed, its traits and the renderer's code. Nothing is hosted, nothing is fetched, and nothing sits behind a URL; a reader that calls the image view gets the finished picture. This profile states what such a collection guarantees, so that a reader can check it with a byte scan and a comparison of hashes.

## The two requirements

### MUST 1 — Self-contained

The bytes a piece's image view returns (the child's `1000`, and `image_data` in its `1008` document) MUST be one complete SVG document that renders without fetching anything. A conformance check is a byte scan, case-insensitive:

- the bytes are UTF-8, open with `<svg` (after an optional XML declaration) and close with `</svg>`;
- no `href` or `xlink:href` has a value other than a `#` fragment, so a `<use>` points only inside the document;
- no `url(` has an argument other than a `#` fragment;
- none of `<script`, `@import`, `<foreignObject` or `<image` appears;
- no `http:`, `https:`, `ipfs:` or `ar:` scheme appears anywhere, except inside an `xmlns` namespace declaration such as `xmlns="http://www.w3.org/2000/svg"`, which is an identifier and is never fetched.

### MUST 2 — Deterministic per piece

A piece's image view MUST return byte-identical bytes at every height from the piece's mint block on. A conformance check reads the image at two or more pinned heights after the mint and compares hashes.

## Two open questions

These are not requirements. Each states what Aries Orbitals does, as measured, and the case each way. Neither is required of a conforming collection while it is open.

### OPEN 1 — Renderer frozen at deploy

**What Aries Orbitals does, as measured.** Every read is pinned to block 973,327 unless a height is named; conditions: `net-mainnet` · `reader-subfrost-anon` · `pinned-block-973327`.

- The `1008` document of #0002, #0007 and #0862 carries `"renderer": "in_contract"` and `"art_version": "v9h-3000"`. The parent's `1007` carries the same `art_version` and `"instances": {"template": "4:333333", "created": 3000}`.
- The parent's `1013` names `"instance_template": "4:333333"`: every piece is an instance of that template. The template itself, asked `99`, refuses `Aries Orbitals: not initialized`.
- No view in the parent's table (STANDARD §3) or the child's (STANDARD §7) names a renderer version other than `art_version`, an upgrade authority, or a proxy relation. `1007` and `1013` were read in full for this; neither carries such a field.
- The parent's `initialize` (`0`), called with four cells, refuses `Aries Orbitals: already initialized`. The refusal names no authority.
- The alkane `2:98434`, created beside the parent, answers `99` with `AUTH AlkaneId { block: 2, tx: 98433 }`, and refuses `101` with `Unrecognized opcode`. No view of the parent and no refusal read here states what this token authorizes.
- #0002's image is byte-identical at its mint block 969,028, at 973,227 and at 973,327 (MUST 2, below).

**Measurable and not measured here:** who holds `2:98434`. **Not measurable from views:** whether the parent's code can be replaced, and what `2:98434` authorizes. No view states either; deciding them needs the contract's code and the protocol's rules for replacing it.

**The case for requiring it.** A frozen renderer makes MUST 2 a property of the contract and not only an observation of its past. A holder's piece cannot be redrawn after the mint by anyone, the deployer included, and a reader can cache an image by its hash for good.

**The case against.** A renderer that cannot change cannot be repaired: a drawing defect found after the mint stays in every piece. Freezing may not be checkable from views alone, which would make this the one requirement a reader cannot check by reading the chain. And MUST 2 already exposes any change, because a redrawn piece fails the hash comparison.

**Open question — weigh in: [issue #ISSUE_A](https://github.com/Aries-Labs-HQ/Orbital-Standard/issues/ISSUE_A).** Resolved into MUST or dropped after input and the second implementation.

### OPEN 2 — Bounds declared

**What Aries Orbitals measures.** Thirty pieces (listed below), every read pinned to block 973,327. Conditions: `net-mainnet` · `reader-subfrost-anon` · `pinned-block-973327`. Fuel figures are per indexer build.

| view | bytes min · median · max | fuel min · median · max |
|---|---|---|
| child `1000` (image) | 1,661 · 3,707.5 · 6,471 | 433,086 · 692,944.5 · 3,968,557 |
| child `1002` (attributes) | 418 · 434 · 446 | 186,833 · 188,140.5 · 189,048 |

No view of the collection declares a bound: the parent's `1007` and `1013` answers carry no size or fuel field.

**The case for requiring it.** Across these thirty pieces the image view's fuel spans almost a factor of ten, so one piece does not predict the next. A declared bound lets an indexer or wallet budget fuel and memory before it calls, and refuse a piece that exceeds what the collection promised.

**The case against.** Fuel is per indexer build, so a fuel figure written into a deployed contract goes stale when the indexer changes, and the contract cannot correct it. Size can be measured by any reader in one pass over the collection. A declared number that the chain can contradict sits awkwardly beside the core's first principle, that the chain is the authority.

**Open question — weigh in: [issue #ISSUE_B](https://github.com/Aries-Labs-HQ/Orbital-Standard/issues/ISSUE_B).** Resolved into MUST or dropped after input and the second implementation.

## Conformance

| requirement | Aries Orbitals (`2:98433`) | measured by |
|---|---|---|
| MUST 1 — Self-contained | ✓ 30 of 30 pieces pass the byte scan. Every reference in them is a `#` fragment, and the only scheme is the SVG namespace declaration. | child `1000` on 30 pieces, `pinned-block-973327` |
| MUST 2 — Deterministic per piece | ✓ #0002, #0007 and #0862: the image and the attributes are byte-identical at 973,227 and at 973,327; #0002's image is also identical at its mint block 969,028 | child `1000` and `1002` at each height |
| OPEN 1 — Renderer frozen at deploy | n/a — open | facts above |
| OPEN 2 — Bounds declared | n/a — open | facts above |

*Conditions: `net-mainnet` · `reader-subfrost-anon` · `pinned-block-973327` (and `pinned-block-973227`, `pinned-block-969028` where named) · subject: Aries Orbitals, minted out. The checker that caught a planted control in the same run: #0862's image with one `<image href="https://…">` injected fails the scan, and #0002's image hash differs from #0862's.*

## Reference implementation

**Aries Orbitals**, parent `2:98433` on Bitcoin mainnet. Measured on 30 pieces at block 973,327: #0002 (`2:98728`), #0007 (`2:98825`) and #0862 (`2:100000`), plus 27 pieces drawn at random (seed `20261027`) from the ids between #0002 and #3000 and kept only where the parent's `1011 index-of` answered `member: true`.

| piece | id | image bytes | image fuel | image sha256 (first 16) |
|---|---|---|---|---|
| #0002 | `2:98728` | 4,751 | 3,476,658 | `0b037de3d7cf4bff` |
| #0007 | `2:98825` | 1,826 | 435,726 | `4d29318406d6c1cc` |
| #0862 | `2:100000` | 6,333 | 1,417,626 | `f93e26862951bc10` |
| #0008 | `2:98843` | 5,078 | 3,701,297 | `7a398f69e22ab336` |
| #0041 | `2:99144` | 2,373 | 446,676 | `1898110980d1817f` |
| #0156 | `2:99260` | 4,400 | 1,028,040 | `9af220d19961b4d7` |
| #0251 | `2:99356` | 3,319 | 649,315 | `cee936a3d8a63f22` |
| #0319 | `2:99438` | 2,429 | 480,733 | `7cd10bd277b42566` |
| #0377 | `2:99498` | 5,478 | 3,672,601 | `77cddfda0b5d7c84` |
| #0389 | `2:99510` | 2,584 | 581,443 | `fe0cf4522faecc8d` |
| #0429 | `2:99551` | 1,661 | 433,086 | `ba51452c1e49f9c4` |
| #0456 | `2:99578` | 2,991 | 582,762 | `3b2a40637f9980a5` |
| #0539 | `2:99661` | 3,972 | 710,645 | `94524aae42604333` |
| #0561 | `2:99683` | 3,760 | 938,375 | `ae57bb4ec615e363` |
| #0650 | `2:99777` | 3,454 | 650,470 | `a03c8a6c98bf0318` |
| #1166 | `2:100306` | 3,409 | 644,995 | `876b4a56c46611d6` |
| #1259 | `2:100403` | 5,346 | 1,062,923 | `4a2482662ebe74cf` |
| #1306 | `2:100451` | 5,701 | 3,968,557 | `74c186e6c2bc013a` |
| #1312 | `2:100457` | 4,442 | 3,400,240 | `542221d750421da3` |
| #1359 | `2:100504` | 5,453 | 1,104,143 | `b784258b294e45a1` |
| #1600 | `2:100748` | 3,940 | 551,316 | `af2bfffbf1c154e6` |
| #1609 | `2:100757` | 3,655 | 675,244 | `b6b50ba25edf307e` |
| #1853 | `2:101001` | 3,466 | 3,384,138 | `bbfd8f7b6fb5962d` |
| #2031 | `2:101182` | 5,114 | 3,820,281 | `52cad7410e5b3be5` |
| #2458 | `2:101619` | 4,207 | 3,462,304 | `e8d49fa5b274b849` |
| #2552 | `2:101715` | 6,471 | 1,447,302 | `b12692e88752dcdd` |
| #2613 | `2:101777` | 2,294 | 496,793 | `211c97da19dd2f36` |
| #2745 | `2:101911` | 2,873 | 604,568 | `11141befe95d7856` |
| #2875 | `2:102041` | 2,196 | 453,555 | `e20d994b54781b80` |
| #2933 | `2:102101` | 3,063 | 507,705 | `d98c380763e6c95d` |

*Conditions: `net-mainnet` · `reader-subfrost-anon` · `pinned-block-973327` · subject: the child alkane named in each row. Fuel figures are per indexer build.*

Aries Honorary will be the second implementation.
