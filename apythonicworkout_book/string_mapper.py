

def string_map(stringy):
    """
    Accept a string and returns a mapping(a dictionary or dictionary-like structure)
    that has words as the keys ans the number of times each word was seen as the values
    """
    maper = {}

    split_string = stringy.split()
    for i in split_string:
        maper[i.lower()] = split_string.count(i)
    return maper


print(string_map("what a busy day"))
print(string_map("oh what a day what a day"))
print(string_map("Oh what a day what a day"))
print(string_map("Oh what a day, what a day!"))
