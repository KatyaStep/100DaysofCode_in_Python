import collections
def merge_the_tools(string, k):
    number_of_groups = len(string) // k
    tmp_groups = []
    groups = []
    print(number_of_groups)
    for i in range(0, len(string), k):
        #if len(string[i + number_of_groups:]) <= len(string):
        tmp_groups.append(string[i:i + k])
    #
    #
    # print(len(groups))
    #
    # for i in range(len(groups)):
    #     groups.append(list(groups[i]))
    # for element in tmp_groups:
    #     groups.append(list(element))
    #
    # for element in groups:
    #     element.sort()
    #     print(*element, sep='')
    print(*tmp_groups, sep='\n')
    duplicates = ''
    groups = []
    for element in tmp_groups:
        for character in element:
            if character not in duplicates:
                duplicates = duplicates + character
        groups.append(duplicates)
        duplicates = ''

    print(*groups, sep='\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
