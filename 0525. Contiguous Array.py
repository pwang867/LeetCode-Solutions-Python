# based on pre_sum, but need to use (index - 2*pre_sum) as the key
# O(N) time/space

# 2*(pre_sum2 - pre_sum1) = j - i => (j - 2*pre_sum2) == (i - 2*pre_sum1),
# # so (index - 2*pre_sum) will be the key

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        d = {-1: -1}  # (index - 2*pre_sum): index, mistake: d = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            key = i - 2 * total
            if key in d:
                max_len = max(max_len, i - d[key])
            else:
                d[key] = i
        return max_len


"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""