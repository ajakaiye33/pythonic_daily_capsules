from datetime import datetime, timedelta
import time


def human_time(sec):
    return str(timedelta(seconds=sec))


print(human_time(0))
print(human_time(5))
print(human_time(60))
print(human_time(86399))
print(human_time(359999))


# def doo(sil):
#     return time.strftime("%H:%M:%S", time.gmtime(sil))
#
#
# print(doo(359999))
