# Changelog

All accepted and declined changes, with reasons. Newest first.

## v0.2.1 — accuracy pass, measured 2026-10-27 at block 973,316
Every claim was measured against the live parent `2:98433`, its children and the Aries build, and the document moved to the chain wherever they differed. The DRAFT label stays.
- **Every row re-read**, each call pinned to block 973,316 through the SUBFROST gateway (anonymous tier), with a positive control on every target:
  - §3: the parent's sixteen opcodes, measured beside children #0002 (`2:98728`) and #0862 (`2:100000`). The source ≠ chain diff is empty, and every answer, refusal text and gas figure is unchanged. Both writes still refuse in the contract's own words.
  - §1: all six survey pieces and both parents' `1002` answers are byte-identical at identical gas.
  - `examples/`: the parent and #0007 files regenerate with no payload difference, and `metadata-document-0007.json` regenerates byte-identical. The files are unchanged; `MEASURED.md` gains the v0.2.1 call list.
- **§3:** the index/number convention is stated once (index 861 is #0862). `998` and `999` are added to the parent's measured-absent list, and `1008` to the views that refuse `Unrecognized opcode` without an index. Reason: measured, and missing from v0.2.
- **§7:** the child list becomes a measured table on #0002 and #0862. It now gives `998` (the string `2:98433`) and `999` (the zero-based index), which v0.2 named without their answers. It also lists the views a child does not answer. Reason: the v0.2 list gave no measured values for these rows.
- **Transfer semantics are regime-neutral** in §7 and proposals 0002 and 0003: a piece moves only under a protostone; a spend without one destroys the piece or carries it to an output the spender did not choose; neither can be undone. Reason: the v0.2 wording named only one outcome of a spend without a protostone.
- **§1:** adds the sentence "the only true incompatibility is object vs array". The Oyly parent's probe set is widened, and Oyly membership stays corroborated, not proven, because no parent view names a child.
- **§9:** every bullet was re-verified at 973,316. Two gaps are added:
  - the document's `origin.txid` is in display order while `1012` wants internal order and answers nulls, not a refusal;
  - `1013` carries no transfer declaration.
- **§10:** now reads "Aries Honorary will be the second implementation." The reservation of an unassigned ticker is removed. Reason: no ticker is named for a contract that is not deployed.
- **§11 Conformance** is added: Aries Orbitals against each principle and required view, ✓ or gap, with heights. It is the table a second collection fills in.
- **README reframed:** the opening states the purpose in one paragraph, names Aries Orbitals as the measured reference implementation, and adds the build facts measured from the chain (deployed at block 968,677; template `4:333333`; one supply-1 child per piece). It adds a way to reach us. "Seven-field document" is corrected to "the §4 document", which has twelve fields.
- **Proposal 0003:** stays a direction. Its status now says that an atomic-swap venue for Orbitals exists (Open Orbit) and that the fill rules match what such a venue must check. Reason: its old status read as if Orbitals had nowhere to trade.
- **Copy:** the hyphenated spelling in §4 becomes "onchain".

## v0.2 — measured
- **§1 re-measured** on 2026-10-04 through the SUBFROST gateway (anonymous tier), the only Alkanes reader on mainnet. The subjects:
  - Alkane Pandas `2:614` (pieces `2:615`, `2:616`) and Oyly `2:10672` (pieces `2:15635`, `2:15636`), at height 969,896;
  - Aries Orbitals `2:98433` (pieces #0007 `2:98825` and #3000 `2:102171`), at 969,800–969,801.

  The v0.1 survey's third subject was an earlier Aries Labs deployment, since closed and superseded; it is replaced by the live collection. The three-shapes claim is re-established, and now stated exactly: one flat object, and two arrays whose members disagree on keys and value types. A lenient `trait_type`/`value` reader reads both arrays, so "incompatible" is now said only of object vs array.
- **§3 re-derived from the certified source** (aries-collection `7bb11eb`) **and verified against mainnet.**
  - Source vs chain findings: **none**. Sixteen opcodes are dispatched: fourteen views that all answered, plus `0 initialize` and `8 public-mint`, which refuse in the contract's own words.
  - The v0.1.1 caveat "at least two parent views missing" was wrong. No view was missing; the two opcodes the table lacked are the writes `0` and `8`.
  - Measured absent: `1001`, `103`, `104`, `1003`, `1004`, `1009`, `7`, `9`, `10`, `12`.
  - A view called without its index refuses with `Unrecognized opcode`, the same text as an absent opcode.
- **§7:** both children measured. Their `1000`, `1002` and `1008` are byte-identical to the parent's answers at the same index.
- **`examples/` filled from `2:98433`:** the parent, pieces #0007 and #3000, the §4 document for #0007 (12 fields answered; `permanent_id` null), and `MEASURED.md`. The old regtest placeholder note is gone.
- **§9 re-checked** against the measurement. Every bullet now cites a measured row, and the "§1 not yet inlined" bullet is gone. Added: a missing argument reads as a missing opcode; `1006` means paid-of on the parent and number on the child.
- **Proposals 0002 (transfer semantics) and 0003 (listing format)** added. The index lists 0001–0003; 0001 is open, with no file yet.
- **Copy sweep:**
  - the status line is now "3,000 pieces. 3,000 offered in the public round — minted out.";
  - the README disclaimer no longer uses the retired phrasing;
  - §10 is reduced to "A separate 333-piece Aries Honorary collection follows." The Sep 21 naming rulings are withdrawn from the public draft, and the sibling ticker is dropped;
  - §4 and §6 examples now point at their measured counterparts.

## v0.1.1 — public
- Repository made public under MIT. README rewritten for public input (issues, PRs, proposals/, this log).
- STANDARD.md status line corrected: public draft, not an internal one; the v1.0 gate is measurement from the mainnet parent.
- §3: `1001` removed from the parent table — it is a child view (measured against the certified bytecode). Parent opcode count measured at 16 vs 15 listed; re-derivation owed.
- §9: first bullet corrected — the minimum donation is readable via opcode 1007; the open item is a zero-argument collection image view.

## v0.1 — internal draft (Sep 21)
- First complete draft: principles, parent views, metadata document, attributes array, supply surface, child views, `standards`, honesty section, sibling-collection naming (withdrawn in v0.2).
- Removed by ruling: opcodes 103, 104, 1003, 1004 (derivable from others).
