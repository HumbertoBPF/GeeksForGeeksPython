class Solution:

    def findPath(self, m, n):
        # Positions of the maze that have already been visited in this path
        positions_current_path = {}

        for i in range(n):
            for j in range(n):
                positions_current_path[(i, j)] = False

        return self.next_step(m, n, (0, 0), "", positions_current_path, "", [])

    def next_step(self, m, n, current_position, direction, positions_current_path, directions_current_path, paths):
        i = current_position[0]
        j = current_position[1]
        # If the position has still not been visited and if it is not blocked
        if not(positions_current_path[(i, j)]) and m[i][j] == 1:
            # Mark this position as visited
            positions_current_path[current_position] = True
            # Increment the string of directions with the current direction
            directions_current_path += direction
            # If the rat arrived to the end, add this path to the list of possible paths
            if (i == n - 1) and (j == n - 1):
                paths.append(directions_current_path)
            # Else, explore every possible direction, paying attention to the limits of the maze
            else:
                if i + 1 < n:
                    self.next_step(m, n, (i + 1, j), "D", positions_current_path, directions_current_path, paths)
                if j + 1 < n:
                    self.next_step(m, n, (i, j + 1), "R", positions_current_path, directions_current_path, paths)
                if i - 1 >= 0:
                    self.next_step(m, n, (i - 1, j), "U", positions_current_path, directions_current_path, paths)
                if j - 1 >= 0:
                    self.next_step(m, n, (i, j - 1), "L", positions_current_path, directions_current_path, paths)
            # When we have explored every possible direction, we come back to the previous position, so we mark the
            # current position as available
            positions_current_path[current_position] = False

        return paths


o1 = Solution()
print(o1.findPath([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]], 4))