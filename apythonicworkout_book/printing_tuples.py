
def print_tuples(lst_tup):
    for i in lst_tup:
        print(f"{i[1]} {i[0]} {round(i[2],2)}")


print(print_tuples([('Donald', 'Trump', 7.85),
                    ('Vladimir', 'Putin', 3.626),
                    ('Jinpinq', 'Xi', 10.603)]))
