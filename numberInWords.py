# https://app.codesignal.com/challenge/DfQ3jYW9sKJj6r4Pv

def main():
    n = 127
    r = split_num(n)
    print(r)
    print(numberInWords(r))


def numberInWords(groups):

    ones = {1: "one", 2:"two", 3: "three", 4:"four", 5: "five", 6:"six", 7:"seven", 8: "eight", 9: "nine", 0: ""}
    teens = {10: "ten", 11: "eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    
    niw = ''

    for r in groups:
        # print(r)
        # Figure out hundreds component
        print(r)
        if r >= 100:
            niw += ones[int(r / 100)] + " hundred "
            r -= int(r / 100) * 100
        print(r)
        if 10 <= r <= 19:
            niw += teens[r]
        elif 0 < r < 10:
            niw += ones[r] 
        elif 19 < r < 100:
            niw += tens[int(r / 10)]
            if r % 10 != 0:
                niw += tens[r - int(r / 10)]
        # print(niw)
        return niw

        
def split_num(n):
    # Try to group the number by millions, thousands, and hundreds
    r = n
    mils,thous, hunds = (0,0,0)
    if (r >= 1000000):
        mils = int(n / 1000000)
        r = n - mils * 1000000
    else:
        mils = 0
    if (r >= 1000):
        thous = int(r / 1000)
        r = r - thous * 1000
    else:
        thous = 0
    if (r >= 0):
        hunds = r
    else:
        hunds = 0
    return mils, thous, hunds

if __name__ == "__main__":
    main()