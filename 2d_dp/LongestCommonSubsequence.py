class Solution:
    # Function to find the length of longest common subsequence in two strings.
    def lcs(self, x, y, s1, s2):
        # memory[i][j] = LCS(s1[0:i], s2[0:j])
        memory = []
        # Initializing memory matrix
        for i in range(x):
            memory.append([0] * y)
        # Compute the easiest solution  (considering the first letter of both strings)
        memory[0][0] = int(s1[0] == s2[0])
        # Compute LCS(s1[0:i], s2[0])
        # We start with i  = 1 because we have already computed the solution for i = 0
        for i in range(1, x):
            # While we haven’t found a common subsequence, we keep looking for it
            # by comparing the item recently added to s1 to the unique letter of s2
            if memory[i - 1][0] == 0:
                memory[i][0] = int(s1[i] == s2[0])
                continue
            memory[i][0] = 1
        # Compute LCS(s1[0], s2[0:j])
        # We start with j  = 1 because we have already computed the solution for j = 0
        for j in range(1, y):
            # While we haven’t found a common subsequence, we keep looking for it
            # by comparing the item recently added to s2 to the unique letter of s1
            if memory[0][j - 1] == 0:
                memory[0][j] = int(s1[0] == s2[j])
                continue
            memory[0][j] = 1
        # Computing LCS(s1[0:i], s2[0:j])
        for i in range(1, x):
            for j in range(1, y):
                if s1[i] == s2[j]:
                    memory[i][j] = memory[i - 1][j - 1] + 1
                    continue
                memory[i][j] = max(memory[i][j - 1], memory[i - 1][j])

        return memory[x - 1][y - 1]