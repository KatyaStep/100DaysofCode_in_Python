import collections


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    number_of_pairs = collections.Counter(ar)
    pairs = 0
    res = 0
    for value in number_of_pairs.values():
        res = value // 2
        pairs += res
    return pairs


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
