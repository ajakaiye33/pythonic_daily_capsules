
def subtract_reversed(lst):
    """
    Using while loop, the function should receive a list and subtract
    all the numbers, starting from the end.
    """
    # contr = 0
    # revr = lst[::-1]
    # while contr < len(revr):
    #     contr -=
    # return contr
    minus = "-"
    for i in lst[::-1]:
        minus + str(i)
    return minus


print(subtract_reversed([3, 7, 18]))
