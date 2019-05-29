
# def ubbi_dubbi():
#     """
#     receives a word and translate to the "ubbi dubbi" language. That is every vowel letter in the
#     word should be prefaced with "ub"
#     """
#     get_words = input("Let have your word > ")
#     vow_letter = "aeiou"
#     cob = []
#     for letr in get_words:
#         for apha in vow_letter:
#             if letr == apha:
#                 seeyah = get_words.replace(letr, "ub")
#     return seeyah
#
#
# print(ubbi_dubbi())


def deleh():
    the_choice = "elephant"
    the_serc = "aeiou"
    comb = []
    for i in the_choice:
        if i in the_serc:
            comb.append(f"ub{i}")
        else:
            comb.append(i)
    return "".join(comb)


print(deleh())
