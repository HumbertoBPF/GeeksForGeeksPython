# User function Template for python3

class Solution:
    def isTree(self, n, m, edges):
        adj = self.get_adjacency_list(n, edges)
        visited = set()
        is_cyclic = self.has_cycle(0, None, adj, visited, set())
        # A graph is connected when we can reach every vertex from a given vertex
        is_connected = len(visited) == n

        if not is_cyclic and is_connected:
            return 1

        return 0

    def get_adjacency_list(self, n, edges):
        adj = [set() for _ in range(n)]

        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]

            adj[v1].add(v2)
            adj[v2].add(v1)

        return adj

    def has_cycle(self, vertex, last_vertex, adj, visited, path):
        # If it's the second time that we are seeing a vertex in the current path, we found a cycle
        if vertex in path:
            return True
        # If the vertex is not in the path, but we have already visited it, then we didn't find a cycle so far
        if vertex in visited:
            return False

        visited.add(vertex)
        neighbors = adj[vertex]

        path.add(vertex)
        for neighbor in neighbors:
            # This condition avoids coming back to the previous vertex of the current DFS path
            if neighbor != last_vertex:
                if self.has_cycle(neighbor, vertex, adj, visited, path):
                    return True
        path.remove(vertex)

        return False