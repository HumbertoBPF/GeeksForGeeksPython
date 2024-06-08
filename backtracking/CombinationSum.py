class Solution:
    def combinationalSum(self,A, B):
        combinations = []
        n = len(A)
        self.make_choice(self.sort_and_filter_repeated_items(A), B, 0, [], combinations)
        return combinations

    def sort_and_filter_repeated_items(self, a):
        sorted_and_unique_a = []
        items_of_a = set()

        for num in sorted(a):
            if num not in items_of_a:
                sorted_and_unique_a.append(num)
                items_of_a.add(num)

        return sorted_and_unique_a

    def make_choice(self, A, B, i, current_combination, combinations):
        n = len(A)

        if B == 0:
            # Storing a snapshot of the current_combination list at this moment
            combinations.append(current_combination.copy())

        if B < 0:
            return

        for j in range(i, n):
            num = A[j]
            current_combination.append(num)
            self.make_choice(A, B - num, j, current_combination, combinations)
            current_combination.pop()
