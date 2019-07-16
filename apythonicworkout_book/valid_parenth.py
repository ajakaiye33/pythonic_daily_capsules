def first_non_repeating_letter(stringy):
    """
    receives a string and return the first no-repeating letter
    """
    stringy_lower = stringy.lower()

    for i, j in enumerate(stringy_lower):
        if stringy_lower.count(j) == 1:
            return stringy_lower[i]
    return "''"


print(first_non_repeating_letter('stress'))
