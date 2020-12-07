number_of_cases = int(input())
# number_of_cases = 1
for _ in range(number_of_cases):
    size_of_cube = int(input())
    cube = map(int, input().split())
    l_cube = list(cube)
    arr = 0

    for i in range(len(l_cube) -1 ):
        start_point = 0
        new_l = []
        flag = 'Null'
        if l_cube[i] >= l_cube[i+1]:
            flag = 'Yes'
        elif l_cube[i] <= l_cube[i+1]:
            if l_cube[i+1] == l_cube[-1]:
                flag = 'Yes'
                break
            else:
                start_point = i+1
                new_l = l_cube[start_point:]
                break

    if len(new_l) > 1:
        for i in range(len(new_l)-1):
            if new_l[i] <= new_l[i+1]:
                flag = 'Yes'
            else:
                flag = 'No'
                break
    print(flag)







