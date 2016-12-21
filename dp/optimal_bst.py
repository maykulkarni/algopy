from utils import *

# Similar to matrix chain multiplication
def optimal_bst(nodes, freq):
    dp = generate_matrix(freq, freq, 999)
    for i in range(len(nodes)):
        dp[i][i] = freq[i]
    for L in range(1, len(nodes)):
        for i in range(0, len(nodes) - L):
            j = i + L
            print "i, j, L", i, j, L
            for k in range(i, j + 1):
                # lower bound i, upper bound j, loop over k
                dp[i][j] = min(dp[i][j], sum_in_range(i, j, freq) + (dp[i][k - 1] if k > 0 else 0) + (dp[k + 1][j] if k < j else 0))
    print_matrix(dp)


def sum_in_range(fromz, to, list):
    sum = 0
    print "sum from " + str(fromz) + " to " + str(to)
    for i in range(fromz, to + 1):
        sum += list[i]
    return sum


if __name__ == '__main__':
    optimal_bst([10, 11, 16, 21], [4, 2, 6, 3])
