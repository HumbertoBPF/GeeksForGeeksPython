class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        topological_sort = []
        visited = set()

        for i in range(V):
            self.dfs(i, adj, visited, topological_sort)

        topological_sort.reverse()
        return topological_sort

    def dfs(self, vertex, adj, visited, topological_sort):
        if vertex in visited:
            return

        visited.add(vertex)
        neighbors = adj[vertex]

        for neighbor in neighbors:
            self.dfs(neighbor, adj, visited, topological_sort)
        # Topological sort needs to have a node before all their neighbors. Here we adding it after because we will
        # revert the list later
        topological_sort.append(vertex)
