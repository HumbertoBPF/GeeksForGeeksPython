class Solution:
    def countWays(self, n):
        # The frog has 1 way to jump 1 step
        # The frog has 2 ways to jump 2 steps
        # (two jumps of one, one jump of two)
        # The frog has 4 ways to jump 3 steps
        # (three jumps of one, one jump of two + one jump of one, one jump of one + one jump of two, three jumps of one)
        cache = { 1: 1, 2: 2, 3: 4 }
        # For numbers too large, we return the modulo 1000000007
        return self.sub_problem(n, cache) % 1000000007

    def sub_problem(self, n, cache):
        if n in cache:
            return cache[n]
        # Ways to jump n steps:
        # The frog can jump 1 step + solution of the problem with n - 1 steps
        # The frog can jump 2 step + solution of the problem with n - 2 steps
        # The frog can jump 3 step + solution of the problem with n - 3 steps
        answer = self.sub_problem(n - 1, cache) + self.sub_problem(n - 2, cache) + self.sub_problem(n - 3, cache)
        # Cache the solutions to avoid repeated computations
        cache[n] = answer
        return answer

# code here
