
class Car(object):
    """
    create a car
    """

    # def __init__(self, color, make, model):
    #     """
    #     Receives three attributes: color, model and make
    #     """
    #     self.color = color
    #     self.make = make
    #     self.model = model


# Instantiation

car1 = Car()
car1.color = "black"
car1.make = "Benz"
car1.model = "Cclass940"


car2 = Car()
car2.color = "white"
car2.make = "BMW"
car2.model = "i790"

print(car1.model)
print(car2.model)
print(car1.make)
print(car1.color)
