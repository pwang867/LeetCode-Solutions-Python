# Analytics Phone Interview, 4/28/2020


'''
Input:
+---+---+---+---+
|   |   |   | x |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   | x | x |
+---+---+---+---+
|   |   | x | x |
+---+---+---+---+
|   |   |   | x |
+---+---+---+---+
|   | x |   |   |
+---+---+---+---+

visited = {}  # hashset

[[True/False]]
[4, 6, 10] = 20

for row:
    for col:
        if we see X:
            cnt += 1
            mark all X to ""

4-direction
boundary: all water

Output:
Perimeter of all islands

unittest
'''


class Island:
    def __init__(self):
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def count_islands(self, grid):  # time 2*m*n = O(m*n), stack memory O(m*n), stack object
        """
        input: grid: [[bool]],
        output:

        example:
        Island().count_islands(grid)
        """
        # grid: [[bool]], True means land, while False is water
        # [[True, True], [True, True]]
        self.cnt = 0  # count of fences
        for i in range(len(grid)):  # i = 0
            for j in range(len(grid[0])):  # j = 0
                if grid[i][j]:  # True
                    visited = set()
                    self.dfs(grid, i, j, visited)  # i=0, j=0
                    self.change_grid(grid, visited)

        return self.cnt  # cnt =1

    def change_grid(self, grid, visited):
        for i, j in visited:
            grid[i][j] = False

    def dfs(self, grid, i, j, visited):  # (1, 1)
        # mark all connected True to False starting from grid[i][j]
        # two conditions for calling dfs: grid[i][j] is True, and i, j are within boundary
        visited.add((i, j))
        for di, dj in self.dirs:
            r, c = i + di, j + dj  # (r, c) = (1, 1)
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):  # out of boundary fence
                self.cnt += 1
            elif not grid[r][c] and (r, c) not in visited:  # original water
                self.cnt += 1
            else:
                self.dfs(grid, r, c, visited)  # (r, c) = (1, 0)

