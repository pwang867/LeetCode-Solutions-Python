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
        
        
