"""
Dashboard routes: aggregate statistics for the logged-in user.
"""

from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/stats")
def get_stats():
    """
    Return aggregate counts (e.g. applications per status).
    No response_model yet - the exact shape will be decided when this
    feature is implemented. Not yet implemented.
    """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/recent")
def get_recent():
    """Return the user's most recently updated applications. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
