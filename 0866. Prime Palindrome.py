# ref: https://leetcode.com/problems/prime-palindrome/discuss/146798/All-Even-Digits-Palindrome-are-Divisible-by-11
# All Even Digits Palindrome are Divisible by 11
class Solution(object):
    def primePalindrome(self, N):
        
        def isPrime(x):
            if x < 2 or x % 2 == 0: return x == 2
            for i in range(3, int(x**0.5) + 1, 2):  # skip even numbers
                if x % i == 0: 
                    return False
            return True
        
        if 8 <= N <= 11: 
            return 11
        for x in xrange(10 ** (len(str(N)) / 2), 10**5):
            s = str(x)
            y = int(s + s[-2::-1])    # construct palindrome number
            if y >= N and isPrime(y): 
                return y


"""
Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.

 

Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101
"""
