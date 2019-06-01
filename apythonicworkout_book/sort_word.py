

def strsort(stringy):
    """
    receive a single string and return a  sorted string for example "cba" becomes
    "abc"
    """

    sort_lst = sorted(stringy)
    return "".join(sort_lst)


print(strsort("cba"))

# Bonus


def strsort2(stringy2):
    """
    Receives a string, break it into individual words and then sort those words
    alphabetically. Then print them with commas(,) between the names
    """

    turn_sent_to_list = stringy2.split()
    alpha_sorted = sorted(turn_sent_to_list)
    display_with_comma = ",".join(alpha_sorted)
    return display_with_comma


print(strsort2("Tom Dick Harry"))
