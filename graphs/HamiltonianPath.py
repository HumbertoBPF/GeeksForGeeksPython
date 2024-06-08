class Solution:
    def check(self, N, M, Edges):
        adj = self.get_adjacency_list(N, Edges)

        for i in range(N):
            if self.has_hamiltonian_path(i, adj, set()):
                return True

        return False


    def has_hamiltonian_path(self, src, adj, path):
        path.add(src)

        if len(path) == len(adj):
            return True

        neighbors = adj[src]

        for neighbor in neighbors:
            # This condition avoids infinite loops (we don't want to revisit repeated vertices when exploring a path)
            if neighbor not in path:

                if self.has_hamiltonian_path(neighbor, adj, path):
                    return True

        path.remove(src)
        return False


    def get_adjacency_list(self, n, edges):
        adj = [set() for _ in range(n)]

        for edge in edges:
            v1, v2 = edge
            # We need to decrement the vertices by one to make them 0-indexed
            adj[v1 - 1].add(v2 - 1)
            adj[v2 - 1].add(v1 - 1)

        return adj