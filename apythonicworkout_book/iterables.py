
def even_odd_sums(lst):
    """
    Receives a list or tuple of numbers. Return a two-element list, containing(respectively)
    the sum of the even index numbers and the sum of the odd index numbers
    """
    even_result = 0
    odd_result = 0
    final_result = []

    for indyx, numbz in enumerate(lst):
        if indyx % 2 == 0:
            even_result += numbz
            final_result.append(even_result)
        elif indyx % 2 != 0:
            odd_result += numbz
            final_result.append(odd_result)
    return final_result[-2:]


print(even_odd_sums([10, 20, 30, 40, 50, 60]))
print(even_odd_sums([100, 200, 300, 400, 500, 600]))
print(even_odd_sums([5, 3, 9, 13, 21, 35, 37]))


def plus_minus(lsty):
    """
    Receives a list or tuple of numbers. return the result of alternatively adding
    and subtracting from each other
    """
    for indyx, numbz in enumerate(lsty):
        #lsty[0] + lsty[1] - lsty[2] + lsty[3] - lsty[4] + lsty[5]
        the_result = 0
        if indyx % 2 == 0:
            the_result -= numbz
        else:
            the_result += numbz
    return the_result


print(plus_minus([10, 20, 30, 40, 50, 60]))

# Bonus


def myzip(ls1, ls2):
    """
    Emulate the built-in zip function, that takes any number of iterables and return
    a list of tuple
    """
    fr = []
    for i in range(len(ls1)):
        fr.append((ls1[i], ls2[i]))
    return fr


print(myzip([10, 20, 30], "abc"))


def to_letters(ls):
    """
    Receives a list which contains any number of elements of any type. Modify this
    list such that it contains six elements, each of which is the letter "a"
    """
    com = []
    for i in ls[0:7]:
        com.append("a")
    return com


print(to_letters([1, 2, 3, 4, 5, 6, 7, 8, 10]))
