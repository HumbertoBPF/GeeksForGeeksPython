from typing import List


class Solution:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        adjacency_list = []
        # Time: O(V), space: O(V) to initialize the adjacency list
        for i in range(V):
            # Use a set to avoid duplicating neighbors nodes
            adjacency_list.append(set())
        # Time: O(E), space: O(E) to populate it with the edges
        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]

            adjacency_list[v1].add(v2)
            adjacency_list[v2].add(v1)

        return [list(item) for item in adjacency_list]

solution = Solution()
V = 5
edges = [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
print(solution.printGraph(V, edges))
