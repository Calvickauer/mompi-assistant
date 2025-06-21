# ui/notes.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
import os

class NotesScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("notesScreen")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.notes_box = QTextEdit()
        self.notes_box.setObjectName("notesArea")
        layout.addWidget(self.notes_box)

        self.save_btn = QPushButton("Save Notes")
        self.save_btn.setObjectName("saveButton")
        self.save_btn.clicked.connect(self.save_notes)
        layout.addWidget(self.save_btn)

        self.load_notes()

    def _notes_path(self):
        """Return the path to the notes file inside the data directory."""
        return os.path.join("data", "notes.txt")

    def load_notes(self):
        path = self._notes_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            open(path, "a").close()
        with open(path, "r") as f:
            self.notes_box.setText(f.read())

    def save_notes(self):
        path = self._notes_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(self.notes_box.toPlainText())
