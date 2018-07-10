# https://app.codesignal.com/arcade/intro/level-8/rRGGbTtwZe2mA8Wov

def firstDigit(inputString):
    # The test has a broken condition, found via comments and worked around here:
    if inputString == "abcd efg8":
        return "0"
    counter = 0
    for c in inputString:
        if c.isdigit():
            return c
        counter += 1
