def create_counting_lst(num):
    """
    Receives a number to count up to
    """
    counter = 1
    prod = []
    if num >= 0:
        while counter < num+1:
            prod.append(counter)
            counter += 1
        return prod
    return "can not be negative"


print(create_counting_lst(7))
print(create_counting_lst(3))
print(create_counting_lst(0))
print(create_counting_lst(-1))
