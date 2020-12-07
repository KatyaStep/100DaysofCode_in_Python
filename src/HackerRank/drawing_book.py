import os
import sys
import math
#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    # page = 0
    #
    # if p < n / 2:
    #     for i in range(n):
    #         if p == 1 or p == n:
    #             break
    #         else:
    #             if i != p:
    #                 if p % 2 == 0 and i % 2 == 0:
    #                     page += 1
    #                 elif p % 2 != 0 and i % 2 != 0:
    #                     page += 1
    #             else:
    #                 break
    #
    # else:
    #     for i in (reversed(range(n))):
    #
    #         if p == 1 or p == n:
    #             break
    #         # elif p % 2 != 0 and
    #         else:
    #             if i != p:
    #                 if p % 2 == 0 and i % 2 != 0:
    #                     page += 1
    #                 elif p % 2 != 0 and i % 2 == 0:
    #                     page += 1
    #             else:
    #                 if n - p == 1 and p % 2 != 0:
    #                     page += 1
    #                 break
    #
    # print(page)
    print(p / 2, n / 2 - p / 2)

    print(min(p // 2, n // 2 - p // 2)))

    return True

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()