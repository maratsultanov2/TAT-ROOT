# TAT-ROOT

**TAT — Biological Memory for LLMs**

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://opensource.org/licenses/AGPL-3.0)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

---

## What is TAT

TAT is a long-term memory architecture for LLMs, inspired by biological processes.

### Key Mechanisms

| Mechanism | Description |
|---|---|
| **Mitosis** | Chunks divide when reaching 50 KB |
| **Apoptosis** | Obsolete chunks archive |
| **Coherence** | Semantic similarity measure (θ=1.987) |
| **Holographic memory** | Recovery from 42% of data |
| **Fractal compression** | 3→5→7→9→11→1 |

---

## Architecture

```
TAT-ROOT/
├── docs/
├── src/
├── examples/
├── tat_sabbath/
├── tat_apoptosis/
├── tat_mitosis/
└── tat_coherence/
```

---

## Quick Start

```python
from tat_coherence import coherence
from tat_mitosis import mitosis
from tat_apoptosis import apoptosis

# Coherence calculation
score = coherence(chunk1, chunk2, theta=1.987)

# Chunk division at 50 KB
new_chunks = mitosis(chunk)

# Clean obsolete chunks
clean_chunks = apoptosis(chunks, threshold=0.3)
```

---

## Installation

```bash
git clone https://github.com/maratsultanov2/TAT-ROOT.git
cd TAT-ROOT
pip install -r requirements.txt
```

---

## Links

- [TreeAngleTap](https://github.com/maratsultanov2/TreeAngleTap)
- [TAT-7](https://github.com/maratsultanov2/TAT-7)
- [TAT-ONE-TAP](https://github.com/maratsultanov2/TAT-ONE-TAP)

---

## Author

**Marat Sultanov**
Forklift operator by day, AI architect by night.
Built without grants, without a team, without a laptop.

- [GitHub](https://github.com/maratsultanov2)
- [Telegram](https://t.me/Marat_Sultanow)

---

## License

- Code: [AGPL-3.0](LICENSE-CODE)
- Data: [CC BY-NC-ND 4.0](LICENSE-DATA)

---

**Star if you find it useful!**

## Validation

TAT has been empirically validated on real-world data. See [docs/VALIDATION.md](docs/VALIDATION.md) for details.

> *"The θ=1.987 threshold mapped to Coherence head divergence — the design principle held on real data, not just synthetic."*
> — qingkong66, DeepSeek-V3 #1285


## Operational Envelope

TAT operates within a 93–96% sufficiency band derived from its internal constants. See:

- [English](docs/en/OPERATIONAL_ENVELOPE.md)
- [Русский](docs/ru/OPERATIONAL_ENVELOPE.md)
- [中文](docs/zh/OPERATIONAL_ENVELOPE.md)

Covered topics:
- The 93–96% envelope (7% and 4% constants)
- Sufficiency as a design constraint
- Downstream contract (three levels)
- Surface coherence (coined by @icophy)


## The Kettle Principle

TAT does not chase 100% accuracy. It operates at the level the task requires.

See:
- [English](docs/en/KETTLE_PRINCIPLE.md)
- [Русский](docs/ru/KETTLE_PRINCIPLE.md)
- [中文](docs/zh/KETTLE_PRINCIPLE.md)

This is the simplest explanation of why TAT doesn't optimize for 100% — and why sufficiency is not a compromise.


## Comparative Benchmark: TripleNet vs TAT-7

Split Fashion-MNIST, 5 tasks, continual learning. TAT-7 retains 79% memory vs 5% for unprotected TripleNet.

See:
- [English](docs/en/benchmarks/COMPARATIVE_BENCHMARK.md)
- [Русский](docs/ru/benchmarks/COMPARATIVE_BENCHMARK.md)
- [中文](docs/zh/benchmarks/COMPARATIVE_BENCHMARK.md)

Data: [CSV traces](data/)


## Cost Efficiency

TAT's chunk architecture reduces memory and token usage by 25–30×. For a typical agent system with 4 months of session logs: 24 MB → <1 MB storage, LLM costs from ~$24/month to <$1/month.

See the full analysis in [TAT-ONE-TAP → Cost Efficiency](https://github.com/maratsultanov2/TAT-ONE-TAP).
