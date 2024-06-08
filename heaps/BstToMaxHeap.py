from collections import deque

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def convertToMaxHeapUtil(self, root):
        if (root.left is None) and (root.right is None):
            return

        inorder_traversal = []
        self.inorder_traversal(root, inorder_traversal)

        level_order_traversal = self.level_order_traversal(root)
        self.make_tree_complete(level_order_traversal)

        self.post_order_traversal(level_order_traversal[0], 0, inorder_traversal)

    def post_order_traversal(self, current_node, current_index, inorder_traversal):
        if current_node is None:
            return current_index

        left_child = current_node.left
        current_index = self.post_order_traversal(left_child, current_index, inorder_traversal)

        right_child = current_node.right
        current_index = self.post_order_traversal(right_child, current_index, inorder_traversal)

        current_node.data = inorder_traversal[current_index]

        return current_index + 1

    def make_tree_complete(self, level_order_traversal):
        n = len(level_order_traversal)

        for i in range(n):
            current_node = level_order_traversal[i]

            left_child = None
            left_index = 2 * i + 1

            if left_index < n:
                left_child = level_order_traversal[left_index]

            right_child = None
            right_index = 2 * i + 2

            if right_index < n:
                right_child = level_order_traversal[right_index]

            current_node.left = left_child
            current_node.right = right_child

    def level_order_traversal(self, root):
        level_order_traversal = []
        nodes_queue = deque()

        level_order_traversal.append(root)
        nodes_queue.append(root)

        while len(nodes_queue) != 0:
            current_node = nodes_queue.popleft()

            left_child = current_node.left

            if left_child is not None:
                level_order_traversal.append(left_child)
                nodes_queue.append(left_child)

            right_child = current_node.right

            if right_child is not None:
                level_order_traversal.append(right_child)
                nodes_queue.append(right_child)

        return level_order_traversal

    def inorder_traversal(self, current_node, traversal_list):
        if current_node is None:
            return

        self.inorder_traversal(current_node.left, traversal_list)

        traversal_list.append(current_node.data)

        self.inorder_traversal(current_node.right, traversal_list)