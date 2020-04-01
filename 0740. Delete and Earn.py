# same as house robber, time O(n)

import collections
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        cnts = collections.Counter(nums)
        arr = sorted(cnts.keys())
        rob, norob = arr[0]*cnts[arr[0]], 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1] + 1:
                norob, rob = max(rob, norob), norob + arr[i]*cnts[arr[i]]
            else:
                norob, rob = max(rob, norob), max(rob, norob)+arr[i]*cnts[arr[i]]
        return max(norob, rob)
    


# time limit exceeded, O(N^3)

import collections
class Solution1(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnts = collections.Counter(nums)
        arr = sorted(cnts.keys())
        dp = [[-1]*len(arr) for _ in range(len(arr))]
        return self.max_points(arr, 0, len(arr)-1, cnts, dp)
    
    def max_points(self, arr, left, right, cnts, dp):
        if left > right:
            return 0
        if left == right:
            return arr[left]*cnts[arr[left]]
        if dp[left][right] != -1:
            return dp[left][right]
        max_point = 0
        for i in range(left, right+1):
            cur = arr[i]*cnts[arr[i]]
            p, q = i-1, i+1
            if p >= 0 and arr[p] + 1 == arr[i]:
                p = i-2
            if q < len(arr) and arr[i] + 1 == arr[q]:
                q = i + 2
            cur += self.max_points(arr, left, p, cnts, dp) \
                    + self.max_points(arr, q, right, cnts, dp)
            max_point = max(cur, max_point)
        dp[left][right] = max_point
        return max_point



"""
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. 
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
 

Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
 

Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
"""
