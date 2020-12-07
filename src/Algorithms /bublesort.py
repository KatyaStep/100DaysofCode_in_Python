#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    is_sorted = False
    count = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                count += 1
                is_sorted = False
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]} ')
    print(f'Last Element: {a[-1]}')


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
