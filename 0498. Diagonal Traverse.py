# time O(m*n)
# simple linear scan


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        for step in range(m+n-1):
            if step%2 == 0:
                start, end, gap = min(step, m-1), max(step-n+1, 0), -1   # from: 0 <= i <= m-1, 0 <= j = step - i <= n-1
            else:
                start, end, gap = max(step-n+1, 0), min(step, m-1), 1
            for i in range(start, end + gap, gap):
                j = step - i
                res.append(matrix[i][j])
        return res


"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal 
order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""
