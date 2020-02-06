# method 3: Manacher's Algorithm 
# refer to leetcode problem #5: longest palindrome substring
# we only need to find the longest palindrome substring that starts with s[0]
class Solution3(object):
    def shortestPalindrome(self, s):
        p = ["#"]
        for i, c in enumerate(s):
            p.append(c)
            p.append("#")
        
        dp = [1]*len(p)  # radius of palindrome, including the center
        max_radius = 0
        center = 0
        front = 0
        for i in range(1, len(p)//2):  
            # optimization, the palindrome has to start with s[0]
            if i <= front:
                dp[i] = min(front-i+1, dp[2*center-i])
            while i+dp[i] < len(p) and i-dp[i] >= 0 and p[i+dp[i]] == p[i-dp[i]]:
                dp[i] += 1
            if i+dp[i]-1 > front:
                center = i
                front = i+dp[i]-1
            if dp[i] == i+1:
                max_radius = max(max_radius, dp[i])
        
        return s[max_radius-1:][::-1] + s


# Solution 2: KMP, time O(n)
# build a lookup table for new_s=s+"#"+s[::-1], 
# the last number in table will be the max length of palindrome substring
# another method: build a lookup table for s (not new_s), and then match s 
# with rev_s=s[::-1], the index in rev_s when matching stopped will be max length
class Solution2(object):
    def shortestPalindrome(self, s):
        pattern = s + "#" + s[::-1]
        table = self.getKMPTable(pattern)
        return s[table[-1]:][::-1] + s
    
    def getKMPTable(self, pattern):
        table = [0]*len(pattern)
        
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = table[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            table[i] = j
            
        return table


# Solution 1: brute force, remove one letter from the end of s at one time, 
# and then check if the rest of s is a palindrome, 
# time O(n^2), space O(1), time limit exceeded
# adding characters in the front is equal to removing characters from the end
class Solution1(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        for i in range(len(s)-1, -1, -1):
            if self.isPalindrome(s[:i+1]):
                return s[len(s)-1:i:-1] + s
        
    
    def isPalindrome(self, s):
        if not s:
            return True
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


"""
Given a string s, you are allowed to convert it to a palindrome by
 adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""
