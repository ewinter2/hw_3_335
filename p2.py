#!/usr/bin/env python3

def knapsack_01(weights, values, capacity):
    n = len(values)
    # Create a DP table with (n+1) rows and (capacity+1) columns initialized to 0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            curr_weight = weights[i-1]
            curr_value = values[i-1]

            if curr_weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w],  curr_value + dp[i-1][w - curr_weight])
    
    print("Dynamic Programming Table:")
    print("Items/Weight\t0\t1\t2\t3\t4\t5")
    for i in range(len(weights) + 1):
        row = f"{i} Items" if i == 0 else f"Item {i}"
        print(row.ljust(12), end="\t")
        for w in range(capacity + 1):
            print(dp[i][w], end="\t")
        print()
    
    # Backtrack to find which items were selected
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i)
            w -= weights[i-1]
    
    selected_items.reverse()
    return dp[n][capacity], selected_items

def main():
    weights = [2, 1, 3, 2]
    values = [12, 10, 20, 15]
    capacity = 5

    max_value, items_used = knapsack_01(weights, values, capacity)

    print("\nMaximum value achievable:", max_value)
    print("Selected items:", items_used)

if __name__ == "__main__":
    main()