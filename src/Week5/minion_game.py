# from collections import Counter, defaultdict


# def minion_game(word, const=False):
#     comb_of_words = []
#     vowels = ['a', 'e', 'i', 'o', 'u']
#
#     for i in range(len(word)):
#         if not const:
#             if word[i] not in vowels and word[i:] not in comb_of_words:
#                 comb_of_words.append(word[i:])
#             if word[i] not in vowels:
#                 for j in range(-1, -(len(word[-i:])), -1):
#                     if word[-i:j] not in comb_of_words:
#                         comb_of_words.append(word[-i:j])
#         else:
#             if word[i] in vowels and word[i:] not in comb_of_words:
#                 comb_of_words.append(word[i:])
#             if word[i] in vowels:
#                 for j in range(-1, -(len(word[-i:])), -1):
#                     if word[-i:j] not in comb_of_words:
#                         comb_of_words.append(word[-i:j])
#
#     score = 0
#     counter_of_words = defaultdict()
#
#     for wrd in comb_of_words:
#         counter_of_words[wrd] = word.count(wrd)
#         score = sum(counter_of_words.values(), 0)
#
#     return score


# def main():
#     input_str = 'banana'
#     score_stuart = minion_game(input_str, False)
#     score_kevin = minion_game(input_str, True)
#
#     if score_stuart > score_kevin:
#         print('Stuart', score_stuart)
#     else:
#         print('Kevin', score_kevin)


def minion_game(s):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

if __name__ == '__main__':
    #main()
    s = 'BANANA'
    minion_game(s)
