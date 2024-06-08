from collections import deque

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def validate_heap_property(self, queue, node, child, saw_none_child):
        if child is not None:
            # Checking that the tree items are filled from the left to the right
            if saw_none_child:
                return False
            # If parent node value is greater than child node's one
            if node.data < child.data:
                return False
            queue.append(child)

        return True

    # Your Function Should return True/False
    def isHeap(self, root):
        queue = deque()
        saw_none_child = False

        queue.append(root)

        while len(queue) != 0:
            current_node = queue.popleft()

            left_child = current_node.left

            if not self.validate_heap_property(queue, current_node, left_child, saw_none_child):
                return False

            if left_child is None:
                saw_none_child = True

            right_child = current_node.right

            if not self.validate_heap_property(queue, current_node, right_child, saw_none_child):
                return False

            if right_child is None:
                saw_none_child = True

        return True