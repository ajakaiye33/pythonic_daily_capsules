
class Car(object):

    def __init__(self, model, color, convertible=False):
        self.model = model
        self.color = color
        self.convertible = convertible


c1 = Car(model="BMW E46", color="Red")
print(c1.model)
print(c1.color)
print(c1.convertible)


c2 = Car(model="Toyota MR2", color="Blue", convertible=True)
print(c2.model)
print(c2.color)
print(c2.convertible)
