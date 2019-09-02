# time O(n), space O(n)
# travel from left and right to calculate the product of nums[:i]
# excluding nums[i], saved into left[], and then right to left 
# to calcualte the produce of nums[i+1:], saved into right[]
# then the answer will be left[i]*right[i]

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [0]*n  # left[i] means the product of nums[:i], excluding nums[i]
        right = [0]*n
        left[0] = 1
        right[n-1] = 1
        for i in range(1, n):
            left[i] = left[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        
        res=[]
        for i in range(n):
            res.append(left[i]*right[i])
        
        return res
        
