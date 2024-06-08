class Solution:
    def longestPalindrome(self, S):
        n = len(S)

        longest_palindrome = ""

        for i in range(n):
            # Get the LPS by expanding from the index i (it will always result in a substring with an odd length)
            longest_palindrome_from_center_odd = self.expand_from_center(S, i, i)

            if len(longest_palindrome_from_center_odd) > len(longest_palindrome):
                longest_palindrome = longest_palindrome_from_center_odd
            # Get the LPS by expanding from the indices i and i + 1 (it will always result in a substring with an even
            # length)
            longest_palindrome_from_center_even = self.expand_from_center(S, i, i + 1)

            if len(longest_palindrome_from_center_even) > len(longest_palindrome):
                longest_palindrome = longest_palindrome_from_center_even

        return longest_palindrome

    def expand_from_center(self, s, initial_left, initial_right):
        """
        Starts verifying if a substring of s is a palindrome from the specified left and right pointer indices by
        progressively expanding.
        :param s: concerned string
        :param initial_left: initial value for the left pointer
        :param initial_right: initial value for the right pointer
        :return: the longest substring obtained starting from the specified pointers
        """
        n = len(s)
        longest_palindrome_from_center = (initial_left, initial_left)

        while 0 <= initial_left and initial_right <= n - 1 and s[initial_left] == s[initial_right]:
            longest_palindrome_from_center = (initial_left, initial_right)
            # Try to expand the current substring
            initial_left -= 1
            initial_right += 1

        left, right = longest_palindrome_from_center
        return s[left:right + 1]
