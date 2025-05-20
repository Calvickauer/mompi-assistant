# ui/main_window.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
)
from PyQt5.QtCore import Qt
from ui.chat import ChatScreen
from ui.weather import WeatherScreen
from ui.notes import NotesScreen
from ui.extra import ExtraScreen

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MomPi Assistant")
        self.setObjectName("mainWindow")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        nav_bar = QHBoxLayout()
        nav_bar.setSpacing(10)
        nav_names = ["Chat", "Weather", "Notes", "Extra"]
        self.buttons = []

        for index, name in enumerate(nav_names):
            btn = QPushButton(name)
            btn.setObjectName(f"{name.lower()}NavButton")
            btn.clicked.connect(lambda _, i=index: self.stack.setCurrentIndex(i))
            self.buttons.append(btn)
            nav_bar.addWidget(btn)

        layout.addLayout(nav_bar)

        self.stack = QStackedWidget()
        self.stack.setObjectName("stackedScreens")
        self.chat_screen = ChatScreen()
        self.weather_screen = WeatherScreen()
        self.notes_screen = NotesScreen()
        self.extra_screen = ExtraScreen()

        for screen in [
            self.chat_screen, self.weather_screen,
            self.notes_screen, self.extra_screen
        ]:
            self.stack.addWidget(screen)

        layout.addWidget(self.stack)
