import unittest
from markdown_notes_app.notes import Notes
from markdown_notes_app.db import Database

class TestNotes(unittest.TestCase):
    def setUp(self):
        self.db_url = "sqlite:///test_notes.db"
        self.notes_dir = "/path/to/notes"
        self.db = Database(self.db_url)
        self.notes = Notes(self.db, self.notes_dir)

    def test_create_note(self):
        note_id = self.notes.create_note("Test Note", "Test Content")
        self.assertGreater(note_id, 0)

    def test_edit_note(self):
        note_id = self.notes.create_note("Test Note", "Test Content")
        self.notes.edit_note(note_id, "New Test Note", "New Test Content")
        self.notes_list = self.notes.list_notes()
        self.assertEqual(self.notes_list[0].title, "New Test Note")
        self.assertEqual(self.notes_list[0].content, "New Test Content")

    def test_delete_note(self):
        note_id = self.notes.create_note("Test Note", "Test Content")
        self.notes.delete_note(note_id)
        self.notes_list = self.notes.list_notes()
        self.assertEqual(len(self.notes_list), 0)

    def test_list_notes(self):
        self.notes.create_note("Test Note 1", "Test Content 1")
        self.notes.create_note("Test Note 2", "Test Content 2")
        notes_list = self.notes.list_notes()
        self.assertEqual(len(notes_list), 2)

if __name__ == "__main__":
    unittest.main()