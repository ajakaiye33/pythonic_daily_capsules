# Create the function doYouPlayTheTheremin.
# If your name starts with the letter "S" or "s", you are playing the Theremin!


def doYouPlayTheTheremin(name):
    """
    If your name starts with the letter
    "S" or "s", you are playing
    the Theremin!"""
    if name[0] == 'S' or name[0] == 's':
        return name + ' plays the Theremin'
    return name + ' does not play the Theremin'


doYouPlayTheTheremin('Scott')
