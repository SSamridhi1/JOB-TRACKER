"""
Pydantic schemas for User.

Why this file exists:
    ORM models (app/models) describe the DATABASE shape. Schemas describe
    the API's INPUT/OUTPUT shape. They're kept separate on purpose:
    - we never want to accidentally expose `password_hash` in an API response
    - request payloads (e.g. registration) don't map 1:1 to DB columns
      (e.g. plaintext `password` in, `password_hash` out)
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    full_name: str
    email: EmailStr


class UserCreate(UserBase):
    """Shape of the request body for POST /api/auth/register."""
    password: str


class UserRead(UserBase):
    """Shape of a User as returned by the API. Never includes password_hash."""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
