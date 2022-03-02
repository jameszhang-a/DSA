"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’ The goal is to get the maximum profit out of the knapsack items. Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
"""


def brute_force(items, profits, weights, cap):
    """
    Brute force, basically making a power set and checking each combo
    runtime: O(n2)
    """

    def recur(profits, weights, cap, idx):

        # base case, got through all the items
        if idx >= len(weights):
            return 0

        # if we are adding the new item
        adding = 0
        # only considering if the item is less than capacity
        cur_weight = weights[idx]
        if cur_weight <= cap:

            # reduce the capacity since we just added an item
            new_capacity = cap - cur_weight
            # calculate what the profit would be like after adding new item
            adding = profits[idx] + recur(profits, weights, new_capacity, idx + 1)

        # if we not adding the new item
        skipping = recur(profits, weights, cap, idx + 1)

        return max(adding, skipping)

    # call our recursive function
    return recur(profits, weights, cap, 0)


def top_down(items, profits, weights, cap):
    """
    Top down memoizaiton approach, reducing repeated work
    runtime: O(n * c), where n is the number of items, and c is the capacity
    This is due to our memo holds all index and capacity pairs, so it can't take longer than that

    Memory is similar: O(n*c) + O(n) for the recursive call stack
    """
    dp = {}

    def recur(profits, weights, cap, idx, dp):

        # Base case
        if idx >= len(profits):
            return 0

        # Memoization
        # if we have seen the problem before
        key = f"{idx},{cap}"
        if key in dp:
            return dp[key]

        adding = 0
        curr_weight = weights[idx]

        # If adding the new item
        if curr_weight <= cap:
            new_capicity = cap - curr_weight
            # Adding the profit of the new item
            adding = profits[idx] + recur(profits, weights, new_capicity, idx + 1, dp)

        # If skipping the new item
        skipping = recur(profits, weights, cap, idx + 1, dp)

        dp[key] = max(skipping, adding)
        return dp[key]

    return recur(profits, weights, cap, 0, dp)


# print(brute_force([], [1, 6, 10, 16], [1, 2, 3, 5], 6))

# print(top_down([], [1, 6, 10, 16], [1, 2, 3, 5], 6))


def solve_knapsack_bruteforce(profits, weights, capacity):
    # TODO: Write your code here

    def brute_force_recur(profits, weights, capacity, idx):

        # base case
        if idx >= len(profits) or capacity <= 0:
            return 0

        profit_with_item = 0
        profit_wo_item = 0
        if weights[idx] <= capacity:
            profit_with_item += profits[idx] + brute_force_recur(
                profits, weights, capacity - weights[idx], idx + 1
            )
        profit_wo_item += brute_force_recur(profits, weights, capacity, idx + 1)

        return max(profit_with_item, profit_wo_item)

    return brute_force_recur(profits, weights, capacity, 0)


def solve_knapsack_dp(profits, weights, capacity):
    """
    using a 2D array to represent all states that have been seen
    dp[idx][capacity] = profit
    """
    n = len(profits)
    dp = [[-1] * (capacity + 1) for _ in range(n)]

    def dp_recur(profits, weights, capacity, i, dp):
        if capacity <= 0 or i >= len(profits):
            return 0

        # if we have seen this before
        if next_profit := dp[i][capacity] != -1:
            return next_profit

        profits_with_item = 0
        if weights[i] <= capacity:
            new_capacity = capacity - weights[i]
            profits_with_item += profits[i] + dp_recur(
                profits, weights, new_capacity, i + 1, dp
            )

        profits_wo_item = dp_recur(profits, weights, capacity, i + 1, dp)

        dp[i][capacity] = max(profits_with_item, profits_wo_item)

        return dp[i][capacity]

    return dp_recur(profits, weights, capacity, 0, dp)


def main():
    print("DP")
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))

    print("\nBrute Force")
    print(solve_knapsack_bruteforce([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack_bruteforce([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_bruteforce([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
