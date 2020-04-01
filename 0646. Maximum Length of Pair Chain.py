# dp, time O(n*log(n)) mainly due to sorting, space O(1)
# similar to longest increasing stack, or similar to merge intervals

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        
        pairs.sort(key=lambda x: x[1])
        
        last = [-float('inf'), -float('inf')]
        max_len = 0
        for pair in pairs:
            if last[1] < pair[0]:
                max_len += 1
                last = pair
        
        return max_len


"""
You are given n pairs of numbers. In every pair, 
the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) 
if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. 
You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""
