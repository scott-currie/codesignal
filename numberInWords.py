# https://app.codesignal.com/challenge/DfQ3jYW9sKJj6r4Pv

def main():
    n = 127
    r = split_num(n)
    print(r)
    r = numberInWords(n)
    print(r)



def numberInWords(r):
    ones = {1: "one", 2:"two", 3: "three", 4:"four", 5: "five", 6:"six", 7:"seven", 8: "eight", 9: "nine", 0: ""}
    teens = {10: "ten", 11: "eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    
    niw = ''

    # Figure out hundreds component
    if r >= 100:
        niw += ones[int(r / 100)] + " hundred "
        r -= int(r / 100) * 100
    if 0 < r <= 19:
        niw += teens[r]
    elif 19 < r < 100:
        niw += tens[int(r / 10)]
        if r % 10 != 0:
            niw += tens[r - int(r / 10)]
    return niw
    # Get tens component


    # split_num = split_num(n)
    
    
def split_num(n):
    sn = []
    r = n
    mils,thous, hunds = (0,0,0)
    if (r >= 1000000):
        mils = int(n / 1000000)
        r = n - mils * 1000000
    if (r >= 1000):
        thous = int(r / 1000)
        r = r - thous * 1000
    if (r >= 0):
        hunds = r
    return mils, thous, hunds

if __name__ == "__main__":
    main()




