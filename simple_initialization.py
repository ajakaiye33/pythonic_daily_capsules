
class Cookie(object):

    def __init__(self, scarf, button):
        """
        Initialize scarf, button and hat
        """

        self.scarf = scarf
        self.botton = button
        self.hat = None


c1 = Cookie(scarf="green", button="blue")

print(c1.scarf)
print(c1.botton)
print(c1.hat)

c2 = Cookie(scarf="yellow", button="red")

print(c2.botton)
print(c2.hat)
print(c2.scarf)
