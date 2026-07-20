# TAT Publications

This page summarizes the peer‑reviewed and archived publications that validate the TAT framework across different domains. Together with the theoretical foundation and cross‑framework calibration, these publications form the core of the TAT‑ROOT ecosystem.

## 📊 Key Results at a Glance

| Domain | Method | Key Metric | DOI |
|--------|--------|------------|-----|
| **Agentic systems (revert detection)** | TAT‑Monitor | F1 = 0.926, AUROC = 0.986 | [10.5281/zenodo.21326757](https://doi.org/10.5281/zenodo.21326757) |
| **Condensed‑matter physics (spin‑charge separation)** | TAT‑Defense | Cross‑framework convergence | [10.5281/zenodo.21393316](https://doi.org/10.5281/zenodo.21393316) |

---

## 📄 Publication 1: TAT-Monitor

**Title:** *When the Benchmark Shortcut Becomes the Answer*  
**Authors:**  
- **Marat Sultanov** ([@maratsultanov2](https://github.com/maratsultanov2)) — Independent Researcher, Russian Federation  
- **Rastislav Drahos** ([@DanceNitra](https://github.com/DanceNitra)) — Agora Scientific, Czech Republic  

**Status:** Preprint / Zenodo archive (DOI)  
**Year:** 2026  
**DOI:** [10.5281/zenodo.21326757](https://doi.org/10.5281/zenodo.21326757)  
**Repository:** [TAT-ONE-TAP/tat_monitor](https://github.com/maratsultanov2/TAT-ONE-TAP/tree/main/tat_monitor)

### Problem
In agentic systems, users often revert a value without naming it explicitly. They refer to a role: “Do what the person responsible for access decided.” To detect such reverts, the system must resolve a chain: **role → anchor → old value**.

### Method
We developed **Direct Contextual Comparison**: cosine similarity between a candidate statement and role strings in the context. If the candidate is closer to the old role than to the new one — it is a revert.

### Key Results
- **F1 = 0.926**, **AUROC = 0.986** on the hardest v4 test set.
- Reproduced on two embedders: all‑MiniLM (0.905) and nomic (0.930).
- On real‑world mnemo data with provenance: **F1 = 0.895**, anchored recall improved from 14/26 to 26/26.

### Impact
Memory systems can detect reverts **without LLMs, without training, without GPUs** — and can be embedded into any agentic application with context and roles.

---

## 📄 Publication 2: Cross‑Framework Verification of Spin‑Charge Separation

**Title:** *Charge and Spin Response of One‑Dimensional Electron Delocalization Relation Networks*  
**Authors:**  
- **Guanghao Li** ([@luoxuejian000](https://github.com/luoxuejian000)) — Independent Researcher, Hefei, China  
- **Rastislav Drahos** ([@DanceNitra](https://github.com/DanceNitra)) — Agora Scientific, Czech Republic  
- **Marat Sultanov** ([@maratsultanov2](https://github.com/maratsultanov2)) — Independent Researcher, Russian Federation  

**Status:** Preprint / Zenodo archive (DOI)  
**Year:** 2026  
**DOI:** [10.5281/zenodo.21393316](https://doi.org/10.5281/zenodo.21393316)  
**Repository:** [luoxuejian000/edrn-dmrg-verification](https://github.com/luoxuejian000/edrn-dmrg-verification)

### Problem
How to test a theory without fitting data to a desired answer? In condensed‑matter physics, predicting scaling exponents for strongly correlated systems is notoriously hard.

### Method
We combined three independent diagnostic frameworks:
- **DMRG** (density matrix renormalization group) for numerical data.
- **Exact Bethe‑ansatz solutions** as theoretical anchors.
- **TAT‑Defense** as a blind structural diagnostic tool.

TAT ran on six DMRG datasets without prior knowledge of the physics, detecting:
- **Silence** on charge‑compressibility data (no structure to find).
- **Anchors at L=120 and 160** in U=1 data — later confirmed as numerical convergence artifacts (χ_max=100).
- **Boundary‑only anchors** in the clean U=2 positive control.

### Key Results
- The original prediction (charge compressibility α=1.75) was falsified.
- Revised prediction: spin gap scales as Δs ~ 1/L with α_spin = −0.94.
- The identity α_charge + α_spin = −1 was confirmed as a numerical manifestation of spin‑charge separation in the Mott insulator.

### Impact
TAT served as an independent diagnostic layer that converged on the same numerical boundary as DMRG and Bethe‑ansatz anchors **without being aligned** to them. This demonstrates that TAT can be a reliable tool for data‑quality assessment and cross‑framework verification.

---

## 🧠 Summary

TAT has been validated in two independent contexts:

| Domain | Method | Key Metric | DOI |
|--------|--------|------------|-----|
| **Agentic systems** | TAT‑Monitor | F1 = 0.926 | [10.5281/zenodo.21326757](https://doi.org/10.5281/zenodo.21326757) |
| **Condensed‑matter physics** | TAT‑Defense | Cross‑framework convergence | [10.5281/zenodo.21393316](https://doi.org/10.5281/zenodo.21393316) |

Both publications share the same core philosophy: **diagnose, don't prescribe — and let the data speak.**

---

## 🔗 Links

- [TAT‑ONE‑TAP](https://github.com/maratsultanov2/TAT-ONE-TAP) — code and modules
- [TAT‑ROOT](https://github.com/maratsultanov2/TAT-ROOT) — theory and documentation
- [EDRN verification repository](https://github.com/luoxuejian000/edrn-dmrg-verification) — DMRG data and analysis
