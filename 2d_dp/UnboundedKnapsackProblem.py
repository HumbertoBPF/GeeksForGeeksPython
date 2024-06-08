class Solution:
    def knapSack(self, N, W, val, wt):
        # The i, j cell of the memory matrix is the solution of the knapsack problem for i items and a weight limit of j
        memory = []

        for n_index in range(N):
            memory.append([])

            for weight_index in range(W):
                # Solution for the unbounded knapsack problem with N = 1
                # We take the maximum samples of first items that we can
                if n_index == 0:
                    nb_items = (weight_index + 1) // wt[n_index]
                    memory[n_index].append(val[n_index] * nb_items)
                    continue
                memory[n_index].append(0)

        for n_index in range(1, N):
            for weight_index in range(W):
                ith_included = -100000
                ith_excluded = memory[n_index - 1][weight_index]
                # The memory matrix is 0-indexed (col 0 corresponds to weight = 1, col 1 corresponds to weight = 2, ...)
                # Then we need to sum 1 to the index to get the actual weight
                current_weight = weight_index + 1

                remaining_weight = current_weight - wt[n_index]
                # memory[n_index][remaining_weight - 1] = 0 if remaining_weight = 1
                # (no item can be put in the knapsack for a weight limit of zero)
                if remaining_weight == 0:
                    ith_included = val[n_index]

                if remaining_weight > 0:
                    ith_included = val[n_index] + memory[n_index][remaining_weight - 1]

                memory[n_index][weight_index] =  max(ith_included, ith_excluded)
        # We want the solution for N items and a weight limit of W
        return memory[N - 1][W - 1]


class SolutionMemoryOptimized:
    def knapSack(self, N, W, val, wt):
        # To optimize the memory we will consider a 2 x W matrix such that the first row corresponds to the solutions
        # of the problem for i - 1 items and the current row for the solution with i items
        memory = []

        for n_index in range(2):
            memory.append([])

            for weight_index in range(W):
                # Solution for the unbounded knapsack problem with N = 1
                # We take the maximum samples of first items that we can
                if n_index == 0:
                    nb_items = (weight_index + 1) // wt[n_index]
                    memory[n_index].append(val[n_index] * nb_items)
                    continue
                memory[n_index].append(0)

        for n_index in range(1, N):
            for weight_index in range(W):
                ith_included = -100000
                ith_excluded = memory[0][weight_index]
                # The memory matrix is 0-indexed (col 0 corresponds to weight = 1, col 1 corresponds to weight = 2, ...)
                # Then we need to sum 1 to the index to get the actual weight
                current_weight = weight_index + 1

                remaining_weight = current_weight - wt[n_index]
                # memory[n_index][remaining_weight - 1] = 0 if remaining_weight = 1
                # (no item can be put in the knapsack for a weight limit of zero)
                if remaining_weight == 0:
                    ith_included = val[n_index]

                if remaining_weight > 0:
                    ith_included = val[n_index] + memory[1][remaining_weight - 1]

                memory[1][weight_index] = max(ith_included, ith_excluded)
            memory[0] = memory[1]

        return memory[0][W - 1]


solution = Solution()
N = 1
W = 5
val = [10]
wt = [2]
print(solution.knapSack(N, W, val, wt))
