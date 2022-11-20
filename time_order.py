import time


def if_time_in(start, end):
    t = int(time.strftime("%S", time.localtime()))
    if start <= t < end:
        return True
    return False


def only_second():
    return int(time.strftime("%S", time.localtime()))
