
def concatenate_string(stringy1, stringy2):
    """
    A function that receives two strings and returns a new one containing both
    strings cocatenated
    """

    return "{} {}".format(stringy1, stringy2)


print(concatenate_string("Hello", "World"))
print(concatenate_string("Hello", ""))

# some other way...


def concatenate_string(string1, stringy2):
    """
    A function that receives two strings and returns a new one containing both
    strings cocatenated
    """
    return string1 + " " + stringy2


print(concatenate_string("Hello", "World"))
print(concatenate_string("Hello", ""))
