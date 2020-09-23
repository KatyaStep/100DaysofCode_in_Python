def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return 'NO'
    elif x2 > x1 and v2 < v1:
        return 'YES'
    else:
        return 'NO'


print(kangaroo(21, 6, 47, 3))