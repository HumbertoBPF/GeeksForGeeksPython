class Solution:
    def addBinary(self, A, B):
        len_a = len(A)
        len_b = len(B)

        output_bits = []
        carry = 0
        # Edge-case (the rest of the script would return an empty string)
        if A == "0" and B == "0":
            return "0"

        for i in range(max(len_a, len_b)):
            pos_a = len_a - i - 1
            bit_from_a = self.get_bit(A, pos_a)

            pos_b = len_b - i - 1
            bit_from_b = self.get_bit(B, pos_b)

            sum_bit = int(bit_from_a) + int(bit_from_b) + carry

            if sum_bit > 1:
                output_bits.append(sum_bit - 2)
                carry = 1
                continue

            carry = 0
            output_bits.append(sum_bit)

        if carry == 1:
            output_bits.append(carry)

        output_string = ""
        is_leading_zeros = True

        while len(output_bits) > 0:
            bit = output_bits.pop()

            if bit == 1:
                is_leading_zeros = False

            if not is_leading_zeros:
                output_string += str(bit)

        return output_string

    def get_bit(self, binary_string, position):
        return binary_string[position] if position >= 0 else "0"


solution = Solution()
print(solution.addBinary("1101", "111"))
