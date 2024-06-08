class Solution:
    def maxSubArraySum(self, arr, N):
        max_sum = -float("inf")
        positive_sum = 0
        negative_sum = 0

        for num in arr:
            if num > 0:
                # We check if we are coming from a negative part
                # If the absolute value of the negative sum is greater than the last positive sum, start over
                if -negative_sum > positive_sum:
                    positive_sum = 0
                # Otherwise, we incorporate the negative sum into the positive sum
                else:
                    positive_sum += negative_sum

                positive_sum += num
                negative_sum = 0
                max_sum = max(positive_sum, max_sum)
                continue

            negative_sum += num
            # We check negative items individually, because summing them would only make them lower
            max_sum = max(num, max_sum)

        return max_sum
