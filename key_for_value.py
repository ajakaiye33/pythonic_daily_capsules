
def search_key_for_value(di, va):
    """
    Receives a dictionary and a value to search for as input. Return a set with
    all the keys from the dictionary that have that values
    """
    apd = []
    for k in di.keys():
        if di[k] == va:
            apd.append(k)
    return set(apd)


print(search_key_for_value({"name": "Billy", "age": 12, "fav_num": 12}, 12))
print(search_key_for_value({1: "hi", 2: "there", 3: "easter egg"}, "easter egg"))
print(search_key_for_value({"a": "i", "b": "love", "c": "programming"}, "howdy"))
