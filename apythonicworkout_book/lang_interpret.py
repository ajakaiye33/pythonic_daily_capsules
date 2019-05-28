
def ubbi_dubbi():
    """
    receives a word to the "ubbi dubbi" language. That is every vowel letter in the
    word should be prefaced with "ub"
    """
    get_words = input("Let have your word > ")
    vow_letter = "aeiou"
    cob = []
    for letr in get_words:
        for apha in vow_letter:
            if letr == apha:
                seeyah = get_words.replace(letr, "ub")
    return seeyah


print(ubbi_dubbi())
