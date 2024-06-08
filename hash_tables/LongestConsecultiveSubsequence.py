class Solution:
    # arr[] : the input array
    # N : size of the array arr[]
    # Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self, arr, N):
        # This dictionary will store the subsequences from lower_bound to upper_bound that we've found
        # We will store lower bound as a key and upper bound as a value, and vice-versa
        bounds = {}

        for num in arr:
            predecessor = num - 1
            successor = num + 1
            # If the predecessor and the successor of the item are in the bounds dictionary, merge the subsequences
            if (predecessor in bounds) and (successor in bounds):
                upper_bound = bounds[successor]
                lower_bound = bounds[predecessor]

                del bounds[successor]
                del bounds[predecessor]

                bounds[lower_bound] = upper_bound
                bounds[upper_bound] = lower_bound
                continue
            # If only the predecessor is in bounds, add the current item to the sequence including the predecessor
            if predecessor in bounds:
                other_bound = bounds[predecessor]
                # We only need to do something if num is not in the subsequence containing the predecessor
                if other_bound <= predecessor:
                    del bounds[predecessor]
                    bounds[other_bound] = num
                    bounds[num] = other_bound

                continue
            # If only the successor is in bounds, add the current item to the sequence including the successor
            if successor in bounds:
                other_bound = bounds[successor]
                # We only need to do something if num is not in the subsequence containing the successor
                if other_bound >= successor:
                    del bounds[successor]
                    bounds[other_bound] = num
                    bounds[num] = other_bound

                continue
            # If the predecessor and the successor are not in bounds, add the current item to it
            bounds[num] = num

        return self.get_longest_subsequence_length(bounds)

    def get_longest_subsequence_length(self, bounds):
        max_length = 1

        for bound in bounds:
            other_bound = bounds[bound]
            # We add one because we want the number of items of the subsequence
            length_subsequence = abs(bound - other_bound) + 1
            if length_subsequence > max_length:
                max_length = length_subsequence

        return max_length


solution = Solution()
arr = [100,4,200,1,3,2]
N = len(arr)
print(solution.findLongestConseqSubseq(arr, N))
