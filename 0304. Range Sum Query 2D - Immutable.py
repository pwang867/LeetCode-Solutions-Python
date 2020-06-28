class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sums = matrix + []

        if matrix and matrix[0]:
            m, n = len(matrix), len(matrix[0])
            for i in range(m):
                for j in range(n):
                    self.sums[i][j] += self.getSum(i - 1, j) + self.getSum(i, j - 1) \
                                       - self.getSum(i - 1, j - 1)

    def getSum(self, i, j):  # to make self.sums initialization and range sum query easy
        if not self.sums or not self.sums[0]:
            return 0
        if i < 0 or i >= len(self.sums) or j < 0 or j >= len(self.sums[0]):
            return 0
        return self.sums[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.getSum(row2, col2) + self.getSum(row1 - 1, col1 - 1) \
               - self.getSum(row1 - 1, col2) - self.getSum(row2, col1 - 1)


# time O(m*n) for pre-processing, space O(m*n)


class NumMatrix1(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.pre_sums = self.cal_pre_sums(matrix)

    def cal_pre_sums(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        pre_sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_sums[i][j] = matrix[i - 1][j - 1] + pre_sums[i - 1][j] \
                                 + pre_sums[i][j - 1] - pre_sums[i - 1][j - 1]
        return pre_sums

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.pre_sums[row2 + 1][col2 + 1] + self.pre_sums[row1][col1] \
               - self.pre_sums[row1][col2 + 1] - self.pre_sums[row2 + 1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by 
its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and 
(row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 <= row2 and col1 <= col2.
"""
