def multiply_table(unit, times):
    for i in range(1, times+1):
        print(" {} x {} = {}".format(unit, i, unit*i))


print(multiply_table(5, 12))
