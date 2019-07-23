def choose():
    print("1: Convert Fahrenheit to celsius")
    print("2: Convert Celsius to Fahrenheit")


def fah_cel():
    temp_fah = float(input("Please enter the Fahrenheit temperature unit> "))
    calc = (temp_fah - 32)*5/9
    print("The temperature in celsius is: {}".format(calc))


def cel_fah():
    temp_cel = float(input("Please enter the Celcius temperature unit> "))
    calc = (temp_cel * 9/5) + 32
    print(" The temperature in Fahrenheit is : {}".format(calc))


choose()

operation_choice = int(
    input("Please indicate the number that correspond to theoperation you want > "))

if operation_choice == 1:
    fah_cel()
elif operation_choice == 2:
    cel_fah()
else:
    print("Please enter a valid choice of operation")
