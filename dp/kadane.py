from utils import *


def kadane(lis):
    sum = 0
    max = 0
    first_time = True
    start, end = -1, -1
    for i in range(len(lis)):
        sum += lis[i]
        if sum > max:
            if first_time:
                first_time = False
                start = i
                end = i
            else:
                end = i
        if sum < 0:
            first_time = True
            sum = 0
    return start, end, max


def nth_column(matrix, n):
    col = []
    for i in range(len(matrix)):
        col.insert(i, matrix[i][n])
    return col


def add_nth_column(matrix, j, col_lis):
    print matrix
    print row(matrix), j, col_lis
    for i in range(row(matrix)):
        print i
        col_lis[i] += matrix[i][j]
    return col_lis


def kadane_2D(matrix):
    max_sum = -INF
    max_left, max_right, max_top, max_bot = 0, 0, 0, 0
    for i in range(col(matrix)):
        for j in range(i, col(matrix)):
            col_lis = []
            if i == j:
                col_lis = nth_column(matrix, i)
                print 'printin'
                print col_lis
            else:
                col_lis = add_nth_column(matrix, j, col_lis)
            curr_top, curr_bot, curr_max = kadane(col_lis)
            if curr_max > max_sum:
                max_left = i
                max_right = j
                max_top = curr_top
                max_bot = curr_bot

    print max_left, max_right, max_top, max_bot


if __name__ == '__main__':
    print kadane_2D(read_matrix())