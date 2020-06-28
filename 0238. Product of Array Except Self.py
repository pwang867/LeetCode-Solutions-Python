# simply use a running product


# time O(n), extra space O(1) except the result
# travel from left and right to calculate the product of nums[:i]
# excluding nums[i], saved into res[], and then travel right to left 
# to calculate the produce of nums[i+1:], multiply to res[i]


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0]*n  
        res[0] = 1
        for i in range(1, n): # calculate product of nums[:i+1]
            res[i] = res[i-1]*nums[i-1]
        
        total = 1
        for i in range(n-2, -1, -1):   # total means the product of nums[i+1:]
            total *= nums[i+1]
            res[i] *= total
        return res


# time O(n), space O(n)
# travel from left and right to calculate the product of nums[:i]
# excluding nums[i], saved into left[], and then right to left 
# to calculate the produce of nums[i+1:], saved into right[]
# then the answer will be left[i]*right[i]


class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [0]*n  # left[i] means the product of nums[:i], excluding nums[i]
        right = [0]*n
        left[0] = 1
        right[n-1] = 1
        for i in range(1, n):
            left[i] = left[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        
        res=[]
        for i in range(n):
            res.append(left[i]*right[i])
        
        return res


"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is 
equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space 
for the purpose of space complexity analysis.)
"""
