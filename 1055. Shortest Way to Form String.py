# linear scan, time O(len(target)*len(source)), space O(1)
class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        if not source:
            return -1
        i, j = 0, 0
        num_sub = 1
        while j < len(target):
            cnt = len(source)
            while source[i] != target[j]:
                i += 1
                if i == len(source):
                    i = 0
                    num_sub += 1
                cnt -= 1
                if cnt == 0:   # when target[j] does not exist in source
                    return -1
            i += 1
            j += 1
            if i == len(source) and j < len(target):    # easy to miss
                i = 0
                num_sub += 1
        return num_sub
                

"""
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
Accepted
"""
