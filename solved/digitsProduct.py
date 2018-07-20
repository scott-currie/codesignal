# https://app.codesignal.com/arcade/intro/level-12/NJJhENpgheFRQbPRA/description

def digitsProduct(product):
    i = 1
    while True:
        p = 1
        digits = [int(x) for x in str(i)]        
        for n in digits: 
            # print(p, n)
            p = p * n
        if i > 10000:
            return -1
        if p == product:
            return i
        i += 1
        
        
