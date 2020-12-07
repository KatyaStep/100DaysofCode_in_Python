import itertools

n = int(input())
s = input().replace(' ', '')
k = int(input())

l = [x.strip() for x in s]
a = itertools.combinations(l, k)
y = [' '.join(i) for i in a]

count = 0
for i in y:
    if 'a' in i:
        count += 1
print(count)
print(f'Probability is {count/len(y):.4f}')