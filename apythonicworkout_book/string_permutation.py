
from itertools import permutations


def permutation(stry):
    """
    permutate the string and return result without duplicate
    """
    comp = []
    perm_str = permutations(stry)
    for i in list(perm_str):
        comp.append("".join(i))
    return list(set(comp))


print(permutation("a"))
print(permutation("ab"))
print(permutation("aabb"))
