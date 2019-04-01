
# def card_play(player1_array, player2_array):
#     rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
#
#     for rank_ind, rank_element in zip(player1_array, player2_array):
#         print(rank_ind, rank_element)
#
#
# print(card_play(['K', 'Q', 'J'], ['Q', 'K', 'J']))
#
#
# # rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

import timeit

# input_list = range(100)
#
#
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False


# # xyz = (i for i in input_list if div_by_five(i))
# xyz = [i for i in input_list if div_by_five(i)]
# print(xyz)

print(timeit.timeit('''input_list = range(100)


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


# xyz = (i for i in input_list if div_by_five(i))
xyz = [i for i in input_list if div_by_five(i)]
''', number=50))
