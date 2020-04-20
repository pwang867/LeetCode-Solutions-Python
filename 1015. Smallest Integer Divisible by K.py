# time/space O(K)
# find the period, pigeon hole principle:
# https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/260875/Python-O(K)-with-Detailed-Explanations

class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        res = 1
        cur = 1
        visited = {1}
        while cur > 0:
            cur = cur % K
            if cur == 0:
                return res
            cur = cur * 10 + 1   # this line can not be moved to be after the if else clause below
            if cur in visited:
                return -1
            else:
                visited.add(cur)
            res += 1
        return res


"""
Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.

 

Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
 

Note:

1 <= K <= 10^5
"""

