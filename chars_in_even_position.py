
def chars_in_even_positions(stringy):
    """
    Receives a string and return all the character in the even positions
    """
    gum = ''
    for pos, char, in enumerate(stringy):
        if pos % 2 != 0:
            gum += char
    return gum


print(chars_in_even_positions("Marvelous"))
print(chars_in_even_positions("Python"))

# alternative solution
s = "Marvelous"
p = "Python"


def rough(t):
    f = ''
    for i in range(0, len(t)):
        if i % 2 != 0:
            f += t[i]
    return f


print(rough(s))
print(rough(p))
