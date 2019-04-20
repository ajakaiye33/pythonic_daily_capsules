
def all_common_element(lst1, lst2):
    """
    Receives two list and return the elements common
    """
    if isinstance(lst1, list) == True and isinstance(lst2, list) == True:
        sey1 = set(lst1)
        sey2 = set(lst2)
        fey = sey1.intersection(sey2)
        return fey
    else:
        return "Param not a type of list"


print(all_common_element([1, 5, 6, 4, 8], [1, 6, 10, 5]))
print(all_common_element([1, 5, 7, 1, 24], [1, 2, 3, 4]))
print(all_common_element([4, 5, 6, 7], [1, 2, 3]))
print(all_common_element([1, 5, 6, 4, 8], (1, 6, 10, 5)))


# lst1 = [1, 5, 6, 4, 8]
# sey = set(lst1)
# print(sey)
