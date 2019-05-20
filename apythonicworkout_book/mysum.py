
def mysum(*args):
    """
    Wriet a function that does the same thing as the built-in sum function
    mysum(2,3,6,89,)
    """

    adder = 0

    for i in args:
        adder += i
    return adder


print(mysum(1, 2, 3))
print(mysum(10, 20, 30, 40, 50))
#print(mysum([1, 2, 3]))
