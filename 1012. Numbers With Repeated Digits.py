# scan digit by digit, time/space O(log(N))
import math
class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 0: return 0
        N = min(N, 9876543210)
        return N - self.noDupDigitsAtMostN(N)
    
    def noDupDigitsAtMostN(self, N):
        # count positive integers only
        if N < 10:
            return N
        digits = map(int, list(str(N)))
        # count the numbers that are shorter than N
        n = len(digits)
        res = 9
        cur = 9
        for i in range(2, n):
            cur *= (11-i)
            res += cur
        # count numbers that are equally long as N
        visited = {digits[0]}
        factor = math.factorial(9)//math.factorial(10-n)    # 9*8*7*6...
        res += (digits[0]-1)*factor
        for i in range(1, n):
            factor //= (10-i)
            for digit in range(digits[i]):
                if digit not in visited:
                    res += factor
            if digits[i] in visited:
                break
            else:
                visited.add(digits[i])
        else:
            res += 1
        return res


"""
Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit.

 

Example 1:

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: 1000
Output: 262
 

Note:

1 <= N <= 10^9
Accepted
"""
