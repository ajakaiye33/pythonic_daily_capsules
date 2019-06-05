
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
