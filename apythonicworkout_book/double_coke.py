
def who_is_next(names, r):
    """

    """
    for ind, val in enumerate(names, 1):

        if ind == r:
            names.append(val)
            names.append(val)
            names += names

            print(names)
    return val


print(who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 9))
