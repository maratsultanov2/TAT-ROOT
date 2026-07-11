# TAT vs Baseline: Structural Anomaly Detection in Value‑Obscuring Reversion

[![TAT](https://img.shields.io/badge/TAT-Experimental-blue)](https://github.com/maratsultanov2/TAT-ROOT)
[![Dataset by Rastislav](https://img.shields.io/badge/Dataset-Rastislav_Drahos-green)](https://github.com/DanceNitra/agora)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey)](../../LICENSE-DATA)
[![Code: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue)](../../LICENSE-CODE)

## Introduction

**Value‑obscuring reversion** is the task of detecting attempts to silently roll back a previously changed value in dialog systems. The user wants to revert, but **names neither the value nor an explicit revert command** (e.g., "go back to what we had", "undo that change"). Standard methods (cosine similarity, keyword search, value matching) are nearly blind here — F1 ranges from 0.03 to 0.60.

**TAT (TreeAngleTap)** demonstrated the ability to capture **structural signal** — the link between an utterance and the edit history, rather than superficial lexical matches.

Data provided by independent co‑author **Rastislav Drahos** (DanceNitra). Fixtures are designed to sequentially exclude possible "shortcuts": entity memorization, keywords, value strings. Each subsequent version is harder than the previous one.

## Methodology

### Features

For each example (old → new → candidate), a feature vector is built that reflects **dialogue structure** rather than semantics:

- **Theme** — entity identifier (normalized hash).
- **Role** — position in the chain (0.0, 0.5, 1.0).
- **Emotion** — intent marker (1.0 revert, 0.0 keep, 0.5 unknown), computed from a fixed dictionary.
- **Meaning** — length ratio of old and new values.
- **Goal / Asserted Value** — which value is asserted by the candidate (old, new, or neither).
- **Cosine Similarity** (for v4) — cosine similarity of the candidate to the old and new context lines.

### Model

**Triplenet** — architecture with three parallel paths (Yang, Yin, To) and constant patterns extracted from the training set. Training: 100 epochs, CPU, under 2 seconds.

### Protocol

Training is performed **only** on the source data (original fixture + first heldout). Test sets (v2, v3, v4) are **never used** for training, feature building, or threshold tuning. Threshold is fixed (0.5).

## Results

| Test | F1 (TAT) | F1 (Baseline) | AUROC | Key Challenge |
|------|----------|---------------|-------|---------------|
| v2 (new phrasings) | 1.0000 | 0.6000 (cosine) | 1.0000 | Paraphrase without revert words |
| v3 (asserted value) | 1.0000 | N/A | 1.0000 | Only structural value assertion |
| v4 (coreference, corrected) | 0.6667 | N/A | 0.6362 | Coreference without named value |

**Baselines for comparison (v2):**
- Object/value match: F1 = 0.03
- Cosine similarity: F1 = 0.60
- Keyword rule (based on revert/keep words): F1 = 1.00 (v2), but drops to chance on v3 and v4

Only TAT maintains high quality across all three levels of difficulty.

On the corrected v4, TAT achieves **recall 1.0** (all reverts detected), but precision is 0.5 due to false positives on keep. The failure is precisely localized: the model perfectly detects whether a role from the context is referenced (named_new 20/20), but cannot link that role to the specific anchor (old vs current value). This is the second hop of the chain, and the next target for improvement.

## Acknowledgements

Special thanks to **Rastislav Drahos** (DanceNitra) for building the fixtures, independent result verification, and constructive scientific discussion.

**Links:**
- Rastislav's repository: [github.com/DanceNitra/agora](https://github.com/DanceNitra/agora/tree/main/agora_output/public_fixtures)
- TAT-ROOT: [github.com/maratsultanov2/TAT-ROOT](https://github.com/maratsultanov2/TAT-ROOT)

## Licenses

- **Code** (notebooks, scripts): AGPL v3.0
- **Documentation, results, graphs**: CC BY-NC-ND 4.0
- **Data (fixtures)**: MIT (owned by Rastislav Drahos)
- **Models (.pt)**: Custom TAT License (commercial use requires permission)

## How to Reproduce

All Google Colab notebooks are in the [`notebooks/`](notebooks/) folder. They load pre‑trained models and output the same metrics as in the table above. No additional data required — fixtures are downloaded automatically from the DanceNitra repository.

*Published: 2026-07-11 09:49*
