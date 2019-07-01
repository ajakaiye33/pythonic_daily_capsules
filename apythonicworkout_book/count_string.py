# from collections import Counter
#
#
# def count_strings(stringy):
#     """
#     The main idea is to count all the occuring characters(UTF-8) in string.
#     If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
#     What if the string is empty ? Then the result should be empty object literal { }
#     """
#     comby = {}
#     for i in stringy:
#         sey = stringy.count(i)
#         comby[i] = sey
#     return comby
#
#
# print(count_strings(""))
#
# # pythonic alternatives
#
#
# def county(string):
#     return {i: string.count(i)for i in string}
#
#
# print(county("aba"))
#
#
# def cont_stringy(stringy):
#     return Counter(stringy)
#
#
# print(cont_stringy("aba"))


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
