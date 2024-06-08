import sys


class Solution:
    def bellman_ford(self, V, edges, S):
        """
        :param V: nodes in graph
        :param edges: list of the graph edges
        :param S: source node
        :return: list with the minimum distances from S to the node at position i. It returns an array filled with -1 if
        the graph has a negative cycle (case where the problem doesn't have a solution)
        """
        distances = self.get_initial_distances(V, S)
        # The Bellman-Ford algorithm consists into checking for relaxations V - 1 times
        for _ in range(V - 1):
            self.iteration_bellman_ford(distances, edges)

        if self.has_negative_cycle(distances, edges):
            return [-1]
        # Checking if there are disconnected nodes
        for i in range(V):
            if distances[i] == sys.maxsize:
                distances[i] = 100000000

        return distances

    def iteration_bellman_ford(self, distances, edges):
        """
        Performs an iteration of the Bellman-Ford algorithm.
        :param distances: list with the distances from the S to the ith vertex
        :param edges: list of the graph edges
        """
        for edge in edges:
            v1, v2, weight = edge
            distance_v1 = distances[v1]

            if distance_v1 != sys.maxsize:
                distance = distance_v1 + weight
                if distances[v2] > distance:
                    distances[v2] = distance

    def has_negative_cycle(self, distances, edges):
        """
        Function to run after the V-1 iterations of Bellman-Ford algorithm to detect negative cycles
        :param distances: list with the distances from S to the ith vertex
        :param edges: list of the graph edges
        :return: a boolean indicating if the graph has a negative cycle
        """
        for edge in edges:
            v1, v2, weight = edge
            distance_v1 = distances[v1]

            if distance_v1 != sys.maxsize:
                distance = distance_v1 + weight
                # A decrement in some distance implies the existence of a negative cycle
                if distances[v2] > distance:
                    return True

        return False

    def get_initial_distances(self, V, S):
        """
        :param V: number of vertices
        :param S: source vertex
        :return: list with the initial distances from the source vertex to the vertex at ith position
        """
        distances = [sys.maxsize for _ in range(V)]
        distances[S] = 0
        return distances