from collections import  OrderedDict

number_of_items = int(input())
items_list = OrderedDict()

for i in range(number_of_items):
    item, price = input().rsplit(' ', 1)

    if item not in items_list:
        items_list[item] = int(price)
    else:
        items_list[item] = int(price) + items_list.get(item)

for key, val in items_list.items():
    print(key, val)

