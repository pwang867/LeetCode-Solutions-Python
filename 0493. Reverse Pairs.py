# ref: https://leetcode.com/problems/reverse-pairs/discuss/97268
# /general-principles-behind-problems-similar-to-reverse-pairs


# method 1: merge sort, time O(n*log(n))
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cnt = 0
        self.mergeSort(nums)
        return self.cnt
    
    def mergeSort(self, nums):
        if len(nums) < 2:
            return nums
        mid = len(nums)//2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        # search reverse pairs, two pointers
        i, j = 0, 0
        while i < len(left):  # mistake: while i < len(left) and j < len(right)
            while j < len(right) and left[i] > 2*right[j]:
                j += 1
            self.cnt += j
            i += 1
        
        # merge left and right and overwrite nums
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                k += 1
                i += 1
            else:
                nums[k] = right[j]
                k += 1
                j += 1
        if i < len(left):
            nums[k:] = left[i:]
        if j < len(right):
            nums[k:] = right[j:]
            
        return nums
    
