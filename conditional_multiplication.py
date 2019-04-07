
def conditional_multiplication(logi, num):
    """
    Takes in boolean and a number, if the boolean is True, the number return is
    multiplied by 10. in other case, it returns it unchanged
    """

    if logi == True:
        return 10 * num
    return num


print(conditional_multiplication(True, 2))
print(conditional_multiplication(False, 5))
print(conditional_multiplication(True, 5))
print(conditional_multiplication(False, 5))
