# time/space O(m*n)
# same method as spiral matrix I and II


class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        if R <= 0 or C <= 0:
            return []
        top, bottom, left, right = r0, r0, c0, c0
        res = []
        while top >= 0 or bottom < R or left >= 0 or right < C:
            if top >= 0:
                for j in range(left, right + 1):
                    if 0 <= j < C:
                        res.append((top, j))
            right += 1
            if right < C:
                for i in range(top, bottom + 1):
                    if 0 <= i < R:
                        res.append((i, right))
            bottom += 1
            if bottom < R:
                for j in range(right, left - 1, -1):
                    if 0 <= j < C:
                        res.append((bottom, j))
            left -= 1
            if left >= 0:
                for i in range(bottom, top - 1, -1):
                    if 0 <= i < R:
                        res.append((i, left))
            top -= 1  # don't forget
        return res


"""
On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid
is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid.

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid
(but may return to the grid boundary later.)

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.



Example 1:

Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]




Example 2:

Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],
        [4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]




Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C
"""