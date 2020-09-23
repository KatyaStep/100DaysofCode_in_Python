


def staircase(n):
    symbol = '#'
    for i in (number+1 for number in range(n)):
        print((symbol*i).rjust(n))

staircase(5)