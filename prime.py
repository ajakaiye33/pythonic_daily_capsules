def prime(num):
    """
    The function prime(num) accepts a number argument and returns the 
    boolean true if the number is a prime number otherwise it returns false.
    """

    if num % 2 != 0 and num > 1 and num != 2:
        return True
    else:
        return False


print(prime(199))


def factorize():

    num = int(input("e factor of what numer are you looking for?"))
    primy = []
    foo = range(num+1)
    bar = range(num+1)
    for i in foo:
        for y in bar:
            if i * y == num:
                primy.append(i)
    return primy


factoz = factorize()


def prime(factoz):
    if len(factoz) > 2:
        res = 'That number is not a prime'
    elif len(factoz) == 2:
        res = "Yeah, that's a prime"
    return res


print(prime(factoz))
