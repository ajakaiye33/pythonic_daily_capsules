
def more_than_three(lst):
    """
    Receives a list and returns "True" if it has more than 3 elements and "False"
    if not
    """
    if len(lst) > 3:
        return True
    return False


print(more_than_three([1, 2, 3, 4, 5, 6]))
print(more_than_three([1, 2, 3]))
