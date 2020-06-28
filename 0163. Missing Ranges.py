# https://leetcode.com/problems/missing-ranges/discuss/50631/Ten-line-python-solution
# easy to make small mistakes
# be very careful about the two edges: lower, upper


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        pre = lower-1  # mistake: pre = lower
        res = []
        for i in range(len(nums)):
            num = nums[i]
            if num > upper:  # I'm allowing that nums[i] > upper
                break
            if num - pre == 2:
                res.append(str(pre+1))
            elif num - pre > 2:
                res.append(str(pre+1) + "->" + str(num-1))
            pre = num
            
        if upper - pre == 1:  # mistake: upper - pre == 2
            res.append(str(upper))
        elif upper - pre > 1:
            res.append(str(pre+1) + "->" + str(upper))
        
        return res


"""
Given a sorted integer array nums, where the range of elements are 
in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""
