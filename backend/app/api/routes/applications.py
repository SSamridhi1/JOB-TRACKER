"""
Application routes: create, list, retrieve, update, delete.
"""

from fastapi import APIRouter, HTTPException, status

from app.schemas.application import ApplicationCreate, ApplicationRead, ApplicationUpdate

router = APIRouter(prefix="/api/applications", tags=["applications"])


@router.post("", response_model=ApplicationRead, status_code=status.HTTP_201_CREATED)
def create_application(payload: ApplicationCreate):
    """Create a new job application. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("", response_model=list[ApplicationRead])
def list_applications():
    """
    List the current user's applications.
    Will later support search / filter / sort query params.
    Not yet implemented.
    """
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/{application_id}", response_model=ApplicationRead)
def get_application(application_id: int):
    """Retrieve a single application by id. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.put("/{application_id}", response_model=ApplicationRead)
def update_application(application_id: int, payload: ApplicationUpdate):
    """Update an application's fields. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(application_id: int):
    """Delete an application. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
