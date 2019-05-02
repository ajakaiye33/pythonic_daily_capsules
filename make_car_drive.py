
class Car(object):
    """
    make a car that drive
    """

    def __init__(self, electric):
        """
        receives a madatory argument: electric
        """

        self. electric = electric

    def drive(self):
        if not self.electric:
            return "VROOOOM"
        else:
            return "WHIRRRRRRRR"


car1 = Car(electric=False)
print(car1.electric)
print(car1.drive())

car2 = Car(electric=True)
print(car2.electric)
print(car2.drive())
