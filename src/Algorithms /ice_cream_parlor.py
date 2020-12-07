import sys
from collections import defaultdict


# Complete the whatFlavors function below.
def whatFlavors(arr, money):
    b = defaultdict(list)
    #b = dict()
    items_in_menu = []

    for i in range(len(arr)):
        b[arr[i]].append(i+1)


    arr.sort()

    for j in range(len(arr)):
        if money - arr[j] > 0:
            search_elem = money - arr[j]
            # find if there is a search element in array
            if search_element(search_elem, arr, 0, len(arr) - 1):
                el1 = arr[j]
                el2 = search_elem
                if el1 == el2:
                    items_in_menu.extend(b[el1])
                else:
                    items_in_menu.extend(b[el1])
                    items_in_menu.extend(b[el2])
                break
            else:
                continue


    # for key, value in b.items():
    #     if value == el1 or value == el2:
    #         items_in_menu.append(key)
    #
    items_in_menu.sort()
    print(*items_in_menu)


def search_element(element, arr, left, right):
    #arr.sort()
    while left <= right:
        mid_point = left + ((right - left) // 2)
        if arr[mid_point] < element:
            left = mid_point + 1
        elif arr[mid_point] > element:
            right = mid_point - 1
        else:
            return True

    return False


if __name__ == '__main__':

    file_name = 'data2.txt'

    if file_name:
        f = open(file_name, "rt")
    else:
        f = sys.stdin

    inL = f.readline()
    st = inL.split()

    #t = int(input())
    t = int(st[0])

    for t_itr in range(t):
        inL = f.readline()
        mn = inL.split()
        money = int(mn[0])

        inL = f.readline()
        num = inL.split()
        n = int(num[0])

        inL = f.readline()
        cost = list(map(int, inL.rstrip().split()))

        whatFlavors(cost, money)