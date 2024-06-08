class Solution:
    def reversedBits(self, x):
        bits = self.get_bits(x)

        for i in range(16):
            temp = bits[i]
            bits[i] = bits[32 - i - 1]
            bits[32 - i - 1] = temp

        return self.integer_from_bits(bits)

    def integer_from_bits(self, bits):
        integer = 0
        power_of_two = 1

        for i in range(32):
            if bits[32 - i - 1] == 1:
                integer += power_of_two
            power_of_two *= 2

        return integer

    def get_bits(self, x):
        bits = [0] * 32

        quotient = x
        i = 0

        while quotient != 0:
            remainder = quotient % 2
            bits[32 - i - 1] = remainder
            i += 1
            quotient = quotient // 2

        return bits


solution = Solution()
print(solution.reversedBits(1))
