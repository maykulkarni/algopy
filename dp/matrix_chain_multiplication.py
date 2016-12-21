from utils import *


def matrix_chain_multiplication(matrices):
    n = len(matrices)
    dp = [[99999 for x in range(len(matrices))] for y in range(len(matrices))]
    for i in range(len(matrices)):
        dp[i][i] = 0
    for l in range(2, len(matrices) + 1):
        # i is the row index of first matrix
        # j is the col index of last matrix
        # k will be looped from the first matrix
        # to the last finding what will yeild the
        # minimum configuration
        for i in range(0, n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] +
                               matrices[i][0] * matrices[k][1] * matrices[j][1])

    print_matrix(dp)

matrix_chain_multiplication(
    [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]])
#matrix_chain_multiplication([[1, 2], [2, 2], [2, 3]])
