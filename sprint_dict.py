
def sprint_dict(num):
    banana = {}
    for i in range(1, num+1):
        iside = "banana" * i
        banana[iside] = i
    return banana


print(sprint_dict(4))
