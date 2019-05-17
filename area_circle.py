
class Circle(object):

    def __init__(self, radius):

        self.radius = radius

    def get_area(self):

        return 3.14 * self.radius


c1 = Circle(radius=1)
print(c1.get_area())


c2 = Circle(radius=3)
print(c2.get_area())


c3 = Circle(radius=9)
print(c3.get_area())

c4 = Circle(radius=4)
print(c4.get_area())
