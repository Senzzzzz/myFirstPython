import datetime
import time
import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon, QFont, QPixmap, QFontDatabase
from PyQt6.QtCore import Qt, QDateTime, QTimer, QTime, QElapsedTimer
import pytesseract


class Client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Placeholder")
        self.setGeometry(500, 200, 800, 800)
        self.initUI()

    def initUI(self):
        window = QWidget()

        self.label = QLabel("Placeholder", self)
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(0, 0, 150, 25)
        self.line_edit.setPlaceholderText("Enter a new task to add: ")

        self.button = QPushButton("Enter", self)
        self.button.setGeometry(100, 0, 100, 25)
        self.button.clicked.connect(self.on_click)

        layout = QHBoxLayout()
        layout.addWidget(self.line_edit)
        window.setLayout(layout)

    def on_click(self):
        text = self.line_edit.text()
        print(text)


def main():
    app = QApplication(sys.argv)
    client1 = Client()
    client1.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
