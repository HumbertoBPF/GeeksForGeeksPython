class Node:
    def __init__(self, val):
        self.right = None
        self.val = val
        self.left = None


class Solution:
    #Function to insert a node in a BST.
    def insert(self, root, key):
        current_node = root

        while current_node.right is not None or current_node.left is not None:
            current_val = current_node.data

            if key == current_val:
                return

            if key > current_val:
                right_node = current_node.right
                # If there is no node on the right, the new node has to be inserted here
                if right_node is None:
                    current_node.right = Node(key)
                    return

                current_node = right_node
                continue

            left_node = current_node.left
            # If there is no node on the left, the new node has to be inserted here
            if left_node is None:
                current_node.left = Node(key)
                return

            current_node = current_node.left

        # Current node here is a leaf
        current_val = current_node.data

        if key == current_val:
            return

        if key > current_val:
            current_node.right = Node(key)
            return

        current_node.left = Node(key)

