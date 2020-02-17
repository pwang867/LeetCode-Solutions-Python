# ref: https://leetcode.com/problems/reverse-pairs/discuss/97268
# /general-principles-behind-problems-similar-to-reverse-pairs

# method 2: Binary Indexed Tree
# dynamically search in the tree and 
# then insert elements into the tree
# the values in the tree needs to be sorted from large to small

class BITree(object):
    def __init__(self, nums):
        self.nums = nums  # sort from large to small
    
    def count(self, i):
        # count of numbers larger than self.nums[i]
        cnt = 0
        while i > 0:
            cnt += self.nums[i]
            i -= i&(-i)
        return cnt
    
    def insert(self, i):
        # add counts into self.nums[i] and relative nums
        while i < len(self.nums):
            self.nums[i] += 1
            i += i&(-i)

class Solution(object):
    def reversePairs(self, nums):
        if not nums:
            return 0
        
        root = BITree([0]*(len(nums)+1))  # add padding to ease implementation
        copy = sorted(nums, reverse=True)  # to find index for BITree
        cnt = 0
        for num in nums:
            i = self.search(copy, 2*num+1)
            if i != -1:
                cnt += root.count(i+1)  # use i+1 due to padding in BITTree
            i = self.search(copy, num)
            root.insert(i+1)
        return cnt
    
    def search(self, nums, target):
        # nums is sorted from large to small
        # return the last index i that nums[i] >= target
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                left = mid
            else:
                right = mid
        if nums[right] >= target:
            return right
        elif nums[left] >= target:
            return left
        else:
            return -1

        
        

# method 1: merge sort, time O(n*log(n))
class Solution1(object):
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
    

"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""
