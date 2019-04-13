
# def get_element_num(lst_str, luk):
#     """
#     Receives a list of strings and a term.Use a loop to go through the list of
#     stringd and find the search term. Return the element number of the first match
#     and "no match" if there is no match
#     """
#     if luk in lst_str:
#         return lst_str.index(luk)
#     return "no match"
#
#
# print(get_element_num(["a", "b", "c"], "c"))
# print(get_element_num(["a", "a", "a"], "a"))
# print(get_element_num(["a", "b", "c"], "s"))

yib = ["a", "b", "c"]
yen = "c"


def cheky(y, t):
    for i in y:
        if i != t:
            res = "no match"
        elif i == t:
            res = y.index(i)
    return res


print(cheky(yib, yen))
