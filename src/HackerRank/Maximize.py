import itertools
from pprint import pprint

k, m = map(int, input().split())
sum_res = 0
lst = []
square_num = lambda x: pow(x, 2)
max_mode = 0

for _ in range(k):
    size, *l = map(int, input(). split())
    lst.append(list(l))

result = list(itertools.product(*lst))

for i in result:
    for j in range(len(i)):
        sum_res += square_num(i[j])
    if sum_res % m > max_mode:
        max_mode = sum_res % m
    sum_res = 0


pprint(result)
print('---------------')
print(max_mode)


# 3 998
# 67828645 425092764 242723908 669696211 501122842 438815206
# 625649397 295060482 262686951 815352670
# 100876777 196900030 523615865

# 3 1000
# 5 4
# 7 8 9
# 5 7 8 9 10