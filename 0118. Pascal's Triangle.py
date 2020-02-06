# dynamic programming, space O(n), time O(n^2)
# bottom up
# https://leetcode.com/problems/pascals-triangle/


# time/space O(res)=O(n^2)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        elif numRows == 1:
            return [[1]]
        
        res = [[1]]
        for i in range(1, numRows):
            vals = [1]
            for j in range(i-1):  # not range(i)
                vals.append(res[-1][j] + res[-1][j+1])
            vals.append(1)
            res.append(vals)
        
        return res
    
  
"""  
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
