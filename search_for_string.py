
def search_for_string(lst_str, stringy):
    """
    Receives a list and a search term. Use a loop to go through the list and see
    if the string is there. if it is return "string found". if not, return "string not found"
    """
    if stringy in lst_str:
        return "Found string"

    else:
        return "string not found"


print(search_for_string(["a", "b", "c"], "d"))
print(search_for_string(["santiago", "santi", "santa"], "santa"))
print(search_for_string([], "a"))


# Using for loop to search term

def search_with_loop(fi, si):

    for i in fi:
        if i == si:
            return "Found string"

    return "string not found"


print(search_with_loop(["a", "b", "c"], "d"))
print(search_with_loop(["santiago", "santi", "santa"], "santa"))
print(search_with_loop([], "a"))
