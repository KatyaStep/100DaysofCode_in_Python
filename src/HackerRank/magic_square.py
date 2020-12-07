import math
import os
import random
import re
import sys


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    data_set = {
        0: [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        1: [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        2: [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        3: [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        4: [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        5: [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        6: [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        7: [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    }

    summary_squares = []
    count = 0
    k = 0
    l = 0

    for value in data_set.values():
        for i in value:
            for j in range(len(i)):
                # print(s[l][k], i[j])
                # print(abs(s[l][k] - i[j]))
                count += abs(s[l][k] - i[j])
                k += 1
            k = 0
            l += 1
            print('-----------')
        l = 0
        summary_squares.append(count)
        count = 0
        print('++++++++++++++++')
    #print(summary_squares)

    return min(summary_squares)


if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)

# 5 3 4
# 1 5 8
# 6 4 2
