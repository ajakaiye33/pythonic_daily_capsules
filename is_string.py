
def is_string(stringy):
    """
    Receives a variable and if it's a string returns 'True' and if not returns 'False'
    """
    if isinstance(stringy, str):
        return True
    return False


print(is_string('happy'))
print(is_string(37))
