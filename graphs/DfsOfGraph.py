class Solution:
    def dfsOfGraph(self, V, adj):
        traversed_nodes = []
        self.dfs(0, adj, set(), traversed_nodes)
        return traversed_nodes

    def dfs(self, current_node, adj, visited_nodes, traversed_nodes):
        if current_node in visited_nodes:
            return
        # Add current node to the list of visited nodes since we don't want to visit it again
        visited_nodes.add(current_node)
        traversed_nodes.append(current_node)

        neighbors =  adj[current_node]

        for neighbor in neighbors:
            self.dfs(neighbor, adj, visited_nodes, traversed_nodes)