# time O(n^2), space O(1), two pointers


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        cnt = 0
        for i in range(2*n-1):
            left, right = i//2, (i+1)//2
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    cnt += 1
                    left -= 1
                    right += 1
                else:
                    break
        return cnt


"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
"""
