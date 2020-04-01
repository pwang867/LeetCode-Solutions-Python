# when creating subsets, we are following this order to avoid duplicate subset division:
# 1. the numbers in each subset should be decreasing
# 2. the first number for each subset should be decreasing
# time O( N! / ((N/K)!)^K / K!)


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return True
        total = sum(nums)
        if total%k != 0:
            return False
        target = total//k
        nums.sort(reverse=True)
        return self.dfs(nums[1:], nums[0], nums[0], target, k)
    
    def dfs(self, nums, last, cur_sum, target, k):
        if k == 1:
            return True
        if cur_sum == target:  # start a new group
            return self.dfs(nums[1:], nums[0], nums[0], target, k-1)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > last or cur_sum + nums[i] > target:
                break
            if self.dfs(nums[:i]+nums[i+1:], nums[i], cur_sum+nums[i], target, k):
                return True
        return False


'''
698. Partition to K Equal Sum Subsets
Medium

1346

79

Add to List

Share
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''
