def factoria(num):
    """
    Create the function factorial(num) that
    returns the factorial of the parameter.
    """
    counter = 1

    for i in range(1, num+1):
        counter *= i
    return counter


print(factoria(20))
