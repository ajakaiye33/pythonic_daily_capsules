

def strsort(stringy):
    """
    receive a single string and return a  sorted string for example "cba" becomes
    "abc"
    """

    sort_lst = sorted(stringy)
    return "".join(sort_lst)


print(strsort("cba"))
