
class Cookie(object):

    DEFAULT_SCARF_COLOR = "Green"
    DEFAULT_BUTTON_COLOR = "Blue"

    # DEFAULT_SCARF_COLOR = "Yellow"
    # DEFAULT_BUTTON_COLOR = "Red"

    def __init__(self, scarf_color=None, buttons_color=None):
        self.scarf_color = scarf_color or self.DEFAULT_SCARF_COLOR
        self. buttons_color = buttons_color or self.DEFAULT_BUTTON_COLOR


c1 = Cookie(scarf_color="Red", buttons_color="Yellow")
print(c1.scarf_color)
print(c1.buttons_color)

c2 = Cookie(scarf_color="Red")
print(c2.scarf_color)
print(c2.buttons_color)


c3 = Cookie(buttons_color="Red")
print(c3.scarf_color)
print(c3.buttons_color)

c4 = Cookie()
print(c4.scarf_color)
print(c4.buttons_color)
