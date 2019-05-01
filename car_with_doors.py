
class Car(object):
    """
    making a car with variable number of doors
    """

    def __init__(self, color, num_doors=4):
        """
        receives at instantiation a color  and with or without number of doors
        of choice
        """
        self.color = color
        self.num_doors = num_doors


car1 = Car(color="blue", num_doors=2)
print(car1.color)
print(car1.num_doors)

car2 = Car("green")
print(car2.color)
print(car2.num_doors)
