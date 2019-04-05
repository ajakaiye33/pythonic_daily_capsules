
def append_x(stringy):
    """
    A function that receives a string and appends the character "X" to it ONLY if
    the string is not empty
    """

    if stringy != "":
        return stringy + "x"
    return " '' "


print(append_x("Hello"))
print(append_x(""))
