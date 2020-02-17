# time O(m+n)
# same as #240. Search a 2D Matrix II
# starting from a corner and skip a whole row or a column in one step
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        i, j = 0, n-1
        cnt = 0
        while 0 <= i < m and 0<= j < n:
            if grid[i][j] < 0:
                cnt += m-i
                j -= 1
            else:
                i += 1
        return cnt
    

"""
Given a m * n matrix grid which is sorted in 
non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""
