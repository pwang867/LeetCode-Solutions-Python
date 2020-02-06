# the candidates are only a few, we will generate all of them and iterate all of them
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        # n is given as a positive int
        if not n:
            return ""
        if len(n) == 1:
            return str(int(n)-1)
        k = len(n)
        candidates = [str(10**i + d) for i in [k, k-1] for d in [1, -1]]  # deal with 100...001, 99...99
        
        # if n= "1234", left = "12", then we only need to consider "12", "13", "14"
        prefix = int(n[:(k+1)//2])
        for left in [prefix-1, prefix, prefix+1]:
            left = str(left)
            right = left[::-1] if k%2==0 else left[:-1][::-1]
            s = left + right
            candidates.append(s)
        
        res = ""
        min_diff = float('inf')
        for candidate in candidates:
            diff = abs(int(candidate)-int(n))
            if diff != 0 and ( diff < min_diff or (diff == min_diff and int(candidate) < int(res)) ):
                min_diff = diff
                res = candidate
        
        return res

"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
Accepted
"""
