import re, email.utils

#reg_pattern = r"^(\w+)\s[<']+(\w+\@\w+\.\w+)[>']+$"
reg_pattern = r"<([A-Za-z](\w|-|\.|_)+)@[A-Za-z]+\.[A-Za-z]{1,3}>"

n = int(input())
for _ in range(n):
    name, address = input().split()
    res = re.match(reg_pattern, address)
    if res:
        print(f'{name} {res.group()}')

    # res = re.match(reg_pattern, user_input)
    # if res:
    #     print(res)

# 2
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>