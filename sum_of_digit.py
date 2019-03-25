def sum_of_digit(diggy):
    """
    Create the function sumOfDigits that adds
    individual digits of a number,
    and returns the sum.
    """
    packy = []
    stringy = str(diggy)
    for i in stringy:
        inty = int(i)
        packy.append(inty)
    return sum(packy)


print(sum_of_digit(414))
