s = 'hackerhappy'
t = 'hackerrank'
k = 9


# if s == t:
#     print('Yes')
# elif len(s) == len(t):
#     for i in range(len(s)-1):
#         if s[i] != t[i]:
#             if len(s[i:]) + len(t[i:]) <= k:
#                 print('Yes')
#             else:
#                 print('No')
# else:
#     if k % 2 != 0:
#         if abs(len(s) - len(t) % 2) != 0:
#             print('Yes')
#         else:
#             print('No')
#     else:
#         if abs(len(s) - len(t)) % 2 == 0:
#             print('Yes')
#         else:
#             print('No')


#     if len(s) > 1 and k > 1:
#         print('Yes')
#     else:
#         print('No')
# else:
#     if len(s) < len(t):
#         for i in range(len(t[:len(s)]) - 1):
#             if t[i] != s[i]:
#                 symbols_s = len(s[i:])
#                 symbols_t = len(t[i:])
#             else:
#                 symbols_s = 0
#                 symbols_t = len(t) - len(s)
#     elif len(s) > len(t):
#         for i in range(len(t)):
#             if t[i] != s[i]:
#                 symbols_t = len(t[i:])
#                 symbols_s = len(s[i:])
#             else:
#                 symbols_t = 0
#                 symbols_s = len(s) - len(t)
#     else:
#         symbols_t = len(t)
#         symbols_s = len(s)
#
#     if symbols_s + symbols_t <= k and symbols_s + symbols_t != 0:
#         print('Yes')
#     else:
#         print('No')


"Solution"

prefix = 0
for c1, c2 in zip(s, t):
    if c1 == c2:
        prefix += 1
    else:
        break

if k >= len(s) + len(t):
    print("Yes")
elif k >= len(s) + len(t) - 2 * prefix and k % 2 == (len(s) + len(t)) % 2:
    print("Yes")
else:
    print("No")