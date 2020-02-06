# method 4, BIT, O(n*log(n))
class BIT:
    def __init__(self, n):
        self.counts = [0]*(n+1)
        self.total = 0
    
    def update(self, i):
        self.total += 1
        i += 1
        while i < len(self.counts):
            self.counts[i] += 1
            i += i&(-i)
    
    def sum(self, i):
        # find total counts <= i
        res = 0
        i += 1
        while i > 0:
            res += self.counts[i]
            i -= i&(-i)
        return self.total - res

class Solution(object):
    def countSmaller(self, nums):
        if not nums: return []
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort()
        tree = BIT(len(nums))
        counts = [0]*len(nums)
        for num, i in nums:    
            # find the count of indexes j such that j > i and nums[j][0] < nums[i][0] (sorted)
            counts[i] = tree.sum(i)
            tree.update(i)
        return counts
    


# solution 3: use merge sort
# time O(n*log(n)), space O(n)
# ref: https://leetcode.com/problems/count-of-smaller-numbers-after-self
# /discuss/76584/Mergesort-solution

class Solution3(object):
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
    

# method 2: use bisect
# worst case time O(n^2)
import bisect
class Solution1(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        counts = [0]*n
        sorted_arr = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            j = bisect.bisect_left(sorted_arr, nums[i])
            counts[i] = j
            sorted_arr.insert(j, nums[i])
            # bisect.insort(sorted_arr, nums[i])
        return counts
    


# solution 1: brute force, time O(n^2), space O(n)
# Time Limit Exceeded
class Solution2(object):
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
    


"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""

