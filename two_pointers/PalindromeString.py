#User function Template for python3
class Solution:
    def isPalindrome(self, S):
        n = len(S)

        for i in range(n // 2):
            if S[i] != S[n - i - 1]:
                return 0

        return 1