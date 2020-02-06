# watch out two corner case: 
# 1. negative numbers, 2. 1232100 (numbers ending with 0)
class Solution():
    def isPalindrome(self, x):
        if x < 0 or (x >= 10 and x%10 == 0):   # edge case: 123210
            return False
        rev = 0
        while(x > rev): # only check half way through
            rev = rev*10 + x%10
            x = x//10
        return x==rev or x==rev//10 # consider integers with both odd and even number of digits



"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
