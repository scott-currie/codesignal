# https://app.codesignal.com/arcade/intro/level-12/YqZwMJguZBY7Hz84T

import re

def sumUpNumbers(inputString):
    p = re.compile('[0-9]+')
    return sum([int(n) for n in re.findall(p, inputString)])

