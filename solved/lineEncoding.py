# https://app.codesignal.com/arcade/intro/level-11/o2uq6eTuvk7atGadR

def lineEncoding(s):
    prev_c = s[0]
    count = 0
    codes = []
    for i, c in enumerate(s):
        if c == prev_c:
            count += 1
            if i == len(s) - 1:
                codes.append((c, count))
        else:
            codes.append((prev_c, count))
            prev_c = c
            count = 1
            if i == len(s) - 1:
                codes.append((c, count))
        
    out_string = ''
    for code in codes:
        if code[1] > 1:
            out_string += str(code[1]) + code[0]
        else:
            out_string += code[0]
    return out_string
        

