# Dominic Jason 2203959

word = input()
no_spaces = word.replace(' ', '')


def reverseword(word_no_spaces):
    return word_no_spaces[::-1]


word2 = reverseword(no_spaces)


if no_spaces == word2:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')
