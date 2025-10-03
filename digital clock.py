import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap, QFontDatabase
from PyQt5.QtCore import Qt, QDateTime, QTimer, QTime


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(750, 250, 600, 200)
        self.setStyleSheet("background-color: black;")
        self.initUI()

    def initUI(self):
        self.label = QLabel(
            f"{QTime.currentTime().toString("hh:mm:ss AP")}", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: #14fc03;"
                                 "font-weight: bold;"
                                 "font-size: 120px;")
        self.font_id = QFontDatabase.addApplicationFont("Seven Segment.ttf")
        family = QFontDatabase.applicationFontFamilies(self.font_id)[0]
        font = f"{family}"
        self.label.setFont(QFont(font))
        self.setCentralWidget(self.label)

        self.current_time = QTimer(self)
        self.current_time.timeout.connect(self.update_time)
        self.current_time.start(1000)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.label.setText(current_time)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowTitle("Digital Clock")
    window.setWindowIcon(QIcon("pyqt5icons/alarm.jpg"))
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
