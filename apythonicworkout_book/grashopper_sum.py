
def grasshoper_sum(n1, n2):
    """
    write a program that finds the summation of every number between 1 and number
    The number will always be a positive interger greater than 0
    """
    n2 = abs(n2)
    if n2 > 0:
        fry = list(range(n1, n2))
        print(fry[n1:n2])
    return sum(fry[n1:n2])


print(grasshoper_sum(1, -10))


def integer_diff(lst, num):
    """
    Receives two arguement: a list containing integers and an integer number
    determine the number of times where two integers in the list have a difference of n
    """
    counter = 0
    for i in lst:
        if i - i == num:
            counter += 1
        return counter


print(integer_diff([1, 4, 7, 8, 3, 6], 2))


# lst = list(range(1, 5))
# print(sum(lst[1:5]))
