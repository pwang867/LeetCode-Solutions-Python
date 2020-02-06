# https://en.wikipedia.org/wiki/Timsort, sorted() in python can do it in O(n)

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        nums = map(lambda x: self.calculate(x, a, b, c), nums)

        res = []
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left]*a >= nums[right]*a:
                res.append(nums[left])
                left += 1
            else:
                res.append(nums[right])
                right -= 1
        if a > 0 or (a==0 and b < 0):
            res.reverse()
        return res
    
    def calculate(self, x, a, b, c):
        return a*x*x + b*x + c


"""
Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
"""
