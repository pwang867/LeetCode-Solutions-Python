# time/space O(n^2)

class Solution():
    def generateMatrix(self, n):
        if n == 0: return []
        if n == 1: return [[1]]
        
        res = [[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1

        while True:
            # top row
            for j in range(left, right+1):
                res[top][j] = num
                num += 1
            top += 1    
            if top > bottom:
                break
            
            # right column
            for i in range(top, bottom+1):
                res[i][right] = num
                num += 1
            right -= 1
            if right < left:
                break

            # bottom row
            for j in range(right, left-1, -1):
                res[bottom][j] = num
                num += 1
            bottom -= 1
            if bottom < top:
                break

            # left column
            for i in range(bottom, top-1, -1):
                res[i][left] = num
                num += 1
            left += 1
            if left > right:
                break

        return res


"""

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""
