

# def hex_converter(hexnum):
#     """
#     receives a hex number and returns the decimal equivalent
#     """
#     return hex(hexnum)
#
#     # else:
#     #     return int(hexnum,16)
#     #
#
#
# print(hex_converter(20))


d = 0
h = input("Enter a hex number to concert to decimal:")
for power, digit in enumerate(reversed(h)):
    d += int(digit, 16) * (16 ** power)
    print(d)
