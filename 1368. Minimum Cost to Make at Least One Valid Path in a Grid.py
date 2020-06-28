# Dijkstra, space O(m*n), time O(V+Elog(V))=O(m*n*log(m*n))

# follow-up: find all the min-cost paths: after finding the min_cost matrix,
# use find the non-decreasing paths searching backwards

import heapq
class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        heap = [(0, 0, 0)]
        m, n = len(grid), len(grid[0])
        min_cost = [[m + n - 1] * n for _ in range(m)]
        while heap:
            cost, i, j = heapq.heappop(heap)
            if i == m - 1 and j == n - 1:
                return cost
            for k, v in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
                dx, dy = v
                p, q = i + dx, j + dy
                penalty = int(grid[i][j] != k + 1)
                if 0 <= p < m and 0 <= q < n and cost + penalty < min_cost[p][q]:
                    min_cost[p][q] = cost + penalty
                    heapq.heappush(heap, (cost + penalty, p, q))
        return min_cost[-1][-1]


"""
Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.



Example 1:


Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.
Example 2:


Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).
Example 3:


Input: grid = [[1,2],[4,3]]
Output: 1
Example 4:

Input: grid = [[2,2,2],[2,2,2]]
Output: 3
Example 5:

Input: grid = [[4]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
"""