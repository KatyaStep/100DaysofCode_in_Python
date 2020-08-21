from collections import Counter, defaultdict

# word = input()
word = 'banana'
vowels = ['a', 'e', 'i', 'o', 'u']

all_consonant_words = []
all_vowels_words = []


def words_start_with_consonants(word):
    for i in range(len(word)):
        if word[i] not in vowels and word[i] not in all_consonant_words:
            all_consonant_words.append(word[i:])
        if word[i] in vowels and word[i] not in all_vowels_words:
            all_vowels_words.append(word[i:])

    return all_consonant_words, all_vowels_words


def create_new_words(consonant_words, vowels_words):
    for i, item in enumerate(consonant_words):
        for j in range(len(item)):
            if item[:j - 1] not in all_consonant_words and item[:j - 1] != '':
                all_consonant_words.append(item[:j - 1])

    for i, item in enumerate(vowels_words):
        for j in range(len(item)):
            if item[:j - 1] not in all_vowels_words and item[:j - 1] != '':
                all_vowels_words.append(item[:j - 1])

    repetition_counter1 = defaultdict()
    repetition_counter2 = defaultdict()
    #
    for wrd in all_consonant_words:
        repetition_counter1[wrd] = word.count(wrd)
    #
    for vowel in all_vowels_words:
        repetition_counter2[vowel] = word.count(vowel)
    #
    print(all_consonant_words)
    print(all_vowels_words)
    # print(repetition_counter1)
    #
    score1 = sum(repetition_counter1.values(), 0)
    score2 = sum(repetition_counter2.values(), 0)
    #
    print(f'Score1:{score1}, Score2:{score2}')
    


def main():
    consonant_words, vowels_words = words_start_with_consonants(word)
    #print(vowels_words, consonant_words)
    create_new_words(consonant_words, vowels_words)


if __name__ == '__main__':
    main()
