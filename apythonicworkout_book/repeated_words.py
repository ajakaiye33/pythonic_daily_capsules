
from collections import Counter
import operator

# def most_repeated_word(wordy):
#     """
#     receives a sequence of strings and return the string that contains the greatest
#     number of repeated letters
#     """
#     container = []
#     new_word = ''.join(wordy)
#     return max(new_word)
#
#
# print(most_repeated_word(["this", "is", "a", "test", "program"]))


def most_repeated_word2(wordz):
    wordz = "".join(wordz)
    return Counter(wordz).most_common(1)[0][1]


print(most_repeated_word2(["this", "is", "a", "test", "program"]))


# Bonus problems

def repeated_vowel(the_word):
    vey = "aeiou"
    fry = []
    for i in the_word:
        if i in vey:
            fry.append(i)
    return Counter(fry).most_common(1)[0][0]


print(repeated_vowel("this word is good and its goodness can reflect on you"))
