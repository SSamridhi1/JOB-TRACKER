"""
Auth routes: register, login, me.

Why this file exists:
    Grouping routes by resource (auth, applications, status_history, notes,
    dashboard) instead of one giant routes.py keeps each file small and
    lets multiple people work on different features without merge conflicts.

Skeleton only: each endpoint is declared with the correct path, method,
and response_model so the API contract is visible and testable from day
one, but the body just raises 501 until the feature is implemented.
"""

from fastapi import APIRouter, HTTPException, status

from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.user import UserCreate, UserRead

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate):
    """Create a new user account. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    """Authenticate a user and return a JWT. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/me", response_model=UserRead)
def get_me():
    """Return the currently authenticated user. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
