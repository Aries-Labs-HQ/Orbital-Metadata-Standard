# Changelog

All accepted and declined changes, with reasons. Newest first.

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
