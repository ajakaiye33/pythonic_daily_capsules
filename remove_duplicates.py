
def remove_duplicate(lst):
    """
    Receives a list and return it without duplicate. ie return a list with unique elements
    """
    re_dup = set(lst)
    return list(re_dup)


print(remove_duplicate([5, 6, 1, 1, 1, 7, 7, 2, 6, 5]))
