# time O((m+n)*klog(k)), space O(k), where k = min(m, n)
# simple sort, be careful about index
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        for step in range(-(m-1), n):
            # get diagonal and sort it
            vals = []
            for i in range(max(-step, 0), min(m-1, n-1-step)+1):   # 0 <= i < m, 0 <= j < n
                j = i + step
                vals.append(mat[i][j])
            vals.sort()
            k = 0
            # assign back to mat
            for i in range(max(-step, 0), min(m-1, n-1-step)+1):
                j = i + step
                mat[i][j] = vals[k]
                k += 1
        return mat


"""
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
Accepted
"""
