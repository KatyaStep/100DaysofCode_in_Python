arr = [1, 2, 3, 4, 5]

def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0

    arr.sort()

    max_sum = sum(arr[1:])
    min_sum = sum(arr[:-1])

    print(min_sum, max_sum)

miniMaxSum(arr)