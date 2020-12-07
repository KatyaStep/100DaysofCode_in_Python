from math import sqrt, ceil


def perfectSquares(l, r):
    # Getting the very first number
    number = ceil(sqrt(l));

    # First number's square
    n2 = number * number;

    # Next number is at the difference of
    number = (number * 2) + 1;
    magic_sqr_numbers = []
    # While the perfect squares
    # are from the range
    while ((n2 >= l and n2 <= r)):
        magic_sqr_numbers.append(n2)

        # Get the next perfect square
        n2 = n2 + number;

        # Next odd number to be added
        number += 2;
    print(magic_sqr_numbers)

print(perfectSquares(4, 9))


