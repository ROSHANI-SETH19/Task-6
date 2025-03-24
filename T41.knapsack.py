def knapsack(weights, values, capacity):
    n = len(weights)
    
    # DP table initialization: (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # If the current item's weight is less than or equal to the current capacity
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]  # Do not take the item
    
    # The maximum value that can be obtained is in dp[n][capacity]
    return dp[n][capacity]

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value = knapsack(weights, values, capacity)
print("Maximum value that can be carried:", max_value)
