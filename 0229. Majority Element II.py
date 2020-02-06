# time O(n*k), space O(k)
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter()
        k = 3
        for num in nums:
            count[num] += 1
            if len(count) == k:
                count -= Counter(set(count))
        res = []
        for key in count:
            if nums.count(key) > len(nums)//k:
                res.append(key)
        return res


"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
