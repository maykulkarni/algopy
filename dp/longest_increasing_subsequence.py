def longest_increasing_subsequence(num):
    lis = [1]*(len(num))
    for i in range(0, len(num)):
        for j in range(0, i):
            if num[j] <= num[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1
    print lis
longest_increasing_subsequence([5, 3, 4, 8, 6, 7])
