import numpy as np


def squared_mat_mult(a, b):
    return np.dot(a, b)


f = [[1, 2],
     [3, 2]]
g = [[3, 2],
     [1, 1]]

d = [[9, 7],
     [0, 1]]

h = [[1, 1],
     [4, 12]]

k = [[1, 2, 3],
     [3, 2, 1],
     [2, 1, 3]]

n = [[4, 5, 6],
     [6, 5, 4],
     [4, 6, 5]]


print(squared_mat_mult(f, g))
print(squared_mat_mult(d, h))
print(squared_mat_mult(k, n))
