import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700, 250, 700, 700)
        self.setWindowIcon(QIcon("guiimage.jpg"))
        self.initUI()

        label = QLabel("TEXT TEXT", self)
        label.setGeometry(0, 0, 300, 300)  # display text
        label.setFont(QFont("Arial", 20))
        label.setStyleSheet("background-color: red;")

        label = QLabel(self)
        label.setGeometry(0, 0, 700, 700)

        pixmap = QPixmap("guiimage.jpg")
        label.setPixmap(pixmap)  # display image
        label.setScaledContents(True)
        label.setGeometry((label.width() - label.width()) // 2,
                          (label.height() - label.height()) // 2,
                          label.width(),
                          label.height())

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("1", self)
        label1.setStyleSheet("background-color: red")
        label2 = QLabel("2", self)
        label2.setStyleSheet("background-color: yellow")
        label3 = QLabel("3", self)
        label3.setStyleSheet("background-color: purple")  # layout
        label4 = QLabel("4", self)
        label4.setStyleSheet("background-color: green")

        vbox = QGridLayout()

        vbox.addWidget(label1, 0, 1)
        vbox.addWidget(label2, 0, 2)
        vbox.addWidget(label3, 1, 1)
        vbox.addWidget(label4, 1, 2)

        central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Sen's GUI")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
