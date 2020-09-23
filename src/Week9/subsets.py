# number_of_cases = int(input())
# set_one = {1, 2, 3, 5, 6}
# set_two = {9, 8, 5, 6, 3, 2, 1, 4, 7}
# for _ in range(number_of_cases):
#     #length_of_set_one = int(input())
#     #set_one = set(input().split())
#     #length_of_set_two = int(input())
#     #set_two = set(input().split())
#     print(set_one.issubset(set_two))

set_a = set(input().split())
number_of_other_sets = int(input())
super_set = []
for _ in range(number_of_other_sets):
    set_b = set(input().split())
    super_set.append(set_a.issuperset(set_b))
if False in super_set:
    print(False)
else:
    print(True)
