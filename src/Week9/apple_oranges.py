import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, apple_tree_location, orange_tree_location, apples, oranges):

    apples_landed = 0
    oranges_landed = 0

    for apple in apples:
        landing = apple + apple_tree_location
        if landing >= s and landing <= t:
            apples_landed += 1

    for orange in oranges:
        landing = orange + orange_tree_location
        if landing <= t and landing >= s:
            oranges_landed += 1

    print(apples_landed, oranges_landed, sep='\n')


if __name__ == '__main__':

    file_name = 'input11.txt'

    if file_name:
        f = open(file_name, "rt")
    else:
        f = sys.stdin


    # while inL:
    #     print
    #     inL.rstrip()
    #     inL = f.readline()

    inL = f.readline()
    st = inL.split()

    start_house = int(st[0])

    end_house = int(st[1])

    inL = f.readline()
    ab = inL.split()

    apple_tree_location = int(ab[0])

    orange_tree_location = int(ab[1])

    inL = f.readline()
    mn = inL.split()

    number_of_apple = int(mn[0])

    number_of_oranges = int(mn[1])

    inL = f.readline()
    apples = list(map(int, inL.rstrip().split()))

    inL = f.readline()
    oranges = list(map(int, inL.rstrip().split()))

    countApplesAndOranges(start_house, end_house, apple_tree_location, orange_tree_location, apples, oranges)

    # countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])