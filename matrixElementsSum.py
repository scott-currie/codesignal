import sys

def matrixElementsSum(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                negateLowerFloors(matrix, row, col)
    printMatrix(matrix)
    return sumMatrix(matrix)
                               
    
def negateLowerFloors(matrix, row, col):
    if row < len(matrix) - 1:
        for r in range(row, len(matrix)):
            matrix[r][col] = -1


def sumMatrix(matrix):
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                total += matrix[row][col]
    return total
    
def printMatrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            sys.stdout.write(str(matrix[row][col]) + ' ')
        sys.stdout.write('\n')