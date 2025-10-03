import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700, 250, 600, 600)
        self.setWindowIcon(QIcon("guiimage.jpg"))
        self.initUI()

    def initUI(self):
        self.button = QPushButton("test", self)
        self.button.setGeometry(250, 150, 150, 100)
        self.button.setStyleSheet("font-size: 50px;")
        self.button.clicked.connect(self.on_click)

        self.label = QLabel("this is some text", self)
        self.label.setStyleSheet("font-size: 30px;")
        self.label.setGeometry(0, 0, 300, 100)

    def on_click(self):
        self.button.setText("doobiaho")
        self.button.setDisabled(True)
        self.label.setText("texttext")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowTitle("My GUI")
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
