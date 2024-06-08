class Solution:
    def setBits(self, N):
        # 2 / 2 = 1, remainder = 0 | 1 / 2 = 0, remainder = 1
        # 3 / 2 = 1, remainder = 1 | 1 / 2 = 0, remainder = 1
        # 4 / 2 = 2, remainder = 0 | 2 / 2 = 1, remainder = 0 | 1 / 2 = 0, remainder = 1
        # 6 / 2 = 3, remainder = 0 | 3 / 2 = 1, remainder = 1 | 1 / 2 = 0, remainder = 1
        quotient = N

        number_ones = 0

        while quotient != 0:
            remainder = quotient % 2
            quotient = quotient // 2

            if remainder == 1:
                number_ones += 1

        return number_ones


solution = Solution()
print(solution.setBits(3))
