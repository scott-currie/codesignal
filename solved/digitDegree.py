# https://app.codesignal.com/arcade/intro/level-9/hoLtYWbjdrD2PF6yo

def digitDegree(n):
    i = 0
    while n >= 10:
        n = sum([int(c) for c in str(n)])
        i += 1
    return i
    