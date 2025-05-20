# core/squeekboard.py
import subprocess

def show_keyboard():
    try:
        subprocess.Popen(["squeekboard"])
    except Exception as e:
        print(f"[Keyboard Show Error] {e}")

def hide_keyboard():
    try:
        subprocess.call(["pkill", "squeekboard"])
    except Exception as e:
        print(f"[Keyboard Hide Error] {e}")
