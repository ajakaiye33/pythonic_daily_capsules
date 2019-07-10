import numpy as np


def determinant(matrix):
    # your code here
    soo = np.array(matrix)
    return round(np.linalg.det(soo))


print(determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]]))
print(determinant([[1, 3], [2, 5]]))
