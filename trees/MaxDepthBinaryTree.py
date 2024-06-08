class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def maxDepth(self,root):
        memory = {"max_depth": 1}
        self.dfs(root, 1, memory)
        return memory["max_depth"]

    def dfs(self, current_node, depth, memory):
        if current_node is None:
            return

        memory["max_depth"] = max(memory["max_depth"], depth)

        self.dfs(current_node.right, depth + 1, memory)
        self.dfs(current_node.left, depth + 1, memory)
