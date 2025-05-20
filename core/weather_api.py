# core/weather_api.py
import requests

def get_weather(lat=36.6, lon=-121.89):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url)
        data = response.json().get("current_weather", {})
        temp_c = data.get("temperature")
        wind = data.get("windspeed")
        temp_f = round(temp_c * 9 / 5 + 32) if temp_c is not None else "N/A"
        return f"Temp: {temp_f}°F\nWind: {wind} mph"
    except Exception as e:
        return f"[Weather Error] {e}"
