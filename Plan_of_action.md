# AI Singularity Clock – Plan of Action

> **A living roadmap** for building an analogue clock that visualises the gap between data, individual intuition, and cultural mood around the AI singularity.

## Overview

The **AI Singularity Clock** is an interactive web‑based clock with three hands:
- **Sentiment Hand** – placed by the user at session start, before seeing any other data.
- **Data Hand** – a composite of objective AI‑progress signals (training compute, benchmark capabilities, research paper volume).
- **Vibe Hand** – an aggregated/curated representation of societal mood (admin‑set in v1).

The clock reveals all three hands after the user places theirs, inviting reflection on the tensions between information, personal feeling, and collective sentiment. This is an **InformArt** piece – the philosophical framing is central, not decorative.

## Core Principles (in priority order)

1. **Philosophical clarity (D)** – The three‑hand structure and reveal order must never be compromised.
2. **Public‑facing product (B)** – Usable, intuitive, and explainable in 2‑3 sentences.
3. **Portfolio quality (C)** – Clean, documented, maintainable code.
4. **Personal learning (A)** – Explore new tools and patterns, but not at the expense of the above.

**Non‑negotiables**:
- User places Sentiment hand **first** – other hands revealed only after.
- Composite metric must be explainable in plain language.
- All data sources free, public, and citeable.
- Analogue, human‑feeling UI – resist over‑digitisation.

## Tech Stack

| Layer       | Choice                         |
|-------------|--------------------------------|
| Backend     | Python + FastAPI               |
| Database    | PostgreSQL (self‑hosted)       |
| Data pipeline | Python scripts + Alembic     |
| Frontend    | Vanilla JS / Svelte (minimal)  |
| Deployment  | Render / Railway (free tier)   |
| Version control | Git + GitHub                 |

## Development Phases & Tasks

*This list is flexible – tasks may be reordered or refined as we learn.*

### Phase 0: Project Scaffolding ✅
- [x] Create directory structure and placeholder files
- [x] Initialize Git repository
- [x] Set up Python virtual environment (Python 3.12.9)
- [x] Install initial dependencies (`fastapi`, `uvicorn`, `requests`, `pandas`, `arxiv`, `apscheduler`, `pytest`, `epochai`, `python-dotenv`, `sqlalchemy`, `asyncpg`, `psycopg2-binary`)
- [x] Create `.gitignore` and basic `requirements.txt`
- [x] Create project skeleton (backend API placeholder, frontend scaffold)

### Phase 1: Backbone & Data Pipeline (Current)
- [x] **Task 1.1 (partial):** Design PostgreSQL schema and set up Alembic
- [ ] **Task 1.1 (continued):** Write ETL script to download/parse Epoch AI datasets into PostgreSQL
- [ ] Task 1.2: Write script to fetch arXiv submission counts
- [ ] Task 1.3: Implement normalisation functions (min‑max scaling per metric)
- [ ] Task 1.4: Implement weighting (compute 50%, capabilities 35%, papers 15%) and composite calculation
- [ ] Task 1.5: Store composite values in `composite_history` table and expose via API
- [ ] Task 1.6: Set up periodic update mechanism (cron/APScheduler)
- [ ] Task 1.7: Build FastAPI endpoint `/api/current` to return latest composite value

### Phase 2: Frontend & UX (Planned)
- [ ] Task 2.1: Design analogue clock face (SVG/Canvas) – static version
- [ ] Task 2.2: Implement three‑hand rendering with distinct styles
- [ ] Task 2.3: Build onboarding flow: blank clock → user places Sentiment hand → store in session
- [ ] Task 2.4: Fetch current Data hand value from backend and render alongside Vibe hand (admin‑curated constant)
- [ ] Task 2.5: Enforce reveal order (other hands only after Sentiment placed)
- [ ] Task 2.6: Apply analogue/human aesthetic styling

### Phase 3: Integration & Deployment (Planned)
- [ ] Task 3.1: Connect frontend to backend API (CORS, error handling)
- [ ] Task 3.2: Local end‑to‑end testing
- [ ] Task 3.3: Prepare deployment (backend on Render/Railway, frontend static hosting)
- [ ] Task 3.4: Set up environment variables for production
- [ ] Task 3.5: Deploy and verify

### Phase 4: Polish & Documentation (Planned)
- [ ] Task 4.1: Add loading states and graceful fallbacks
- [ ] Task 4.2: Write thorough `README.md` (this document will already exist, but expand with setup instructions)
- [ ] Task 4.3: Document composite metric in 2‑3 sentences for UI tooltip
- [ ] Task 4.4: Prepare portfolio write‑up

## Current Status

**Completed:** Phase 0, partial Phase 1 (database schema & Alembic setup).  
**Working on:** Task 1.1 – Loading Epoch AI datasets into PostgreSQL.  
**Next:** After successful data load, move to Task 1.2 (arXiv) and normalisation.

## Working Style (for AI & Human)

- **Small, testable increments** – we build piece by piece, verifying each step.
- **Explain reasoning** – AI should always explain *why* a suggestion is made, not just *what*.
- **Flag uncertainties** – if unsure, say so and ask clarifying questions.
- **Respect existing patterns** – don’t refactor without discussion.
- **Keep documentation updated** – this plan evolves with the project.

## For AI Assistants

*Start every session with this context:*

You are assisting with the **AI Singularity Clock** project.  
**Project goal:** Build an analogue web clock with three hands (Sentiment, Data, Vibe) where the user places their Sentiment hand first.  
**Current phase:** Phase 1 (data pipeline).  
**Current task:** Task 1.1 – Load Epoch AI datasets (models & benchmarks) into PostgreSQL using an ETL script.  
**Tech stack:** Python/FastAPI, PostgreSQL, Alembic, vanilla JS frontend.  
**Constraints:** Free data sources, no paid APIs, explainable composite, UX reveal order inviolable.  
**Repo:** https://github.com/Git-Lister/Singularity-Clock_Dev – refer to existing code when suggesting changes.  
**Working style:** Explain why, flag issues, ask if ambiguous, prefer incremental changes.

---

*This document is a living guide. Last updated: 2026-02-23.*