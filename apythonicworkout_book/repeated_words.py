

def most_repeated_word(wordy):
    """
    receives a sequence of strings and return the string that contains the greatest
    number of repeated letters
    """
    container = []
    new_word = ''.join(wordy)
    return max(new_word)


print(most_repeated_word(["this", "is", "a", "test", "program"]))
