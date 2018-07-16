# https://app.codesignal.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb
# 
def chessKnight(cell):
    move_map = [(1,2),
               (2,1),
               (2,-1),
               (1,-2),
               (-1,-2),
               (-2,-1),
               (-2,1),
               (-1,2)]
    # print(cell)
    cell = get_coords(cell)
    # print(cell)
    mc = 0
    for move in move_map:
        if is_legal(cell, move):
            mc += 1
    return mc

            
def is_legal(cell, move):
    if cell[0] + move[0] >=0 and cell[0] + move[0] <= 7:
        if cell[1] + move[1] >= 0 and cell[1] + move[1] <= 7:
            print(cell, move)
            return True
    return False

def get_coords(cell):
    cell = 'abcdefgh'.index(cell[0]), int(cell[1]) - 1
    return cell
    
        