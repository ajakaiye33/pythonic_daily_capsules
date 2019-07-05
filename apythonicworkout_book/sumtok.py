import random
from itertools import permutations


def sum_to_k(lst, k):
    """
    This problem was recently asked by Google.
    Given a list of numbers and a number k, return whether any two numbers
    from the list add up to k.
    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    Bonus: Can you do this in one pass?
    """
    # sey = random.sample(lst, 2)
    # print(sum(sey))
    #
    for idy, val in enumerate(lst):
        sey = lst[idy] + val

        print(sey)


print(sum_to_k([10, 15, 3, 7], 17))
