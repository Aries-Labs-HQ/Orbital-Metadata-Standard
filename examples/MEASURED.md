# How `examples/` was measured

Nothing in this directory was typed. Every value was read from Bitcoin mainnet and decoded by a script from the bytes the reader returned.

## Conditions

| | |
|---|---|
| network | Bitcoin mainnet |
| reader | SUBFROST gateway, `https://mainnet.subfrost.io/v4/jsonrpc`, **anonymous tier** (no key; 20 calls/min) |
| method | `alkanes_simulate [{target:{block,tx}, inputs:[opcode, args…]}, "latest"]`; `metashrew_height` for heights |
| heights | 969,800–969,896 (`metashrew_height` read before and after each batch) |
| date | 2026-10-04, 05:07–20:38 UTC |
| pacing | ≥ 3.1 s between calls |
| gateway calls | **114** in total, every one logged (method, params, raw response) |
| subjects | `examples/`: parent `2:98433`; children #0007 `2:98825` and #3000 `2:102171`. §1 survey: Alkane Pandas `2:614` (`2:615`, `2:616`), Oyly `2:10672` (`2:15635`, `2:15636`) |

## The limitation that cannot be removed today

Mainnet has **one** Alkanes reader, so these answers were not cross-checked against a second, independent reader. Instead, every view call was preceded by a **positive control on the same contract in the same minute**: `99 get-name`, a view known to answer. A refusal is reported only beside a control that answered, so "reverts" is a measured verdict and never a silent reader. Each row in the JSON files names its control (`positive_control.ledger_call`). Two rows first landed outside the one-minute window (child `0` at +60 s, parent `0` with four arguments at +123 s). Both were re-measured inside a fresh window, and the files carry the re-measurement.

`alkanes_simulate` returns no height, so `height_window` is a bracket: the first number is a lower bound on the state that answered.

## Controls that make a refusal mean something

- **Undefined opcode.** `4242` on the parent and on both children refuses `Unrecognized opcode`. That is the absent-opcode answer.
- **`1000` without an index, beside `1000` with one.** Without an index, the parent refuses with the same `Unrecognized opcode`. With index 7, it returns a 5,078-byte SVG.
- **Padding.** `1007` with four extra argument cells answers byte-identically to `1007` with none, so a padded call that still refuses is a measured absence (`1001`, `103`, `104`, `1003`, `1004`, `1009`, `7`, `9`, `10`, `12`).

## Files

| file | what | sha256 |
|---|---|---|
| [`parent-2-98433.json`](parent-2-98433.json) | every parent view, the two writes, the absent numbers and the controls; each with opcode, args, raw hex, decoded value, gas, height window | `e658aef0690a86f97c9ec240a098bbd265cb2fd890038caf4ff1803cb7c7ee62` |
| [`piece-0007.json`](piece-0007.json) | every child view of #0007; `image_data` is the SVG exactly as `1000` returned it, with its sha256 | `a69c8e3119982f08dca6c3bcaa6370084b73021370addc3f52b8b31d0f596021` |
| [`piece-3000.json`](piece-3000.json) | the same for #3000 | `9410424e1e3b9169664c3fcfc3c6348bc5ebe7f95e0a7e69ddf5101c09920620` |
| [`metadata-document-0007.json`](metadata-document-0007.json) | the §4 document: the child's `1008` answer verbatim (byte-identical to the parent's `1008(6)`), plus `permanent_id: null`, the one §4 field the contract does not answer | `89d995b683053587ab9cb74e9bdb7149eca556c32c9e22cd3187499b1463bb3f` |

## The calls

In order. `n` is the call's number in the run's ledger. Calls 1–76 measured §3, §7 and the files above; calls 77 onward measured the §1 survey.

