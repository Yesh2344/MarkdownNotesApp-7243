import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_url: str):
        self.conn = sqlite3.connect(db_url)
        self.cursor = self.conn.cursor()

        # Create notes table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT,
                deleted_at TEXT
            )
        """)
        self.conn.commit()

    def create_note(self, title: str, content: str):
        """
        Create a new note.

        Args:
            title (str): Note title.
            content (str): Note content.

        Returns:
            int: Note ID.
        """
        self.cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        self.conn.commit()
        return self.cursor.lastrowid

    def edit_note(self, note_id: int, title: str, content: str):
        """
        Edit an existing note.

        Args:
            note_id (int): Note ID.
            title (str): New note title.
            content (str): New note content.
        """
        self.cursor.execute("UPDATE notes SET title = ?, content = ?, updated_at = ? WHERE id = ?", (title, content, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), note_id))
        self.conn.commit()

    def delete_note(self, note_id: int):
        """
        Delete a note.

        Args:
            note_id (int): Note ID.
        """
        self.cursor.execute("UPDATE notes SET deleted_at = ? WHERE id = ?", (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), note_id))
        self.conn.commit()

    def list_notes(self):
        """
        List all notes.

        Returns:
            list: List of notes.
        """
        self.cursor.execute("SELECT id, title, content FROM notes WHERE deleted_at IS NULL")
        return self.cursor.fetchall()

    def get_note_created_at(self, note_id: int):
        """
        Get note creation date.

        Args:
            note_id (int): Note ID.

        Returns:
            str: Note creation date.
        """
        self.cursor.execute("SELECT created_at FROM notes WHERE id = ?", (note_id,))
        return self.cursor.fetchone()[0]

    def get_note_updated_at(self, note_id: int):
        """
        Get note update date.

        Args:
            note_id (int): Note ID.

        Returns:
            str: Note update date.
        """
        self.cursor.execute("SELECT updated_at FROM notes WHERE id = ?", (note_id,))
        return self.cursor.fetchone()[0]

    def get_note_deleted_at(self, note_id: int):
        """
        Get note deletion date.

        Args:
            note_id (int): Note ID.

        Returns:
            str: Note deletion date.
        """
        self.cursor.execute("SELECT deleted_at FROM notes WHERE id = ?", (note_id,))
        return self.cursor.fetchone()[0]