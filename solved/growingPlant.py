# https://app.codesignal.com/arcade/intro/level-9/xHvruDnQCx7mYom3T

def growingPlant(upSpeed, downSpeed, desiredHeight):
    # return int(desiredHeight / (upSpeed - downSpeed))
    h = 0
    d = 0
    while True:
        d += 1
        h += upSpeed
        if h >= desiredHeight:
            return d
        h -= downSpeed
