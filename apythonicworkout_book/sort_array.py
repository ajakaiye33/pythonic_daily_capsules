

def sort_array(lst):
    foo = []
    for i, j in enumerate(lst):
        if j % 2 == 0:
            print(i)

    # print(i.sorted())


print(sort_array([5, 3, 2, 8, 1, 4]))  # == [1, 3, 2, 8, 5, 4]
print(sort_array([5, 3, 1, 8, 0]))  # [1, 3, 5, 8, 0]
