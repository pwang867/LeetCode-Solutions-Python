# time, space O(m*n)
# 1. use presum, dp[i][j] doesn't have to be exactly the max side length 
# of the valid square ending at mat[i][j], we only need to care about the max square 
# among all the squares

class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        if not mat or not mat[0]:
            return 0
        m, n = len(mat), len(mat[0])
        dp = [[0]*n for _ in range(m)]
        # presum
        for i in range(m):
            for j in range(n):
                if mat[i][j] <= threshold:
                    dp[i][j] = 1
                if i-1 >= 0:
                    mat[i][j] += mat[i-1][j]
                if j-1 >= 0:
                    mat[i][j] += mat[i][j-1]
                if i-1 >= 0 and j-1 >= 0:
                    mat[i][j] -= mat[i-1][j-1]
        # find squares
        res = 0
        for i in range(m):
            for j in range(n):
                if i-1 >= 0 and j-1 >= 0:
                    side = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    if side > 0:    
                        # we only need to check the area of the square side + 1
                        # don't have to check all length < side-1
                        side += 1
                        cur = mat[i][j]
                        if i - side >= 0:
                            cur -= mat[i-side][j]
                        if j - side >= 0:
                            cur -= mat[i][j-side]
                        if i - side >= 0 and j - side >= 0:
                            cur += mat[i-side][j-side]
                        if cur <= threshold:
                            dp[i][j] = side
                        else:
                            dp[i][j] = side - 1  
                res = max(res, dp[i][j])
        return res

mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]
threshold = 40184
print(Solution().maxSideLength(mat, threshold))


"""
Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
Example 3:

Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3
Example 4:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2
 

Constraints:

1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold <= 10^5
Accepted
"""


