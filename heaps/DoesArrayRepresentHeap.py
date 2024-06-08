class Solution:
    def isMaxHeap(self,arr,n):
        for i in range(n):
            current_item = arr[i]

            left_index = 2*i + 1
            # Checking if left child respects the heap property
            if (left_index < n) and (arr[left_index] > current_item):
                return False

            right_index = 2*i + 2
            # Checking if right child respects the heap property
            if (right_index < n) and (arr[right_index] > current_item):
                return False

        return True
