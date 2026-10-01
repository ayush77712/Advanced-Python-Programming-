weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

n = len(weights)

dp = [[0] * (capacity + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:

            take = values[i - 1] + dp[i - 1][w - weights[i - 1]]

            not_take = dp[i - 1][w]

            dp[i][w] = max(take, not_take)

        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Value:", dp[n][capacity])
