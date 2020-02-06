# time O(n*k*n), space O(n*k + n*n)
class Solution(object):
    def palindromePartition(self, s, k):
        if not s or k >= len(s) or k <= 0:
            return 0
        dp = {}   # {(i,k):cost}, the cost to change s[:i+1] into k groups of palindromes
        palindrome = {}   # {(i,j):cost}, the cost to change s[i:j+1] to a single palindrome
        res = self.partitionHelper(s, len(s)-1, k, dp, palindrome)
        return res
    
    def partitionHelper(self, s, end, k, dp, palindrome):
        ''' find the cost to partition s[:end+1] into k groups '''
        if (end, k) in dp:
            return dp[(end, k)]
        if k <= 0:
            return float('inf')
        if k == 1:
            return self.to_palindrome(s, 0, end, palindrome)
        cost = float('inf')
        for i in range(k-1, end+1):   # i is the start of the last group
            cost = min(cost, self.partitionHelper(s, i-1, k-1, dp, palindrome) \
                             + self.to_palindrome(s, i, end, palindrome))
        dp[(end, k)] = cost
        return cost
    
    def to_palindrome(self, s, start, end, palindrome):
        ''' find the cost to change s[start:end+1] to a single palindrome '''
        if (start, end) in palindrome:
            return palindrome[(start, end)]
        cost = 0
        i, j = start, end
        while start < end:
            if s[start] != s[end]:
                cost += 1
            start += 1
            end -= 1
        palindrome[(i, j)] = cost
        return cost
    
"""
You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
Return the minimal number of characters that you need to change to divide the string.

 

Example 1:

Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
Example 2:

Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
Example 3:

Input: s = "leetcode", k = 8
Output: 0
 

Constraints:

1 <= k <= s.length <= 100.
s only contains lowercase English letters.
"""
