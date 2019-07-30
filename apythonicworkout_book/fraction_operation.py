from fractions import Fraction


def add_fractions(a, b):
    print('The result of addition is {}'.format(a + b))


def sub_fractions(a, b):
    print('The result of subtraction is {}'.format(a - b))


def mult_fractions(a, b):
    print('The result of multiplication is {}'.format(a * b))


def div_fractions(a, b):
    print("The result of dividing 'a' by 'b' is {}".format(a / b))


if __name__ == "__main__":
    a = Fraction(input("Enter the first fraction > "))
    b = Fraction(input("Enter the second fraction > "))
    op = input(
        " Enter the letter of the Operations to perform: add[a], substract[s], multiplication[m], division[d] ?")
    op = op.lower()
    if op == 'a':
        add_fractions(a, b)
    elif op == "s":
        sub_fractions(a, b)
    elif op == "m":
        mult_fractions(a, b)
    elif op == "d":
        div_fractions(a, b)
