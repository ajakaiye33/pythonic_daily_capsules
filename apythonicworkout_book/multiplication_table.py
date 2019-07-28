def multiply_table(unit, times):
    for i in range(1, times+1):
        print(" {} x {} = {}".format(unit, i, unit*i))


if __name__ == "__main__":
    unit = int(input('Enter a number: > '))
    times = int(input('The number of times: > '))

multiply_table(unit, times)
#print(multiply_table(5, 12))
