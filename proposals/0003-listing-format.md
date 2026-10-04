# 0003 — A shared listing format for Alkanes collectibles

## Problem
A marketplace listing is a seller's signed partial transaction. Each venue invents its own envelope, so a listing made on one venue cannot be read, verified or filled by another, and a venue that is not Alkanes-aware can build a fill that destroys the piece or strands it. Holders should be able to list once and have any honest venue fill it; venues should be able to integrate a collection from its document and the chain alone.

## Change
A JSON envelope:

    { "format": "alkanes-listing/0",
      "parent": "2:98433", "piece": "2:98825",
      "outpoint": "<txid>:<vout>",
      "price_sats": 123456, "seller": "<address>",
      "psbt": "<base64>", "expires_height": 970000 }

The PSBT has exactly one input — the piece's outpoint, signed SIGHASH_SINGLE|ANYONECANPAY — and exactly one output — `price_sats` to `seller`. A filler: verifies the signature against the outpoint's script; verifies through an indexer that the outpoint is unspent, confirmed, and holds exactly one unit of a child of `parent`; refuses an outpoint holding more sats than `price_sats` (the excess would not reach the seller); builds the fill with a protostone whose edict moves the piece to the buyer's own output and whose pointer and refund pointer name that output; tags every input per proposal 0002 and admits none that holds an asset; adds fee and change after. Cancel is the seller spending the outpoint to themselves under a protostone. Prices are in sats.

## What it breaks
Nothing on chain. Venues keep their own storage and fees. A venue that adopts the envelope can fill listings made anywhere else that adopts it.

## What readers do differently
Verify, never trust: refuse envelopes whose PSBT has more than one input or output, whose signature does not verify, or whose outpoint fails the exact-one-piece check. Never broadcast a fill without the protostone.

## Status
A reference construction is under test on regtest. Measurements will be attached to this proposal when they exist; until then it is a proposal with no implementation of record.
