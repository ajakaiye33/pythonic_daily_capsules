

class Calculator(object):
    """
    model a calculator
    """

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2


a = Calculator()
print(a.add(2, 5))

s = Calculator()
print(s.subtract(9, 6))
