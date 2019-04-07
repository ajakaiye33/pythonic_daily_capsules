
def even_or_odd(num):
    """
    Function takes  in a number, and return whether it's even or odd
    """
    if type(num) == int:
        if num % 2 == 0:
            res = 'even'
        elif num % 3 == 0:
            res = 'odd'
        return res
    else:
        return 'multiples can only be found on numbers'


print(even_or_odd('she'))
