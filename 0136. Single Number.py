
# method 1: 0^x = x, x^x = 0
class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        res = 0
        for num in nums:
            res ^= num
        return res

# method 2, quick selection (divide and conquer), O(n) on average, worst case O(n^2)
import random
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, p, q):
        if p > q:
            return None
        if p == q:
            return nums[p]
        
        i = random.randint(p, q)
        nums[p], nums[i] = nums[i], nums[p]
        left, cur = p+1, p+1
        pivot = nums[p]
        while cur <= q:
            if nums[cur] == pivot:  # at most happens once
                nums[p+1], nums[cur] = nums[cur], nums[p+1]   # p and p+1 are used to save the pivot, pivot at most appears twice
                if left == p+1:
                    left += 1
            if nums[cur] < pivot:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
            cur += 1
        
        if nums[p+1] != nums[p]:  # when pivot itself is the single number
            return nums[p]
        
        small = left - (p+2)
        if small%2 == 1:
            return self.helper(nums, p+2, left-1)
        else:
            return self.helper(nums, left, q)
        



"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
print("solution ", Solution().singleNumber(nums))

