
def color_mixer(color1, color2):
    """
    Receives two colors and returns the color resulting from mixing them in
    EITHER ORDER. The colors received are either "red", "blue", or "yellow" and
    should return:
    "Magenta" if the colors mixed are "red" and "blue"
    "Green" if the colors mixed are "blue" and "yellow"
    "Orange" if the color mixed are "yellow" and "red"
    """

    if (color1 == "red" and color2 == "blue") | (color2 == "red" and color1 == "blue"):
        res = "Magenta"
    elif (color1 == "blue" and color2 == "yellow") | (color2 == "blue" and color1 == "yellow"):
        res = "Green"
    elif (color1 == "yellow" and color2 == "red") | (color2 == "yellow" and color1 == "red"):
        res = "Orange"
    return res


print(color_mixer("red", "blue"))
print(color_mixer("blue", "red"))
print(color_mixer("blue", "yellow"))
print(color_mixer("yellow", "red"))
print(color_mixer("red", "yellow"))
print(color_mixer("yellow", "blue"))
