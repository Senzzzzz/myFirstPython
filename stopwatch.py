import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap, QFontDatabase
from PyQt5.QtCore import Qt, QDateTime, QTimer, QTime, QElapsedTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 250, 500, 300)
        self.label = QLabel("00:00:00", self)
        self.timer = QTimer()
        self.time = QTime(0, 0, 0, 0)
        self.initUI()

    def initUI(self):
        self.label.setStyleSheet("background-color: #42c2f5;"
                                 "font-size: 60px;"
                                 "font-weight: bold;")

        self.label.setAlignment(Qt.AlignCenter)

        self.button1 = QPushButton("Start", self)
        self.button2 = QPushButton("Stop", self)
        self.button3 = QPushButton("Reset", self)

        self.setStyleSheet("""
            QPushButton {
                padding: 10px;
                font-size: 30px;
                font-weight: bold;

            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()

        vbox.addWidget(self.label)
        central_widget.setLayout(vbox)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        vbox.addLayout(hbox)

        self.button1.clicked.connect(self.start)
        self.button2.clicked.connect(self.stop)
        self.button3.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.label.setText("00:00:00")

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}:{miliseconds:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.label.setText(self.format_time(self.time))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowTitle("Stop Watch")
    window.setWindowIcon(QIcon("pyqt5icons/guiimage.jpg"))
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
