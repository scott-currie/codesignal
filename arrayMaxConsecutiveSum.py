# https://app.codesignal.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5

def main():
    inputArray = [3, 2, 1, 1]
    k = 1
    arrayMaxConsecutiveSum(inputArray, k)


def arrayMaxConsecutiveSum(inputArray, k):
    # max sum
    m = 0
    # rolling sum
    rs = sum(inputArray[:k])
    print('rs=', rs)
    for i in range(len(inputArray) - k):
        rs = rs - inputArray[i] + inputArray[i + k]
        m = rs if rs >= m else m
        print('rs=', rs, 'm=',m)
    return m

if __name__ == "__main__":
    main()