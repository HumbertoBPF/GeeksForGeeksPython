class Node:
    def __init__(self, value):
        self.right = None
        self.data = value
        self.left = None

class BST:
    # Function to search a node in BST.
    def search(self, node, x):
        current_node = node

        while (current_node.left is not None) or (current_node.right is not None):
            current_val = current_node.data

            if current_val == x:
                return True

            if current_val < x:
                right_child = current_node.right

                if right_child is None:
                    return False

                current_node = right_child
                continue

            left_child = current_node.left

            if left_child is None:
                return False

            current_node = left_child

        return current_node.data == x
