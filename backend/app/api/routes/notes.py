"""
Notes routes.
"""

from fastapi import APIRouter, HTTPException, status

from app.schemas.note import NoteCreate, NoteRead

router = APIRouter(prefix="/api", tags=["notes"])


@router.post("/applications/{application_id}/notes", response_model=NoteRead, status_code=status.HTTP_201_CREATED)
def create_note(application_id: int, payload: NoteCreate):
    """Add a note to an application. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/applications/{application_id}/notes", response_model=list[NoteRead])
def list_notes(application_id: int):
    """List all notes for an application. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int):
    """Delete a note. Not yet implemented."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
