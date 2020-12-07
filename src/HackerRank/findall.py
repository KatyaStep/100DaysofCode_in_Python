import re

res = re.findall(r'(?<=[^AEIOUaeiou])[AEIOUaeiou]{2,}(?=[^AEIOUaeiou])', input())
# if res:
#     print(*res, sep='\n')
# else:
#     print(-1)
#res = []
#print(res if res else -1, sep='\n')
#escape special characters
#rabcdeefgyYhFjkIoomnpOeorteeeeet

