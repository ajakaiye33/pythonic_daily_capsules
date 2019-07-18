from collections import defaultdict


def unique_string(a):
    d = {}
    c = defaultdict(int)
    for e in a:
        t = frozenset(e.strip().lower())
        d[t] = e
        c[t] += 1

    return d[next(filter(lambda k: c[k] == 1, c))]


print(unique_string(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
