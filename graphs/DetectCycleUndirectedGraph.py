from typing import List

class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = set()
        # Since the graph is not connected, we have to try to find a cycle from every vertex. We avoid unnecessary
        # repetitions by skipping already visited nodes
        for i in range(V):
            if i not in visited:
                if self.has_cycle(i, None, adj, visited, set()):
                    return True

        return False


    def has_cycle(self, current_node, last_node, adj, visited, path):
        # If the current node is in the DFS path, we found a cycle
        if current_node in path:
            return True
        # If we are visiting again a node that isn't in the current path, we should return here
        if current_node in visited:
            return False

        visited.add(current_node)
        neighbors = adj[current_node]

        path.add(current_node)
        for neighbor in neighbors:
            # This condition avoids returning to the previous node since the graph is undirected
            if neighbor != last_node:
                if self.has_cycle(neighbor, current_node, adj, visited, path):
                    return True
        path.remove(current_node)

        return False
