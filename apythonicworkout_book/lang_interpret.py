
def ubbi_dubbi():
    """
    receives a word and translate to the "ubbi dubbi" language. That is every vowel letter in the
    word should be prefaced with "ub"
    """
    result = []
    the_vowel = "aeiou"
    get_words = input("Let have your world > ")
    for i in get_words:
        if i in the_vowel:
            result.append(f"ub{i}")
        else:
            result.append(i)
    return "".join(result)


print(ubbi_dubbi())

# Bonus


def cap_ubbi():
    """
    if the word is capitalize, ubbi_dubbi translation should be capitalize
    """
    see_aske = input("The word")
    see_aske = see_aske.lower()
    gather = []
    vywel = "aioue"

    for k in see_aske:
        if k in vywel:
            gather.append(f"ub{k}")
        else:
            gather.append(k)

    return "".join(gather).title()


print(cap_ubbi())

Bonus


def remove_author(lst_name):
    temp_house = []
    for i in lst_name:
        temp_house.append(i.replace(i, "_"))
    return temp_house


print(remove_author(["Aloba", "Francis", "Nnamdi", "Osita", "Garry"]))
