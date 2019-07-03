

# def sort_array(lst):
#     foo = []
#     boo = []
#     for i, j in enumerate(lst):
#         if j % 2 == 0:
#             foo.insert(i, j)
#         elif j % 2 != 0:
#             boo.append(j)
#             sorted(boo)
#             boo[::-1]
#     return boo + foo

# print(i.sorted())
# correct solution
def sort_array(lst):
    result = [i for i in lst if i % 2 != 0]
    for indy, val in enumerate(lst):
        if val % 2 == 0:
            result.insert(indy, val)
    return result


print(sort_array([5, 3, 2, 8, 1, 4]))  # == [1, 3, 2, 8, 5, 4]
print(sort_array([5, 3, 1, 8, 0]))  # [1, 3, 5, 8, 0]
