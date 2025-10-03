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
        self.button1 = QPushButton("#1", self)
        self.button2 = QPushButton("#2", self)
        self.button3 = QPushButton("#3", self)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QHBoxLayout()

        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)

        central_widget.setLayout(vbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        for button in [self.button1, self.button2, self.button3]:
            button.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Arial;
                margin: 25px;
                padding: 15px;
                border: 5px solid yellow;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: black;
            }
            QPushButton#button1 {
                background-color: red;         
            }
            QPushButton#button2 {
                background-color: blue;
                           
            }
            QPushButton#button3 {
                background-color: crimson;           
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QIcon("guiimage.jpg"))
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
