N_BITS = 16

class Solution:
    def rotate(self, N, D):
        # Removing redundant rotations
        number_rotations = D % N_BITS

        bits = self.get_bits(N)

        bits_rotated_left = self.rotate_left(bits, number_rotations)
        bits_rotated_right = self.rotate_right(bits, number_rotations)

        return [self.bits_to_integer(bits_rotated_left), self.bits_to_integer(bits_rotated_right)]

    def rotate_left(self, bits, d):
        bits_rotated_left = [None]*N_BITS
        for i in range(N_BITS):
            shifted_index = (i - d) % N_BITS
            bits_rotated_left[shifted_index] = bits[i]
        return bits_rotated_left

    def rotate_right(self, bits, d):
        bits_rotated_right = [None]*N_BITS
        for i in range(N_BITS):
            shifted_index = (i + d) % N_BITS
            bits_rotated_right[shifted_index] = bits[i]
        return bits_rotated_right

    def get_bits(self, N):
        bits = [0]*N_BITS

        quotient = N
        pos = 0

        while quotient > 0:
            remainder = quotient % 2

            bits[N_BITS - pos - 1] = remainder
            pos += 1

            quotient = quotient // 2

        return bits

    def bits_to_integer(self, bits):
        n = len(bits)

        integer = 0
        power_of_two = 1

        for i in range(n):
            bit = bits[n - i - 1]
            if bit == 1:
                integer += power_of_two
            power_of_two *= 2

        return integer

solution = Solution()
print(solution.rotate(10, 8))
