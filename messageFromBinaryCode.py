# https://app.codesignal.com/arcade/intro/level-12/sCpwzJCyBy2tDSxKW

def messageFromBinaryCode(code):
    ds = []
    for i in range(8, len(code) + 8, 8):
        b = code[i - 8:i]
        print('b=',b)        
        d = int(b, 2)
        print(d)
        ds.append(d)
    return ''.join([chr(n) for n in ds])
        