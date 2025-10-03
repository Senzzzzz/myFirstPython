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
        self.label = QLabel("", self)
        self.label.setGeometry(200, 150, 200, 200)
        self.label.setStyleSheet("background-color: purple;")

        self.checkbox = QCheckBox("text", self.label)
        self.checkbox.setStyleSheet("font-size: 50px")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.on_click)

    def on_click(self, state):
        if state == Qt.Checked:  # check if state is = 2. 2 = checked, 0 = unchecked
            print("box is checked")
        else:
            print("box unchecked")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QIcon("guiimage.jpg"))
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
