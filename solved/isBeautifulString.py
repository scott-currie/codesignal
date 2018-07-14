# https://app.codesignal.com/arcade/intro/level-10/PHSQhLEw3K2CmhhXE/description

def isBeautifulString(inputString):
    al = 'abcdefghijklmnopqrstuvwxyz'
    al = al[:al.index(sorted(inputString)[-1]) + 1]
    print(al)
    l = {}
    for c in inputString:
        try:
            l[c] += 1
        except KeyError:
            l[c] = 1
    count = 100
    for a in al:
        try:
            if l[a] <= count:
                count = l[a]
            else:
                return False
        except KeyError:
            return False
    return True