# to be continued ...
# def triple_double(num1, num2):
#     """which takes numbers num1 and num2 and returns 1 if there is a
#     straight triple of a number at any place in num1 and also a straight
#     double of the same number in num2.If this isn't the case, return 0"""
#     vt = 0
#     frst = list(str(num1))
#     scd = list(str(num2))
#
#
# print(triple_double(451999277, 41177722899))


def split_string(stringy):
    """Complete the solution so that it splits the string into pairs of two characters.
    If the string contains an odd number of characters then it should replace the
    missing second character of the final pair with an underscore ('_').
    Examples:
    solution('abc') # should return ['ab', 'c_']
    solution('abcdef') # should return ['ab', 'cd', 'ef']"""
    sey = [stringy[i:i+2] for i in range(0, len(stringy), 2)]
    return sey


print(split_string("abc"))
print(split_string("abcdef"))
