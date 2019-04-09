
def how_many_days_in(month):
    """
    Receives a given month and returns the number of days in it(non leap years)
    """
    if month == "January":
        days = 31
    elif month == "February":
        days = 28
    elif month == "March":
        days = 30
    elif month == "April":
        days = 30
    elif month == "May":
        days = 31
    elif month == "June":
        days = 30
    elif month == "July":
        days = 31
    elif month == "August":
        days = 31
    elif month == "September":
        days = 30
    elif month == "October":
        days = 31
    elif month == "November":
        days = 30
    elif month == "December":
        days = 31
    return days


print(how_many_days_in("December"))
print(how_many_days_in("February"))

# another way
# def how_many_days_in(month):
#     monthanddays = {"January": 31, "February": 28, "March": 30, "April": 30, "May": 31,
#                     "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
#     return monthanddays[month]
#
#
# print(how_many_days_in("December"))
# print(how_many_days_in("February"))
