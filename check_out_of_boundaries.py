def out_of_boundaries(num):
    """
    Receives a number and returns "True" if it's greater than 10 OR less than 0
    and "False" otherwise.
    """
    if num > 10 or num < 0:
        return True
    return False


print(out_of_boundaries(7))
print(out_of_boundaries(12))
print(out_of_boundaries(-3))
