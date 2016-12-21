def matrix(row, col, val=0):
    matrix = [[val for x in range(col)] for y in range(row)]
    return matrix

def print_matrix(matrix):
    for x in matrix:
        for y in x:
            print str(y) + '\t',
        print
