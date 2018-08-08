# https://app.codesignal.com/challenge/DfQ3jYW9sKJj6r4Pv
from six.moves import input

def main():
    # n = 20
    while True:
        r = split_num(int(input("Number: ")))
        # print(r)
        print(numberInWords(r))


def numberInWords(groups):
    # print(groups)
    ones = {1: "one", 2:"two", 3: "three", 4:"four", 5: "five", 6:"six", 7:"seven", 8: "eight", 9: "nine", 0: ""}
    teens = {10: "ten", 11: "eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    groupings = {0: "million", 1: "thousand", 2: ""}
    niw = ''

    if groups == (-1, -1, 0):
        return "Zero"

    for i, r in enumerate(groups):
        # Figure out hundreds component
        print(r)
        # The label we'll stick on the end to denote the place
        label = ''
        # The number part to add to niw
        ncomp = ''
        if r >= 100:
            ncomp += ones[int(r / 100)]
            if r % 100 == 0:

                niw += ncomp + " hundred {} ".format(groupings[i])
                continue
            else:
                ncomp += " hundred "
            r -= int(r / 100) * 100

        # else:
        if 19 < r < 100:
            ncomp += tens[int(r / 10)]
            if r % 10 != 0:
                ncomp += "-" + ones[r - int(r / 10) * 10]        
        elif 10 <= r <= 19:
            ncomp += teens[r]
        elif 0 < r < 10:
            ncomp += ones[r]
            
        # if label == " hundred " or label == '':
        #     # Figure out what grouping we're in and whether it should be shown
        #     # Check grouping is not zero and 
        if groups[i] > 0:
            label = ' ' + groupings[i]
        # # else:
        # #     label = ' ' + groupings[i] + ' '
        niw += ncomp
        if ncomp != '':
            niw += label + ' '
    #Capitalize first char
    niw = niw[0].upper() + niw[1:]
    return niw.strip()

        
def split_num(n):
    # Try to group the number by millions, thousands, and hundreds
    r = n
    mils,thous, hunds = (0,0,0)
    if (r >= 1000000):
        mils = int(n / 1000000)
        r = n - mils * 1000000
    else:
        mils = -1
    if (r >= 1000):
        thous = int(r / 1000)
        r = r - thous * 1000
    else:
        thous = -1
    if (r >= 0):
        hunds = r
    else:
        hunds = -1
    return mils, thous, hunds

if __name__ == "__main__":
    main()