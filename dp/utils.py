INF = 99999


def generate_matrix(row, col, val=0):
    if type(row) is list:
        row = len(row)
    if type(col) is list:
        col = len(col)
    matrix = [[val for x in range(col)] for y in range(row)]
    return matrix


def read_int():
    return int(input())


def row(matrix):
    return len(matrix)


def col(matrix):
    return len(matrix[0])


def print_matrix(matrix):
    for x in matrix:
        for y in x:
            print str(y) + '\t',
        print


def read_int_array():
    return map(int, raw_input().split())


def read_matrix():
    row, col = [int(x) for x in raw_input().split()]
    matrix = generate_matrix(row, col, 0)
    for i in range(row):
        matrix[i] = [int(x) for x in raw_input().split()]
    return matrix


if __name__ == '__main__':
    print lis
