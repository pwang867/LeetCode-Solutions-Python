# scan from left to right, find the first i that s[i] < s[i-1]
# reduce s[i-1] by 1 and then change all the numbers after to 9
# watch out for N containing consective duplicates, such as N=14423 (res = 13999)
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = str(N)
        j = -1  # don't forget
        for i in range(1, len(s)):
            if s[i] < s[i-1]:
                j = i-1
                while j-1 >= 0 and s[j] == s[j-1]:   # find consecutive equal numbers
                    j -= 1
                break
        
        if j == -1:  # when the number N itself is good
            return N
        
        res = s[:j] + str(int(s[j])-1) + "9"*(len(s)-j-1)
        return int(res)
    
"""
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
"""
