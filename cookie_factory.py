
class Cookie(object):

    @classmethod
    def creat_cookies(cls, num):
        combine = []
        for i in range(num):
            combine.append(cls())
        return combine


van = Cookie.creat_cookies(2)

print(van)
