def make_choice():
    print("1. Convert miles to Kilometers")
    print("2. Convert kilometers to miles")


def km_miles():
    get_miles = float(input("Kindly enter measurement in kilometers:"))
    calc = get_miles/1.609
    print("The measurement in miles is: {}".format(calc))


def mile_km():
    get_kilo = float(input("Kindly enter measurement in miles:"))
    calc = get_kilo * 1.609
    print("The measurement in kilometers is:{}".format(calc))


make_choice()

answer = int(input("Please enter the number of your choice >"))
if answer == 1:
    mile_km()
elif answer == 2:
    km_miles()
else:
    print("Please enter a valid choice")
