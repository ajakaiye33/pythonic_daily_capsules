
def traffic_light(color):
    """
    Receives a color and returns:
    "stop" if the color is "red"
    "slow down" if the color is "yellow"
    "go" if the color is "green"
    """
    traff_dict = {"red": "stop", "yellow": "slow down", "green": "go"}
    return traff_dict[color]


print(traffic_light("red"))
print(traffic_light("yellow"))
print(traffic_light("green"))
