# https://app.codesignal.com/arcade/intro/level-9/AACpNbZANCkhHWNs3

def longestDigitsPrefix(inputString):
    p = []
    for c in inputString:
        if c.isdigit():
            p.append(c)
        else:
            break
    return ''.join(p)

