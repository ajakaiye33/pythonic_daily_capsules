
# def generate_hashtag(stringy):
#     """
#     receives a sentence return same with hashtag added if it is not empty string
#     and the len is less than 140
#     """
#     uper = stringy.title()
#     stripy = uper.split()
#     stripy.insert(0, "#")
#     comby = "".join(stripy)
#     if len(comby) > 140 or stringy == "":
#         return False
#     else:
#         return comby
#
#
# print(generate_hashtag("Hello there thanks for trying my Kata"))
#
# print(generate_hashtag("Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"))
# print(generate_hashtag(""))

import numpy as np


def determinant(matrix):
    # your code here
    soo = np.array(matrix)
    return np.linalg.det(soo)


print(determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]]))
print(determinant([[1, 3], [2, 5]]))
