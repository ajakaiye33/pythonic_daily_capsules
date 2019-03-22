
def repeat_string(stringy, no):
    """
    function repeat that accepts two arguments...the string to repeat, and a number
    that represents how many times to repeat
    the string. Return a string that concatenates the number
    of times the string is repeated.
    """
    counter = 0
    horiz = ''

    while counter < no:
        horiz += stringy
        counter += 1
    return horiz


print(repeat_string('bye', 7))

#################################
# using forloop


def repeatstring(stingy, no):
    """
    function repeat that accepts two arguments...the string to repeat, and a number
    that represents how many times to repeat
    the string. Return a string that concatenates the number
    of times the string is repeated.
    """
    packup = ''
    for i in range(no):
        packup += stingy
    return packup


print(repeatstring('yo', 0))
