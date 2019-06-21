
def create_phone_number(n):
    """
    trandsfor to phone number format
    """
    nf = ''
    for i in n:
        nf += str(i)
    return f"({nf[0:3]}) {nf[3:6]}-{nf[6:]}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
