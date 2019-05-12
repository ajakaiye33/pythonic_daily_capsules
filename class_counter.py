
class Cookie(object):

    COUNT = 0

    def __init__(self):
        Cookie.COUNT += 1

    @classmethod
    def count(cls):
        return cls.COUNT

    @classmethod
    def reset_counter(cls):
        cls.COUNT = 0


Cookie.count()

c1 = Cookie()
c2 = Cookie()

Cookie.count()
c3 = Cookie()
c4 = Cookie()

print(Cookie.count())

Cookie.reset_counter()
print(Cookie.count())
