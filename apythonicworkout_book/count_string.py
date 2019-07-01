from collections import Counter


def count_strings(stringy):
    """
    The main idea is to count all the occuring characters(UTF-8) in string.
    If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
    What if the string is empty ? Then the result should be empty object literal { }
    """
    comby = {}
    for i in stringy:
        sey = stringy.count(i)
        comby[i] = sey
    return comby


print(count_strings(""))

# pythonic alternatives


def county(string):
    return {i: string.count(i)for i in string}


print(county("aba"))


def cont_stringy(stringy):
    return Counter(stringy)


print(cont_stringy("aba"))
