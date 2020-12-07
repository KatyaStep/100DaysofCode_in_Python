import itertools

a_list = '12233311'
#an_iterator = list(itertools.groupby(a_list))

for key, thing in itertools.groupby(input()):
    print(f'({int(key)}, {len(list(thing))})', end=" ")

#print(combo_list)
# for i, element in enumerate(combo_list):
#     print(len(combo_list[i]), combo_list[i][0])
    #print(', '.join(combo_list),)
    #print(f'(''.join({list(thing)[0]}, {key}))')