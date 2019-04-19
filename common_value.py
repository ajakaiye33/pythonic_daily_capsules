
def common_values(tup1, tup2):
    """
    Receives two tuple and return element common with them
    """
    u_d = tup1 + tup2
    return set(u_d)


print(common_values((1, 5, 6, 4, 8), (1, 6, 10, 5)))
