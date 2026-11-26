"""
Pydantic schemas for Note.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NoteCreate(BaseModel):
    """Shape of the request body for POST /api/applications/{id}/notes."""
    content: str


class NoteRead(BaseModel):
    id: int
    application_id: int
    content: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
