# ui/chat.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QLabel
)
from PyQt5.QtCore import Qt
from core.llm import ask_openai
from core.voice import transcribe_voice

class ChatScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("chatScreen")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.chat_output = QListWidget()
        self.chat_output.setObjectName("chatOutput")
        layout.addWidget(self.chat_output)

        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Ask something...")
        self.input_line.setObjectName("chatInput")
        layout.addWidget(self.input_line)

        button_row = QHBoxLayout()

        ask_btn = QPushButton("Ask")
        ask_btn.setObjectName("askButton")
        ask_btn.clicked.connect(self.handle_text_input)

        speak_btn = QPushButton("Speak")
        speak_btn.setObjectName("speakButton")
        speak_btn.clicked.connect(self.handle_voice_input)

        button_row.addWidget(ask_btn)
        button_row.addWidget(speak_btn)

        layout.addLayout(button_row)

    def add_message(self, text, sender="user"):
        label = QLabel(text)
        label.setWordWrap(True)
        label.setObjectName(f"{sender}Bubble")
        item = QListWidgetItem()
        item.setSizeHint(label.sizeHint())
        self.chat_output.addItem(item)
        self.chat_output.setItemWidget(item, label)
        self.chat_output.scrollToBottom()

    def handle_text_input(self):
        prompt = self.input_line.text().strip()
        if not prompt:
            return
        self.input_line.clear()
        self.add_message(f"You: {prompt}", sender="user")
        response = ask_openai(prompt)
        self.add_message(f"Assistant: {response}", sender="assistant")

    def handle_voice_input(self):
        self.add_message("Listening...", sender="user")
        result = transcribe_voice()
        if result:
            self.input_line.setText(result)
            self.handle_text_input()
        else:
            self.add_message("Sorry, couldn't understand that.", sender="assistant")
