def unique_string(stringy):
    for i in range(len(stringy)):
        doo = stringy[i]
        for j in doo:
            if doo.count(j) > 1:
                foo = stringy[i]
    return foo


print(unique_string(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
