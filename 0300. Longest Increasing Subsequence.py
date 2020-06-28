

# method 2: dp, time < O(log(n!))=O(n*log(n)), 
# also time < O(n*log(k)), k=length of longest subsequence
# space=O(n)
# dp[i] means the smallest ending element for a LIS with length i+1
# this method will have trouble returning the sequence


import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  
        for num in nums:
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                i = bisect.bisect_left(dp, num)
                dp[i] = num
        return len(dp)


# method 1: dp, time/space O(n^2), but is able to return the longest sequence
# dp[i] means the length of LIS ending with nums[i]


class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp) if dp else 0
    

# follow up: return the longest subsequence, not only the max length
# method 1: dp, time/space O(n^2), but is able to return the longest sequence
# dp[i] means the length of LIS ending with nums[i]
class Solution0(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # list of list, each list is the longest subsequence at each index i
        sequences = []
        for i, num in enumerate(nums):
            temp_sequence = self.MaxSequence(sequences, num)
            sequences.append(temp_sequence + [num])
        
        res = 0
        for seq in sequences:
            res = max(res, len(seq))
        return res
    
    def MaxSequence(self, sequences, num):
        # find the longest sequence before num whose end is smaller than num
        res = []
        for i in range(len(sequences)-1, -1, -1):
            seq = sequences[i]
            if i+1 < len(res):  # early termination
                break 
            if seq[-1] >= num:
                continue
            if len(seq) > len(res):
                res = seq
        return res



"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


