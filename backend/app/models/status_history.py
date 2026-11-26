"""
StatusHistory model.

Why this file exists:
    Every time an application's status changes, a row is (eventually)
    written here, giving a full audit trail (e.g. "12 Aug - APPLIED",
    "15 Aug - SCREENING"). This skeleton only prepares the table structure -
    the write-on-status-change logic is a future feature, not implemented
    yet, per the project brief.
"""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.core.database import Base


class StatusHistory(Base):
    __tablename__ = "status_history"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    application_id: Mapped[int] = mapped_column(
        ForeignKey("applications.id"), nullable=False, index=True
    )
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    changed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    application: Mapped["Application"] = relationship("Application", back_populates="status_history")
