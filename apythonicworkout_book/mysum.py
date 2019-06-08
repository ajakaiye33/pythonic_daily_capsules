#
# def mysum(*args):
#     """
#     Write a function that does the same thing as the built-in sum function
#     mysum(2,3,6,89,)
#     """
#
#     adder = 0
#
#     for i in args:
#         adder += i
#     return adder
#
#
# print(mysum(1, 2, 3))
# print(mysum(10, 20, 30, 40, 50))
# #print(mysum([1, 2, 3]))
#
#
# # Bonus
# def mysum2(lst, num=0):
#     """
#     Takes in a list and a number from which the summation may begin
#     """
#     sumy = 0
#     for i in lst:
#         sumy += i
#     return sumy + num
#
#
# print(mysum2([1, 2, 3], 10))
#
#
# def aveg(lst):
#     """
#     Takes a list of numbers. and return the average(i.e arithmetic mean) of those numbers
#     """
#     fly = 0
#     for i in lst:
#         fly += i
#     return round(fly/len(lst), 2)
#
#
# print(aveg([4, 5, 8, 2, 9, 10, 21]))
#
#
# def stringy_av(*word_list):
#     """
#     Takes a list of words(strings) and return a tuple containing  three integers
#     representing the length of the shortest word, the length of the longest word and
#     the average word length
#     """
#     check = []
#     for i in word_list:
#         check.append(len(i))
#         max_len = max(check)
#         min_len = min(check)
#         ave_len = round(sum(check)/len(check), 2)
#     return (max_len, min_len, ave_len)
#
#
# print(stringy_av("policy", "politics", "president"))
#
#
# def intey(*p_obj):
#     storky = []
#     for i in p_obj:
#         if type(i) == int:
#             if int(i):
#                 storky.append(i)
#             return storky
#
#
# print(intey("34", 56, "good", "100"))


def infiny(*items):
    addy = 0

    for i in items:
        for j in i:
            addy += j
        return addy


print(infiny([1, 2, 3], [4, 5, 6]))
