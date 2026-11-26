"""
Pydantic schemas for StatusHistory.

Skeleton only - matches the STATUS HISTORY REQUIREMENT in the project brief.
The endpoints that use these schemas are defined as placeholders and will
be implemented in a later feature pass.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class StatusUpdate(BaseModel):
    """Shape of the request body for PATCH /api/applications/{id}/status."""
    status: str


class StatusHistoryRead(BaseModel):
    id: int
    application_id: int
    status: str
    changed_at: datetime

    model_config = ConfigDict(from_attributes=True)
