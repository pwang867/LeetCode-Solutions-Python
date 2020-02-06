# method 2, standard BFS
from collections import deque
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        def dist(r1, c1, r2, c2):
            return abs(r1-r2) + abs(c1-c2)
        
        res = []
        queue = deque([(r0, c0, 0)])
        visited = {(r0, c0)}
        while queue:
            i, j, d = queue.popleft()
            res.append((i, j))
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                p, q = i + dx, j + dy
                if 0 <= p < R and 0 <= q < C and (p, q) not in visited:
                    cur_d = dist(p, q, r0, c0)
                    if cur_d > d:
                        visited.add((p, q))
                        queue.append((p, q, cur_d))
        return res


# method 1: time/space O(res)
class Solution1(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        def isValid(i, j):
            if i >= 0 and i < R and j >= 0 and j < C:
                return True
            else:
                return False
        
        def manDist(i, j):
            return abs(i-r0) + abs(j-c0)
        
        max_dist = max(manDist(0,0), manDist(0, C-1), manDist(R-1,0), manDist(R-1,C-1))
        
        ans = [[r0, c0]]
        for dist in range(1, max_dist+1):
            for r_dist in range(dist+1):
                c_dist = dist - r_dist
                if r_dist!=0 and c_dist!=0:
                    candidates = [[r0 - r_dist, c0 - c_dist], 
                              [r0 + r_dist, c0 - c_dist], 
                              [r0 - r_dist, c0 + c_dist], 
                              [r0 + r_dist, c0 + c_dist]]
                elif r_dist == 0:
                    candidates = [[r0, c0 - c_dist], [r0, c0 + c_dist]]
                else:
                    candidates = [[r0 - r_dist, c0], [r0  + r_dist, c0]]
                    
                for point in candidates:
                    if isValid(*point):
                        ans.append(point)
        
        return ans


# method 1, sort by distance, O(nlog(n))


"""
We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)

 

Example 1:

Input: R = 1, C = 2, r0 = 0, c0 = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (r0, c0) to other cells are: [0,1]
Example 2:

Input: R = 2, C = 2, r0 = 0, c0 = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
Example 3:

Input: R = 2, C = 3, r0 = 1, c0 = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
 

Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C
"""


R, C, r0, c0 = 1, 2, 0, 0
print Solution().allCellsDistOrder(R, C, r0, c0)