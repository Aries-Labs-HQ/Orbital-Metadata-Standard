# How `examples/` was measured

Nothing in this directory was typed. Every value was read from Bitcoin mainnet and decoded by a script from the bytes the reader returned.

## Conditions

| | |
|---|---|
| network | Bitcoin mainnet |
| reader | SUBFROST gateway, `https://mainnet.subfrost.io/v4/jsonrpc`, **anonymous tier** (no key; 20 calls/min) |
| method | `alkanes_simulate [{target:{block,tx}, inputs:[opcode, args…]}, "latest"]`; `metashrew_height` for heights |
| heights | 969,800–969,801 (`metashrew_height` read before and after each batch) |
| date | 2026-10-04, 05:07–05:14 UTC |
| pacing | ≥ 3.1 s between calls |
| gateway calls | **76** in total, every one logged (method, params, raw response) |
| subjects | parent `2:98433`; children #0007 `2:98825` and #3000 `2:102171` |

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

In order. `n` is the call's number in the run's ledger.

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
