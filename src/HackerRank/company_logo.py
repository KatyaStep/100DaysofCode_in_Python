#!/bin/python3

import math
import os
import random
import re
import sys
import collections
import itertools


if __name__ == '__main__':
    s = input()
    new_s = sorted(s)
    c = collections.Counter(new_s)
    print(c)

    sort_letters = sorted(c.items(), key=lambda x: x[1], reverse=True)
    n_items = itertools.islice(sort_letters, 0, 3)
    for key, value in n_items:
        print(key, value)
