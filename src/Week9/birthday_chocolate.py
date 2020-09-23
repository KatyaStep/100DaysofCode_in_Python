import collections
# def birthday(s, d, m):
#     chocolate_bars = 0
#     counter_for_list = 0
#     if len(s) < m:
#         return 0
#     while counter_for_list + m <= len(s):
#         if sum(s[counter_for_list:counter_for_list+m]) == d:
#             chocolate_bars += 1
#         counter_for_list += 1
#     return chocolate_bars
#
#
# print(birthday([1,1,1,1,1,1], 7, 7))


def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        j = i+1
        while j < n:
            if (ar[i] + ar[j]) % k == 0:
                count += 1
            j += 1
    return count


print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))