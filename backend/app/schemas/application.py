"""
Pydantic schemas for Application.
"""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class ApplicationBase(BaseModel):
    company: str
    position: str
    location: str | None = None
    job_type: str | None = None
    application_date: date | None = None
    job_url: str | None = None
    salary_range: str | None = None


class ApplicationCreate(ApplicationBase):
    """Shape of the request body for POST /api/applications."""
    pass


class ApplicationUpdate(BaseModel):
    """Shape of the request body for PUT /api/applications/{id}. All optional."""
    company: str | None = None
    position: str | None = None
    location: str | None = None
    job_type: str | None = None
    application_date: date | None = None
    job_url: str | None = None
    salary_range: str | None = None


class ApplicationRead(ApplicationBase):
    """Shape of an Application as returned by the API."""
    id: int
    user_id: int
    current_status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
