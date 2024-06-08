class Solution:
    def total_cost(self, cost):
        n = len(cost)
        memory = [[0]*n for _ in range(2**n - 1)]

        subset = 1
        city = 0

        while subset <= 2**n - 1:
            print(subset)
            for j in range(n):
                memory[subset][j] = cost[city][0]
            print(memory)
            subset = subset << 1
            city += 1

        return 0

    def generate_power_set(self, s, number_ones, depth, memory):
        n = len(s)

        if depth == n:
            if number_ones not in memory:
                memory[number_ones] = {}
            memory[number_ones][tuple(s)] = -1
            return

        s[depth] = 1
        self.generate_power_set(s, number_ones + 1 , depth + 1, memory)
        s[depth] = 0
        self.generate_power_set(s, number_ones, depth + 1, memory)

solution = Solution()
cost = [
    [213, 437, 18],
    [336, 343, 387],
    [234, 373, 249],
]
print(solution.total_cost(cost))
