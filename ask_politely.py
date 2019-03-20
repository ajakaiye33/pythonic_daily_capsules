# Create the function askPolitely that
# accepts a sentence as an argument. If the last
# character of the sentence is a question
# mark, then make sure the question ends with
# the word "please?".
# If a question is already polite
# (meaning it already ends with "please") or
# the sentence is not a question, ​then return
# the inputted string without modification.


def ask_politely(sentence):
    """
    return 'please?' if the
    sentence ends with a question mark
    and if the sentence is already polite or just a statement
    return the sentence/statement unchanged
    """
    if sentence.endswith('?') and sentence.split()[-1] != 'please?':
        return sentence[0:-1] + ' please' + '?'

    elif sentence.split()[-1] == 'please?' or sentence[-1] != '?':
        return sentence


print(ask_politely("My name is Grace Hopper"))

###########################################


# INPUT: askPolitely("May I borrow your pencil?");
# - OUTPUT: "May I borrow your pencil please?"
#
#
# - INPUT: askPolitely("May I ask a question please?");
# - OUTPUT: "May I ask a question please?"
#
#
# - INPUT: askPolitely("My name is Grace Hopper.");
# - OUTPUT: "My name is Grace Hopper.";
