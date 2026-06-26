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