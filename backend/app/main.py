"""
FastAPI application entrypoint.

Why this file exists:
    This is the single place that assembles the app: creates the FastAPI
    instance, wires up CORS, and includes every route module. Route files
    themselves know nothing about the app object - they just define an
    APIRouter - which keeps them testable in isolation and avoids one
    massive file with every endpoint in it.

Run locally with:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import applications, auth, dashboard, notes, status_history

app = FastAPI(
    title="Job Application Tracker API",
    description="Backend API for tracking job applications, statuses, and notes.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Every route module exposes an `APIRouter` - included here, not defined here.
app.include_router(auth.router)
app.include_router(applications.router)
app.include_router(status_history.router)
app.include_router(notes.router)
app.include_router(dashboard.router)


@app.get("/health", tags=["health"])
def health_check():
    """Basic liveness check used by Docker/CI to confirm the app is up."""
    return {"status": "ok"}
