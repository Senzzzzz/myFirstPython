import datetime
import time
import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap, QFontDatabase
from PyQt5.QtCore import Qt, QDateTime, QTimer, QTime, QElapsedTimer
import pytesseract


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 300, 600, 500)
        self.setWindowIcon(QIcon("pyqt5icons/sunny.jpg"))
        label = QLabel("asdasd", self)
        piximap = QPixmap("pyqt5icons/guiimage.jpg")
        piximap.scaled(label.width(), label.height())
        label.setGeometry(0, 0, 550, 450)
        label.setPixmap(piximap)
        label.show()

    def initUi():
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
