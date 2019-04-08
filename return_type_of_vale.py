
def return_type_value(obj):
    """
    return the type of a given value
    """
    if isinstance(obj, str):
        res = "string"
    elif type(obj) == int:
        res = "integer"
    elif isinstance(obj, float):
        res = "float"
    elif type(obj) == bool:
        res = "boolean"
    return res


print(return_type_value(2))
print(return_type_value("cookies, now!"))
print(return_type_value(True))
print(return_type_value(42.0))


# print(isinstance(False, bool))
