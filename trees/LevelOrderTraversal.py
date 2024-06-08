from collections import deque


class Solution:
    def levelOrder(self,root):
        level_order = []
        to_visit = deque()

        to_visit.append(root)

        while len(to_visit) > 0:
            node = to_visit.popleft()
            level_order.append(node.data)

            left_child = node.left

            if left_child is not None:
                to_visit.append(left_child)

            right_child = node.right

            if right_child is not None:
                to_visit.append(right_child)

        return level_order
