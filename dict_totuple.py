def dict_to_tuple(the_dict):
    """
    Receives a dictionary and returns a list of tuples containing the key-value pairs
    """
    the_pair = []
    for k, v in the_dict.items():
        the_pair.append((k, v))
    return the_pair


print(dict_to_tuple({"a": 1, "b": 2}))
print(dict_to_tuple({"Hello": "world"}))
