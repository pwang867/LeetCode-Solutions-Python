# a zigzag sequence + a continous increasing(when k is odd) or decreasing (when k is even) sequence
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if k > n-1 or k < 1:
            return None
        
        cnt = k//2
        res = []
        for i in range(1, cnt+1):
            res.append(i)
            res.append(n+1-i)
        left, right = 1+cnt, n-cnt
        if k%2 == 0:
            res.extend(list(range(right, left-1, -1)))
        else:
            res.extend(list(range(left, right+1)))
        return res


"""
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104.
"""
