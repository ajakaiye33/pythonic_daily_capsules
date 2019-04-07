
def make_number_odd(num):
    """
    Receives a number, adds 1 to that number if it's even and returns the number
    if the original number passed is odd, just return it
    """
    if num % 2 == 0:
        num += 1
    return num


print(make_number_odd(2))
print(make_number_odd(5))
