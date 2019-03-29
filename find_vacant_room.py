def find_vacant_room(room_status_array):
    """
    function returns the index-in a list- of element
    that are 'vacant' in the room_status_array
    """
    vacant_room_no = []
    for room_no, room in enumerate(room_status_array):
        if room == 'vacant':
            vacant_room_no.append(room_no)
    return vacant_room_no


print(find_vacant_room(['vacant', 'occupied', 'occupied', 'vacant', 'vacant']))
