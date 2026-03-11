import os
import logging
from typing import List
from markdown_notes_app.db import Database

class Note:
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content

class Notes:
    def __init__(self, db: Database, notes_dir: str):
        self.db = db
        self.notes_dir = notes_dir

    def create_note(self, title: str, content: str):
        """
        Create a new note.

        Args:
            title (str): Note title.
            content (str): Note content.

        Returns:
            int: Note ID.
        """
        note_id = self.db.create_note(title, content)
        return note_id

    def edit_note(self, note_id: int, title: str, content: str):
        """
        Edit an existing note.

        Args:
            note_id (int): Note ID.
            title (str): New note title.
            content (str): New note content.
        """
        self.db.edit_note(note_id, title, content)

    def delete_note(self, note_id: int):
        """
        Delete a note.

        Args:
            note_id (int): Note ID.
        """
        self.db.delete_note(note_id)

    def list_notes(self):
        """
        List all notes.

        Returns:
            List[Note]: List of notes.
        """
        notes_list = self.db.list_notes()
        return [Note(note[0], note[1], note[2]) for note in notes_list]

    def get_note_created_at(self, note_id: int):
        """
        Get note creation date.

        Args:
            note_id (int): Note ID.

        Returns:
            str: Note creation date.
        """
        return self.db.get_note_created_at(note_id)

    def get_note_updated_at(self, note_id: int):
        """
        Get note update date.

        Args:
            note_id (int): Note ID.

        Returns:
            str: Note update date.
        """
        return self.db.get_note_updated_at(note_id)

    def get_note_deleted_at(self, note_id: int):
        """
        Get note deletion date.

        Args:
            note_id (int): Note ID.

        Returns:
            str: Note deletion date.
        """
        return self.db.get_note_deleted_at(note_id)