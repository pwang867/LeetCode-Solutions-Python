# method 2, iteration, O(n^2) due to nums.pop(i)

import math
class Solution(object):
    def getPermutation(self, n, k):
        factorial = math.factorial(n)
        k -= 1
        res = []
        nums = [str(i) for i in range(1, n+1)]
        while n > 0:
            factorial /= n   # don't put this line after n -= 1, otherwise divide by zero for last round
            i, k = divmod(k, factorial)
            res.append(nums[i])  
            nums.pop(i)  # O(n) time
            n -= 1
        return "".join(res)
    


# method 1, backtracking, O(n)
class Solution1(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # calculate n!
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1 # change from 1-indexed to 0-indexed
        return self.helper(factorial, n, k, nums)
    
    def helper(self, factorial, n, k, nums):
        # factorial = n!
        # n is the remaining number of digits
        # k is the remaining order 
        # nums is the remaining digits
        if n == 1:
            return nums[0]
        factorial = factorial/n
        i, k = k/factorial, k%factorial
        return nums[i] + self.helper(factorial, n - 1, k, nums[:i] + nums[i+1:])


"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
 we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
"""