| n | UTC | method | target | inputs | verdict |
|---|---|---|---|---|---|
| 1 | 05:07:10 | `metashrew_height` | — | — | 969800 |
| 2 | 05:07:13 | `alkanes_simulate` | `2:98433` | `99` | DATA, 14 B |
| 3 | 05:07:17 | `alkanes_simulate` | `2:98433` | `100` | DATA, 8 B |
| 4 | 05:07:21 | `alkanes_simulate` | `2:98433` | `101` | DATA, 16 B |
| 5 | 05:07:25 | `alkanes_simulate` | `2:98433` | `102` | DATA, 16 B |
| 6 | 05:07:29 | `alkanes_simulate` | `2:98433` | `1007` | DATA, 275 B |
| 7 | 05:07:32 | `alkanes_simulate` | `2:98433` | `1013` | DATA, 764 B |
| 8 | 05:07:37 | `alkanes_simulate` | `2:98433` | `4242` | REVERT: `Unrecognized opcode` |
| 9 | 05:07:40 | `alkanes_simulate` | `2:98433` | `1000` | REVERT: `Unrecognized opcode` |
| 10 | 05:07:45 | `alkanes_simulate` | `2:98433` | `1000, 7` | DATA, 5,078 B |
| 11 | 05:07:48 | `alkanes_simulate` | `2:98433` | `1008, 6` | DATA, 3,135 B |
| 12 | 05:07:53 | `metashrew_height` | — | — | 969800 |
| 13 | 05:08:13 | `metashrew_height` | — | — | 969800 |
| 14 | 05:08:16 | `alkanes_simulate` | `2:98433` | `99` | DATA, 14 B |
| 15 | 05:08:20 | `alkanes_simulate` | `2:98433` | `1002, 6` | DATA, 434 B |
| 16 | 05:08:23 | `alkanes_simulate` | `2:98433` | `1006, 6` | DATA, 16 B |
| 17 | 05:08:27 | `alkanes_simulate` | `2:98433` | `1010, 6` | DATA, 71 B |
| 18 | 05:08:31 | `alkanes_simulate` | `2:98433` | `1011, 2, 98825` | DATA, 57 B |
| 19 | 05:08:34 | `alkanes_simulate` | `2:98433` | `1005, 34, 81, … (36 cells)` | DATA, 114 B |
| 20 | 05:08:38 | `alkanes_simulate` | `2:98433` | `1012, 32, 55, … (34 cells)` | DATA, 136 B |
| 21 | 05:08:41 | `alkanes_simulate` | `2:98433` | `1008, 2999` | DATA, 5,265 B |
| 22 | 05:08:45 | `alkanes_simulate` | `2:98433` | `1010, 2999` | DATA, 79 B |
| 23 | 05:08:49 | `alkanes_simulate` | `2:98433` | `1002` | REVERT: `Unrecognized opcode` |
| 24 | 05:08:52 | `alkanes_simulate` | `2:98433` | `0` | REVERT: `Unrecognized opcode` |
| 25 | 05:08:58 | `alkanes_simulate` | `2:98433` | `8` | REVERT: `Aries Orbitals: no minter output found in mint tx` |
| 26 | 05:09:02 | `metashrew_height` | — | — | 969800 |
| 27 | 05:09:11 | `metashrew_height` | — | — | 969800 |
| 28 | 05:09:14 | `alkanes_simulate` | `2:98825` | `99` | DATA, 19 B |
| 29 | 05:09:18 | `alkanes_simulate` | `2:98825` | `100` | DATA, 13 B |
| 30 | 05:09:21 | `alkanes_simulate` | `2:98825` | `101` | DATA, 16 B |
| 31 | 05:09:25 | `alkanes_simulate` | `2:98825` | `998` | DATA, 7 B |
| 32 | 05:09:29 | `alkanes_simulate` | `2:98825` | `999` | DATA, 16 B |
| 33 | 05:09:32 | `alkanes_simulate` | `2:98825` | `1000` | DATA, 1,826 B |
| 34 | 05:09:37 | `alkanes_simulate` | `2:98825` | `1001` | DATA, 13 B |
| 35 | 05:09:46 | `alkanes_simulate` | `2:98825` | `1002` | DATA, 434 B |
| 36 | 05:09:58 | `alkanes_simulate` | `2:98825` | `1006` | DATA, 16 B |
| 37 | 05:10:02 | `alkanes_simulate` | `2:98825` | `1008` | DATA, 3,135 B |
| 38 | 05:10:09 | `alkanes_simulate` | `2:98825` | `4242` | REVERT: `Unrecognized opcode` |
| 39 | 05:10:14 | `alkanes_simulate` | `2:98825` | `0, 6` | REVERT: `Aries Orbitals: already initialized` |
| 40 | 05:10:19 | `alkanes_simulate` | `2:98433` | `0, 3000, 0, 0, 0` | REVERT: `Aries Orbitals: already initialized` |
| 41 | 05:10:25 | `metashrew_height` | — | — | 969801 |
| 42 | 05:10:44 | `metashrew_height` | — | — | 969801 |
| 43 | 05:10:47 | `alkanes_simulate` | `2:102171` | `99` | DATA, 19 B |
| 44 | 05:10:54 | `alkanes_simulate` | `2:102171` | `100` | DATA, 13 B |
| 45 | 05:10:59 | `alkanes_simulate` | `2:102171` | `101` | DATA, 16 B |
| 46 | 05:11:04 | `alkanes_simulate` | `2:102171` | `998` | DATA, 7 B |
| 47 | 05:11:08 | `alkanes_simulate` | `2:102171` | `999` | DATA, 16 B |
| 48 | 05:11:13 | `alkanes_simulate` | `2:102171` | `1000` | DATA, 3,885 B |
| 49 | 05:11:18 | `alkanes_simulate` | `2:102171` | `1001` | DATA, 13 B |
| 50 | 05:11:23 | `alkanes_simulate` | `2:102171` | `1002` | DATA, 431 B |
| 51 | 05:11:32 | `alkanes_simulate` | `2:102171` | `1006` | DATA, 16 B |
| 52 | 05:11:37 | `alkanes_simulate` | `2:102171` | `99` | DATA, 19 B |
| 53 | 05:11:40 | `alkanes_simulate` | `2:102171` | `1008` | DATA, 5,265 B |
| 54 | 05:11:45 | `alkanes_simulate` | `2:102171` | `4242` | REVERT: `Unrecognized opcode` |
| 55 | 05:11:50 | `alkanes_simulate` | `2:102171` | `0, 2999` | REVERT: `Aries Orbitals: already initialized` |
| 56 | 05:11:55 | `alkanes_simulate` | `2:98825` | `99` | DATA, 19 B |
| 57 | 05:12:00 | `alkanes_simulate` | `2:98825` | `0, 6` | REVERT: `Aries Orbitals: already initialized` |
| 58 | 05:12:04 | `alkanes_simulate` | `2:98433` | `99` | DATA, 14 B |
| 59 | 05:12:10 | `alkanes_simulate` | `2:98433` | `0, 3000, 0, 0, 0` | REVERT: `Aries Orbitals: already initialized` |
| 60 | 05:12:13 | `metashrew_height` | — | — | 969801 |
| 61 | 05:13:39 | `metashrew_height` | — | — | 969801 |
| 62 | 05:13:43 | `alkanes_simulate` | `2:98433` | `99` | DATA, 14 B |
| 63 | 05:13:46 | `alkanes_simulate` | `2:98433` | `1007, 0, 0, 0, 0` | DATA, 275 B |
| 64 | 05:13:50 | `alkanes_simulate` | `2:98433` | `1001, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 65 | 05:13:54 | `alkanes_simulate` | `2:98433` | `103, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 66 | 05:13:58 | `alkanes_simulate` | `2:98433` | `104, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 67 | 05:14:01 | `alkanes_simulate` | `2:98433` | `1003, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 68 | 05:14:05 | `alkanes_simulate` | `2:98433` | `1004, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 69 | 05:14:09 | `alkanes_simulate` | `2:98433` | `1009, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 70 | 05:14:13 | `alkanes_simulate` | `2:98433` | `7, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 71 | 05:14:21 | `alkanes_simulate` | `2:98433` | `9, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 72 | 05:14:25 | `alkanes_simulate` | `2:98433` | `10, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 73 | 05:14:29 | `alkanes_simulate` | `2:98433` | `99` | DATA, 14 B |
| 74 | 05:14:32 | `alkanes_simulate` | `2:98433` | `12, 0, 0, 0, 0` | REVERT: `Unrecognized opcode` |
| 75 | 05:14:36 | `alkanes_simulate` | `2:98433` | `1000, 0, 0, 0, 0` | DATA, 2,776 B |
| 76 | 05:14:40 | `metashrew_height` | — | — | 969801 |
| 77 | 20:36:01 | `metashrew_height` | — | — | 969896 |
| 78 | 20:36:04 | `alkanes_simulate` | `2:614` | `99` | DATA, 13 B |
| 79 | 20:36:08 | `alkanes_simulate` | `2:614` | `101` | DATA, 16 B |
| 80 | 20:36:11 | `alkanes_simulate` | `2:614` | `1002, 0` | DATA, 5 B |
| 81 | 20:36:15 | `alkanes_simulate` | `2:614` | `1002, 1` | DATA, 5 B |
| 82 | 20:36:19 | `alkanes_simulate` | `2:615` | `99` | DATA, 16 B |
| 83 | 20:36:22 | `alkanes_simulate` | `2:615` | `998` | DATA, 5 B |
| 84 | 20:36:26 | `alkanes_simulate` | `2:615` | `999` | DATA, 32 B |
| 85 | 20:36:29 | `alkanes_simulate` | `2:615` | `1002` | DATA, 112 B |
| 86 | 20:36:34 | `metashrew_height` | — | — | 969896 |
| 87 | 20:36:39 | `metashrew_height` | — | — | 969896 |
| 88 | 20:36:42 | `alkanes_simulate` | `2:616` | `99` | DATA, 16 B |
| 89 | 20:36:46 | `alkanes_simulate` | `2:616` | `998` | DATA, 5 B |
| 90 | 20:36:49 | `alkanes_simulate` | `2:616` | `1002` | DATA, 106 B |
| 91 | 20:36:54 | `alkanes_simulate` | `2:15635` | `99` | DATA, 10 B |
| 92 | 20:36:57 | `alkanes_simulate` | `2:15635` | `998` | DATA, 7 B |
| 93 | 20:37:01 | `alkanes_simulate` | `2:15635` | `999` | DATA, 16 B |
| 94 | 20:37:04 | `alkanes_simulate` | `2:15635` | `1002` | DATA, 271 B |
| 95 | 20:37:09 | `metashrew_height` | — | — | 969896 |
| 96 | 20:37:36 | `metashrew_height` | — | — | 969896 |
| 97 | 20:37:40 | `alkanes_simulate` | `2:10672` | `99` | DATA, 4 B |
| 98 | 20:37:43 | `alkanes_simulate` | `2:10672` | `101` | DATA, 16 B |
| 99 | 20:37:47 | `alkanes_simulate` | `2:10672` | `1002, 4962` | DATA, 271 B |
| 100 | 20:37:51 | `alkanes_simulate` | `2:10672` | `1002, 0` | DATA, 272 B |
| 101 | 20:37:55 | `alkanes_simulate` | `2:10672` | `999, 4962` | REVERT: `Failed to parse message: Unknown opcode: 999` |
| 102 | 20:37:58 | `alkanes_simulate` | `2:10672` | `1003, 4962` | REVERT: `Failed to parse message: Unknown opcode: 1003` |
| 103 | 20:38:02 | `alkanes_simulate` | `2:10672` | `998` | DATA, 7 B |
| 104 | 20:38:06 | `metashrew_height` | — | — | 969896 |
| 105 | 20:38:18 | `metashrew_height` | — | — | 969896 |
| 106 | 20:38:21 | `alkanes_simulate` | `2:15636` | `99` | DATA, 10 B |
| 107 | 20:38:25 | `alkanes_simulate` | `2:15636` | `998` | DATA, 7 B |
| 108 | 20:38:29 | `alkanes_simulate` | `2:15636` | `999` | DATA, 16 B |
| 109 | 20:38:32 | `alkanes_simulate` | `2:15636` | `1002` | DATA, 277 B |
| 110 | 20:38:37 | `metashrew_height` | — | — | 969896 |
| 111 | 20:38:45 | `metashrew_height` | — | — | 969896 |
| 112 | 20:38:48 | `alkanes_simulate` | `2:10672` | `99` | DATA, 4 B |
| 113 | 20:38:51 | `alkanes_simulate` | `2:10672` | `1002, 4963` | DATA, 277 B |
| 114 | 20:38:55 | `metashrew_height` | — | — | 969896 |

## v0.2.1 — the re-measurement (2026-10-27)

Every row of §1, §3 and §7 and every payload in this directory was read again. Nothing in v0.2's tables or files changed; the files above keep their v0.2 conditions.

| | |
|---|---|
| network | Bitcoin mainnet |
| reader | SUBFROST gateway, `https://mainnet.subfrost.io/v4/jsonrpc`, **anonymous tier** (no key; 20 calls/min) |
| method | `alkanes_simulate [{target:{block,tx}, inputs:[opcode, args…]}, "<height>"]`: every simulate is **pinned** by its block tag, so it answers from the state at exactly that height. `metashrew_height` brackets each batch. Build facts: `metashrew_view alkanes_id_to_outpoint`, `esplora_tx`, `alkanes_protorunesbyoutpoint` (a height string reads the outpoint as it stood at that block) |
| heights | **973,316** for every §1, §3 and §7 row; 968,676 and 968,677 (the parent's deployment); 968,700, 969,027 and 969,028 (principle 5); tip 973,316–973,318 during the run |
| date | 2026-10-27, 00:40–00:58 UTC |
| pacing | ≥ 3.2 s between dispatches, ≤ 19 in any minute; no call was refused for rate |
| gateway calls | **222** in total, every one logged; 214 answered; 5 refused at the gateway's edge before the anonymous tier was used; 3 got no answer and were repeated |
| subjects | parent `2:98433`; children #0002 `2:98728`, #0007 `2:98825`, #0862 `2:100000`, #3000 `2:102171`; §1 survey: Alkane Pandas `2:614` (`2:615`, `2:616`), Oyly `2:10672` (`2:15635`, `2:15636`) |

**Pinning is a measured property, not an assumption.** `101` on the parent answers `3000` at `latest` and `0` pinned to 968,700; `99` refuses `unexpected end-of-file` pinned to 968,676 and answers `Aries Orbitals` pinned to 968,677, the block of its creating transaction.

**Positive controls.** Every target got `99 get-name` at the same pin before its first view, again on every change of target, and again whenever its last control was more than 45 s old. Every control answered.

**What was compared.** The regenerated parent and #0007 files differ from the committed ones only in their conditions (`height_window`, `at`, `positive_control.ledger_call` and `.at`, `reader`, `height_note`, `measured_by`). Every opcode, argument, verdict, raw payload, refusal text and gas figure is identical, in the same order. `metadata-document-0007.json` regenerates byte-identical.

### The calls

| n | UTC | method | target | inputs | verdict |
|---|---|---|---|---|---|
| 1 | 00:40:52 | `metashrew_height` | — | — | refused at the gateway's edge (HTTP 401); no chain data |
| 2 | 00:40:53 | `alkanes_simulate` | — | — | refused at the gateway's edge (HTTP 401); no chain data |
| 3 | 00:40:55 | `alkanes_simulate` | — | — | refused at the gateway's edge (HTTP 401); no chain data |
| 4 | 00:40:57 | `alkanes_simulate` | — | — | refused at the gateway's edge (HTTP 401); no chain data |
| 5 | 00:40:58 | `alkanes_simulate` | — | — | refused at the gateway's edge (HTTP 401); no chain data |
| 6 | 00:42:33 | `metashrew_height` | — | — | 973316 |
| 7 | 00:42:36 | `alkanes_simulate` | `2:98433` | `101` @ `latest` | DATA, 16 B |
| 8 | 00:42:39 | `alkanes_simulate` | `2:98433` | `101` @ `968700` | DATA, 16 B |
| 9 | 00:42:42 | `alkanes_simulate` | `2:98433` | `99` @ `968676` | REVERT: `unexpected end-of-file (at offset 0x0)` |
| 10 | 00:42:46 | `alkanes_simulate` | `2:98433` | `99` @ `968677` | DATA, 14 B |
| 11 | 00:43:42 | `metashrew_height` | — | — | 973317 |
| 12 | 00:43:45 | `alkanes_simulate` | `2:98433` | `99` @ `973316` | DATA, 14 B |
| 13 | 00:43:49 | `alkanes_simulate` | `2:98433` | `100` @ `973316` | DATA, 8 B |
| 14 | 00:43:52 | `alkanes_simulate` | `2:98433` | `101` @ `973316` | DATA, 16 B |
| 15 | 00:43:55 | `alkanes_simulate` | `2:98433` | `102` @ `973316` | DATA, 16 B |
| 16 | 00:43:58 | `alkanes_simulate` | `2:98433` | `1007` @ `973316` | DATA, 275 B |
| 17 | 00:44:01 | `alkanes_simulate` | `2:98433` | `1013` @ `973316` | DATA, 764 B |
| 18 | 00:44:05 | `alkanes_simulate` | `2:98433` | `4242` @ `973316` | REVERT: `Unrecognized opcode` |
| 19 | 00:44:08 | `alkanes_simulate` | `2:98433` | `1000` @ `973316` | REVERT: `Unrecognized opcode` |
| 20 | 00:44:11 | `alkanes_simulate` | `2:98433` | `1000, 7` @ `973316` | DATA, 5,078 B |
| 21 | 00:44:14 | `alkanes_simulate` | `2:98433` | `1008, 6` @ `973316` | DATA, 3,135 B |
| 22 | 00:44:18 | `alkanes_simulate` | `2:98433` | `1002, 6` @ `973316` | DATA, 434 B |
| 23 | 00:44:22 | `alkanes_simulate` | `2:98433` | `1006, 6` @ `973316` | DATA, 16 B |
| 24 | 00:44:26 | `alkanes_simulate` | `2:98433` | `1010, 6` @ `973316` | DATA, 71 B |
| 25 | 00:44:29 | `alkanes_simulate` | `2:98433` | `1011, 2, 98825` @ `973316` | DATA, 57 B |
| 26 | 00:44:32 | `alkanes_simulate` | `2:98433` | `1005, 34, 81, … (36 cells)` @ `973316` | DATA, 114 B |
| 27 | 00:44:35 | `alkanes_simulate` | `2:98433` | `99` @ `973316` | DATA, 14 B |
| 28 | 00:44:39 | `alkanes_simulate` | `2:98433` | `1012, 32, 55, … (34 cells)` @ `973316` | DATA, 136 B |
| 29 | 00:44:42 | `alkanes_simulate` | `2:98433` | `1008, 2999` @ `973316` | DATA, 5,265 B |
| 30 | 00:44:46 | `alkanes_simulate` | `2:98433` | `1010, 2999` @ `973316` | DATA, 79 B |
| 31 | 00:44:49 | `alkanes_simulate` | `2:98433` | `1002` @ `973316` | REVERT: `Unrecognized opcode` |
| 32 | 00:44:53 | `alkanes_simulate` | `2:98433` | `0` @ `973316` | REVERT: `Unrecognized opcode` |
| 33 | 00:44:56 | `alkanes_simulate` | `2:98433` | `8` @ `973316` | REVERT: `Aries Orbitals: no minter output found in mint tx` |
| 34 | 00:44:59 | `alkanes_simulate` | `2:98433` | `0, 3000, 0, 0, 0` @ `973316` | REVERT: `Aries Orbitals: already initialized` |
| 35 | 00:45:02 | `alkanes_simulate` | `2:98433` | `1007, 0, 0, 0, 0` @ `973316` | DATA, 275 B |
| 36 | 00:45:05 | `alkanes_simulate` | `2:98433` | `1001, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 37 | 00:45:10 | `alkanes_simulate` | `2:98433` | `103, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 38 | 00:45:13 | `alkanes_simulate` | `2:98433` | `104, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 39 | 00:45:17 | `alkanes_simulate` | `2:98433` | `1003, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 40 | 00:45:21 | `alkanes_simulate` | `2:98433` | `1004, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 41 | 00:45:24 | `alkanes_simulate` | `2:98433` | `99` @ `973316` | DATA, 14 B |
| 42 | 00:45:27 | `alkanes_simulate` | `2:98433` | `1009, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 43 | 00:45:30 | `alkanes_simulate` | `2:98433` | `7, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 44 | 00:45:34 | `alkanes_simulate` | `2:98433` | `9, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 45 | 00:45:37 | `alkanes_simulate` | `2:98433` | `10, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 46 | 00:45:42 | `alkanes_simulate` | `2:98433` | `12, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 47 | 00:45:45 | `alkanes_simulate` | `2:98433` | `1000, 0, 0, 0, 0` @ `973316` | DATA, 2,776 B |
| 48 | 00:45:48 | `alkanes_simulate` | `2:98433` | `1010, 1` @ `973316` | DATA, 71 B |
| 49 | 00:45:51 | `alkanes_simulate` | `2:98433` | `1011, 2, 98728` @ `973316` | DATA, 57 B |
| 50 | 00:45:55 | `alkanes_simulate` | `2:98433` | `1010, 861` @ `973316` | DATA, 77 B |
| 51 | 00:45:58 | `alkanes_simulate` | `2:98433` | `1011, 2, 100000` @ `973316` | DATA, 62 B |
| 52 | 00:46:01 | `alkanes_simulate` | `2:98433` | `1002, 1` @ `973316` | DATA, 434 B |
| 53 | 00:46:04 | `alkanes_simulate` | `2:98433` | `1002, 861` @ `973316` | DATA, 429 B |
| 54 | 00:46:08 | `alkanes_simulate` | `2:98433` | `1006, 1` @ `973316` | DATA, 16 B |
| 55 | 00:46:11 | `alkanes_simulate` | `2:98433` | `99` @ `973316` | DATA, 14 B |
| 56 | 00:46:14 | `alkanes_simulate` | `2:98433` | `1006, 861` @ `973316` | DATA, 16 B |
| 57 | 00:46:17 | `alkanes_simulate` | `2:98433` | `1008, 1` @ `973316` | DATA, 6,214 B |
| 58 | 00:46:20 | `alkanes_simulate` | `2:98433` | `1008, 861` @ `973316` | DATA, 7,841 B |
| 59 | 00:46:24 | `alkanes_simulate` | `2:98433` | `1008` @ `973316` | REVERT: `Unrecognized opcode` |
| 60 | 00:46:27 | `alkanes_simulate` | `2:98433` | `998, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 61 | 00:46:30 | `alkanes_simulate` | `2:98433` | `999, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 62 | 00:46:33 | `alkanes_simulate` | `2:98433` | `1011, 2, 615` @ `973316` | DATA, 62 B |
| 63 | 00:46:37 | `alkanes_simulate` | `2:98433` | `1011, 2, 98433` @ `973316` | DATA, 64 B |
| 64 | 00:46:40 | `alkanes_simulate` | `2:98433` | `1011, 4, 333333` @ `973316` | DATA, 65 B |
| 65 | 00:46:43 | `alkanes_simulate` | `2:98433` | `1010, 3000` @ `973316` | REVERT: `Aries Orbitals: #3001 is outside the collection (#0001-#3000)` |
| 66 | 00:46:46 | `alkanes_simulate` | `2:98433` | `1002, 3000` @ `973316` | no answer (transport failure); the call was repeated |
| 67 | 00:46:49 | `alkanes_simulate` | `2:98433` | `1008, 3000` @ `973316` | REVERT: `Aries Orbitals: #3001 is outside the collection (#0001-#3000)` |
| 68 | 00:46:53 | `alkanes_simulate` | `2:98433` | `1006, 3000` @ `973316` | REVERT: `Aries Orbitals: #3001 is outside the collection (#0001-#3000)` |
| 69 | 00:46:56 | `alkanes_simulate` | `2:98433` | `1012, 32, 0, … (34 cells)` @ `973316` | DATA, 137 B |
| 70 | 00:46:59 | `alkanes_simulate` | `2:98825` | `99` @ `973316` | DATA, 19 B |
| 71 | 00:47:02 | `alkanes_simulate` | `2:98825` | `100` @ `973316` | DATA, 13 B |
| 72 | 00:47:05 | `alkanes_simulate` | `2:98825` | `101` @ `973316` | DATA, 16 B |
| 73 | 00:47:09 | `alkanes_simulate` | `2:98825` | `998` @ `973316` | DATA, 7 B |
| 74 | 00:47:12 | `alkanes_simulate` | `2:98825` | `999` @ `973316` | DATA, 16 B |
| 75 | 00:47:15 | `alkanes_simulate` | `2:98825` | `1000` @ `973316` | DATA, 1,826 B |
| 76 | 00:47:18 | `alkanes_simulate` | `2:98825` | `1001` @ `973316` | DATA, 13 B |
| 77 | 00:47:21 | `alkanes_simulate` | `2:98825` | `1002` @ `973316` | DATA, 434 B |
| 78 | 00:47:25 | `alkanes_simulate` | `2:98825` | `1006` @ `973316` | DATA, 16 B |
| 79 | 00:47:28 | `alkanes_simulate` | `2:98825` | `1008` @ `973316` | DATA, 3,135 B |
| 80 | 00:47:32 | `alkanes_simulate` | `2:98825` | `4242` @ `973316` | REVERT: `Unrecognized opcode` |
| 81 | 00:47:35 | `alkanes_simulate` | `2:98825` | `0, 6` @ `973316` | REVERT: `Aries Orbitals: already initialized` |
| 82 | 00:47:38 | `alkanes_simulate` | `2:98728` | `99` @ `973316` | DATA, 19 B |
| 83 | 00:47:41 | `alkanes_simulate` | `2:98728` | `100` @ `973316` | DATA, 13 B |
| 84 | 00:47:45 | `alkanes_simulate` | `2:98728` | `101` @ `973316` | DATA, 16 B |
| 85 | 00:47:48 | `alkanes_simulate` | `2:98728` | `998` @ `973316` | DATA, 7 B |
| 86 | 00:47:51 | `alkanes_simulate` | `2:98728` | `999` @ `973316` | DATA, 16 B |
| 87 | 00:47:54 | `alkanes_simulate` | `2:98728` | `1000` @ `973316` | DATA, 4,751 B |
| 88 | 00:47:57 | `alkanes_simulate` | `2:98728` | `1001` @ `973316` | DATA, 13 B |
| 89 | 00:48:01 | `alkanes_simulate` | `2:98728` | `1002` @ `973316` | DATA, 434 B |
| 90 | 00:48:04 | `alkanes_simulate` | `2:98728` | `1006` @ `973316` | DATA, 16 B |
| 91 | 00:48:07 | `alkanes_simulate` | `2:98728` | `1008` @ `973316` | DATA, 6,214 B |
| 92 | 00:48:10 | `alkanes_simulate` | `2:98728` | `4242` @ `973316` | REVERT: `Unrecognized opcode` |
| 93 | 00:48:13 | `alkanes_simulate` | `2:98728` | `0, 1` @ `973316` | REVERT: `Aries Orbitals: already initialized` |
| 94 | 00:48:17 | `alkanes_simulate` | `2:98728` | `102, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 95 | 00:48:20 | `alkanes_simulate` | `2:98728` | `1005, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 96 | 00:48:23 | `alkanes_simulate` | `2:98728` | `1007, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 97 | 00:48:26 | `alkanes_simulate` | `2:98728` | `99` @ `973316` | DATA, 19 B |
| 98 | 00:48:30 | `alkanes_simulate` | `2:98728` | `1010, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 99 | 00:48:33 | `alkanes_simulate` | `2:98728` | `1011, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 100 | 00:48:36 | `alkanes_simulate` | `2:98728` | `1012, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 101 | 00:48:39 | `alkanes_simulate` | `2:98728` | `1013, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 102 | 00:48:43 | `alkanes_simulate` | `2:98728` | `8, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 103 | 00:48:46 | `alkanes_simulate` | `2:100000` | `99` @ `973316` | no answer (transport failure); the call was repeated |
| 104 | 00:49:44 | `metashrew_height` | — | — | 973318 |
| 105 | 00:49:48 | `alkanes_simulate` | `2:98433` | `99` @ `973316` | DATA, 14 B |
| 106 | 00:49:51 | `alkanes_simulate` | `2:98433` | `1002, 3000` @ `973316` | REVERT: `Aries Orbitals: #3001 is outside the collection (#0001-#3000)` |
| 107 | 00:49:54 | `alkanes_simulate` | `2:100000` | `99` @ `973316` | DATA, 19 B |
| 108 | 00:49:57 | `alkanes_simulate` | `2:100000` | `100` @ `973316` | DATA, 13 B |
| 109 | 00:50:01 | `alkanes_simulate` | `2:100000` | `101` @ `973316` | DATA, 16 B |
| 110 | 00:50:04 | `alkanes_simulate` | `2:100000` | `998` @ `973316` | DATA, 7 B |
| 111 | 00:50:07 | `alkanes_simulate` | `2:100000` | `999` @ `973316` | DATA, 16 B |
| 112 | 00:50:10 | `alkanes_simulate` | `2:100000` | `1000` @ `973316` | DATA, 6,333 B |
| 113 | 00:50:13 | `alkanes_simulate` | `2:100000` | `1001` @ `973316` | DATA, 13 B |
| 114 | 00:50:17 | `alkanes_simulate` | `2:100000` | `1002` @ `973316` | DATA, 429 B |
| 115 | 00:50:20 | `alkanes_simulate` | `2:100000` | `1006` @ `973316` | DATA, 16 B |
| 116 | 00:50:23 | `alkanes_simulate` | `2:100000` | `1008` @ `973316` | DATA, 7,841 B |
| 117 | 00:50:26 | `alkanes_simulate` | `2:100000` | `4242` @ `973316` | REVERT: `Unrecognized opcode` |
| 118 | 00:50:29 | `alkanes_simulate` | `2:100000` | `0, 861` @ `973316` | REVERT: `Aries Orbitals: already initialized` |
| 119 | 00:50:33 | `alkanes_simulate` | `2:100000` | `102, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 120 | 00:50:36 | `alkanes_simulate` | `2:100000` | `1005, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 121 | 00:50:39 | `alkanes_simulate` | `2:100000` | `1007, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 122 | 00:50:42 | `alkanes_simulate` | `2:100000` | `99` @ `973316` | DATA, 19 B |
| 123 | 00:50:46 | `alkanes_simulate` | `2:100000` | `1010, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 124 | 00:50:49 | `alkanes_simulate` | `2:100000` | `1011, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 125 | 00:50:52 | `alkanes_simulate` | `2:100000` | `1012, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 126 | 00:50:55 | `alkanes_simulate` | `2:100000` | `1013, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 127 | 00:50:59 | `alkanes_simulate` | `2:100000` | `8, 0, 0, 0, 0` @ `973316` | REVERT: `Unrecognized opcode` |
| 128 | 00:51:02 | `metashrew_height` | — | — | 973318 |
| 129 | 00:51:05 | `metashrew_height` | — | — | 973318 |
| 130 | 00:51:08 | `alkanes_simulate` | `2:615` | `99` @ `973316` | DATA, 16 B |
| 131 | 00:51:12 | `alkanes_simulate` | `2:615` | `998` @ `973316` | DATA, 5 B |
| 132 | 00:51:15 | `alkanes_simulate` | `2:615` | `999` @ `973316` | DATA, 32 B |
| 133 | 00:51:18 | `alkanes_simulate` | `2:615` | `1002` @ `973316` | DATA, 112 B |
| 134 | 00:51:21 | `alkanes_simulate` | `2:616` | `99` @ `973316` | DATA, 16 B |
| 135 | 00:51:25 | `alkanes_simulate` | `2:616` | `998` @ `973316` | DATA, 5 B |
| 136 | 00:51:28 | `alkanes_simulate` | `2:616` | `999` @ `973316` | DATA, 32 B |
| 137 | 00:51:31 | `alkanes_simulate` | `2:616` | `1002` @ `973316` | no answer (transport failure); the call was repeated |
| 138 | 00:53:01 | `alkanes_simulate` | `2:616` | `1002` @ `973316` | DATA, 106 B |
| 139 | 00:53:04 | `alkanes_simulate` | `2:614` | `99` @ `973316` | DATA, 13 B |
| 140 | 00:53:07 | `alkanes_simulate` | `2:614` | `101` @ `973316` | DATA, 16 B |
| 141 | 00:53:11 | `alkanes_simulate` | `2:614` | `1002, 0` @ `973316` | DATA, 5 B |
| 142 | 00:53:14 | `alkanes_simulate` | `2:614` | `1002, 1` @ `973316` | DATA, 5 B |
| 143 | 00:53:17 | `alkanes_simulate` | `2:15635` | `99` @ `973316` | DATA, 10 B |
| 144 | 00:53:21 | `alkanes_simulate` | `2:15635` | `998` @ `973316` | DATA, 7 B |
| 145 | 00:53:24 | `alkanes_simulate` | `2:15635` | `999` @ `973316` | DATA, 16 B |
| 146 | 00:53:27 | `alkanes_simulate` | `2:15635` | `1002` @ `973316` | DATA, 271 B |
| 147 | 00:53:30 | `alkanes_simulate` | `2:15636` | `99` @ `973316` | DATA, 10 B |
| 148 | 00:53:33 | `alkanes_simulate` | `2:15636` | `998` @ `973316` | DATA, 7 B |
| 149 | 00:53:37 | `alkanes_simulate` | `2:15636` | `999` @ `973316` | DATA, 16 B |
| 150 | 00:53:40 | `alkanes_simulate` | `2:15636` | `1002` @ `973316` | DATA, 277 B |
| 151 | 00:53:43 | `alkanes_simulate` | `2:10672` | `99` @ `973316` | DATA, 4 B |
| 152 | 00:53:46 | `alkanes_simulate` | `2:10672` | `101` @ `973316` | DATA, 16 B |
| 153 | 00:53:50 | `alkanes_simulate` | `2:10672` | `1002, 4962` @ `973316` | DATA, 271 B |
| 154 | 00:53:53 | `alkanes_simulate` | `2:10672` | `1002, 4963` @ `973316` | DATA, 277 B |
| 155 | 00:53:56 | `alkanes_simulate` | `2:10672` | `999, 4962` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 999` |
| 156 | 00:53:59 | `alkanes_simulate` | `2:10672` | `1003, 4962` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1003` |
| 157 | 00:54:02 | `alkanes_simulate` | `2:10672` | `1004, 4962` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1004` |
| 158 | 00:54:06 | `alkanes_simulate` | `2:10672` | `1005, 4962` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1005` |
| 159 | 00:54:09 | `alkanes_simulate` | `2:10672` | `1006, 4962` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1006` |
| 160 | 00:54:12 | `alkanes_simulate` | `2:10672` | `1007, 4962` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1007` |
| 161 | 00:54:15 | `alkanes_simulate` | `2:10672` | `1008, 4962` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1008` |
| 162 | 00:54:18 | `alkanes_simulate` | `2:10672` | `1010, 4962` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1010` |
| 163 | 00:54:22 | `alkanes_simulate` | `2:10672` | `1011, 2, 15635` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1011` |
| 164 | 00:54:25 | `alkanes_simulate` | `2:10672` | `1012, 2, 15635` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1012` |
| 165 | 00:54:28 | `alkanes_simulate` | `2:10672` | `1013` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1013` |
| 166 | 00:54:31 | `alkanes_simulate` | `2:10672` | `99` @ `973316` | DATA, 4 B |
| 167 | 00:54:34 | `alkanes_simulate` | `2:10672` | `998, 4962` @ `973316` | DATA, 7 B |
| 168 | 00:54:38 | `alkanes_simulate` | `2:10672` | `1000, 4962` @ `973316` | DATA, 1,692 B |
| 169 | 00:54:41 | `alkanes_simulate` | `2:10672` | `1001` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 1001` |
| 170 | 00:54:44 | `alkanes_simulate` | `2:10672` | `4242` @ `973316` | REVERT: `Failed to parse message: Unknown opcode: 4242` |
| 171 | 00:54:48 | `alkanes_simulate` | `2:102171` | `99` @ `973316` | DATA, 19 B |
| 172 | 00:54:51 | `alkanes_simulate` | `2:102171` | `998` @ `973316` | DATA, 7 B |
| 173 | 00:54:54 | `alkanes_simulate` | `2:102171` | `999` @ `973316` | DATA, 16 B |
| 174 | 00:54:57 | `alkanes_simulate` | `2:102171` | `1002` @ `973316` | DATA, 431 B |
| 175 | 00:55:00 | `metashrew_height` | — | — | 973318 |
| 176 | 00:55:26 | `metashrew_height` | — | — | 973318 |
| 177 | 00:55:29 | `alkanes_simulate` | `2:98433` | `99` @ `968700` | DATA, 14 B |
| 178 | 00:55:32 | `alkanes_simulate` | `2:98433` | `1002, 0` @ `968700` | REVERT: `Aries Orbitals: #0001 not minted` |
| 179 | 00:55:35 | `alkanes_simulate` | `2:98433` | `1008, 0` @ `968700` | REVERT: `Aries Orbitals: #0001 not minted` |
| 180 | 00:55:39 | `alkanes_simulate` | `2:98433` | `1010, 0` @ `968700` | DATA, 38 B |
| 181 | 00:55:42 | `alkanes_simulate` | `2:98433` | `1000, 0` @ `968700` | REVERT: `Aries Orbitals: #0001 not minted` |
| 182 | 00:55:45 | `metashrew_height` | — | — | 973318 |
| 183 | 00:55:48 | `metashrew_height` | — | — | 973318 |
| 184 | 00:55:51 | `alkanes_simulate` | `2:98433` | `99` @ `969027` | DATA, 14 B |
| 185 | 00:55:55 | `alkanes_simulate` | `2:98433` | `1002, 1` @ `969027` | REVERT: `Aries Orbitals: #0002 not minted` |
| 186 | 00:55:58 | `alkanes_simulate` | `2:98433` | `1010, 1` @ `969027` | DATA, 38 B |
| 187 | 00:56:01 | `alkanes_simulate` | `2:98433` | `1011, 2, 98728` @ `969027` | DATA, 64 B |
| 188 | 00:56:04 | `metashrew_height` | — | — | 973318 |
| 189 | 00:56:08 | `metashrew_height` | — | — | 973318 |
| 190 | 00:56:11 | `alkanes_simulate` | `2:98433` | `99` @ `969028` | DATA, 14 B |
| 191 | 00:56:14 | `alkanes_simulate` | `2:98433` | `1002, 1` @ `969028` | DATA, 434 B |
| 192 | 00:56:17 | `alkanes_simulate` | `2:98433` | `1010, 1` @ `969028` | DATA, 71 B |
| 193 | 00:56:20 | `alkanes_simulate` | `2:98433` | `1011, 2, 98728` @ `969028` | DATA, 57 B |
| 194 | 00:56:24 | `metashrew_height` | — | — | 973318 |
| 195 | 00:56:27 | `metashrew_height` | — | — | 973318 |
| 196 | 00:56:30 | `alkanes_simulate` | `2:98433` | `99` @ `973316` | DATA, 14 B |
| 197 | 00:56:33 | `alkanes_simulate` | `2:98433` | `1012, 32, 106, … (34 cells)` @ `973316` | DATA, 137 B |
| 198 | 00:56:36 | `metashrew_height` | — | — | 973318 |
| 199 | 00:56:40 | `metashrew_view` | — | `alkanes_id_to_outpoint`, 2:98433 | `0x0a2083373f82…` |
| 200 | 00:56:43 | `esplora_tx` | — | `83373f82…5e0b` | confirmed at 968,677; 1 in, 3 out |
| 201 | 00:56:46 | `metashrew_view` | — | `alkanes_id_to_outpoint`, 4:333333 | `0x0a206e62f6cb…` |
| 202 | 00:56:49 | `esplora_tx` | — | `6e62f6cb…cd3e` | confirmed at 968,622; 1 in, 3 out |
| 203 | 00:56:53 | `esplora_tx` | — | `4026e1ec…4d39` | confirmed at 969,028; 1 in, 4 out |
| 204 | 00:56:56 | `alkanes_protorunesbyoutpoint` | — | `4026e1ec…4d39:0` @ `969028` | 2:98728 × 1 |
| 205 | 00:56:59 | `alkanes_protorunesbyoutpoint` | — | `4026e1ec…4d39:1` @ `969028` | no alkane |
| 206 | 00:57:02 | `alkanes_protorunesbyoutpoint` | — | `4026e1ec…4d39:3` @ `969028` | no alkane |
| 207 | 00:57:06 | `alkanes_protorunesbyoutpoint` | — | `70124e00…ae1b:3` @ `latest` | no alkane |
| 208 | 00:57:09 | `esplora_tx` | — | `ad0a116c…6f44` | confirmed at 969,527; 1 in, 4 out |
| 209 | 00:57:12 | `alkanes_protorunesbyoutpoint` | — | `ad0a116c…6f44:0` @ `969527` | 2:100000 × 1 |
| 210 | 00:57:15 | `alkanes_protorunesbyoutpoint` | — | `ad0a116c…6f44:1` @ `969527` | no alkane |
| 211 | 00:57:18 | `alkanes_protorunesbyoutpoint` | — | `ad0a116c…6f44:3` @ `969527` | no alkane |
| 212 | 00:57:22 | `alkanes_protorunesbyoutpoint` | — | `ec09ff72…b83f:1` @ `latest` | no alkane |
| 213 | 00:57:25 | `esplora_tx` | — | `bef7ef54…3f05` | confirmed at 969,566; 1 in, 4 out |
| 214 | 00:57:28 | `alkanes_protorunesbyoutpoint` | — | `bef7ef54…3f05:0` @ `969566` | 2:102171 × 1 |
| 215 | 00:57:31 | `alkanes_protorunesbyoutpoint` | — | `bef7ef54…3f05:1` @ `969566` | no alkane |
| 216 | 00:57:35 | `alkanes_protorunesbyoutpoint` | — | `bef7ef54…3f05:3` @ `969566` | no alkane |
| 217 | 00:57:38 | `alkanes_protorunesbyoutpoint` | — | `5d242c8c…0231:3` @ `latest` | no alkane |
| 218 | 00:58:29 | `alkanes_protorunesbyoutpoint` | — | `4026e1ec…4d39:0` @ `latest` | 2:98728 × 1 |
| 219 | 00:58:32 | `alkanes_protorunesbyoutpoint` | — | `4026e1ec…4d39:3` @ `latest` | no alkane |
| 220 | 00:58:51 | `alkanes_protorunesbyoutpoint` | — | `70124e00…ae1b:3` @ `969027` | no alkane |
| 221 | 00:58:54 | `alkanes_protorunesbyoutpoint` | — | `ec09ff72…b83f:1` @ `969526` | no alkane |
| 222 | 00:58:57 | `alkanes_protorunesbyoutpoint` | — | `5d242c8c…0231:3` @ `969565` | no alkane |
