# method 2: use binary search twice to search, time O(log(n))
class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        
        # search the first num equal to target
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            i = left
        elif nums[right] == target:
            i == right
        else:
            return [-1, -1]
        
        # if the program reaches here, it means target must be found
        # and the left boundary if at least i
        
        # search the last num equal to target
        left, right = i, len(nums)-1  # better than 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left)  // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            j = right
        else:
            j = left
        
        return [i, j]



# method 1: use binary search only once to 
# find a number equal to target, then 
# linearly search its neighbors in two directions for duplicates
# time O(n) in worst case, generally O(log(n))
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # edge cases
        if len(nums) == 0:
            return [-1, -1]
        
        # check the begin and end if they are target
        if nums[0] == target:
            return self.helper(nums, 0, target)
        else:
            left = 0
        if nums[-1] == target:
            return self.helper(nums, len(nums) - 1, target)
        else:
            right = len(nums) - 1
        
        # binary search
        while left + 1 < right:
            mid = (left + right)/2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return self.helper(nums, mid, target)
        
        return [-1, -1]
    
    
    def helper(self, nums, i, target):
        # this is linear search, tie O(n)
        left, right = i, i
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        return [left, right]
    
