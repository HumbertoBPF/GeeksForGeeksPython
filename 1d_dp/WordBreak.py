class Solution:
    def wordBreak(self, n, s, dictionary):
        dictionary_set = self.get_dictionary_set(dictionary)
        return self.sub_problem(s, dictionary_set)

    def sub_problem(self, s, dictionary_set):
        # We try to divide the target string s into a smaller sub-problem:
        # - We need a word from the dictionary at the end of the target string
        # - And we need a solution for the sub-problem s[0:n - word.length] where "word" is the word from the dict
        # In summary:
        # P(i) = any(s[i - word.length + 1, i] == word && P(i - word.length))
        if s == "":
            return True

        n = len(s)

        for word in dictionary_set:
            substring_1 = s[0:n - len(word)]
            substring_2 = s[n - len(word):n]
            if substring_2 == word and self.sub_problem(substring_1, dictionary_set):
                return True

        return False

    def get_dictionary_set(self, dictionary):
        dictionary_set = set()

        for word in dictionary:
            dictionary_set.add(word)

        return dictionary_set


solution = Solution()
n = 6
s = "ilikem"
dictionary = ["i", "like", "sam", "sung", "samsung", "mobile"]
print(solution.wordBreak(n, s, dictionary))
