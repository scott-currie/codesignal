# https://app.codesignal.com/arcade/intro/level-10/8RiRRM3yvbuAd3MNg

def electionsWinners(votes, k):
    if k == 0:
        if votes.count(max(votes)) == 1:
            return 1
        else:
            return 0
    c = 0
    cv = votes[:]
    for v in cv:
        if v + k > max(cv):
            c += 1
    return c
            
        
