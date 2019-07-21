import numpy as np
import math
import random
#
#
# def determinant(mat):
#     # your code here
#     #soo = np.array(matrix)
#     # return round(np.linalg.det(soo))
#     return round(np.linalg.det(np.matrix(mat)))
#
#
# print(determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]]))
# print(determinant([[1, 3], [2, 5]]))


def ispp(val):
    goo = []
    uper = range(1, val)
    base = range(1, val)
    for i in uper:
        for j in base:
            if j**i == val:
                goo.append([j, i])
    return goo

    # foo = math.sqrt(val)
    # if foo**2 == val:
    #     return True


print(ispp(81))
print(ispp(81))
print(ispp(4))
print(ispp(9))
print(ispp(5))
