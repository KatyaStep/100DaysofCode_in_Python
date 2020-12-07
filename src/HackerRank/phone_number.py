import re

n = int(input())

for _ in range(n):
    number = re.search(r'^[7|8|9]\d{9}', input())
    if number:
        print('YES')
    else:
        print('NO')


# 3
# 8956324712
# FACBGEGADB
# 85234789651