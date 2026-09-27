# Saudi Companies Encyclopedia

A scalable Saudi company encyclopedia and search platform built with Next.js, FastAPI, PostgreSQL/PostGIS, OpenSearch, Redis, and Docker.

This project intentionally uses demo data only and clearly marks it as non-authoritative.

## Architecture

- Frontend: Next.js + TypeScript + Tailwind CSS + App Router + Arabic RTL
- Backend: FastAPI + SQLAlchemy + Pydantic + Alembic
- Database: PostgreSQL + PostGIS
- Search: OpenSearch
- Cache: Redis
- Background jobs: Celery-ready service layer
- Infra: Docker Compose + GitHub Actions

## Structure

- `/frontend` – web app
- `/backend` – API and business logic
- `/infrastructure` – Docker and CI
- `/docs` – docs and architecture notes
- `/scripts` – helper scripts
- `/tests` – top-level tests

## Quick start

```bash
cp .env.example .env

docker compose up --build
```

Then open:

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/docs
- OpenSearch: http://localhost:9200

## Demo note

The data in this repository is DEMO DATA only. It does not represent the official Saudi company registry.

## License

MIT
