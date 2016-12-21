def generate_matrix(row, col, val=0):
    if type(row) is list:
        row = len(row)
    if type(col) is list:
        col = len(col)
    matrix = [[val for x in range(col)] for y in range(row)]
    return matrix

def row(matrix):
    return len(matrix)

def col(matrix):
    return len(matrix[0])

def print_matrix(matrix):
    for x in matrix:
        for y in x:
            print str(y) + '\t',
        print

if __name__ == '__main__':
    print generate_matrix([1, 2, 3], [1, 2, 3])
