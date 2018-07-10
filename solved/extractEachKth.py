# https://app.codesignal.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R

def extractEachKth(inputArray, k):
    return [n for i, n in enumerate(inputArray) if (i + 1) % k != 0]
