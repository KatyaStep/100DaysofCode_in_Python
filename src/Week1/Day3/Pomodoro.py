""" TODO1: get current datetime
    TODO2: define pomodoro timer ad deltatime (minutes = 25 )
    TODO3: while new datetime not equal current datetime plus deltatime print datetime.now()
"""
from datetime import datetime, timedelta
import time

timestamp = datetime.now()
timer = timedelta(minutes=2)


def pomodoro_timer(timestamp, timer):
    new_timestamp = timestamp + timer

    while True:
        if datetime.now() < new_timestamp:
            print(datetime.now().strftime('%H:%M:%S'))
            time.sleep(1)
        else:
            break
    return new_timestamp


def main():
    pomodoro_timer(timestamp, timer)


if __name__ == '__main__':
    main()
