# time O(10**(len(R)//4))

class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        small = int(L)
        large = int(R)
        m = (len(L))//4
        n = ((len(R) + 1)//2 + 1)//2
        cnt = 0
        for num in range(10**m, 10**n+1):
            s = str(num)
            s1 = s + s[::-1]   # even length
            s2 = s[:-1] + s[::-1]   # odd length
            for candidate in [s1, s2]:
                x = int(candidate)
                x = x**2
                sx = str(x)
                if x >= small and x <= large and sx == sx[::-1]:
                    cnt += 1
        return cnt

"""
Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers L and R (represented as strings), return the number of superpalindromes in the inclusive range [L, R].

 

Example 1:

Input: L = "4", R = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
 

Note:

1 <= len(L) <= 18
1 <= len(R) <= 18
L and R are strings representing integers in the range [1, 10^18).
int(L) <= int(R)
"""
