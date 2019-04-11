
def sum_of_num_in_list(a_lst):
    """
    Receives a list of numbers "a_lst" of an unknown length and calculates the sum
    of those numbers using a for loop. Do not use the sum function
    """
    adder = 0
    for i in a_lst:
        adder += i
    return adder


print(sum_of_num_in_list([0]))
print(sum_of_num_in_list([4]))
print(sum_of_num_in_list([2, 3]))
print(sum_of_num_in_list([2, 3, 4]))
