Absolutely! Let's create two separate documents:

1. **`README.md`** – the standard public-facing project README (best‑practice, concise, with placeholders for later completion).
2. **`PROGRESS.md`** – our internal co‑working document, containing the phased todo list, current status, working style, and AI context. This is the document we'll update together as we go.

---

## 📄 `README.md` (Standard Best‑Practice)

```markdown
# AI Singularity Clock

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3129/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)

An interactive web clock that visualises the gap between data, individual intuition, and cultural mood around the AI singularity.

**Live demo:** [Coming soon]  
**Status:** Active development

## Overview

The AI Singularity Clock is an **InformArt** piece – a philosophical tool wrapped in an analogue clock interface. It presents three hands:

- **Sentiment Hand** – placed by the user at the start of their session, before seeing any other data.
- **Data Hand** – a composite of objective AI‑progress signals (training compute, benchmark capabilities, research paper volume).
- **Vibe Hand** – an aggregated/curated representation of societal mood (admin‑set in v1).

After the user sets their own hand, the other two are revealed, inviting reflection on the tensions between information, personal feeling, and collective sentiment.

## Features

- 🕰️ Analogue clock face with three visually distinct hands.
- 🔒 **UX‑first**: Sentiment hand placed first – no data influence.
- 📊 Data hand updated periodically from public sources (Epoch AI, arXiv).
- 🌐 Self‑contained backend with PostgreSQL for historical tracking.
- 🎨 Deliberately human, non‑digital aesthetic.

## Tech Stack

| Component       | Technology                         |
|-----------------|------------------------------------|
| Backend         | Python 3.12 + FastAPI              |
| Database        | PostgreSQL (self‑hosted)           |
| Data pipeline   | Python scripts + Alembic           |
| Frontend        | Vanilla JavaScript (or minimal Svelte) |
| Deployment      | Render / Railway (free tier)       |

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL (or Docker)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Git-Lister/Singularity-Clock_Dev.git
   cd Singularity-Clock_Dev
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env` and fill in your PostgreSQL credentials.

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```

7. Serve the frontend:
   ```bash
   cd ../frontend
   npx http-server public
   ```

8. Open `http://localhost:8080` in your browser.

## Data Sources

- [Epoch AI](https://epoch.ai/data) – AI models and benchmarking datasets (CC BY licensed).
- [arXiv](https://arxiv.org/) – Publication counts for cs.AI category.

## Project Status

The project is in **Phase 1 (Data Pipeline)**. See [`PROGRESS.md`](./PROGRESS.md) for detailed tasks and current focus.

## Contributing

Contributions are welcome! Please read our [working style](#) (see `PROGRESS.md`) and open an issue or pull request.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.  
Data from Epoch AI is used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Acknowledgements

- [Epoch AI](https://epoch.ai) for providing open data on AI progress.
- The arXiv API team.
```

---

## 📄 `PROGRESS.md` (Internal Co‑working Document)

```markdown
# AI Singularity Clock – Progress & Co‑working Plan

*This document is our shared roadmap and task tracker. It will evolve as we build.*

## Core Principles (Priority Order)

1. **Philosophical clarity (D)** – The three‑hand structure and reveal order are inviolable.
2. **Public‑facing product (B)** – Usable, intuitive, explainable in 2‑3 sentences.
3. **Portfolio quality (C)** – Clean, documented, maintainable code.
4. **Personal learning (A)** – Explore new tools, but not at expense of above.

**Non‑negotiables:**
- User places Sentiment hand **first** – other hands revealed only after.
- Composite metric explainable in plain language.
- All data sources free, public, citeable.
- Analogue, human‑feeling UI – resist over‑digitisation.

## Development Phases & Tasks

*Checkboxes reflect current completion.*



*Last updated: 2026-02-23*
```

---

