# method 2: slice the array into two pieces, 
# recur on each side, and choose the minimum
# early terminations are important
class Solution(object):
    def findMin(self, nums):
        if not nums:
            return None
        return self.findMinHelper(nums, 0, len(nums)-1)
    
    def findMinHelper(self, nums, left, right):
        if right - left < 2:
            return min(nums[left], nums[right])
        if nums[left] < nums[right]:  # early termination 1
            return nums[left]
        if nums[left] != nums[right]:  # early termination 2 (easy to miss)
            return self.findMinNoDup(nums, left, right)
        
        mid = left + (right - left)//2
        return min(self.findMinHelper(nums, left, mid),
                   self.findMinHelper(nums, mid+1, right))
    
    def findMinNoDup(self, nums, left, right):
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid
        
        return min(nums[left], nums[right])


# method 1: remove duplicates on one side, 
# then the problem is reduced to 
# problem # Find Minimum in Rotated Sorted Array
# O(n) in worst case depending on the number of duplicates
class Solution1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        # linearly remove duplicates on the left side
        # worst case O(n)
        left, right = 0, len(nums)-1
        while left + 1 < right:
            if nums[left] == nums[right]:
                left += 1
            else:
                break
        
        # search for minimum using binary search
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid
        
        return min(nums[left], nums[right])
    
