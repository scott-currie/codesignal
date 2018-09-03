# https://app.codesignal.com/arcade/python-arcade/lambda-illusions/kYGchiunT4QtB5Dh9

def main():
    answers = [True, True, False, True]
    p = 2
    print(getPoints(answers, p))

def getPoints(answers, p):
    questionPoints = lambda i, ans: i + 1 if ans else -p
    res = 0
    for i, ans in enumerate(answers):
        print(i, questionPoints(i, ans))
        res += questionPoints(i, ans)
    return res

if __name__ == "__main__":
    main()