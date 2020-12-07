# from datetime import date
# def libraryFine(d1, m1, y1, d2, m2, y2):
#     result = [d2-d1, m2-m1, y2-y1]
#
#     if result[1] < 0 and (result[0] <= 0 or result[0] > 0) and result[2] == 0:
#         return abs(500 * result[1])
#     elif result[0] < 0 and result[1] == 0 and result[2] == 0:
#         return abs(15 * result[0])
#     elif result[2] < 0:
#         return 10000
#     else:
#         return 0
#
#
# print(libraryFine(5, 5, 1014, 23, 2, 1014))


# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    candies_left = m - (n * (m // n))
    pris = s-1 + candies_left

    if pris > n:
        res = abs(n - pris)
    elif pris == 0:
        res = n
    else:
        res = pris


    return res


if __name__ == '__main__':
    file_name = 'prisoner.txt'
    fptr = open(file_name, 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()


# print(saveThePrisoner(7, 19, 2))
# print(saveThePrisoner(3, 7, 3))
# # # print(saveThePrisoner(5, 2, 1))
# # # print(saveThePrisoner(5, 2, 2))
# # print(saveThePrisoner(46934, 543563655, 46743))
# # print(saveThePrisoner(530, 533048047, 529))
# print(saveThePrisoner(352926151,380324688, 94730870))
# print(saveThePrisoner(94431605, 679262176, 5284458))
# print(saveThePrisoner(59, 78693934, 2))
# print(saveThePrisoner(46934, 543563655, 46743))
# print(saveThePrisoner(999999999, 29010, 1))
#print(saveThePrisoner(530, 533048047, 529))