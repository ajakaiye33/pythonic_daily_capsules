
def pig_latin():
    """
    The program should asks the user to enter an english word. your program should
    then print the word, translated into Pig Latin.
    If the word begins with a vowel(a,e,i,o,u), then add way to the end of the word e.g
    so "air" becomes "airway" eat becomes "eatway"
    if the word begin with any other letter, put it on the end of the word and then add "ay"
    so python  becomes "ythonpay"
    """

    your_word = input("type a word > ")
    vowel = "aeiou"
    if your_word[0] in vowel:
        wayword = your_word[1:] + "way"
    else:
        frst_word = your_word[0]
        wayword = your_word[1:] + frst_word + "ay"
    return wayword


print(pig_latin())

Bonus


def pig_latin2():
    """
    if the word contains two different vowels "way" should added at its end but if
    it contain one vowel the first word should placed at it end and subsequently add "ay"
    """
    the_vow = "aeiou"
    counter = []
    ask_word = input("Give us a word > ")
    for i in the_vow:
        if i in ask_word:
            counter.append(i)
            if len(counter) == 2:
                res = f"{ask_word}way"
            else:
                res = f"{ask_word[1:]}{ask_word[0]}ay"

    return res


print(pig_latin2())


def pig_latin3():
    fly = []
    vow_the = "aeiou"
    the_sentence = input("Lets have your sentence > ")
    for word in the_sentence.split():
        if word[0] in vow_the:
            fly.append(f"{word}way")
        else:
            fly.append(f"{word[1:]}{word[0]}ay")
    return " ".join(fly)


print(pig_latin3())


# Morsels python problem

def unique_only(lst):
    return [i for i in set(lst)]


print(unique_only([1, 2, 2, 1, 1, 3, 2, 1]))
# print(unique_only())

nums = [1, -3, 2, 3, -1]
sqr = [i**2for i in nums]
print(unique_only(sqr))
