
"""
The program should asks the user to enter an english word. your program should
then print the word, translated into Pig Latin.
If the word begins with a vowel(a,e,i,o,u), then add way to the end of the word e.g
so "air" becomes "airway" eat becomes "eatway"
if the word begin with any other letter, put it on the end of the word and then add "ay"
so python  becomes "ythonpay"
"""


def pig_latin():
    your_word = input("type a word > ")
    vowel = "aeiou"
    if your_word[0] in vowel:
        wayword = your_word[1:] + "way"
    else:
        frst_word = your_word[0]
        wayword = your_word[1:] + frst_word + "ay"
    return wayword


print(pig_latin())
