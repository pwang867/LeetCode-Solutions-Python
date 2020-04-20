# time/space O(n)


class Solution(object):
    def findGoodStrings(self, n, s1, s2, evil):
        """
        :type n: int
        :type s1: str
        :type s2: str
        :type evil: str
        :rtype: int
        """
        table = self.get_KMP_table(evil)
        dp = {}
        
        def helper(i, j, eq1, eq2):
            # i is index for current path, j is for evil
            # eq1 means current path is equal to s1[:i+1], eq2 is for s2
            if j == len(evil):  # generated a virus, this line must be in front of the next one!!!
                return 0
            if i == n:          # generated a successful string
                return 1
            key = (i, j, eq1, eq2)
            if key in dp:
                return dp[key]
            res = 0
            lo = ord(s1[i]) if eq1 else ord('a')
            hi = ord(s2[i]) if eq2 else ord('z')
            for k in range(lo, hi+1):
                c = chr(k)
                new_j = j
                while new_j > 0 and evil[new_j] != c:
                    new_j = table[new_j-1]
                if evil[new_j] == c:
                    new_j += 1
                new_eq1 = eq1 and (c == s1[i])
                new_eq2 = eq2 and (c == s2[i])
                res += helper(i+1, new_j, new_eq1, new_eq2)
            dp[key] = res % (10**9 + 7)
            return dp[key]
        
        return helper(0, 0, True, True)
    
    
    def get_KMP_table(self, evil):
        if not evil:
            return []
        table = [0]*len(evil)
        j = 0
        for i in range(1, len(evil)):
            while j > 0 and evil[j] != evil[i]:
                j = table[j-1]
            if evil[j] == evil[i]:
                j += 1
            table[i] = j
        return table
    


"""
Given the strings s1 and s2 of size n, and the string evil. Return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or 
equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, 
return this modulo 10^9 + 7.


Example 1:

Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings 
tarting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da". 
Example 2:

Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", 
therefore, there is not any good string.
Example 3:

Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2


Constraints:

s1.length == n
s2.length == n
1 <= n <= 500
1 <= evil.length <= 50
All strings consist of lowercase English letters.
"""

