"""
Application model - represents a single job application.

Why this file exists:
    This is the core entity of the whole product. It intentionally has NO
    business logic (no "apply()" or "mark_rejected()" methods) - just
    columns and relationships. Keeping ORM models "dumb" (data-only) and
    putting behaviour in app/services is a deliberate architectural choice
    that keeps the model layer easy to test and reason about.
"""

from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)

    company: Mapped[str] = mapped_column(String(255), nullable=False)
    position: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    job_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    application_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    job_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    salary_range: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # Stored as plain string for now; matches the fixed set of statuses
    # defined in app/constants (frontend) / to be enforced with a Python
    # Enum once the status-update feature is implemented.
    current_status: Mapped[str] = mapped_column(String(50), nullable=False, default="WISHLIST")

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # --- Relationships ---
    user: Mapped["User"] = relationship("User", back_populates="applications")

    status_history: Mapped[list["StatusHistory"]] = relationship(
        "StatusHistory", back_populates="application", cascade="all, delete-orphan"
    )

    notes: Mapped[list["Note"]] = relationship(
        "Note", back_populates="application", cascade="all, delete-orphan"
    )
