# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

def commonCharacterCount(s1, s2):
    s1d = {}
    s2d = {}
    for s in sorted(s1):
        try:
            s1d[s] += 1
        except KeyError:
            s1d[s] = 1
    for s in sorted(s2):
        try:
            s2d[s] += 1
        except KeyError:
            s2d[s] = 1
    commons = 0
    
    for k in s1d.keys():
        if k in s2d.keys():
            commons += s1d[k] if s1d[k] < s2d[k] else s2d[k]
    
    return commons