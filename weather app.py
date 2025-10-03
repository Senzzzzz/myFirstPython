import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap, QFontDatabase
from PyQt5.QtCore import Qt, QDateTime, QTimer, QTime, QElapsedTimer
import pytesseract


api_path = "http://api.openweathermap.org/data/2.5/weather?"
api = "7ff86048a377b29917c48967a3575749"
city = "Tokyo"
url = api_path + "appid=" + api + "&q=" + city
response = requests.get(url).json()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700, 250, 400, 500)
        self.label = QLabel("Enter a city name: ", self)
        self.line_edit = QLineEdit("", self)
        self.button = QPushButton("Get Weather", self)
        self.label2 = QLabel("", self)
        self.label3 = QLabel("", self)
        self.label4 = QLabel("", self)
        self.initUI()

    def initUI(self):
        self.label.setStyleSheet(
            "font-size: 30px;")
        self.label.setMaximumHeight(40)
        self.label.setAlignment(Qt.AlignHCenter)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label3.setAlignment(Qt.AlignHCenter)
        self.label4.setAlignment(Qt.AlignHCenter)
        self.line_edit.setAlignment(Qt.AlignCenter)

        self.button.setStyleSheet("font-size: 20px;"
                                  "font-weight: bold;"
                                  "padding: 10px 0px;")
        self.line_edit.setStyleSheet("font-size: 25px;")
        self.label3.setStyleSheet("font-family: Segoe UI emoji;"
                                  "font-size: 140px")
        self.label4.setStyleSheet("font-size: 40px;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()

        vbox.addWidget(self.label)

        central_widget.setLayout(vbox)

        vbox2 = QVBoxLayout()

        vbox2.addWidget(self.line_edit)
        vbox2.addWidget(self.button)
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.label3)
        vbox2.addWidget(self.label4)

        vbox.addLayout(vbox2)

        self.button.clicked.connect(self.get_Weather)

        self.emojis = {
            "Mist": "🌁",
            "Clouds": "☁",
            "Clear": "☀",
            "Rain": "🌧",
            "Snow": "🌨"
        }

    def get_Weather(self):
        api = "7ff86048a377b29917c48967a3575749"
        city = self.line_edit.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

        try:
            response = requests.get(url)
            response.raise_for_status()
            self.data = response.json()

            if self.data["cod"] == 200:
                self.update_label()

        except requests.exceptions.HTTPError as HTTPError:
            match response.status_code:
                case 400: self.display_error_message("Bad request: \n Please check your input")
                case 401: self.display_error_message("Invalid API key")
                case 404: self.display_error_message("404 yo yo")
                case _: self.display_error_message(HTTPError)
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.TooManyRedirects:
            pass

    def display_error_message(self, message):
        self.label2.setText(message)
        self.label2.setStyleSheet("font-size: 25px;")
        self.label3.clear()
        self.label4.clear()

    def update_label(self):
        self.label2.setStyleSheet(
            "font-size: 50px;"
            "font-weight: bold;"
            "font-family: calibri")
        weather = self.data["weather"][0]["main"]
        for key, value in self.emojis.items():
            if key == weather:
                self.label3.setText(value)
                self.label4.setText(key)
        self.label2.setText(f"{self.data["main"]["temp"]}°C")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
