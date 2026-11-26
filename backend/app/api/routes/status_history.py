"""
Status history routes.

Per the project brief: "Do not implement the feature yet. Only prepare
the structure for it." These endpoints exist so the API contract (URL,
method, request/response shape) is visible, but the bodies are placeholders.
"""

from fastapi import APIRouter, HTTPException, status

from app.schemas.status_history import StatusHistoryRead, StatusUpdate

router = APIRouter(prefix="/api/applications", tags=["status-history"])


@router.patch("/{application_id}/status", response_model=StatusHistoryRead)
def update_status(application_id: int, payload: StatusUpdate):
    """
    Change an application's current status and append a StatusHistory row.
    Not yet implemented.
    """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/{application_id}/history", response_model=list[StatusHistoryRead])
def get_status_history(application_id: int):
    """Return the full status history for an application. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
