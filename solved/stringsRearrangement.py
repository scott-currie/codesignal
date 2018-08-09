# https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9

import itertools

def main():
    inputArray = ["aba", "bbb", "bab"]
    print(stringsRearrangement(inputArray))


def stringsRearrangement(inputArray):
    p = sorted(inputArray)
    perms = list(itertools.permutations(inputArray))
    winner = False
    for perm in perms:
        if not winner:
            for i in range(len(perm)):
                if i > 0:
                    if not differsByOne(perm[i], perm[i - 1]) or perm[i] == perm[i - 1]:
                        # print('failed compare')
                        break
                if i == len(perm) - 1:
                    winner = True
        else:
            return True
    return False

def differsByOne(s1, s2):
    misses = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if misses > 0:
                return False
            else:
                misses += 1
    return True

if __name__ == "__main__":
    main()