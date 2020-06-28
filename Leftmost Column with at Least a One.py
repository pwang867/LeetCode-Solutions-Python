# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

# similar to sorted matrix
# two methods: 1. binary search O(n*log(m)), 2. two pointer O(m+n)


class Solution2(object):    # optimal
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        n, m = binaryMatrix.dimensions()
        i, j = 0, m - 1
        while i < n and j >= 0:
            val = binaryMatrix.get(i, j)
            if val == 0:
                i += 1
            else:
                j -= 1
        j += 1
        if j == m:
            return -1
        return j


# binary search

class Solution1(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m, n = binaryMatrix.dimensions()
        left, right = 0, n - 1

        def has_one_in_col(col):
            for i in range(m):
                if binaryMatrix.get(i, col) == 1:
                    return True
            return False

        while left + 1 < right:
            mid = left + (right - left) // 2
            if has_one_in_col(mid):
                right = mid
            else:
                left = mid
        if has_one_in_col(left):
            return left
        elif has_one_in_col(right):
            return right
        else:
            return -1


"""

(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix,
this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with
at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples.
You will not have access the binary matrix directly.


Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1


Constraints:

1 <= mat.length, mat[i].length <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
   Hide Hint #1
1. (Binary Search) For each row do a binary search to find the leftmost one on that row and update the answer.
   Hide Hint #2
2. (Optimal Approach) Imagine there is a pointer p(x, y) starting from top right corner.
p can only move left or down. If the value at p is 0, move down. If the value at p is 1, move left.
Try to figure out the correctness and time complexity of this algorithm.
"""