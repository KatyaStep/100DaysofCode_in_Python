
s = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()

    if len(command) > 1:
        getattr(s, command[0])(int(command[1]))
    else:
        getattr(s, command[0])()


print(f'{sum(s)}')
