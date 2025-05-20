# ui/weather.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from core.weather_api import get_weather

class WeatherScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("weatherScreen")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        self.weather_label = QLabel("Loading weather...")
        self.weather_label.setObjectName("weatherLabel")
        layout.addWidget(self.weather_label)
        self.refresh()

    def refresh(self):
        weather = get_weather()
        self.weather_label.setText(weather)
