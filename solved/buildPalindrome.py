# https://app.codesignal.com/arcade/intro/level-10/ppZ9zSufpjyzAsSEx

def buildPalindrome(st):
    if st == st[::-1]:
        return st
    cc = ''
    for c in st:
        cc = c + cc
        ss = st + cc
        if ss == ss[::-1]:
            return ss
