from collections import Counter

number_of_words = int(input())

word_list = [input() for i in range(number_of_words)]
x = Counter([word for word in word_list])


print(len(x))
print(*x.values())


