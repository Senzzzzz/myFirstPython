import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(750, 250, 600, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.buttongroup1 = QButtonGroup(self)
        self.buttongroup2 = QButtonGroup(self)

        self.radio1 = QRadioButton("dogs", self)
        self.radio1.setStyleSheet("background-color: red;"
                                  "font-size: 30px;")
        self.radio2 = QRadioButton("cats", self)
        self.radio2.setStyleSheet("background-color: green;"
                                  "font-size: 30px;")
        self.radio3 = QRadioButton("hedgehogs", self)
        self.radio3.setStyleSheet("background-color: crimson;"
                                  "font-size: 30px;")
        self.radio4 = QRadioButton("bakenekos", self)
        self.radio4.setStyleSheet("background-color: orange;"
                                  "font-size: 30px;")

        self.buttongroup1.addButton(self.radio1)
        self.buttongroup1.addButton(self.radio2)
        self.buttongroup2.addButton(self.radio3)
        self.buttongroup2.addButton(self.radio4)

        vbox = QVBoxLayout()

        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(self.radio3)
        vbox.addWidget(self.radio4)

        central_widget.setLayout(vbox)

        self.radio1.toggled.connect(self.on_click)
        self.radio2.toggled.connect(self.on_click)
        self.radio3.toggled.connect(self.on_click)
        self.radio4.toggled.connect(self.on_click)

    def on_click(self):
        radio_button = self.sender()
        print(radio_button.text())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QIcon("guiimage.jpg"))
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
