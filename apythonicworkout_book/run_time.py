

def runny_time():
    """
    enter 10 km time: 10
    enter 20 km run :r
    return Average of 15.0 over 3 runs
    """
    bag_time = 0
    toge_time = 0
    while True:
        today_time = int(input("Enter 10km run time > "))

        if today_time == "q":
            break
        else:
            toge_time += 1
            bag_time += today_time
            average_time = bag_time/toge_time

    return f" Average of {average_time} over toge_time"


print(runny_time())
