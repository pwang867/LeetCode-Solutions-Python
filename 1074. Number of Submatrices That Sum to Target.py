# time O(m^2*n), space O(n)
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        cnt = 0
        for i in range(m):  # top edge of submatrices
            row = [0] * n
            for j in range(i, m):  # bottom edge
                for k in range(n):
                    row[k] += matrix[j][k]
                cnt += self.count_1D(row, target)
        return cnt

    def count_1D(self, nums, target):
        # find the number of continuous subarray that sum to target
        res = 0
        pre_sums = {0: 1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            res += pre_sums.get(total - target, 0)
            pre_sums[total] = pre_sums.get(total, 0) + 1
        return res


"""
Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.



Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.


Note:

1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""