# method 3: one pass, time O(n), space O(1)
class Solution(object):
    def isGoodArray(self, nums):
        return reduce(self.gcd, nums) == 1
    
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x%y)


# method 2: find the greatest common divisor for all the numbers 
# by mod nums over its minimum every time, while loop will be executed log(max_num) times
# time O(log(max_num)*n), space O(n)
# return True if the gcd of the whole array is 1
class Solution2(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        _min = min(nums)
        if _min == 1:
            return True
        while True:
            next_nums = [_min]
            next_min = _min
            for num in nums:
                x = num%_min
                if x == 0:
                    continue
                if x == 1:
                    return True
                next_nums.append(x)
                next_min = min(next_min, x)
            nums = next_nums
            _min = next_min
            if len(nums) == 1:
                return nums[0] == 1
        

# time (n!)^2, find the gcd of the whole array by calculating the gcd of every two numbers
class Solution1(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == 1
        nums.sort()
        while True:
            cur = set()
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    x = self.gcd(nums[i], nums[j])
                    if x == 1:
                        return True
                    else:
                        cur.add(x)
                if i==0 and len(cur) == 1:
                    return False
            if len(cur) == 1:
                return False
            nums = list(cur)
        
    
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x%y)



"""
Given an array nums of positive integers. 
Your task is to select some subset of nums, multiply each element by an integer 
and add all these numbers. The array is said to be good if you can obtain a sum 
of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.

 

Example 1:

Input: nums = [12,5,7,23]
Output: true
Explanation: Pick numbers 5 and 7.
5*3 + 7*(-2) = 1
Example 2:

Input: nums = [29,6,10]
Output: true
Explanation: Pick numbers 29, 6 and 10.
29*1 + 6*(-3) + 10*(-1) = 1
Example 3:

Input: nums = [3,6]
Output: false
"""



print(Solution().isGoodArray(nums))

