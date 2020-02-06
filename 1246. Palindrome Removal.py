# same as method 1
# dp, time O(n^3), space O(n^2)
# dp[i][j] means the minimum moves for arr[i:j+1]
class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        n = len(arr)
        dp = [[n+1]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1):
            dp[i][i+1] = 1 if arr[i] == arr[i+1] else 2
        for size in range(3, n+1):
            for i in range(n-size+1):
                j = i + size - 1
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i+1][j-1]
                dp[i][j] = min(dp[i][j], 1 + dp[i+1][j], 1 + dp[i][j-1])
                if dp[i][j] <= 2:
                    continue
                # process edge cases to make index in for loop easier
                if arr[i] == arr[i+1]:
                    dp[i][j] = min(dp[i][j], 1 + dp[i+2][j])
                for k in range(i+2, j+1):
                    if arr[i] == arr[k]:    # optimization
                        temp = dp[k+1][j] if k+1 <= j else 0
                        dp[i][j] = min(dp[i][j], dp[i+1][k-1] + temp)
        return dp[0][n-1]

# recursion with memo
# dp, time O(n^3), space O(n^2)
# dp[i][j] means the minimum moves for arr[i:j+1]
class Solution1(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        n = len(arr)
        self.dp = [[n+1]*n for _ in range(n)]
        self.helper(arr, 0, n-1)
        return self.dp[0][n-1]
    
    def helper(self, arr, left, right):
        if left == right:
            return 1
        if right < left:
            return 0
        if self.dp[left][right] != len(arr)+1:
            return self.dp[left][right]
        res = float('inf')
        if arr[left] == arr[right]:
            res = min(res, max(1, self.helper(arr, left+1, right-1)))
        for k in range(left, right):
            res = min(res, self.helper(arr, left, k) \
                           + self.helper(arr, k+1, right))
        self.dp[left][right] = res
        return res

from time import time
t1 = time()
arr = [5,13,12,4,11,7,9,2,18,8,3,19,14,8,13,17,9,18,13,14,5,10,6,13,1,20,2,14,15,6,19,13,9,2,8,20,3,4,1,11,2,9,5,17,6,4,3,17,9,13,14,19,17,20,6,14,12,13,2,13,9,17,3,17,20,9,16,18,1,3,16,7,16,13,4,14,2,4,20,11,4,10,10,6,1,4,19,11,15,1,7,8,8,5,8,4,15,8,6,1]

print(Solution().minimumMoves(arr))
print(time() - t1)

"""
Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] where i <= j, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.

 

Example 1:

Input: arr = [1,2]
Output: 2
Example 2:

Input: arr = [1,3,4,1,5]
Output: 3
Explanation: Remove [4] then remove [1,3,1] then remove [5].
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 20
"""
