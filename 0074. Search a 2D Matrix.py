# binary search, O(log(m*n))
# we can use binary search to search row first, and then col
# but can also use smart index to do binary search only once
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        
        left, right = 0, m*n-1
        while left + 1 < right:
            
            mid = left + (right - left)//2
            t = matrix[mid//n][mid%n]
            if t == target:
                return True
            elif t > target:
                right = mid
            else:
                left = mid
        
        return matrix[left//n][left%n] == target or \
                matrix[right//n][right%n] == target
    

"""
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
"""
