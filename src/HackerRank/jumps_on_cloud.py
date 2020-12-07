def jumping_on_clouds(arr):
    counter = list()
    step = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            if i not in counter:
                counter.append(i)
                step = 2
            if i == len(arr) - 2:
                step = 1
        else:
            step = -1

        i = i + step
    print(counter)
    print(len(counter)-1)


if __name__ == '__main__':
    #c = [0, 0, 0, 0, 1, 0]
    #c = [0, 0, 1, 0, 0, 1, 0]
    c = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    #c= [0, 0, 0, 0, 0, 0]

    jumping_on_clouds(c)
