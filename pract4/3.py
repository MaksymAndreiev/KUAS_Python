from datetime import datetime


def pad(n):
    return f'{n:02d}'


def alarm_format(h, m, s):
    h, m, s = map(pad, (h, m, s))
    return h, m, s


def time_string():
    h, m, s = alarm_format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    return f'{h}:{m}:{s}'


print(time_string())
