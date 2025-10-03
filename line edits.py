import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(750, 250, 600, 600)
        self.initUI()

    def initUI(self):
        self.line_widget = QLineEdit(self)
        self.line_widget.setGeometry(0, 0, 200, 50)
        self.line_widget.setStyleSheet("font-size: 30px;")
        self.line_widget.setPlaceholderText("Enter text")

        self.button = QPushButton("Submit", self)
        self.button.setGeometry(200, 0, 100, 50)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        text = self.line_widget.text()
        print(text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QIcon("guiimage.jpg"))
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
