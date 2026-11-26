"""
User model.

Why this file exists:
    One model per file (instead of one giant models.py) keeps each table's
    definition easy to find and easy to review in a pull request. This is
    the standard convention in most professional FastAPI/SQLAlchemy repos.

Skeleton only: columns and relationships are defined, but no query logic
(create_user, get_user_by_email, etc.) lives here. That belongs in
app/services later.
"""

from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # One user has many applications.
    applications: Mapped[list["Application"]] = relationship(
        "Application", back_populates="user", cascade="all, delete-orphan"
    )
