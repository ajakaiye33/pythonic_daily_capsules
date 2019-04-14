
def custom_zip(col1, col2):
    """
    Receives two collections and must "zip" their elements if their respective
    length are uniform or same otherwise return "none". without using the zip
    function
    """
    joiner = []
    if len(col1) == len(col2):
        for ind, el in enumerate(col1):
            for id, xt in enumerate(col2):
                if ind == id:
                    com = el, xt
                joiner.append(com)
            return joiner
    else:
        return "None"


print(custom_zip(["A", "B", "C"], [1, 2, 3]))
print(custom_zip([1, 1, 1], [2, 2, 2]))
print(custom_zip(["A", "B"], [1, 2, 3]))
