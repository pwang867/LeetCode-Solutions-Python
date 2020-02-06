# time O(m*n), space O(n)
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        rowhits = 0
        colhits = [0]*len(grid[0])
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == 0 or grid[i][j-1] == "W":    # for row
                    rowhits = 0   # don't forget to reset
                    k = j
                    while k < len(grid[0]) and grid[i][k] != "W":   # stretch out to see the max enemy to kill in row
                        if grid[i][k] == "E":
                            rowhits += 1
                        k += 1
                if i == 0 or grid[i-1][j] == "W":   # for col
                    colhits[j] = 0
                    k = i
                    while k < len(grid) and grid[k][j] != "W":
                        if grid[k][j] == "E":
                            colhits[j] += 1
                        k += 1
                if grid[i][j] == "0":   # You can only put the bomb at an empty cell
                    res = max(res, rowhits + colhits[j])
        return res



"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
"""


