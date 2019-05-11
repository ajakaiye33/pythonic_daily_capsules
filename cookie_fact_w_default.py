
class Cookie(object):
    DEFAULT_SCARF_COLOR = "Green"
    DEFAULT_BUTTON_COLOR = "Blue"

    def __init__(self, scarf_color, buttons_color):
        self.scarf_color = scarf_color
        self.buttons_color = scarf_color

    @classmethod
    def creat_cookies(cls, num, scarf_color=None, buttons_color=None):
        combined = []

        for _ in range(num):
            combined.append(cls(
                scarf_color or cls.DEFAULT_SCARF_COLOR,
                buttons_color or cls.DEFAULT_BUTTON_COLOR))

        return combined


cookies = Cookie.creat_cookies(2, scarf_color="Red", buttons_color="Yellow")

print(cookies)
