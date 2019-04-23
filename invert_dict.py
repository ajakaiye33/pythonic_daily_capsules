
def invert_dict(a_dict):
    """
    Receives a dictionary and return it with it keys and value element inverted
    """
    the_engine = {}
    for k, v in a_dict.items():
        the_engine[v] = k
    return the_engine


fley = {1: "a", 2: "b", 3: "c"}

print(invert_dict(fley))
