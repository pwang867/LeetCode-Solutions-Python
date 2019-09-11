# method 2: O(n*log(n))
# build a sums array, and use binary search to search sums[j]
# so that sums[j] - sums[i] >= s
class Solution(object):
    def minSubArrayLen(self, s, nums):
        sums = [0]
        total = 0
        res = float('inf')
        left = 0
        for i, num in enumerate(nums):
            total += num
            sums.append(total)
            if total >= s:
                left = self.binarySearch(sums, left, total-s)
                res = min(res, i+1-left)  # mistake: i-j, there is padding in sums
        return res if res != float('inf') else 0
    
    def binarySearch(self, nums, left, target):
        # find the last index i fron nums[left:] 
        # such that nums[i] <= target
        # there must exist a number
        
        left, right = left, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        
        if nums[right] <= target:
            return right
        else:
            return left


# method 1: two pointers, O(n)
class Solution1(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        left, right = 0, 0
        total = nums[0]
        res = len(nums) + 1
        while right < len(nums):
            if total < s:
                right += 1
                if right < len(nums):
                    total += nums[right]
            else:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res if res < len(nums)+1 else 0
    
