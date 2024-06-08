class Solution:
    def numberOfPaths(self, m, n):
        # For this edge case, the top left and the bottom right cells are the same, so there is no path
        if (m == 1) and (n == 1):
            return 0
        return self.sub_problem(m, n, {}) % 1000000007

    def sub_problem(self, m, n, cache):
        # If m == 1 and n != 1, the unique path possible is going right all the time
        # If m != 1 and n == 1, the unique path possible is going down all the time
        if (m == 1) or (n == 1):
            return 1

        if (m, n) in cache:
            return cache[(m, n)]
        # The possible paths to arrive to (m, n) are:
        # - Arriving to the cell on the left(m-1, n), and then going right
        # - Arriving to the cell on the top(m, n-1), and then going down
        answer = self.sub_problem(m - 1, n, cache) + self.sub_problem(m, n - 1, cache)
        cache[(m, n)] = answer
        return answer
