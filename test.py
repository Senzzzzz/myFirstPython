import datetime
import time


while True:
    date = datetime.datetime.now()
    time.sleep(1)
    print(date.strftime("%H:%M:%S"))
