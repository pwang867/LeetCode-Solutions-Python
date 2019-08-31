# method 3: divide and conquer, time O(n*long(n))
# compare left part, right part, and middle part
# for middle max, we need to search in two directions
class Solution(object):
    def maxSubArray(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums)-1)
    
    def maxSubArrayHelper(self, nums, left, right):
        if left > right:
            return -float('inf')  # wrong: return 0
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        left_max = self.maxSubArrayHelper(nums, left, mid-1)
        right_max = self.maxSubArrayHelper(nums, mid+1, right)
        
        mid_max = nums[mid]
        temp = mid_max
        for i in range(mid-1, left-1, -1):
            temp += nums[i]
            mid_max = max(mid_max, temp)
        temp = mid_max
        for i in range(mid+1, right+1):
            temp += nums[i]
            mid_max = max(mid_max, temp)
        
        return max([left_max, right_max, mid_max])
        


# method 2: simplified from method 1
class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxSum = nums[0]
        curSum = 0
        
        for num in nums:
            curSum = max(curSum+num, num)
            maxSum = max(maxSum, curSum)
        
        return maxSum
    


# method 1: O(n), sliding window
class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxSum = nums[0]
        curSum = 0
        
        for num in nums:
            curSum += num
            maxSum = max(maxSum, curSum)
            if curSum < 0:  # reset to start accumulate from next num
                curSum = 0
        
        return maxSum
    
