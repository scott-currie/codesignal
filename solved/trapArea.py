# https://app.codesignal.com/challenge/sGDJsXcFYhkoejcrq
# This was kinda fun. These formulas came straight from the internet, though
# I probably had enough basic geometry to figure them out eventually.

import math

def trapArea(n, p, r):
    A_small = getAreaFromP(n, p)
    A_large = getAreaFromr(n, r)
    return int(round(A_large - A_small))

def getAreaFromP(n, p):
    # side
    s = p / n
    # interior angle
    x = (n - 2) / n * 180
    # apothem
    a = s / (2 * math.tan(math.radians(180) / n))
    # area
    A = p * a / 2
    return A 

def getAreaFromr(n, r):
    A = (math.pow(r, 2) * n * math.sin(math.radians(360) / n)) / 2
    return A