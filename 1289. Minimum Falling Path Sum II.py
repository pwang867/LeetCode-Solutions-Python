import heapq
class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        if not arr or not arr[0]:
            return 0
        m, n = len(arr), len(arr[0])
        dp = [[float('inf')]*n for _ in range(m)]
        dp[0] = arr[0][:]
        smallest, second= heapq.nsmallest(2, dp[0])
        for i in range(1, m):
            for j in range(n):
                if dp[i-1][j] != smallest:
                    dp[i][j] = smallest + arr[i][j]
                else:
                    dp[i][j] = second + arr[i][j]
            smallest, second = heapq.nsmallest(2, dp[i])
        return smallest


"""
Given a square grid of integers arr, a falling path with non-zero shifts is a choice of exactly one element from each row of arr, such that no two elements chosen in adjacent rows are in the same column.

Return the minimum sum of a falling path with non-zero shifts.

 

Example 1:

Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
 

Constraints:

1 <= arr.length == arr[i].length <= 200
-99 <= arr[i][j] <= 99
"""
