
# def perimeter(n):
#     # your code
#     se = 0
#     for i in range(n+1):
#         se += i
#     return se * 4
#
#
# print(perimeter(5))


# The goal of this exercise is to convert a string to a new string where each
# character in the new string is "(" if that character appears only once in
# the original string, or ")" if that character appears more than once in the
# original string. Ignore capitalization when determining if a character is
# a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("


def duplicate_encode(stringy):
    dey = ''
    lty = list(stringy)
    for ind, vay in enumerate(lty):
        if lty.count(vay) > 2:
            print(")")
        else:
            print("(")


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
