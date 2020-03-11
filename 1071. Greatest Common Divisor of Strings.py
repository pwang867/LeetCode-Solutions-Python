# simple scan, optimize by gcd
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if not str1 or not str2:
            return ""
        max_len = self.gcd(len(str1), len(str2))
        for length in range(max_len, 0, -1):    # watch out: do not do binary search on length!
            if self.possible(str1, str2, length):
                return str1[:length]
        return ""

    def gcd(self, m, n):
        if n == 0:
            return m
        else:
            return self.gcd(n, m % n)

    def possible(self, s1, s2, length):
        # check if s1 and s2 are both repeating sequence of s1[:length]
        if len(s1) % length != 0 or len(s2) % length != 0:
            return False
        if s1[:length] != s2[:length]:
            return False
        return self.isPeriodic(s1, length) and self.isPeriodic(s2, length)

    def isPeriodic(self, s, length):
        # check if s is a repeating sequencing of s[:length]
        for i in range(length, len(s)):
            if s[i] != s[i - length]:
                return False
        return True


"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
"""