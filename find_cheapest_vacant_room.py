

def find_cheap_vancant_room(occupancy):
    room_no_cheapest = []
    for room_no, occu_price in enumerate(occupancy, 0):
        if type(occu_price) == int:
            room_no_cheapest.append(occu_price)
            miny = min(room_no_cheapest)

    return min([room_no, miny])


print(find_cheap_vancant_room(["occupied", 820, "occupied", 700, 455, 722]))
