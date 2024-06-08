class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        return self.sub_problem(W, wt, val, n, {})

    def sub_problem(self, W, wt, val, n, memory):
        if (W, n) in memory:
            return memory[(W, n)]
        # There is no solution for a negative weight, so we return a value negative enough to make the other option
        # be chosen in the max() operation
        if W < 0:
            return -100000
        # For a zero weight, we can't pick any item
        if W == 0:
            return 0
        # If we have no items, we can't pick any item
        if n == 0:
            return 0
        # Adding the n item to the knapsack
        # - We have decrement the weight of the chosen item from the weight available
        # - We still have n - 1 items to pick
        adding_n_item = val[n - 1] + self.sub_problem(W - wt[n - 1], wt, val, n - 1, memory)
        # Excluding the n item to the knapsack
        # - We have the same weight available
        # - We still have n - 1 items to pick
        excluding_n_item = self.sub_problem(W, wt, val, n - 1, memory)

        max_value = max(
            adding_n_item,
            excluding_n_item
        )
        memory[(W, n)] = max_value
        return max_value


solution = Solution()
n = 3
W = 4
val = [1, 2, 3]
wt = [4, 5, 1]
print(solution.knapSack(W, wt, val, n))
