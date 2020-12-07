s = input()
lower_case = []
upper_case = []
odd = []
even = []

for i in range(len(s)):
    if s[i].islower():
        lower_case.append(s[i])
    elif s[i].isupper():
        upper_case.append(s[i])
    elif int(s[i]) % 2 == 0:
        even.append(s[i])
    else:
        odd.append(s[i])

lower_case.sort()
upper_case.sort()
odd.sort()
even.sort()

print(''.join(lower_case+upper_case+odd+even))