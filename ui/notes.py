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

    def load_notes(self):
        if os.path.exists("notes.txt"):
            with open("notes.txt", "r") as f:
                self.notes_box.setText(f.read())

    def save_notes(self):
        with open("notes.txt", "w") as f:
            f.write(self.notes_box.toPlainText())
