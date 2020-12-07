cube = lambda x: x ** 3  # complete the lambda function


def recursion_fib(n):
    if n <= 1:
        return n
    else:
        return recursion_fib(n - 1) + recursion_fib(n - 2)


def fibonacci(n):
    # return a list of fibonacci numbers
    res = []

    for i in range(n):
        res.append(recursion_fib(i))

    return res


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
