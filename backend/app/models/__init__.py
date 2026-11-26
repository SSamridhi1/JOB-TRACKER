"""
Importing all models here ensures they are registered on `Base.metadata`
before Alembic autogenerates a migration, and before `Base.metadata.create_all()`
is called anywhere (e.g. in tests).
"""

from app.models.user import User
from app.models.application import Application
from app.models.status_history import StatusHistory
from app.models.note import Note

__all__ = ["User", "Application", "StatusHistory", "Note"]
