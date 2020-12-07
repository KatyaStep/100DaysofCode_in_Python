from collections import deque

d = deque()

for _ in range(int(input())):

    cmd = input().split()
    print(cmd)
    print(len(cmd))

    if len(cmd) > 1:
        getattr(d, cmd[0])(cmd[1])
    else:
        getattr(d, cmd[0])()

print(*[item for item in d])
#print(d)