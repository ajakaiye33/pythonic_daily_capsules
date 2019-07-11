from word2number import w2n


def pare_int(string):
    """
    receives figers in words and return their related integers
    one => 1
    """
    return w2n.word_to_num(string)


print(pare_int("one"))
print(pare_int("twenty"))
print(pare_int("Two hundred and forty six"))
print(pare_int("twenty nine"))
