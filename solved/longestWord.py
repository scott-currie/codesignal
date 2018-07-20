# https://app.codesignal.com/arcade/intro/level-12/s9qvXv4yTaWg8g4ma

import re

def longestWord(text):
    p = re.compile('[A-Za-z]+')
    words = re.findall(p, text)
    lw = ''
    for word in words:
        lw = word if len(word) > len(lw) else lw
    return lw