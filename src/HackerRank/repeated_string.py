from collections import Counter

def repeatedString(s, n):
    part_1 = s.count("a") * (n // len(s))
    part_2 = s[:n % len(s)].count("a")
    print(part_1 + part_2)


abc = 'aba'
print(repeatedString(abc, 10))

