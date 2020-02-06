# method 2: plot nums vs index, then this problem is actually 
# just counting the nums of peaks (local max and min), O(n)
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        cnt = 1
        direction = 0  # -1: going down, 1: going up
        for i in range(1, len(nums)):
            if direction != 1 and nums[i] > nums[i-1]:
                cnt += 1
                direction = 1
            if direction != -1 and nums[i] < nums[i-1]:
                cnt += 1
                direction = -1
        
        return cnt


# method 1: O(n^2)
class Solution1(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp1 = [1]*n  # dp1[i] is the length of the subsequence with positive end
        dp2 = [1]*n  # with negative end
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] < nums[j]:
                    dp2[i] = max(dp2[i], dp1[j] + 1)
                elif nums[i] > nums[j]:
                    dp1[i] = max(dp1[i], dp2[j] + 1)
        
        return max(dp1[-1], dp2[-1])
        

    
"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""
