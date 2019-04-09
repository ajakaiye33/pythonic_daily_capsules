
def only_integers(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 + num2

    return "Invalid parameters"


print(only_integers(2, "what"))
