#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


# def getTotalX(a, b):
#     # Write your code here
#     lcm = reduce(compute_lcm, a)
#     gcd_number = reduce(math.gcd, b)
#
#     count = 0
#     min_lcm = lcm
#
#     print(lcm, gcd_number)
#     # while min_lcm <= gcd_number:
#     #     if gcd_number % min_lcm == 0:
#     #         count += 1
#     #     min_lcm += lcm
#     #
#     # return count
#
#
# def compute_lcm(x, y):
#     # choose the greater number
#     if x > y:
#         greater = x
#     else:
#         greater = y
#
#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         greater += 1
#
#     return lcm
#
#
# if __name__ == '__main__':
#     # fptr = open(os.environ[ 'OUTPUT_PATH' ], 'w')
#     #
#     # first_multiple_input = input().rstrip().split()
#     #
#     # n = int(first_multiple_input[ 0 ])
#     #
#     # m = int(first_multiple_input[ 1 ])
#     #
#     # arr = list(map(int, input().rstrip().split()))
#     #
#     # brr = list(map(int, input().rstrip().split()))
#
#     arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
#     brr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print(getTotalX(arr, brr))
#
#     # fptr.write(str(total) + '\n')
#     #
#     # fptr.close()


# def compute_lcm(x, y):
#
#     lcm = (x*y) // math.gcd(x,y)
#
#     return lcm
#
# print(compute_lcm(25, 30))

def add_two(x):
    return x + 2


#print(list(map(add_two, [16, 36, 96])))

def my_min(a, b):
    return min(a, b)

print(reduce(my_min, [2, 4, 6]))