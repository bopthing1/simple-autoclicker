import sys
import time
import threading
import mouse
import keyboard
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont, QIntValidator

F6_KEY = 16777269

windowClosed = False
interval = 0.0001
keyPressed = False
enabled = False

ticks = 1


def toggle():
    global enabled
    enabled = not enabled
    print(enabled)


keyboard.add_hotkey("f6", toggle)


def tickFunc(self):
    while True:
        global enabled
        global keyPressed
        global interval
        global windowClosed
        global ticks
        # print("TI")

        ticks = ticks + 1

        if windowClosed:
            print("loop breaking cuz window closed :(")
            break

        # print(keyboard.read_key())

        # if keyboard.read_key() == "f6":
        #     if not keyPressed:
        #         keyPressed = True
        #         enabled = not enabled
        #         print("PRESS")
        # elif not keyboard.read_key() == "f6":
        #     print("release")
        #     keyPressed = False

        # keyboard.read_key()

        if enabled:
            mouse.click("left")
            interval = float(self.interval.text())
            time.sleep(interval)


class Window(QWidget):
    # def keyPressEvent(self, event):
    #     # print(event.key())
    #         enabled = True
    #         print(enabled

    def __init__(self):
        super().__init__()

        self.setWindowTitle("simple autoclicker")
        self.setWindowIcon(QIcon("maps.ico"))
        self.setFixedSize(350, 340)

        MAIN_FONT = QFont("Arial", 14)
        BOLD_FONT = QFont("Arial", 14)
        BOLD_FONT.setBold(True)
        TITLE_FONT = QFont("Arial", 19)
        TITLE_FONT.setBold(True)

        self.title = QLabel("simple autoclicker", self)
        self.title.setFont(TITLE_FONT)

        intervalLabel = QLabel("interval:", self)
        intervalLabel.move(0, 40)
        intervalLabel.setFixedSize(340, 50)
        intervalLabel.setFont(MAIN_FONT)

        self.interval = QLineEdit(self)
        self.interval.setFont(MAIN_FONT)
        self.interval.setText(str(interval))
        self.interval.move(0, 80)
        self.interval.setValidator(QIntValidator(1, 2147483647, self))

        # buttonLabel = QLabel("button:", self)
        # buttonLabel.move(0, 120)
        # buttonLabel.setFixedSize(340, 50)
        # buttonLabel.setFont(MAIN_FONT)

        # self.buttonSelect = QLineEdit(self)
        # self.buttonSelect.setFont(MAIN_FONT)
        # self.buttonSelect.move(0, 160)
        # self.buttonSelect.setValidator(QIntValidator(1, 2147483647, self))

        tick = threading.Thread(target=tickFunc, args=(self,))
        tick.start()


app = QApplication(sys.argv)
window = Window()
window.show()

try:
    sys.exit(app.exec())
except SystemExit:
    print("closing window :(")
    windowClosed = True
