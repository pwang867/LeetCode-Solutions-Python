"""
easy to miss those edge cases:

[[0]]: return 0

[[1]]: return -1

[[2]]: return 0

[[2, 1, 1], [0, 0, 0], [1, 1, 1]]: return -1


# time/space O(m*n)
# edge case: grid is initially all rotten or all good
"""


import collections

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:   # return -1 or 0 ? discuss with interviewer
            return 0
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
        day = -1     # wrong initilization: day = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = i + dx, j + dy
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == 1:
                        grid[p][q] = 2
                        queue.append((p, q))
            day += 1
        for i in range(m):       # easy to forget double check. Edge case: [[2, 1, 1], [0, 0, 0], [1, 1, 1]]
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return max(day, 0)    # easy to miss max(), when the grid is all 0


"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""
