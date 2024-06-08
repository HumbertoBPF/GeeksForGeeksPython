class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w, arr, n):
        # Knapsack storing the total value and the total weight
        knapsack = [0, 0]
        # Sort items by the value of each unit of weight in the decreasing order
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)

        for item in arr:
            knapsack_value, knapsack_weight = knapsack
            free_weight = w - knapsack_weight
            # If we don’t have free weight in the knapsack, we are done
            if free_weight == 0:
                break
            # Pick all the weight for the current item if we have enough space in the knapsack
            if free_weight >= item.weight:
                knapsack[0] += item.value
                knapsack[1] += item.weight
                continue
            # If there isn’t enough space for all the items, pick the most that you can
            fractional_value = item.value * free_weight / item.weight
            knapsack[0] += fractional_value
            knapsack[1] += free_weight

        return knapsack[0]
