# two pointers
# same as problem 33. Search in Rotated Sorted Array
# be careful with duplicates on the two edges, remove them first
# time complexity worst case is O(n) due to duplicates, space is O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        # deal with the unwanted duplicates in the edges of array
        while left < right and nums[left] == nums[right]:
            left += 1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[left]:  # mid is in left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # mid is in right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
    
        
                    
