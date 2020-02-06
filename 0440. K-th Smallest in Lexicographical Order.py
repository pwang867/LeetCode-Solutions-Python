# time O(h^2), where h is the height of the denary tree, space O(1)
# ref: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/92242/ConciseEasy-to-understand-Java-5ms-solution-with-Explaination
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k > n:
            return -1
        cur = 1
        k -= 1
        while k > 0:
            steps = self.countNodes(cur, cur+1, n)
            if steps <= k:
                cur += 1    # move to its right neighbor
                k -= steps
            else:
                cur *= 10   # move to the successor which is its leftmost child
                k -= 1
        return cur
    
    def countNodes(self, left, right, n):
        count = 0
        while left <= n:  # mistake: left < n
            if n >= right:
                count += right - left
            else:
                count += n + 1 - left
            left *= 10
            right *= 10
        return count
    
"""
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""
