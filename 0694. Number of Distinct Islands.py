# method 2: record the path as a string
# time/space O(mn)

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    s = []
                    self.dfs(grid, i, j, s)
                    islands.add("".join(s))
        return len(islands)

    def dfs(self, grid, i, j, path):
        grid[i][j] = 0
        for dx, dy, v in [(1, 0, 'd'), (-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l')]:
            p, q = i + dx, j + dy
            if 0 <= p < len(grid) and 0 <= q < len(grid[0]) and grid[p][q] == 1:
                path.append(v)
                self.dfs(grid, p, q, path)
        path.append('b')  # must add backtracking !!!


# method 1: record the index of the whole island
# and then offset the whole island by the topleft index


"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""