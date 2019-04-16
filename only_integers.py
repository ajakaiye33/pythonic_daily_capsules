
def only_integers(num1, num2):
    """
    Receives two numbers and returns the sum of them ONLY if they are both integers
    if that not the case, returns the string "invalid parameters"
    """

    if type(num1) == int and type(num2) == int:
        return num1 + num2

    return "Invalid parameters"


print(only_integers(2, "what"))
