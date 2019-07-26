def even_odd(c):
    """
    Print whether the number is even or odd.
    Display the number followed by the next 9 even or odd numbers
    """

    for i in range(1, c+1):
        if i % 2 == 0:
            print('even')
            print(i)
        elif i % 3 == 0:
            print('odd')
            print(i)


if __name__ == "__main__":
    c = float(input("Enter your number: > "))
    if c > 0 and c.is_integer():
        even_odd(int(c))
    else:
        print("Please enter a valid number")
