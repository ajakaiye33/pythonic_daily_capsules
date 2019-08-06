
def pedu(lst1, lst2):
    foo = 1
    soo = 1
    if len(lst1) == 3 and len(lst2) == 3:
        for i in lst1:
            if i > 0:
                soo *= i
        for j in lst2:
            if j > 0:
                foo *= j

        goo = foo - soo
        return abs(goo)


print(pedu([2, 2, 3], [5, 4, 1]))
