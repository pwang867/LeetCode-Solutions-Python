# Boyer–Moore majority vote algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        count = 1
        ans = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != ans:
                if count == 0:
                    ans = nums[i]
                    count = 1
                else:
                    count -= 1
            else:
                count += 1
        
        return ans


"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
