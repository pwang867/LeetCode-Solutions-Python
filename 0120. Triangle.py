# use dynamic programming, bottom up
# space O(n) if original data can't be overwritten
# time O(n^2), where n is the length of row

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return []
        
        dp = triangle[-1]
        
        for row in range(len(triangle)-2, -1, -1):  # bottom up
            for i, num in enumerate(triangle[row]):
                dp[i] = num + min(dp[i], dp[i+1])
        
        return dp[0]
    
"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
