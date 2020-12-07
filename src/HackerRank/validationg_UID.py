import re

for _ in range(int(input())):
    res = re.findall(r"^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$", input())
    if res:
        print('Valid')
    else:
        print('Invalid')