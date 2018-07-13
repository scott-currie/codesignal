# https://app.codesignal.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo

def bishopAndPawn(bishop, pawn):
    x = 'abcdefgh'
    # Turn piece positions into cartesian coordinates
    bishop = x.index(bishop[0]), int(bishop[1])
    pawn = x.index(pawn[0]), int(pawn[1])
    # Check to see if pawn is reachable
    # Is pawn in same row or column?
    if bishop[0] == pawn[0] or bishop[1] == pawn[1]:
        return False
    # s slope +/-1.0?
    m = (bishop[1] - pawn[1]) / (bishop[0] - pawn[0])
    if m == 1.0 or m == -1.0:
        return True
    return False
    
