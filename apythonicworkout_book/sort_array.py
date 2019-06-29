

def sort_array(lst):
    foo = []
    boo = []
    for i in lst:
        if i % 2 != 0:
            foo.append(i)
            sorted(foo)
        elif i % 2 == 0:
            boo.append(i)
    return boo + foo

    return sorted(foo)

    # print(i.sorted())


print(sort_array([5, 3, 2, 8, 1, 4]))  # == [1, 3, 2, 8, 5, 4]
