from datetime import datetime
import os


# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'

    date1 = datetime.strptime(t1, fmt)
    date2 = datetime.strptime(t2, fmt)

    result = int((abs(date1-date2)).total_seconds())

    return str(result)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
