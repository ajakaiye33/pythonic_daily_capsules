

def runny_time():
    """
    enter 10 km time: 10
    enter 20 km run :r
    return Average of 15.0 over 3 runs
    """
    bag_time = 0
    toge_time = 0
    while True:
        today_time = input("Enter 10km run time > ")

        if today_time == "q":
            break
        else:
            toge_time += 1
            bag_time += int(today_time)
    average_time = bag_time/toge_time

    return f" Average of {average_time} over {toge_time}"

# without function


print(runny_time())

total_time = 0
no_of_runs = 0
while True:
    one_time = input("Enter 10km run time > ")

    if one_time == 'q':
        break
    else:
        no_of_runs += 1
        total_time += float(no_of_runs)
average_time = total_time/no_of_runs
print(f"average of {average_time} for {no_of_runs}")
