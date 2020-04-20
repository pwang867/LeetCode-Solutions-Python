# time O(res) < O(2^N)
# space O(res)


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return list(range(10))
        res = []
        for i in range(1, 10):
            self.dfs(i, i, N - 1, K, res)
        return res

    def dfs(self, num, last_digit, num_digits, K, res):
        if num_digits == 0:
            res.append(num)
            return
        for digit in {last_digit - K, last_digit + K}:  # edge case: K==0
            if 0 <= digit <= 9:
                self.dfs(num * 10 + digit, digit, num_digits - 1, K, res)


"""
Return all non-negative integers of length N such that the absolute difference between 
every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 
01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1 <= N <= 9
0 <= K <= 9
"""
