# import operator
#
#
# def print_tuples(lst_tup):
#     for i in lst_tup:
#         print(f"{i[1]} {i[0]} {round(i[2],2)}")
#
#
# print(print_tuples([('Donald', 'Trump', 7.85),
#                     ('Vladimir', 'Putin', 3.626),
#                     ('Jinpinq', 'Xi', 10.603)]))
#
# # alternate solution
# for person in sorted(people, key=operator.itemgetter(1, 0)):
#     print("{1: 10} {0: 10}
#           {2: 5.2f}").format(*person)

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
combine = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix2[i])):
        row.append(matrix1[i][j] + matrix2[i][j])
    combine.append(row)
print(combine)
