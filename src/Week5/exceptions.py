number_of_cases = int(input())
i = 0
for i in range(number_of_cases):
    try:
        a, b = input().split()
        try:
            print(int(a) / int(b))
        except ZeroDivisionError:
            print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print('Error Code:', e)



