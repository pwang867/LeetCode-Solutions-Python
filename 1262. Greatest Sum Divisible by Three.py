# method 1: dp. time O(n*3), this method is more general to extend to divisible by k
class Solution1(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [[0]*(len(nums)) for _ in range(3)]  # dp[i][j] is the max sum of nums[:j+1] which sum%3 == i
        dp[nums[0]%3][0] = nums[0]
        for j in range(1, len(nums)):
            # do not use nums[j]
            for i in range(3):
                dp[i][j] = dp[i][j-1]
            # only use nums[j]
            dp[nums[j]%3][j] = max(dp[nums[j]%3][j], nums[j])    # don't forget choosing nums[j] itself !!!!
            # use nums[j] and previous numbers
            for i in range(3):
                if dp[i][j-1] > 0:   # don't forget this requirement !!!
                    p = (i+nums[j])%3
                    dp[p][j] = max(dp[p][j], dp[i][j-1]+nums[j])
        return dp[0][-1]


# method 2: math, count number of mod 0, 1, 2, time/space O(n)
import heapq
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        total = sum(nums)
        if total%3 == 0:
            return total
        zeros = []
        ones = []
        twos = []
        for num in nums:
            if num%3 == 0:
                zeros.append(num)
            elif num%3 == 1:
                ones.append(num)
            else:
                twos.append(num)
        if total%3 == 1:
            res = -float('inf')
            if ones:
                res = max(res, total - min(ones))
            if twos and len(twos) > 1:
                heapq.heapify(twos)
                temp = heapq.heappop(twos)
                temp += heapq.heappop(twos)
                res = max(res, total-temp)
            return res
        if total%3 == 2:
            res = -float('inf')
            if twos:
                res = max(res, total-min(twos))
            if ones and len(ones) > 1:
                heapq.heapify(ones)
                temp = heapq.heappop(ones)
                temp += heapq.heappop(ones)
                res = max(res, total-temp)
            return res




"""
Given an array nums of integers, we need to find the maximum possible 
sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 
(maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
"""
