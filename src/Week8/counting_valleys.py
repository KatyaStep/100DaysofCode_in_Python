#!/bin/python3

import math
import os
import random
import re
import sys
import collections


# Complete the countingValleys function below.
def counting_valleys(n, s):
    # numbers = []
    # hiking_route = 0
    # calc_route = []
    # valley = 0
    # for letter in s:
    #     if letter == 'U':
    #         numbers.append(1)
    #     else:
    #         numbers.append(-1)
    #
    # for number in numbers:
    #     hiking_route += number
    #     calc_route.append(hiking_route)
    #
    # print(f'hiking_route:{numbers}')

    # while True:
    #     if -1 in calc_route and 0 in calc_route and calc_route:
    #         below_zero = calc_route.index(-1)
    #         sea_level = calc_route.index(0)
    #         if sea_level < below_zero:
    #             calc_route.remove(sea_level)
    #         else:
    #             del calc_route[below_zero:sea_level+1]
    #             valley += 1
    #         print(calc_route)
    #     else:
    #         break
    # return valley
    cur_pos = 0
    mode = ''
    valley_counter = 0

    for item in s:
        if item == 'U':
            cur_pos += 1
        else:
            cur_pos -= 1
        #if not mode:
        if cur_pos > 0:
            mode = 'm'
        if cur_pos < 0:
            mode = 'v'

        if cur_pos == 0 and mode == 'v':
            valley_counter += 1
            continue

    return valley_counter

if __name__ == '__main__':
    # n = int(input())

    # s = input()

    n = 100
    #s = 'DDUUDDUDUUUD'
    #s = 'DDUDDUUDUU'
    s = 'UDDDUDUU'
    #s = 'DDUDUDDUDDUDDUUUUDUDDDUUDDUUDDDUUDDUUUUUUDUDDDDUDDUUDUUDUDUUUDUUUUUDDUDDDDUDDUDDDDUUUUDUUDUUDUUDUDDD'
    result = counting_valleys(n, s)

    print(result)
