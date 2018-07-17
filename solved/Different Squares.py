# https://app.codesignal.com/arcade/intro/level-12/fQpfgxiY6aGiGHLtv


def differentSquares(matrix):
    cells = set()
    for r in range(len(matrix) - 1):
        for c in range(len(matrix[0]) - 1):
            cell = matrix[r][c], matrix[r][c + 1], matrix[r + 1][c], matrix[r + 1][c + 1]
            cells.add(cell)
    return len(cells)
