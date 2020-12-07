from _collections import defaultdict

word_groups = defaultdict(list)

n_word, m_word = map(int, input().split())

# Appending words into group A
for i in range(n_word):
    word = input()
    word_groups['A'].append(word)

# Appending words into group B
for j in range(m_word):
    word = input()
    word_groups['B'].append(word)

for w_b in word_groups['B']:
    print('\n')
    for i, w_a in enumerate(word_groups['A']):
        if w_b == w_a:
            print(i+1, end=' ')
            #print(word_groups['A'].index(word_groups['A'][w]))


# print(f"Group A: {word_groups['A']}, Group B: {word_groups['B']}")
