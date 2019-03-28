
def palindrome(sen):
    """
    accept a string argument, and return
    the boolean true if the argument is a
    palindrome (meaning that the string is
    the same forward as it is backward).
    Otherwise, return the boolean false.
    """
    sen = sen.lower()
    if sen == sen[::-1]:
        return True
    return False


print(palindrome('Madam'))
