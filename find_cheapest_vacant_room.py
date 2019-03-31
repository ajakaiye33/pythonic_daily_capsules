

def find_cheap_vancant_room(occupancy):
    room_no_cheapest = []
    for room_no, occu_price in enumerate(occupancy):
        if type(occu_price) == int:
            room_no_cheapest.append(occu_price)
            get_miny = min(room_no_cheapest)
    return [room_no, get_miny]


print(find_cheap_vancant_room(["occupied", 820, "occupied", 700, 455, 722]))
print(find_cheap_vancant_room([112, "occupied", 150, 175, "occupied"]))


def odd(x):
    return x * 2+1


print(map(odd, range(6)))
