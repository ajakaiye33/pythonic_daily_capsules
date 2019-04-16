#
def insert_dashes(stringy):
    """
    Receives a string and insert dashes every 3 characters
    """
    counter = 1
    dash = "-"
    for i in stringy:
        res += char
        if counter == 3:
            res += dash
            counter = 1
        else:
            counter += 1
    return res


print(insert_dashes("Hello world"))


def digy(s):
    da = "-"
    sey = list(s)
    for i in range(1, len(s)):
        if i % 3 == 0:
            sey.insert(i, "-")
            gey = "".join(sey)

    return gey


print(digy("awesomePythonRmotr"))


dey = "awesomePythonRmotr"
