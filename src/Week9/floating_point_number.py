import re

# number_of_tests = int(input())
#
# for _ in range(number_of_tests):
#     number = input()
#     if '.' in number:
#         try:
#             float(number)
#             print(True)
#         except ValueError:
#             print(False)
#     else:
#         print(False)

for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
