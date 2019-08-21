

# Solution 2, time O(n), space O(1) and do not modify original nums
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        curr = 0

        for i in nums:
            pre, curr = curr, max(curr, pre + i)
        return curr

# method 2: time O(n), space: modified original data O(n)
class Solution1(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        nums[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i]+nums[i-2], nums[i-1])
        
        return nums[-1]
