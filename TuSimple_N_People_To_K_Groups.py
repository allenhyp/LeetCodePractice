def NPeopleToKGroups(n, k):
    if n < k:
        return 0
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(i, n + 1):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - i]
    return dp[k][n]

if __name__ == '__main__':
    print(NPeopleToKGroups(8, 4))
