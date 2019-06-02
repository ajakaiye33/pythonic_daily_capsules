
def firstlast(seq):
    """
    receives a sequence example string, list tuple and returns the first and last
    elements of that sequence in a two element of the same type
    """

    result = []

    first_element = seq[0]
    laste_element = seq[-1]
    result.append(first_element)
    result.append(laste_element)
    return result


print(firstlast("abc"))
print(firstlast([1, 2, 3, 4, 5]))
