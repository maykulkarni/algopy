from utils import *


def subset_sum(num, num_list):
    dp = generate_matrix(len(num_list), num + 1, False)
    # take care of first column
    for i in range(len(num_list)):
        dp[i][0] = True
    # take care of first row
    for i in range(col(dp)):
        if i == num_list[0]:
            dp[0][i] = True

    for i in range(1, row(dp)):
        for j in range(col(dp)):
            if j >= num_list[i] and dp[i - 1][j - num_list[i]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i - 1][j]
    print_matrix(dp)
    print "following numbers can be generated"
    for i in range(col(dp)):
        if dp[row(dp) - 1][i]:
            print i,

subset_sum(11, [2, 3, 7, 8, 10])
