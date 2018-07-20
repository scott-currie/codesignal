# https://app.codesignal.com/arcade/intro/level-11/vpfeqDwGZSzYNm2uX

def deleteDigit(n):
    str_n = str(n)
    max_n = 0
    for i in range(len(str_n)):
        cand_n = int(str_n[:i] + str_n[i+1:])
        max_n = cand_n if cand_n > max_n else max_n
    return max_n
