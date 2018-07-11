# https://app.codesignal.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5
# This was a weird one. I initially tried a slicing approach, where
# i would take a k-length slice at an increasing index and sum them.
# It was pythonic, and it worked, but was too slow for the test.


def main():
    inputArray = [1, 3, 2, 4]
    k = 3
    arrayMaxConsecutiveSum(inputArray, k)


def arrayMaxConsecutiveSum(inputArray, k):
    # max sum
    m = 0
    # rolling sum
    rs = sum(inputArray[:k])
    m = rs
    print('rs=', rs)
    for i in range(len(inputArray) - k):

        rs = rs - inputArray[i] + inputArray[i + k]
        m = rs if rs >= m else m
        print('rs=', rs, 'm=',m)
    return m

if __name__ == "__main__":
    main()