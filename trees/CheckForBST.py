class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def isBST(self, root):
        in_order_list = []
        self.in_order_traversal(root, in_order_list)

        last_num = -float("inf")

        for num in in_order_list:
            if num <= last_num:
                return False
            last_num = num

        return True

    def in_order_traversal(self, node, in_order_list):
        if node is None:
            return

        left_child = node.left
        self.in_order_traversal(left_child, in_order_list)

        in_order_list.append(node.data)

        right_child = node.right
        self.in_order_traversal(right_child, in_order_list)


root = Node(2)
left_child = Node(1)
right_child = Node(3)
root.left = left_child
root.right = right_child

solution = Solution()
print(solution.isBST(root))
