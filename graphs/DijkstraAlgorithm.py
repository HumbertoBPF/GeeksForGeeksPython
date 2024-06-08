import sys
import heapq

class Solution:
    def get_minimum_distance(self, distances, visited):
        """
        Util function to get the vertex that has not been visited yet and that has the minimum distance.
        :param distances: dictionary with the distances of each vertex (vertices as keys, distances as values)
        :param visited: set with the visited vertices
        :return: a tuple with the non-visited vertex and the associated minimum distance
        """
        n = len(distances)
        min_vertex = (None, sys.maxsize)

        for vertex in range(n):
            if vertex not in visited:
                distance = distances[vertex]
                _, min_distance = min_vertex
                if min_distance >= distance:
                    min_vertex = (vertex, distance)

        return min_vertex

    def get_initial_distances(self, V, S):
        """
        :param V: number of vertices
        :param S: source vertex
        :return: list such that the ith item is the minimum distance so far to the vertex i
        """
        distances = []

        for i in range(V):
            if i == S:
                distances.append(0)
                continue
            distances.append(sys.maxsize)

        return distances

    #Function to find the shortest distance of all the vertices from the source vertex S.
    def dijkstra(self, V, adj, S):
        distances = self.get_initial_distances(V, S)
        visited = set()

        while len(visited) < V:
            current_vertex, _ = self.get_minimum_distance(distances, visited)
            neighbors = adj[current_vertex]
            visited.add(current_vertex)

            for neighbor in neighbors:
                neighbor_vertex, edge_weight = neighbor

                if neighbor_vertex not in visited:
                    # Compute the distance to the neighbor obtained at this iteration
                    distance = distances[current_vertex] + edge_weight
                    # If we have found a better candidate of shortest path, update the distances dictionary
                    if distance < distances[neighbor_vertex]:
                        distances[neighbor_vertex] = distance

        return distances

    def get_initial_distance_heap(self, V, S):
        """
        :param V: number of vertices
        :param S: source vertex
        :return: distance heap (the distance is the priority value and the vertex is specified in the second position)
        """
        distances_heap = [[sys.maxsize, i] for i in range(V)]
        distances_heap[S] = [0, S]
        heapq.heapify(distances_heap)
        return distances_heap

    # Function to find the shortest distance of all the vertices from the source vertex S.
    def dijkstra_with_heap(self, V, adj, S):
        distances = self.get_initial_distances(V, S)
        # We are going to use a heap to get the minimum distance
        distances_heap = self.get_initial_distance_heap(V, S)

        visited = set()

        while len(visited) < V:
            _, current_vertex = heapq.heappop(distances_heap)
            neighbors = adj[current_vertex]
            visited.add(current_vertex)

            for neighbor in neighbors:
                neighbor_vertex, edge_weight = neighbor

                if neighbor_vertex not in visited:
                    # Compute the distance to the neighbor obtained at this iteration
                    distance = distances[current_vertex] + edge_weight
                    # If we have found a better candidate of shortest path, update the distances dictionary
                    if distance < distances[neighbor_vertex]:
                        distances[neighbor_vertex] = distance
                        # Since we don't know the position in the heap of the distance to update, we push it as a new item
                        heapq.heappush(distances_heap, [distance, neighbor_vertex])

        return distances

solution = Solution()
V = 4
S = 0
adj = [
    [[1, 9], [2, 1], [3, 1]],
    [[0, 9], [3, 3]],
    [[0, 1], [3, 2]],
    [[0, 1], [1, 3], [2, 2]]
]
print(solution.dijkstra_with_heap(V, adj, S))
