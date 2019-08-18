# nethod 2: dp, n*log(n)
# dp[i] means the smallest ending element for a LIS with length i+1
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
    

# method 1: dp, n^2
# dp[i] means the length of LIS ending with nums[i]
class Solution1(object):
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
        # find the longest sequence whose end is smaller than num
        res = []
        for seq in sequences:
            if seq[-1] >= num:
                continue
            if len(seq) > len(res):
                res = seq
        return res
    
