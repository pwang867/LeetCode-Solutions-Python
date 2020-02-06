class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        left = 0
        ranges = []
        for right in range(1, len(nums)):
            if nums[right] > nums[right-1] + 1:
                self.addRange(ranges, nums[left], nums[right-1])
                left = right
        self.addRange(ranges, nums[left], nums[-1])  # easy to forget
        return ranges
    
    def addRange(self, ranges, left, right):
        if left == right:
            ranges.append(str(left))
        elif left < right:
            ranges.append(str(left) + "->" + str(right))
        
        
"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
