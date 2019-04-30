
class Car(object):
    """
    make a car with the following characteristics: make, model and color
    """

    def __init__(self, color, make, model):
        """
        each car should habe a make model and color
        """
        self.color = color
        self. make = make
        self . model = model


car1 = Car("blue", "Tesla", "Model  s")
car2 = Car("red", "Chevy", "Camara")

print(car1.color)
print(car1.make)
print(car1.model)


print(car2.color)
print(car2.make)
print(car2.model)
