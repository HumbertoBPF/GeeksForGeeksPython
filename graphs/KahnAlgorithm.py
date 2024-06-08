from collections import deque


class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        queue = deque()
        # The in degree represents the number of incoming edges of a vertex
        in_degree = [0]*V

        for i in range(V):
            for j in adj[i]:
                # Taking into account that i -> j is an incoming edge of the vertex "j"
                in_degree[j] += 1
        # We start from the vertices that don't have incoming edges (they come first in the topological sort)
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)

        topological_sort = []

        while len(queue) > 0:
            vertex = queue.popleft()

            topological_sort.append(vertex)

            neighbors = adj[vertex]

            for neighbor in neighbors:
                # We decrement the in degree of the neighbor (it represents removing the current vertex from the graph)
                in_degree[neighbor] -= 1
                # If the neighbor vertex doesn't have an incoming vertex, it will be visited next
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return topological_sort
