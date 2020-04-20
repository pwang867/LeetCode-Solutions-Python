# time/space O(n*log(n)), n = log(num)
# compare num with sorted num (if we can do unlimited swaps)
# find the first digit that is smaller than any digit after it, then swap


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        sorted_s = sorted(s, reverse=True)  # sort in reverse
        for i in range(len(s)):
            if s[i] != sorted_s[i]:
                target = sorted_s[i]
                for j in range(len(s) - 1, i, -1):  # must search backwards
                    if s[j] == target:
                        s[i], s[j] = s[j], s[i]
                        return int("".join(s))
        return num


"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. 
Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""

