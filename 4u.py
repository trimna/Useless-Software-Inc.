import sys
import os
import random
import time
import threading

import pyautogui
import keyboard

from PyQt5 import QtWidgets, uic


running = False


def resource_path(filename):
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        filename
    )


def click_randomly():
    global running

    width, height = pyautogui.size()

    while running:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        pyautogui.click(x, y)

        time.sleep(1)


def start_clicker():
    global running

    if not running:
        running = True

        threading.Thread(
            target=click_randomly,
            daemon=True
        ).start()


def stop_clicker():
    global running
    running = False


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi(
    resource_path("epicui.ui")
)


window.pushButton.clicked.connect(start_clicker)
window.pushButton_2.clicked.connect(stop_clicker)


keyboard.add_hotkey("f6", start_clicker)
keyboard.add_hotkey("f4", stop_clicker)


window.show()

try:
    sys.exit(app.exec_())
finally:
    keyboard.unhook_all()
