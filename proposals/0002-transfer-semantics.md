# 0002 — Transfer semantics: a protostone-required declaration, and asset tagging in PSBTs

## Problem
An Alkanes piece moves only under a protostone. A plain spend of its outpoint destroys it, and a spend under a protostone that does not address it sends it wherever the pointer says. Nothing at the outpoint tells a wallet, a PSBT co-signer or a marketplace that this is so: the piece sits on 546 sats and looks like postage. In the Aries Orbitals public round, on the order of a hundred pieces out of 3,000 were moved by their holders' own wallets without the holder choosing to move them, because coin selection treated the piece's output as an ordinary coin. No contract change prevents this; the information has to travel with the document and with the transaction.

## Change
1. The metadata document's `standards` array carries the token `alkanes-transfer-protostone`, declaring: every outpoint holding a unit of this collection requires a protostone to move, and a plain spend destroys it. A reader that sees the token asks an Alkanes indexer before letting any outpoint of this collection into coin selection.
2. A PSBT proprietary key (BIP-174 type 0xFC, identifier `alkanes`, subtype 0x00) on every input whose outpoint an indexer reports as holding alkanes. Value: the list of (alkane id, amount) at that outpoint. Builders set it. A signer that understands the key shows the assets to the user and refuses to sign a transaction that spends a tagged input unless the transaction carries a protostone addressing that asset — an edict for it, or a pointer at a non-OP_RETURN output.

## What it breaks
Nothing on chain. A deployed contract cannot add the standards token; for Aries Orbitals the declaration is carried by this repository until a conforming successor exists. The PSBT key only protects when both builder and signer implement it; wallets that ignore proprietary keys behave exactly as today.

## What readers do differently
Indexers expose "asset-bearing" per outpoint. Wallets exclude tagged outpoints from coin selection and warn before any spend of one. Marketplaces tag every input they build and never broadcast a fill or a cancel without the protostone.
