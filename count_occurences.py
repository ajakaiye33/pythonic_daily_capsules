
def count_occurence(lst):
    """
    Receives a list as input and returns a dictionary that counts how many
    times the data in the list is repeated
    """
    dix = {}
    for i in lst:
        dix[i] = lst.count(i)
    return dix


print(count_occurence(["a", "b", "c", "a", "a", "b"]))
print(count_occurence(["a", "b", "c"]))
print(count_occurence([12, 42, 42]))
