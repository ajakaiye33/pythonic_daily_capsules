
def card_play(player1_array, player2_array):
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    player1_score = 0
    playyer2_score = 0

    for level, element in enumerate(rank):
        if element in player1_array:
            if element in player2_array:
                return level


print(card_play(['K', 'Q', 'J'], ['Q', 'K', 'J']))
