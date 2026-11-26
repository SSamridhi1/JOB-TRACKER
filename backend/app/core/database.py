"""
Database connection setup.

Why this file exists:
    This is the ONE place that knows how to talk to Postgres. Every model
    and every route depends on `Base` (to define tables) and `get_db`
    (to get a session) from here, instead of each file creating its own
    engine. That keeps connection handling consistent and easy to change
    later (e.g. swapping to a connection pool, a different DB, etc).

No models or queries live in this file - only the plumbing.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All ORM models will inherit from this Base class.
Base = declarative_base()


def get_db():
    """
    FastAPI dependency that yields a database session and guarantees
    it gets closed afterwards, even if an exception is raised.

    Usage in a route:
        @router.get("/applications")
        def list_applications(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
