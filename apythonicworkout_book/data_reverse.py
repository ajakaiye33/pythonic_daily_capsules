def data_reverse(data):
    foo = []

    set1 = data[0:8]
    set2 = data[8:16]
    set3 = data[16:24]
    set4 = data[24:]
    comby = [set1, set2, set3, set4]
    for i in comby[::-1]:
        foo.extend(i)
    return foo


print(data_reverse([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]))
print(data_reverse([0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]))
