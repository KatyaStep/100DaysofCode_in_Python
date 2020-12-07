import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[ 0 ])

    m = int(nm[ 1 ])

    arr = [ ]

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i][k] > arr[i + 1][k]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                is_sorted = False


    for el in arr:
        print(*el)
