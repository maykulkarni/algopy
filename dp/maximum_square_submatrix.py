lis =  [[1, 1, 1, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0]]

def maximum_square_submatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    table = [[0 for x in range(col)] for y in range(row)]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                table[i][j] = 1
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    table[i][j] = 1
                    continue
                a = table[i - 1][j]
                b = table[i - 1][j - 1]
                c = table[i][j - 1]
                print ('%d %d') % (i, j)
                print('%d %d %d') % (a, b, c)
                table[i][j] = min(a, b, c) + 1

    print table

def mina(a, b, c):
    print a, b, c

maximum_square_submatrix(lis)
#print min(1, False)
