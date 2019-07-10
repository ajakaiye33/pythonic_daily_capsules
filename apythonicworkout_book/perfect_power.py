
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
