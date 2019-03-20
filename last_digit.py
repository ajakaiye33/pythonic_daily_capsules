# The lastDigit function accepts two non-negative
# integer arguments and returns true or false
# if they have the same last digit.

# For example, lastDigit accepts two non-negative
# integer values. Return true if both
# number arguments have the same last digit,
# such as 27 and 57 and false if the last two
# digits are not equal, such as 998 and 999


def last_digit(first, second):
    """
    lastDigit accepts two non-negative
    integer values. Return true if both
    number arguments have the same last digit
    and false if otherwise
    """
    ab_first = str(first)
    ab_second = str(second)
    if ab_first[-1] == ab_second[-1]:
        return True
    return False


print(last_digit(33, 3))

#############################

# - INPUT: lastDigit(22,32);
# - OUTPUT: true
#
#
# - INPUT: lastDigit(77, 999);
# - OUTPUT: false
#
#
# - INPUT: lastDigit(33,3);
# - OUTPUT: true
