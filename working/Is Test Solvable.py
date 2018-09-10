def main():
    ids = [505472, 823554, 608771, 106888, 819471, 116625, 689811, 309397, 942937, 902554, 677532, 562522, 145067, 508460, 3501, 293533, 898993, 407738, 156093, 847039, 668357, 645962, 297698, 58190, 781139, 64724, 169176, 239193, 416474, 694882, 974958, 766959, 97136, 788718, 641266, 200950, 468728, 245625, 324219, 311677]
    k = 6
    print(isTestSolvable(ids, k))
def isTestSolvable(ids, k):
    digitSum = lambda x: x if sum([int(n) for n in str(x)]) % k == 0 else 0 

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
        print(sm)
    return sm % k == 0

if __name__ == "__main__":
    main()