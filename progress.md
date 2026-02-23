### Phase 0: Project Scaffolding ✅
- [x] Create directory structure and placeholder files
- [x] Initialize Git repository
- [x] Set up Python virtual environment (Python 3.12.9)
- [x] Install initial dependencies
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
- [ ] Task 4.2: Expand `README.md` with detailed setup instructions
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
- **Keep this document updated** – reflect progress and decisions.

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