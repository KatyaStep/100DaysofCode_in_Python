import collections
import numpy as np
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    purchase = []
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                purchase.append(i+j)
    if purchase:
        return max(purchase)
    else:
        return -1

#a = [4, 6, 5, 3, 3, 1]
# a = [1, 2, 2, 3, 1, 2]
# def pickingNumbers(a):
#     a.sort()
#     subarray = []
#     subarray_len = 0
#     for i in range(len(a)):
#         for j in a[i:]:
#             if not subarray:
#                 subarray.append(a[i])
#             else:
#                 if min(subarray) == j or abs(min(subarray) - j) == 1:
#                     if max(subarray) == j or abs(max(subarray) - j) == 1:
#                         subarray.append(j)
#         print(subarray)
#         if len(subarray) > subarray_len:
#             subarray_len = len(subarray)
#         subarray = []
#
#     print(subarray_len)
#
#
# pickingNumbers(a)


def circularArrayRotation(a,k, queries):
    for i in range(len(queries)):
        queries[i] = a[(queries[i] - k) % len(a)]
    return queries

print(circularArrayRotation([1,2,3], 2, [0,1,2]))