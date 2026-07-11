# Direct Context Comparison Method for Structural Anomaly Detection

[![TAT](https://img.shields.io/badge/TAT-Experimental-blue)](https://github.com/maratsultanov2/TAT-ROOT)
[![Dataset by Rastislav](https://img.shields.io/badge/Dataset-Rastislav_Drahos-green)](https://github.com/DanceNitra/agora)
[![License: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue)](../../LICENSE-CODE)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/Data-CC%20BY--NC--ND%204.0-lightgrey)](../../LICENSE-DATA)
[![Status: Peer‑Reviewed](https://img.shields.io/badge/Status-Peer--Reviewed-brightgreen)](https://github.com/DanceNitra/agora)

## Authors and Roles

- **Marat Sultanov** — author of the direct context comparison method, TAT architecture, Triplenet model, and all experiments on v2, v3, v4, and v4nat. Conducted the research independently, reported both successes and failures with full transparency.
- **Rastislav Drahos (DanceNitra)** — independent co‑author. Designed the value‑obscuring reversion fixtures (v2, v3, v4, v4nat), conducted multiple audits to eliminate lexical shortcuts, reproduced the method on his side with a different embedder, and discovered the factorization of the task into reference resolution and recency attribution.

## The Problem

**Value‑obscuring reversion** — detecting a silent attempt to roll back a previously changed value in a dialog system. The user wants to revert, but names neither the value nor an explicit revert command, only referring to the person who set the value by their role.

Standard methods are nearly blind on this task:
- Object/value match: F1 ≈ 0.00
- Cosine similarity: F1 ≈ 0.48
- Keyword rules: F1 ≈ 0.00
- Template‑signature learners: F1 ≈ 0.00

## The Method

**Direct comparison of the candidate with the context lines by their structural roles.**

Each example in the naturalized v4nat fixture contains exactly four context lines:
1. Old action (who set the old value)
2. New action (who set the new value)
3. Old role (what the old anchor is responsible for)
4. New role (what the new anchor is responsible for)

The candidate never names the value or the anchor — only the role.

**Algorithm:**
1. Compute cosine similarity between the candidate and each of the four context lines.
2. Average the similarity with the old lines (action + role) → `sim_old`.
3. Average the similarity with the new lines (action + role) → `sim_new`.
4. If `sim_old > sim_new` → revert. Otherwise → keep.

No model training. No LLM. No multi‑hop reasoning. Only the structure of the dialog.

## Results

| Fixture | F1 (TAT) | F1 (Cosine Baseline) | AUROC | Key Challenge |
|---------|----------|----------------------|-------|---------------|
| v2 (new phrasings) | 1.0000 | 0.6000 | 1.0000 | Entity/value substitution |
| v3 (asserted value) | 1.0000 | N/A | 1.0000 | Structural value assertion |
| v4 (coreference, corrected) | 0.9800 | N/A | 1.0000 | Coreference without named value |
| v4nat (naturalized, heldout) | **0.9048** | 0.481 | **0.9635** | Natural language, no shortcuts |

**On v4nat heldout (46 examples):**
- Accuracy: 0.9130
- Precision: 0.8636
- Recall: 0.9500
- F1: 0.9048
- AUROC: 0.9635
- Confusion matrix: [23 3; 1 19]

**Independent reproduction by Rastislav Drahos:**
- F1: 0.930, AUROC: 1.000, Confusion: [23 3; 0 20] (different embedder)

## Key Insight: Task Factorization

Rastislav Drahos decomposed the task into two independent sub‑problems:
1. **Reference resolution** (text problem) — which role does the candidate refer to? Solved by our structural similarity method.
2. **Recency attribution** (ledger problem) — is that role linked to the old or current value? Solved by the fixed line order in the fixture (which models real‑world provenance metadata).

TAT's structural thesis and DanceNitra's object ledger turned out to be two halves of one detector.

## Known Limitations

The method requires role lines in the context. In the three false positive cases (ids 48, 54, 91), the target role matches neither context role line, so the reference is unresolvable. The correct behaviour in these cases is abstention, which a confidence threshold on the match score would provide.

A bare "go back" without any referent remains undecidable from text alone — it requires an authorization channel (ledger lookup or user confirmation).

## Licenses

- **Code** (notebooks, scripts): AGPL v3.0
- **Documentation, results, graphs**: CC BY‑NC‑ND 4.0
- **Data (fixtures)**: MIT (Rastislav Drahos)
- **Models (.pt)**: Custom TAT License

## Reproducibility

All Colab notebooks and prediction CSVs are available in this folder. The method requires only `sentence-transformers`, `scikit-learn`, and the public fixture files — no proprietary code, no API keys, no GPU.

*Published: 2026-07-11 21:16*
