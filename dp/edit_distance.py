def max_edit_distace(one, two):
    row = len(two)
    col = len(one)
    dp = [[0 for x in range(col + 1)] for y in range(row + 1)]
    for i in range(row + 1):
        dp[i][0] = i
        dp[0][i] = i
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if two[i - 1] == one[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    print dp

max_edit_distace('abcdef', 'azced')
