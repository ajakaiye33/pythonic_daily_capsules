
def anagram(wrd1, wrd2):
    """
    Recives two strings and return True if the two are anagram and false if Otherwise
    """
    wrd1 = wrd1.upper()
    wrd2 = wrd2.upper()
    spt_w1 = list(wrd1)
    spt_w2 = list(wrd2)
    if len(spt_w1) == len(spt_w2):
        return True
    else:
        return False


print(anagram("tea", "Eat"))
print(anagram("skin", "sinks"))
print(anagram("Listen", "silent"))
print(anagram("tea", "treat"))
