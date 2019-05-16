

class Calculator(object):

    def add(self, num1,  num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2


calc = Calculator()

print(calc.add(2, 3))

print(calc.subtract(10, 3))
