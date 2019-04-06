
def is_numeric(obj):
    if type(obj) == int:
        return "{}, It's an integer".format(True)
    elif type(obj) == float:
        return "{}, It's a float".format(True)
    elif type(obj) == str:
        return "{}, It's a string".format(False)
    elif type(obj) == bool:
        return "{}, It's a boolean".format(False)


print(is_numeric(10))
print(is_numeric('10'))
print(is_numeric(0.1))
print(is_numeric('0.5'))
print(is_numeric(True))
print(is_numeric(False))
