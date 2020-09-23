arr = [-4, 3,  -9,  0,  4,  1]


def plusMinus(arr):
    length_of_arr = len(arr)
    positive_elements = 0
    negative_elements = 0
    zero_elements = 0

    for item in arr:
        if item > 0:
            positive_elements += 1
        elif item < 0:
            negative_elements += 1
            continue
        else:
            zero_elements += 1

    prop_positive = positive_elements / length_of_arr
    prop_negative = negative_elements / length_of_arr
    prop_zero = zero_elements / length_of_arr

    print('{:.6f}\n{:.6f}\n{:.6f}'.format(prop_positive, prop_negative, prop_zero))


plusMinus(arr)
