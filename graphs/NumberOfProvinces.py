class Solution:
    def numProvinces(self, adj, V):
        number_provinces = 0
        visited = set()

        for i in range(V):
            # Visit all the vertices in the province, and never return to any of them again
            if i not in visited:
                number_provinces += 1
                self.dfs(i, adj, visited)

        return number_provinces

    def dfs(self, vertex, adj, visited):
        if vertex in visited:
            return
        # Marking the vertex as visited
        visited.add(vertex)
        # Getting the row with the information concerning the neighbors of the vertex
        row = adj[vertex]
        n = len(row)

        for i in range(n):
            # We only visit neighbor vertices
            if row[i] == 1:
                self.dfs(i, adj, visited)
