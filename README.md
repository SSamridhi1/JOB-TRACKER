# Job Application Tracker

A full-stack app for tracking job applications, statuses, and notes — built
as a learning project to practice React, FastAPI, PostgreSQL, REST API
design, auth, testing, Docker, and CI/CD.

This repository is currently a **project skeleton**: folder structure,
config, models, schemas, and route contracts are in place, but business
logic is intentionally not implemented yet. Endpoints return `501 Not
Implemented` until each feature is built.

## Tech stack

| Layer     | Choice                                              |
|-----------|------------------------------------------------------|
| Frontend  | React + Vite (JavaScript), React Router, Axios       |
| Backend   | FastAPI, SQLAlchemy, Alembic, Pydantic, PyJWT         |
| Database  | PostgreSQL                                            |
| Infra     | Docker, Docker Compose, GitHub Actions                |

Deliberately **not** included: Redis, Kafka, microservices, or any
infrastructure beyond what a small full-stack app needs. See
`docs/architecture/README.md` for the reasoning.

## Getting started

```bash
# 1. Copy env files and fill in real values
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# 2. Start the full stack (Postgres + API + frontend)
docker compose up --build
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000 (interactive docs at `/docs`)
- Backend health check: http://localhost:8000/health

## Running tests

```bash
# Backend
cd backend && pytest

# Frontend
cd frontend && npm test
```

## Project structure

See the full tree in the pull request / project docs. High level:

```
backend/    FastAPI app (app/api, app/core, app/models, app/schemas, app/tests)
frontend/   React app (src/components, src/pages, src/routes, src/services)
docs/       ERD, API design, architecture notes, decision records
.github/    CI workflow
```

## Next steps (feature-by-feature)

1. Auth: register / login / JWT issuance and validation
2. Applications: CRUD
3. Status history: write-on-status-change + history retrieval
4. Notes: CRUD
5. Search / filter / sort on the applications list
6. Dashboard stats
7. Deployment

## Author

**Samridhi**
