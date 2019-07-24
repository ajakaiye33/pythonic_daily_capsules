def root(a, b, c):
    """
    a, b, c are constant which is feed to the quadratic formular:
    x_1 = (-b +(b**2 - 4*a*c)**(1/2))/2*a
    x_2 = (-b - (b**2 - 4*a*c)**(1/2))/2*a
    """

    d = (b*b - 4 * a * c)**0.5
    x_1 = -b - d/(2*a)
    x_2 = -b + d/(2*a)

    print("x_1 = {}".format(x_1))
    print("x_2 = {}".format(x_2))


if __name__ == '__main__':
    a = float(input("Enter value of a > "))
    b = float(input("Enter value of b > "))
    c = float(input("Enter value of c > "))
root(a, b, c)
