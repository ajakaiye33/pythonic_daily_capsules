
# def calc(expr):
#     d = expr.split()
#     #f = int(d[0])
#     #s = int(d[1])
#     #sym = d[2]
#     #ge = f"{f}{sym}{s}"
#     print(d)
#
#     #e = int(expr[0])
#     # symbol = int(expr[])
#
#
# print(calc("3 3 *"))


# def anagrams(word, words):
#     # your code here
#     sey = []
#     for i in words:
#         for c in word:
#             if c  ==:
#                 sey.append(i)
#         return sey
#
#
# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))  # ['aabb', 'bbaa']
#
# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))  # ['carer', 'racer']
#
# # print(anagrams('laser', ['lazing', 'lazy',  'lacer']))  # []
#
#
# v = "abba"
# d = "bbaa"
# print(v[::-1])
# print(d[::-1])


def zeros(n):
    sey = 1
    pey = []
    for i in range(1, n+1):
        print(i)
        sey *= i
        pey.append(sey)
        return pey.count(0)


print(zeros(6))  # = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

print(zeros(12))  # = 2
# 12! = 479001600 --> 2 trailing zeros
