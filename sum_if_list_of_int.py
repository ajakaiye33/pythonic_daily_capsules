
def sum_if_list_of_int(lst_str):
    """
    Receives a list and use a loop to make sure the list only contain integers
    if so, it returns the sum of the integers if not returns "not an int"
    """
    for letr in lst_str:
        if not isinstance(letr, int):
            return "not an int"

    return sum(lst_str)


print(sum_if_list_of_int([]))
print(sum_if_list_of_int([1, 2, 3]))
print(sum_if_list_of_int([1, "a", 3]))
