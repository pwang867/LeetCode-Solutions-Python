# similar to N-queen, space O(N), for each query, O(1)
# Hashmap, i+j for diagonal, and i-j for off-diagonal


class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        d = [{} for _ in range(4)]
        lamps = set(map(tuple, lamps))
        for x, y in lamps:
            d[0][x] = d[0].get(x, 0) + 1  # row
            d[1][y] = d[1].get(y, 0) + 1  # col
            d[2][x + y] = d[2].get(x + y, 0) + 1  # diagonal
            d[3][x - y] = d[3].get(x - y, 0) + 1  # off diagonal
        res = []
        for query in queries:
            # check illumination
            x, y = query
            if x in d[0] or y in d[1] or x + y in d[2] or x - y in d[3]:
                res.append(1)
            else:
                res.append(0)
            # remove lamps
            for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1),  # don't forget (0, 0)
                           (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                p, q = x + dx, y + dy
                if (p, q) in lamps:
                    lamps.remove((p, q))
                    d[0][p] -= 1
                    if d[0][p] == 0:
                        del d[0][p]
                    d[1][q] -= 1
                    if d[1][q] == 0:
                        del d[1][q]
                    d[2][p + q] -= 1
                    if d[2][p + q] == 0:
                        del d[2][p + q]
                    d[3][p - q] -= 1
                    if d[3][p - q] == 0:
                        del d[3][p - q]
        return res


"""
On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.  Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y) or are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)

Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].

 

Example 1:

Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: 
Before performing the first query we have both lamps [0,0] and [4,4] on.
The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
1 1 1 1 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1
Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
1 0 0 0 1
0 1 0 0 1
0 0 1 0 1
0 0 0 1 1
1 1 1 1 1
Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.
 

Note:

1 <= N <= 10^9
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
lamps[i].length == queries[i].length == 2
"""