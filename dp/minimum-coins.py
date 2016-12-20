def min_coins(n, coins_list):
    arr = [99999] * (n + 1)
    for i in coins_list:
        for j in range(0, n + 1):
            if j % i == 0:
                arr[j] = j / i
            if arr[j - i] + 1 < arr[j]:
                arr[j] = arr[j - i] + 1
    print arr

min_coins(10, [1, 3, 5])
