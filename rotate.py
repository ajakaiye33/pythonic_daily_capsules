def rotate(array, times):
    """
    Rotate an array to the right by a certain number of "steps".
    """
    return array[-times:] + array[:-times]


print(rotate([1, 2, 3, 4, 5, 6, 7], 0))
