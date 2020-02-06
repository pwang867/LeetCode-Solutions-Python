# use Binary indexed tree
# update: time O(log(n)), sumRange: time O(log(n))
# space: O(n)
# i=0 is a dummy for BIT array (self.sums)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # wrong initialization: self.nums = nums
        # then the self.sums won't be initialized
        self.nums = [0]*(len(nums))  
        
        # use binary indexed tree
        self.sums = [0]*(len(nums)+1)  # self.sums save partial sums
        for i in range(len(nums)):
            self.update(i, nums[i])
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        # i is index in self.nums
        if i < 0 or i >= len(self.nums):
            return
        
        diff = val - self.nums[i]
        cur = i+1  # do not modify i! i will be used in the end again
        while cur < len(self.sums):
            self.sums[cur] += diff
            cur += cur&-cur
            
        self.nums[i] = val   
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # i, j are index in self.nums
        return self.getSum(j) - self.getSum(i-1)
    
    def getSum(self, i):
        # i is index in self.nums
        if i < 0:  # i might be used as -1 by self.sumRange(0, j)
            return 0
        i = min(i, len(self.nums)-1)
        
        res = 0
        cur = i + 1
        while cur > 0:  # wrong: cur >= 0
            res += self.sums[cur]
            cur -= cur&-cur
        
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)



"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""
