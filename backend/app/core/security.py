"""
Auth / security placeholders.

Why this file exists:
    Password hashing and JWT creation/verification are security-sensitive
    and used from multiple places (register, login, route protection).
    Keeping them in one module avoids copy-pasted crypto code and gives us
    a single spot to review during a security audit.

NOTE: These are placeholders only. Real implementations come later when
the auth feature is built - this skeleton just defines the shape.
"""

from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """Hash a plaintext password for storage. Not yet wired into a route."""
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plaintext password against a stored hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Create a signed JWT. Placeholder - not yet called from any route."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str) -> dict:
    """Decode and validate a JWT. Placeholder - not yet called from any route."""
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
