import math

# a = int(input())
# b = int(input())


# TODO: 1. find hypotenuse
# TODO: 2. find angle of a given triangle

def find_angle(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    angle_c = math.acos(b/hypotenuse)
    medium_in_triangle = 0.5 * math.sqrt(2 * a**2 + 2 * b**2 - hypotenuse**2)

    angle_b = round(math.degrees((hypotenuse/2 * angle_c)/medium_in_triangle))
    degree_sign = u'\N{DEGREE SIGN}'

    return f'{angle_b}{degree_sign}'

    #print('{:.2f}'.format(hypotenuse))
    #print(angle_c)


if __name__ == '__main__':
    angle = find_angle(1, 10)
    print(angle)
