
def max_char(stringy):
    """
    Receives a string and returns the maximum character in it
    """
    if stringy != "":
        return max(stringy)
    elif stringy == "":
        return "''"


print(max_char("azq"))
print(max_char(""))
