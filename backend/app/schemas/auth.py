"""
Pydantic schemas for authentication endpoints.
"""

from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """Shape of the request body for POST /api/auth/login."""
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Shape of the response for a successful login."""
    access_token: str
    token_type: str = "bearer"
