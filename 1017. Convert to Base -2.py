# time/space log(N)
# this method can be generated to any K-base
class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0 or N == 1:
            return str(N)
        res = []
        while N != 0:
            res.append(N%2)    # res.append(N%abs(K))          for K-base
            N = (N - res[-1])//(-2)   # N = (N - res[-1])//K   for K-base
        res.reverse()
        return "".join(map(str, res))
    



"""
Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".

 

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4
 

Note:

0 <= N <= 10^9
"""
