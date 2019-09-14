# solution 2: use merge sort, average and worst case time O(n*log(n))
# space O(n)
# ref: https://leetcode.com/problems/count-of-smaller-numbers-after-self
# /discuss/76584/Mergesort-solution
class Solution(object):
    def countSmaller(self, nums):
        if not nums:
            return []
        smaller = [0]*len(nums)
        self.mergeSort(list(enumerate(nums)), smaller)
        return smaller
    
    def mergeSort(self, nums, smaller):
        # nums is a list of (index, value)
        if len(nums) < 2:
            return nums
        
        mid = len(nums)//2
        left = self.mergeSort(nums[:mid], smaller)
        right = self.mergeSort(nums[mid:], smaller)
        
        # merge, from large (end) to small (beginning)
        # use nums to store sorted list to save space
        for k in range(len(nums)-1, -1, -1):  
            if not left:
                nums[:k+1] = right
                break
            if not right:
                nums[:k+1] = left
                break
            if left[-1][1] > right[-1][1]:
                # all values in right will be smaller to left[-1][1]
                # and to the right of left[-1]
                smaller[left[-1][0]] += len(right)  
                nums[k] = left.pop()
            else:
                nums[k] = right.pop()
        
        return nums
    


# solution 1: brute force, time O(n^2), space O(n)
# Time Limit Exceeded
class Solution1(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    cnt[i] += 1
        
        return cnt
    
