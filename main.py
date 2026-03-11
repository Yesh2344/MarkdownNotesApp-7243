import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from markdown_notes_app.config import get_config
from markdown_notes_app.notes import Notes
from markdown_notes_app.db import Database

app = FastAPI()

# Get configuration
config = get_config()

# Create a database connection
db = Database(config.db_url)

# Create a notes manager
notes = Notes(db, config.notes_dir)

@app.post("/notes")
async def create_note(title: str, content: str):
    """
    Create a new note.

    Args:
        title (str): Note title.
        content (str): Note content.

    Returns:
        JSONResponse: Note ID and creation date.
    """
    note_id = notes.create_note(title, content)
    return JSONResponse({"id": note_id, "created_at": notes.get_note_created_at(note_id)})

@app.put("/notes/{note_id}")
async def edit_note(note_id: int, title: str, content: str):
    """
    Edit an existing note.

    Args:
        note_id (int): Note ID.
        title (str): New note title.
        content (str): New note content.

    Returns:
        JSONResponse: Note ID and updated date.
    """
    notes.edit_note(note_id, title, content)
    return JSONResponse({"id": note_id, "updated_at": notes.get_note_updated_at(note_id)})

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    """
    Delete a note.

    Args:
        note_id (int): Note ID.

    Returns:
        JSONResponse: Note ID and deletion date.
    """
    notes.delete_note(note_id)
    return JSONResponse({"id": note_id, "deleted_at": notes.get_note_deleted_at(note_id)})

@app.get("/notes")
async def list_notes():
    """
    List all notes.

    Returns:
        JSONResponse: List of notes.
    """
    notes_list = notes.list_notes()
    return JSONResponse([{"id": note.id, "title": note.title, "content": note.content} for note in notes_list])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)