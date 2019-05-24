
def triangular_name():
    """
    A pragram that asks the user for their name and then produces a "name triangle"
    the first letter of their name, then the first two letters the the first three
    and so forth, until the name is writen o the final line.
    """
    get_name = input("want to see something magical? let have your name > ")
    glue = ''
    for index, letty in enumerate(get_name):
        glue += letty
        print(glue)


print(triangular_name())
