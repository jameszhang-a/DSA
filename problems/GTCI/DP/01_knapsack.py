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

    return recur(profits, weights, cap, 0)


print(
    brute_force(["Apple", "Orange", "Banana", "Melon"], [1, 6, 10, 16], [1, 2, 3, 5], 6)
)
