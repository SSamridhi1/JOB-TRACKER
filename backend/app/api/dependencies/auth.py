"""
Auth dependency placeholder.

Why this file exists:
    Protected routes (e.g. "GET /api/applications") need a way to say
    "this route requires a logged-in user". FastAPI's dependency injection
    pattern is the idiomatic way to do that: routes declare
    `user = Depends(get_current_user)` and FastAPI handles the wiring.

This is a placeholder - it is not yet imported by any route. It will be
completed once the login/JWT feature is implemented.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Placeholder dependency. Will eventually:
      1. Decode the JWT (app.core.security.decode_access_token)
      2. Look up the user in the database
      3. Return the User object, or raise 401 if invalid
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="get_current_user is not implemented yet",
    )
