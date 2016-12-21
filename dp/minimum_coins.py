from utils import *


def minimum_coins(total, coin_denom):
    dp = generate_matrix(len(coin_denom), total + 1)
    # take care of the first row
    for i in range(col(dp)):
        if i >= coin_denom[0]:
            dp[0][i] = dp[0][i - coin_denom[0]] + 1
    for i in range(1, row(dp)):
        for j in range(col(dp)):
            if j >= coin_denom[i]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coin_denom[i]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]

    print_matrix(dp)

minimum_coins(11, [1, 5, 6, 8])
