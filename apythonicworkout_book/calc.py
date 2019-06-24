
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


def anagrams(word, words):
    # your code here
    sey = []
    for i in word:
        for s in words:
            if i in s:
                sey.append(s)
                return sey


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))  # ['aabb', 'bbaa']

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))  # ['carer', 'racer']

# print(anagrams('laser', ['lazing', 'lazy',  'lacer']))  # []


v = "abba"
d = "bbaa"
v[::-1]
