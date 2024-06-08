from typing import List
from collections import deque


class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # Queue with the items that still need to be visited
        nodes_to_visit = deque()
        scheduled_nodes = set()
        traversal_list = []

        nodes_to_visit.append(0)
        scheduled_nodes.add(0)

        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.popleft()

            traversal_list.append(current_node)

            neighbors = adj[current_node]
            # Adding non-visited neighbors
            for neighbor in neighbors:
                if neighbor not in scheduled_nodes:
                    # Mark the neighbor as scheduled to avoid "scheduling a visit" again
                    scheduled_nodes.add(neighbor)
                    nodes_to_visit.append(neighbor)

        return traversal_list


solution = Solution()
V = 13
adj = [
    [0, 1],
    [0, 2],
    [0, 4],
    [0, 8],
    [1, 5],
    [1, 6],
    [1, 9],
    [2, 4],
    [3, 7],
    [3, 8],
    [5, 8],
    [6, 7],
    [6, 9]
]
print(solution.bfsOfGraph(V, adj))
