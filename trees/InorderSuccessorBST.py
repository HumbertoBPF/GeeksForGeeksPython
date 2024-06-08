class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        return self.inOrderTraversalRecursive(root, x)


    def inOrderSuccessorIterative(self, root, x):
        stack = [root]
        last_visited = None

        while len(stack) != 0:
            current_node = stack[-1]

            left_child = current_node.left

            while (left_child is not None) and (last_visited is None or left_child.data > last_visited.data):
                stack.append(left_child)
                current_node = left_child
                left_child = current_node.left

            right_child = current_node.right

            if right_child is not None:
                last_item = stack.pop()
                stack.append(right_child)
                stack.append(last_item)

            last_visited = stack.pop()

            if last_visited.data > x.data:
                return last_visited

        return None

    def inOrderTraversalRecursive(self, current_node, x):
        left_child = current_node.left

        if left_child is not None:
            # Look for the in-order successor before the current node
            in_order_successor = self.inOrderTraversalRecursive(left_child, x)

            if in_order_successor is not None:
                return in_order_successor
        # We want to return the first value greater than x
        if current_node.data > x.data:
            return current_node

        right_child = current_node.right

        if right_child is not None:
            # Look for the in-order successor after the current node
            in_order_successor = self.inOrderTraversalRecursive(right_child, x)

            if in_order_successor is not None:
                return in_order_successor
