# https://app.codesignal.com/arcade/intro/level-12/ywMyCTspqGXPWRZx5

def validTime(time):
    hours, mins = [int(n) for n in time.split(':')]
    if 0 <= hours <= 23:
        if 0 <= mins <= 59:
            return True
    return False
